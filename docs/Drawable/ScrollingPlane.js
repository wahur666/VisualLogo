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
        
        if(this.sidePanelActive) {
            this.sidePanel.IsInside(position);
            for (const item of this.grid) {
                if(item.IsInside(position)) {
                    console.log("Scrolling plane isinside");
                    this.clicked = item;
                    return true;
                }
            }

            if(this.clearCommandsButton.IsInside(position)){
                if(this.plateItems[this.currentActivePlane].length) {
                    this.clicked = this.clearCommandsButton;
                    return true;
                }
            }
        }

        for (const item of this.plateItems[this.currentActivePlane]) {
            if(item.IsInside(position)) {
                this.clicked = item;
                return true;
            }
        }

        for (const item of this.items) {
            if(item.IsInside(position)){
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
            if(element instanceof Logo.Loop) {
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

        if(this.selectedCommand){
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
        var tabHeight = 30;
        for (let i = 0; i < this.tabs; i++) {
            var tab = new Tab(this.x + i * tabWidth, this.y, tabWidth, tabHeight, undefined, i, 1, false);
            this.Add(tab);
        }

        this.sidePanel = new Rect(700, 75, 121, 520, undefined, 1, false, false);
        
        this.clearCommandsButton = new Button(771, 594, 50, 50, undefined, FONT_AWESOME.ROUND_X, 4);
        this.clearCommandsButton.OnClick = this.ClearCurrentSource.bind(this);
        this.clearCommandsButton.SetTextIconColor(COLOR.RED);

        this.PrepareSidePanelForLogo();
        this.mainPanel = new Rect(this.x, this.y + tabHeight, this.w, this.h, undefined, 1, false, false);
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
        if(this.selectedCommand) {
            this.selectedCommand.Drag(event.realpos);
            if(!this.selectedCommand in this.plateItems[this.currentActivePlane] && this.mainPanel.IsInside(event.realpos)) {
                if(this.selectedCommand instanceof Logo.Loop) {
                    this.selectedCommand.loopend.SetPosition(this.selectedCommand.x, this.selectedCommand.y + 55);
                    this.AddItemToCurrentPlane(this.loopend);
                }
                this.AddItemToCurrentPlane(this.selectedCommand);
                this.RearrangeCommands(this.selectedCommand);
            }
            if(this.selectedCommand in this.plateItems[this.currentActivePlane] && ! this.mainPanel.IsInside(event.realpos)) {
                this.plateItems[this.currentActivePlane].remove(this.selectedCommand);
                if(this.selectedCommand instanceof Logo.Loop) {
                    if(this.selectedCommand.loopend in this.plateItems[this.currentActivePlane]) {
                        this.plateItems[this.currentActivePlane].remove(this.selectedCommand.loopend);
                    }
                }
                if(this.selectedCommand instanceof Logo.LoopEnd) {
                    for (const item of this.plateItems[this.currentActivePlane]) {
                        if(item instanceof Loop) {
                            if(item.loopEnd == this.selectedCommand) {
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
            if(this.selectedCommand in this.plateItems[this.currentActivePlane]) {
                for (const item of this.plateItems[this.currentActivePlane]) {
                    if(this.selectedCommand != item && item != null) {
                        if (item.y - item.h / 2 < this.selectedCommand / 2) {
                            MoveElementList(this.plateItems[this.currentActivePlane], this.selectedCommand, this.plateItems[this.currentActivePlane].indexOf(item));
                            this.RearrangeCommands(this.selectedCommand);
                        }
                    }
                }
            }
            if(this.mainPanel.x < event.realpos[0] && event.realpos[0] < this.mainPanel.x + this.mainPanel.w){
                if(event.realpos[1] < 20) {
                    this.MoveSourcePanel(1);
                }
                if(event.realpos[1] > 700) {
                    this.MoveSourcePanel(-1);
                }
            }
            if(adjustmentNeeded) {
                while(this.mainPanel.y + this.mainPanel.h < 700 && this.mainPanel.h > 700) {
                    this.MoveSourcePanel(1);
                }
            }
        }
    }

    OnRelease(event) {
        if(this.selectedCommand) {
            if(this.mainPanel.IsInside(event.realpos)){
                this.SetCommandPosition();
                if(!this.selectedCommand in this.plateItems[this.currentActivePlane]) {
                    this.AddItemToCurrentPlane(this.selectedCommand);
                    if(this.selectedCommand instanceof Logo.Loop) {
                        this.AddItemToCurrentPlane(this.selectedCommand.loopend);
                    }
                }
            } else {
                while (this.mainPanel.y + this.mainPanel.h < 700 && this.mainPanel.h > 700) {
                    this.MoveSourcePanel(1);
                }
                if(this.mainPanel.h < 700);{
                    this.ResetPosition();
                    this.ResizeSourceBlock();
                }
                if(this.selectedCommand in this.plateItems[this.currentActivePlane]){
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

        //console.log("Event: ",  event);
        console.log("button down: ", this.gui.button_down);
        if(event.type == "mousedown"){
            if(this.clicked instanceof Tab) {
                var id = this.clicked.GetId();
                this.currentActivePlane = id;
                this.ResetPosition();
                this.RepaintTabs(id);
                this.ResizeSourceBlock();
            } else if (this.clicked instanceof Command) {
                console.log(this.gui.button_down.a, event.button, MOUSE.LMB);
                
                if(event.button == MOUSE.MMB || this.gui.button_down.a && event.button == MOUSE.LMB) {
                    if(!this.clicked instanceof Logo.LoopEnd) {
                        this.CreateACommandCopy();
                        this.AddItemToCurrentPlane(this.selectedCommand);
                        if(this.selectedCommand instanceof Logo.Loop) {
                            this.AddItemToCurrentPlane(this.selectedCommand.loopend);
                        }
                        this.selectedCommand = null;
                        this.RearrangeCommands();
                        this.ResizeSourceBlock();
                    }
                } else if (event.button == MOUSE.RMB || this.gui.button_down.s && event.button == MOUSE.LMB) {
                    
                    if(this.clicked instanceof Logo.PenColor) {
                        this.clicked.ChangeColor();
                    } else if(this.clicked instanceof Logo.PenWidth) {
                        this.clicked.Extend();
                    } else if (this.clicked instanceof Logo.Loop) {
                        this.clicked.ChangeCycleNumber();
                    }
                } else if (event.button == MOUSE.LMB && this.gui.button_down.d) {
                    if(this.mainPanel.IsInside(event.realpos)) {
                        this.selectedCommand = this.clicked;
                        if(this.selectedCommand instanceof Logo.Loop) {
                            this.loopend = this.selectedCommand.loopend;
                        }
                        this.plateItems[this.currentActivePlane].remove(this.selectedCommand);
                        if(this.loopend) {
                            this.plateItems[this.currentActivePlane].remove(this.loopend);
                        }
                        this.selectedCommand = null;
                        this.loopend = null;
                        this.RearrangeCommands();
                        this.ResizeSourceBlock();
                        while(this.mainPanel.y + this.mainPanel.h < 700 && this.mainPanel.h > 700) {
                            this.MoveSourcePanel(1);
                        }
                        if(this.mainPanel.h < 700) {
                            this.ResetPosition();
                            this.ResizeSourceBlock();
                        }
                    }
                } else if (event.button == MOUSE.LMB) {
                    console.log("event", event);
                    
                    if(! this.mainPanel.IsInside(event.realpos)) {
                        if(!this.clicked instanceof Logo.LoopEnd) {
                            this.CreateACommandCopy();
                        }
                    } else {
                        this.selectedCommand = this.clicked;
                        if(this.selectedCommand instanceof Logo.Loop) {
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
            if(this.mainPanel.IsInside(event.realpos)) {
                if(this.mainPanel.h > 600) {
                    if(event.delta_y < 0) {
                        this.MoveSourcePanel(-1);
                    } else {
                        this.MoveSourcePanel(1);
                    }
                }
            }
        }
    }

    MoveSourcePanel(direction = 1, reset = true) {
        if(this.items[0].y >=20 && direction > 0) {
            return;
        }

        if(this.mainPanel.y + this.mainPanel.h <= 700 && direction < 0) {
            return;
        }

        for (const item of this.items) {
            if(item == this.sidePanel) {
                return;
            }
            var position_y = item.y + 20 * direction;
            item.SetPosition(item.x, position_y);
            if(item instanceof Tab) {
                item.UpdatePoints();
            }
        }
        this.RearrangeCommands(undefined, reset);
    }

    ResetPosition() {
        for (const item of this.items) {
            if(item == this.sidePanel) {
                return;
            }
            item.ResetPosition();
        }
        this.RearrangeCommands();
    }

    SetCommandPosition() {
        if(!this.selectedCommand in this.plateItems[this.currentActivePlane]) {
            this.selectedCommand.SetPosition(this.mainPanel.x + this.mainPanel.w / 2 - 25, this.mainPanel.y + 5 + this.plateItems[this.currentActivePlane].length * 55);
        } else {
            this.selectedCommand.SetPosition(this.mainPanel.x + this.mainPanel.w / 2 - 25, this.mainPanel.y + 5 + this.plateItems[this.currentActivePlane].indexOf(this.selectedCommand) * 55);
        }
    }

    RearrangeCommands(ignore = null, needReset = true) {

    }

    AddItemToCurrentPlane(item, plane = null) {
        if(plane) {
            this.plateItems[plane].push(item);
        } else {
            this.plateItems[this.currentActivePlane].push(item);
        }
    }

    ResizeSourceBlock() {
        this.mainPanel.h = Math.max(this.plateItems[this.currentActivePlane].length * 55 + 5, this.base.h);
    }

    RepaintTabs(id) {
        for (const item of this.items) {
            if(item instanceof Tab) {
                if( id == item.GetId()) {
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

    }

    HasNext(counter) {
        return counter < this.plateItems[this.currentActivePlane].length;
    }

    EnableSidepanel(state) {
        this.sidePanelActive = state;
    }

    FindLoopBase(loopEnd) {
        for (const elem of this.plateItems[this.currentActivePlane]) {
            if(elem instanceof Logo.Loop) {
                if(elem.loopend == loopEnd) {
                    return elem;
                }
            }
        }
    }

    FindLoopEnd(loopBase) {
        for (const elem of this.plateItems[this.currentActivePlane]) {
            if(elem instanceof Logo.LoopEnd){
                if(loopBase.loopend == elem) {
                    return elem;
                }
            }
        }
    }

    CompileLoops() {
        for (const element of this.plateItems[this.currentActivePlane]) {
            if(element instanceof Logo.Loop) {
                if(!element.compileInformation.compiled) {
                    var loopEnd = this.FindLoopEnd(element);
                    var loopEndIndex = this.plateItems[this.currentActivePlane].indexOf(loopEnd);
                    var loopStartIndex = this.plateItems[this.currentActivePlane].indexOf(element);
                    var preTest = loopEndIndex > loopStartIndex;
                    element.SetCompileInfo(preTest, loopEndIndex);
                    loopEnd.SetCompileInfo(preTest, loopStartIndex);
                }
            }
            if(element instanceof Logo.LoopEnd) {
                if(!element.compileInformation.compiled) {
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
            if(element instanceof Logo.Loop || element instanceof Logo.LoopEnd) {
                element.ResetCompileInfo();
            } 
        }
    }

    StopRunning() {
        for (const elem of this.plateItems[this.currentActivePlane]) {
            if(elem instanceof Logo.Loop) {
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

        while(i.y + i.h > 700 && !t) {
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
        console.log("COPPPYY");
        this.selectedCommand = JSON.parse(JSON.stringify(this.clicked));
        if(this.selectedCommand instanceof Logo.Loop) {
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