import { AbstractDrawable } from "./Base/AbstractDrawable.js";
import { RunPointer } from "./RunPointer.js";
import { Tab } from "./Tab.js";
import { Rect } from "./Rectangle.js";
import { Button } from "./Button.js";
import { FONT_AWESOME, COLOR } from "../System/Constants.js";
import * as Logo from "./LogoModule/DrawableCommands.js";


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

    IsInside() {

    }

    DrawObject(screen) {
        this.items.forEach(element => {
            element.DrawObject(screen);
        });

        this.plateItems[this.currentActivePlane].forEach(element => {
            element.DrawObject(screen);
        });

        if (this.sidePanelActive) {
            this.sidePanel.DrawObject(screen);

            this.grid.forEach(element => {
                element.DrawObject(screen);
            });

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

    }

    OnRelease(event) {

    }

    OnClick(event) {

    }

    MoveSourcePanel(direction = 1, reset = true) {

    }

    ResetPosition() {

    }

    SetCommandPosition() {

    }

    RearrangeCommands(ignore = null, needReset = true) {

    }

    AddItemToCurrentPlane(item, plane = null) {

    }

    ResizeSourceBlock() {

    }

    RepaintTabs(id) {
        this.items.forEach(item => {
            if(item instanceof Tab) {
                if( id == item.GetId()) {
                    item.selected = true;
                } else {
                    item.selected = false;
                }
            }
        });
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

    }

    FindLoopEnd(loopBase) {

    }

    CompileLoops() {

    }

    ResetCompileInfos() {
        this.plateItems[this.currentActivePlane].forEach(element => {
            if(element instanceof Logo.Loop || element instanceof Logo.LoopEnd) {
                element.ResetCompileInfo();
            } 
        });
    }

    StopRunning() {

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

    }

    SetCurrentActiveCommandList(list) {
        this.plateItems[this.currentActivePlane] = list;
    }

    GetCurrentActiveCommandList() {
        return this.plateItems[this.currentActivePlane];
    }

}