import { AbstractDrawable } from "./Base/AbstractDrawable.js";
import { RunPointer } from "./RunPointer.js";
import { Tab } from "./Tab.js";
import { Rect } from "./Rectangle.js";
import { Button } from "./Button.js";
import { FONT_AWESOME, COLOR, MOUSE } from "../System/Constants.js";
import * as Logo from "./LogoModule/DrawableCommands.js";
import { Command } from "./Base/Command.js";
import { MoveElementList } from "../System/SupportFunctions.js";


export class ScrollingPlane extends AbstractDrawable {
    constructor(x, y, w, h, tabs = 2, parent = null) {
        super(x, y, w, h);

        this.gui = parent;

        this.tabs = tabs;
        this.items = [];

        this.clicked = null;
        this.plateItems = []; // Ez egy lista ami listákat tárol majd #ListaCeption
        this.currentActivePlane = 0;
        this.InitBefore();
        this.GenerateWindow();
        this.InitAfter();
        this.selectedCommand = null;
        this.loopend = null;

        this.sidePanelActive = true;

        this.base = {
            "h": this.h,
            "x": this.x,
            "y": this.y,
            "w": this.w
        };

        this.counter = 0;

    }

    IsInside(position) {

        if (this.sidePanelActive) {
            this.sidePanel.IsInside(position);
            for (const item of this.grid) {
                if (item.IsInside(position)) {
                    this.clicked = item;
                    return true;
                }
            }

            if (this.clearCommandsButton.IsInside(position)) {
                if (this.plateItems[this.currentActivePlane].length) {
                    this.clicked = this.clearCommandsButton;
                    return true;
                }
            }
        }

        for (const item of this.plateItems[this.currentActivePlane]) {
            if (item.IsInside(position)) {
                this.clicked = item;
                return true;
            }
        }

        for (const item of this.items) {
            if (item.IsInside(position)) {
                this.clicked = item;
                return true;
            }
        }
    }

    DrawObject(screen) {
        for (const element of this.items) {
            element.DrawObject(screen);

        }

        for (const element of this.plateItems[this.currentActivePlane]) {
            element.DrawObject(screen);
        }

        for (const element of this.plateItems[this.currentActivePlane]) {
            if (element instanceof Logo.Loop) {
                element.DrawLoopend(screen);
            }
        }

        if (this.sidePanelActive) {
            this.sidePanel.DrawObject(screen);

            for (const element of this.grid) {
                element.DrawObject(screen);
            }

            if (this.plateItems[this.currentActivePlane].length) {
                this.clearCommandsButton.DrawObject(screen);
            }
        }

        if (this.selectedCommand) {
            this.selectedCommand.DrawObject(screen);
        }
    }

    InitBefore() {
        for (let index = 0; index < this.tabs; index++) {
            this.plateItems.push([]);
        }
        this.runPointer = new RunPointer(0, 0, 40, 40);
    }

    GenerateWindow() {
        var tabWidth = this.w / this.tabs;
        this.tabHeight = 30;
        for (let i = 0; i < this.tabs; i++) {
            var tab = new Tab(this.x + i * tabWidth, this.y, tabWidth, this.tabHeight, undefined, i, 1, false);
            this.Add(tab);
        }

        this.sidePanel = new Rect(700, 75, 121, 520, undefined, 1, false, false);

        this.clearCommandsButton = new Button(771, 594, 50, 50, undefined, FONT_AWESOME.ROUND_X, 4);
        this.clearCommandsButton.OnClick = this.ClearCurrentSource.bind(this);
        this.clearCommandsButton.SetTextIconColor(COLOR.RED);

        this.PrepareSidePanelForLogo();
        this.mainPanel = new Rect(this.x, this.y + this.tabHeight, this.w, this.h, undefined, 1, false, false);
        this.Add(this.mainPanel);

    }

    InitAfter() {
        this.RepaintTabs(0);
    }

    Add(elem) {
        this.items.push(elem);
    }

    OnDrag(event) {
        var adjustmentNeeded = false;
        if (this.selectedCommand) {
            this.selectedCommand.Drag(event.realpos);

            if (!(this.plateItems[this.currentActivePlane].includes(this.selectedCommand)) && this.mainPanel.IsInside(event.realpos)) {
                if (this.selectedCommand instanceof Logo.Loop) {
                    this.selectedCommand.loopend.SetPosition(this.selectedCommand.x, this.selectedCommand.y + 55);
                    this.AddItemToCurrentPlane(this.loopend);
                }
                this.AddItemToCurrentPlane(this.selectedCommand);
                this.RearrangeCommands(this.selectedCommand);
            }

            if (this.plateItems[this.currentActivePlane].includes(this.selectedCommand) && !this.mainPanel.IsInside(event.realpos)) {
                this.plateItems[this.currentActivePlane].remove(this.selectedCommand);
                if (this.selectedCommand instanceof Logo.Loop) {
                    if (this.plateItems[this.currentActivePlane].includes(this.selectedCommand.loopend)) {
                        this.plateItems[this.currentActivePlane].remove(this.selectedCommand.loopend);
                    }
                }
                if (this.selectedCommand instanceof Logo.LoopEnd) {
                    for (const item of this.plateItems[this.currentActivePlane]) {
                        if (item instanceof Logo.Loop) {
                            if (item.loopend == this.selectedCommand) {
                                this.plateItems[this.currentActivePlane].remove(item);
                                this.selectedCommand = null;
                                adjustmentNeeded = true;
                                break;
                            }
                        }
                    }
                }
                this.RearrangeCommands();
            }

            this.ResizeSourceBlock();

            if (this.plateItems[this.currentActivePlane].includes(this.selectedCommand)) {
                for (const item of this.plateItems[this.currentActivePlane]) {
                    if (this.selectedCommand != item && item != null) {
                        if (item.y - item.h / 2 < this.selectedCommand.y) {
                            MoveElementList(this.plateItems[this.currentActivePlane], this.selectedCommand, this.plateItems[this.currentActivePlane].indexOf(item));
                            this.RearrangeCommands(this.selectedCommand);
                        }
                    }
                }
            }

            if (this.mainPanel.x < event.realpos[0] && event.realpos[0] < this.mainPanel.x + this.mainPanel.w) {
                if (event.realpos[1] < 20) {
                    this.MoveSourcePanel(1);
                }
                if (event.realpos[1] > 700) {
                    this.MoveSourcePanel(-1);
                }
            }

            if (adjustmentNeeded) {
                while (this.mainPanel.y + this.mainPanel.h < 700 && this.mainPanel.h > 700) {
                    this.MoveSourcePanel(1);
                }
            }
        }
    }

    OnRelease(event) {
        if (this.selectedCommand) {
            if (this.mainPanel.IsInside(event.realpos)) {
                this.SetCommandPosition();
                if (!(this.plateItems[this.currentActivePlane].includes(this.selectedCommand))) {
                    this.AddItemToCurrentPlane(this.selectedCommand);
                    if (this.selectedCommand instanceof Logo.Loop) {
                        this.AddItemToCurrentPlane(this.selectedCommand.loopend);
                    }
                }
            } else {
                while (this.mainPanel.y + this.mainPanel.h < 700 && this.mainPanel.h > 700) {
                    this.MoveSourcePanel(1);
                }
                if (this.mainPanel.h < 700); {
                    this.ResetPosition();
                    this.ResizeSourceBlock();
                }
                if (this.plateItems[this.currentActivePlane].includes(this.selectedCommand)) {
                    this.plateItems[this.currentActivePlane].remove(this.selectedCommand);
                }
                for (const item of this.plateItems[this.currentActivePlane]) {
                    if (item == null) {
                        this.plateItems[this.currentActivePlane].remove(item);
                    }
                }
                this.selectedCommand = null;

                this.RearrangeCommands();

            }
        }
        this.selectedCommand = null;
    }

    OnClick(event) {
        if (event.type == "mousedown") {
            if (this.clicked instanceof Tab) {
                var id = this.clicked.GetId();
                this.currentActivePlane = id;
                this.ResetPosition();
                this.RepaintTabs(id);
                this.ResizeSourceBlock();
            } else if (this.clicked instanceof Command) {
                if (event.button == MOUSE.MMB || this.gui.button_down.a && event.button == MOUSE.LMB) {
                    if (!(this.clicked instanceof Logo.LoopEnd)) {
                        this.CreateACommandCopy();
                        this.AddItemToCurrentPlane(this.selectedCommand);
                        if (this.selectedCommand instanceof Logo.Loop) {
                            this.AddItemToCurrentPlane(this.selectedCommand.loopend);
                        }
                        this.selectedCommand = null;
                        this.RearrangeCommands();
                        this.ResizeSourceBlock();
                    }
                } else if (event.button == MOUSE.RMB || this.gui.button_down.s && event.button == MOUSE.LMB) {

                    if (this.clicked instanceof Logo.PenColor) {
                        this.clicked.ChangeColor();
                    } else if (this.clicked instanceof Logo.PenWidth) {
                        this.clicked.Extend();
                    } else if (this.clicked instanceof Logo.Loop) {
                        this.clicked.ChangeCycleNumber();
                    }
                } else if (event.button == MOUSE.LMB && this.gui.button_down.d) {
                    if (this.mainPanel.IsInside(event.realpos)) {
                        this.selectedCommand = this.clicked;
                        if (this.selectedCommand instanceof Logo.Loop) {
                            this.loopend = this.selectedCommand.loopend;
                        }
                        this.plateItems[this.currentActivePlane].remove(this.selectedCommand);
                        if (this.loopend) {
                            this.plateItems[this.currentActivePlane].remove(this.loopend);
                        }
                        this.selectedCommand = null;
                        this.loopend = null;
                        this.RearrangeCommands();
                        this.ResizeSourceBlock();
                        while (this.mainPanel.y + this.mainPanel.h < 700 && this.mainPanel.h > 700) {
                            this.MoveSourcePanel(1);
                        }
                        if (this.mainPanel.h < 700) {
                            this.ResetPosition();
                            this.ResizeSourceBlock();
                        }
                    }
                } else if (event.button == MOUSE.LMB) {
                    if (!this.mainPanel.IsInside(event.realpos)) {
                        if (!(this.clicked instanceof Logo.LoopEnd)) {
                            this.CreateACommandCopy();
                        }
                    } else {
                        this.selectedCommand = this.clicked;
                        if (this.selectedCommand instanceof Logo.Loop) {
                            this.loopend = this.selectedCommand.loopend;
                        }
                    }
                    this.selectedCommand.SetDelta(event.realpos);
                }
            } else if (this.clicked instanceof Button) {
                this.clicked.OnClick(event);
            } else {
                console.log("Clicked element: ", this.clicked);
            }
        } else { // wheel
            if (this.mainPanel.IsInside(event.realpos)) {
                if (this.mainPanel.h > 600) {
                    if (event.deltaY > 0) {
                        this.MoveSourcePanel(-1);
                    } else {
                        this.MoveSourcePanel(1);
                    }
                }
            }
        }
    }

    MoveSourcePanel(direction = 1, reset = true) {
        if (this.items[0].y >= 20 && direction > 0) {
            return;
        }

        if (this.mainPanel.y + this.mainPanel.h <= 700 && direction < 0) {
            return;
        }

        for (const item of this.items) {
            if (item == this.sidePanel) {
                return;
            }
            var position_y = item.y + 20 * direction;
            item.SetPosition(item.x, position_y);
            if (item instanceof Tab) {
                item.UpdatePoints();
            }
        }
        this.RearrangeCommands(undefined, reset);
    }

    ResetPosition() {
        for (const item of this.items) {
            if (item == this.sidePanel) {
                return;
            }
            item.ResetPosition();
        }
        this.RearrangeCommands();
    }

    SetCommandPosition() {
        if (!(this.plateItems[this.currentActivePlane].includes(this.selectedCommand))) {
            this.selectedCommand.SetPosition(this.mainPanel.x + this.mainPanel.w / 2 - 25, this.mainPanel.y + 5 + this.plateItems[this.currentActivePlane].length * 55);
        } else {
            this.selectedCommand.SetPosition(this.mainPanel.x + this.mainPanel.w / 2 - 25, this.mainPanel.y + 5 + this.plateItems[this.currentActivePlane].indexOf(this.selectedCommand) * 55);
        }
    }

    RearrangeCommands(ignore = null, needReset = true) {
        if (needReset) {
            this.gui.NeedCompile();
            this.ResetCompileInfos();
            this.gui.reset = true;
        }
        for (const item of this.plateItems[this.currentActivePlane]) {
            if (item) {
                if (item != ignore) {
                    item.SetPosition(this.mainPanel.x + this.mainPanel.w / 2 - 25, this.mainPanel.y + 5 + this.plateItems[this.currentActivePlane].indexOf(item) * 55);
                }
            }
        }

        for (const item of this.plateItems[this.currentActivePlane]) {
            if (item instanceof Logo.Loop) {
                item.ark_level = 0;
            }
        }

        var active_queue = [];
        for (let i = 0; i < this.plateItems[this.currentActivePlane].length; i++) {
            const item = this.plateItems[this.currentActivePlane][i];
            if (item instanceof Logo.Loop) {
                var start = this.plateItems[this.currentActivePlane].indexOf(item);
                var end = this.plateItems[this.currentActivePlane].indexOf(item.loopend);
                if (start < end) {
                    active_queue.push([start, end, item]);
                } else {
                    active_queue.push([end, start, item]);
                }
            }
        }

        for (const item of active_queue) {
            for (const elem of active_queue) {
                if (item == elem) {
                    continue;
                }
                if (item[0] < elem[0] && item[1] > elem[1]) {
                    item[2].ark_level += 1;
                }
            }
        }

    }

    AddItemToCurrentPlane(item) {
        this.plateItems[this.currentActivePlane].push(item);
    }

    ResizeSourceBlock() {
        this.mainPanel.h = Math.max(this.plateItems[this.currentActivePlane].length * 55 + 5, this.base.h);
        for (let item of this.items) {
            if (item instanceof Tab) {
                item.y = this.mainPanel.y - this.tabHeight;
            }
        }
    }

    RepaintTabs(id) {
        for (let item of this.items) {
            if (item instanceof Tab) {
                if (id == item.GetId()) {
                    item.selected = true;
                } else {
                    item.selected = false;
                }
            }
        }
    }

    PrepareSidePanelForLogo() {
        this.grid = [];

        var command = new Logo.Forward(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.Backward(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.Forward(0, 0, 50, 50, undefined, 2);
        this.grid.push(command);

        var command = new Logo.Backward(0, 0, 50, 50, undefined, 2);
        this.grid.push(command);

        var command = new Logo.Left(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.Right(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.Left(0, 0, 50, 50, undefined, 6);
        this.grid.push(command);

        var command = new Logo.Right(0, 0, 50, 50, undefined, 6);
        this.grid.push(command);

        var command = new Logo.Home(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.FloodFill(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.PenWidth(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.PenColor(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.PenDown(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.PenUp(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.ShowTurtle(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.HideTurtle(0, 0, 50, 50);
        this.grid.push(command);

        var command = new Logo.Loop(0, 0, 105, 50);
        this.grid.push(command);

        this.DrawGrid();
    }

    DrawGrid() {
        var base_x = 708;
        var base_y = 88;
        var delta_x = 55;
        var delta_y = 55;

        for (let i = 0; i < Math.trunc(Math.ceil(this.grid.length / 2)); i++) {
            for (let j = 0; j < 2; j++) {
                var counter = i * 2 + j;
                if (counter == this.grid.length) {
                    return;
                }

                this.grid[counter].SetPosition(base_x + delta_x * j, base_y + delta_y * i);

            }
        }

    }

    Play(counter) {
        var i = this.plateItems[this.currentActivePlane][counter];
        this.MoveSourceToShowPointer(i);
        this.runPointer.SetPosition(i.x + 25 - 70, i.y + 25);
        var logoCore = this.gui.application_core.logoCore;
        if (i instanceof Logo.Forward) {
            logoCore.Forward(i.mul * 20);
        } else if (i instanceof Logo.Backward) {
            logoCore.Backward(i.mul * 20);
        } else if (i instanceof Logo.Left) {
            logoCore.Left(15 * i.mul);
        } else if (i instanceof Logo.Right) {
            logoCore.Right(15 * i.mul);
        } else if (i instanceof Logo.PenDown) {
            logoCore.PenDown();
        } else if (i instanceof Logo.PenUp) {
            logoCore.PenUp();
        } else if (i instanceof Logo.PenWidth) {
            logoCore.Width((i.pen_width + 1) * 2 + 1);
        } else if (i instanceof Logo.PenColor) {
            logoCore.Color(i.penColor);
        } else if (i instanceof Logo.Home) {
            logoCore.Home();
        } else if (i instanceof Logo.FloodFill) {
            logoCore.Fill();
        } else if (i instanceof Logo.ShowTurtle) {
            logoCore.ShowTurtle();
        } else if (i instanceof Logo.HideTurtle) {
            logoCore.HideTurtle();
        } else if (i instanceof Logo.Loop) {
            i.running = true;
            if(i.compileInformation.pre_test) {
                if(i.remainingCycle == 0) {
                    counter = i.compileInformation.loopend_index;
                    i.ResetCycleCounter();
                } else {
                    i.CountDown();
                }
            } else {
                if(i.remainingCycle == 0){
                    i.ResetCycleCounter();
                } else {
                    counter = i.compileInformation.loopend_index;
                    i.CountDown();
                }
            }
        } else if (i instanceof Logo.LoopEnd) {
            if(i.compileInformation.pre_test) {
                counter = i.compileInformation.loopbase_index - 1;
            }
        }

        counter += 1;
        return counter;
    }

    HasNext(counter) {
        return counter < this.plateItems[this.currentActivePlane].length;
    }

    EnableSidepanel(state) {
        this.sidePanelActive = state;
    }

    FindLoopBase(loopEnd) {
        for (const elem of this.plateItems[this.currentActivePlane]) {
            if (elem instanceof Logo.Loop) {
                if (elem.loopend == loopEnd) {
                    return elem;
                }
            }
        }
    }

    FindLoopEnd(loopBase) {
        for (const elem of this.plateItems[this.currentActivePlane]) {
            if (elem instanceof Logo.LoopEnd) {
                if (loopBase.loopend == elem) {
                    return elem;
                }
            }
        }
    }

    CompileLoops() {
        for (const element of this.plateItems[this.currentActivePlane]) {
            if (element instanceof Logo.Loop) {
                if (!element.compileInformation.compiled) {
                    var loopEnd = this.FindLoopEnd(element);
                    var loopEndIndex = this.plateItems[this.currentActivePlane].indexOf(loopEnd);
                    var loopStartIndex = this.plateItems[this.currentActivePlane].indexOf(element);
                    var preTest = loopEndIndex > loopStartIndex;
                    element.SetCompileInfo(preTest, loopEndIndex);
                    loopEnd.SetCompileInfo(preTest, loopStartIndex);
                }
            }
            if (element instanceof Logo.LoopEnd) {
                if (!element.compileInformation.compiled) {
                    var loopBase = this.FindLoopBase(element);
                    var loopStartIndex = this.plateItems[this.currentActivePlane].indexOf(loopBase);
                    var loopEndIndex = this.plateItems[this.currentActivePlane].indexOf(element);
                    var preTest = loopEndIndex > loopStartIndex;
                    element.SetCompileInfo(preTest, loopStartIndex);
                    loopBase.SetCompileInfo(preTest, loopEndIndex);
                }
            }
        }
    }

    ResetCompileInfos() {
        for (const element of this.plateItems[this.currentActivePlane]) {
            if (element instanceof Logo.Loop || element instanceof Logo.LoopEnd) {
                element.ResetCompileInfo();
            }
        }
    }

    StopRunning() {
        for (const elem of this.plateItems[this.currentActivePlane]) {
            if (elem instanceof Logo.Loop) {
                elem.running = false;
                elem.ResetCycleCounter();
            } else if (elem instanceof Logo.LoopEnd) {
                elem.running = false;
            }
        }
    }

    DrawRunPointer(screen) {
        this.runPointer.DrawObject(screen);
    }

    MoveSourceToShowPointer(i) {
        var flag = false;
        var t = false;

        while (i.y + i.h > 700 && !t) {
            flag = true;
            this.MoveSourcePanel(-1, false);
        }
        t = flag;
        while (i.y < 20 && !t) {
            this.MoveSourcePanel(1, false);
        }
    }

    ClearCurrentSource() {
        this.plateItems[this.currentActivePlane] = [];
        this.ResetPosition();
        this.ResizeSourceBlock();
    }

    CreateACommandCopy() {
        this.selectedCommand = _.cloneDeep(this.clicked);
        if (this.selectedCommand instanceof Logo.Loop) {
            this.selectedCommand.RollColor();
            this.loopend = new Logo.LoopEnd(this.selectedCommand.x, this.selectedCommand.y + 55, 50, 50);
            this.loopend.SetLoopBase(this.selectedCommand);
            this.selectedCommand.SetLoopend(this.loopend);
        }

    }

    SetCurrentActiveCommandList(list) {
        this.plateItems[this.currentActivePlane] = list;
    }

    GetCurrentActiveCommandList() {
        return this.plateItems[this.currentActivePlane];
    }

}