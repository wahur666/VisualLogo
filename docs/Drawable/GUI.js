import { COLOR, FONT_AWESOME } from "../System/Constants.js";
import { Timer } from "../System/Timer.js";
import { Button } from "./Button.js";
import { DrawingIcon } from "./DrawingIcon.js";
import { Rect } from "./Rectangle.js";
import { ScrollingPlane } from "./ScrollingPlane.js";
import { DrawRect } from "../System/SupportFunctions.js";
import { Tab } from "./Tab.js";

export class GUI {
    constructor(application_core){
        this.application_core = application_core;
        this.items = [];
        this.Initialize();
    }

    Initialize() {
        this.background_color = COLOR.LIGHTGRAY;
        this.background_color_index = 7;
        this.canvas = this.application_core.canvas;
        this.screen = this.canvas.getContext("2d");
        this.canvasRect = this.canvas.getBoundingClientRect();


        this.drawingWindow = new Rect(20, 20, 630, 600, COLOR.BLACK, 1, false, false);
        this.Add(this.drawingWindow);

        var buttonPlay = new Button(380, 640, 60, 60, undefined, FONT_AWESOME.PLAY, 5);
        buttonPlay.OnClick = this.OnClickPlay.bind(this);
        buttonPlay.SetAccentColor(COLOR.HATTER_1);
        this.Add(buttonPlay);

        var buttonStepOver = new  Button(450, 640, 60, 60, undefined, FONT_AWESOME.STEPOVER, 10);
        buttonStepOver.OnClick = this.OnClickStepOver.bind(this);
        buttonStepOver.SetAccentColor(COLOR.HATTER_4);
        this.Add(buttonStepOver);

        var buttonStop = new Button(520, 640, 60, 60, undefined, FONT_AWESOME.STOP, 4);
        buttonStop.OnClick = this.OnClickStop.bind(this);
        buttonStop.SetAccentColor(COLOR.HATTER_7);
        this.Add(buttonStop);

        var buttonReset = new Button(590, 640, 60, 60, undefined, FONT_AWESOME.RESET, 4);
        buttonReset.OnClick = this.OnClickReset.bind(this);
        buttonReset.SetAccentColor(COLOR.HATTER_8);
        this.Add(buttonReset);

        var buttonBackground = new Button(20, 660, 40,40, undefined, FONT_AWESOME.BACKGROUND_PICTURE, -1);
        buttonBackground.OnClick = this.ChangeBackgroundColor.bind(this);
        this.Add(buttonBackground);

        this.scrollplane = new ScrollingPlane(820, 20, 263, 600, 3, this);
        this.Add(this.scrollplane);

        this.mouseDown = false;
        this.timer = new Timer();
        this.running = false;
        this.reset = true;
        this.compile_needed = true;
        this.global_counter = 0;
        this.drawing_arrow = new DrawingIcon(0, 0, 30, 30, COLOR.RED, 0);
        this.show_run_pointer = false;
        this.step_over_mode = false;
        this.show_data_management_panel = false;
        this.skip_wait = false;
        this.data_index = null;
        this.wait_next_draw = false;
        this.disable_input = false;
        this.button_down = {
            "a" : false,
            "s" : false,
            "d" : false
        };
    }

    DrawGUI(){
        DrawRect(this.screen, this.background_color, 0, 0, this.canvas.width, this.canvas.height, 0);

        for (const element of this.items) {
            element.DrawObject(this.screen);
            
        }

        var [pos, rot, show] = this.application_core.logoCore.GetTurtleInformationToRender();
        
        if(show) {
            this.drawing_arrow.SetPosition(pos[0], pos[1]);
            this.drawing_arrow.DrawObject(this.screen, rot);
        }

    }

    Add(item){
        this.items.push(item);
    }

    MouseHandler(event) {
        event["realpos"] = this.EventPos(event);
        if(event.type == "mousemove") {
            if (this.mouseDown) {
                this.OnDrag(event);
            }
        } else if(event.type == "mousedown" || event.type == "wheel") {
            this.OnClick(event);
        } else { // MouseUp, MouseOut
            this.OnRelease(event);
        }
        
    }

    KeyboardHandler(event) {
        if(event.type == "keyup") {
            if(event.key == "a") {
                this.button_down.a = false;
            }
            if(event.key == "s") {
                this.button_down.s = false;
            }
            if(event.key == "d") {
                this.button_down.d = false;
            }
        } else {
            if(event.key == "ArrowUp") {
                this.scrollplane.MoveSourcePanel(1);
            }
            if(event.key == "ArrowDown") {
                this.scrollplane.MoveSourcePanel(-1);
            }
            if(event.key == "a") {
                this.button_down.a = true;
                this.button_down.s = false;
                this.button_down.d = false;
            }
            if(event.key == "s") {
                this.button_down.a = false;
                this.button_down.s = true;
                this.button_down.d = false;
            }
            if(event.key == "d") {
                this.button_down.a = false;
                this.button_down.s = false;
                this.button_down.d = true;
            }
        }
    }

    OnClickPlay() {

    }

    OnClickStepOver() {

    }

    OnClickStop() {

    }

    OnClickReset() {

    }

    OnDrag(event){ 
        for (const element of this.items) {
            if(element instanceof ScrollingPlane) {
                element.OnDrag(event);
            }
        }
    }

    OnRelease(event) {
        this.mouseDown = false;
        for (const item of this.items) {
            if(item instanceof ScrollingPlane) {
                item.OnRelease(event);
            }
        }
    }

    OnClick(event) {
        this.mouseDown = true;
        if(!this.disable_input) {
            for (const item of this.items) {
                if(item.IsInside(event.realpos)) {
                    if(item instanceof Rect){
                        return;
                    } else if (item instanceof Button) {
                        item.OnClick(event);
                        return;
                    } else if (item instanceof Tab) {
                        return;
                    } else if (item instanceof ScrollingPlane) {
                        if (this.running) {
                            return;
                        }
                        item.OnClick(event);
                        return;
                    } else {
                        console.log("Undefined click");
                        return;
                    }
                } 
            }
        }
    }

    ChangeBackgroundColor(event){
        this.background_color_index = (this.background_color_index + 1) % COLOR.COLOR_LIST.length;
        this.background_color = COLOR.COLOR_LIST[this.background_color_index];
    }

    EventPos(event) {
        return [Math.round((event.clientX - this.canvasRect.left) / (this.canvasRect.right - this.canvasRect.left) * this.canvas.width),
                    Math.round((event.clientY - this.canvasRect.top) / (this.canvasRect.bottom - this.canvasRect.top) * this.canvas.height)];
    }

}