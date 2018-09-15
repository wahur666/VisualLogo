import { COLOR, FONT_AWESOME } from "../System/Constants.js";
import { Timer } from "../System/Timer.js";
import { Button } from "./Button.js";
import { DrawingIcon } from "./DrawingIcon.js";
import { Rect } from "./Rectangle.js";
import { ScrollingPlane } from "./ScrollingPlane.js";

export class GUI {
    constructor(application_core){
        this.application_core = application_core;
        this.items = [];
        this.Initialize();
    }

    Initialize() {
        this.drawingWindow = new Rect(20, 20, 630, 600, COLOR.BLACK, 1, false, false);
        this.Add(this.drawingWindow);

        var buttonPlay = new Button(380, 640, 60, 60, undefined, FONT_AWESOME.PLAY, 5);
        buttonPlay.Bind(this.OnClickPlay);
        buttonPlay.SetAccentColor(COLOR.HATTER_1);
        this.Add(buttonPlay);

        var buttonStepOver = new  Button(450, 640, 60, 60, undefined, FONT_AWESOME.STEPOVER, 10);
        buttonStepOver.Bind(this.OnClickStepOver);
        buttonStepOver.SetAccentColor(COLOR.HATTER_4);
        this.Add(buttonStepOver);

        var buttonStop = new Button(520, 640, 60, 60, undefined, FONT_AWESOME.STOP, 4);
        buttonStop.Bind(this.OnClickStop);
        buttonStop.SetAccentColor(COLOR.HATTER_7);
        this.Add(buttonStop);

        var buttonReset = new Button(590, 640, 60, 60, undefined, FONT_AWESOME.RESET, 4);
        buttonReset.Bind(this.OnClickReset);
        buttonReset.SetAccentColor(COLOR.HATTER_8);
        this.Add(buttonReset);

        var buttonBackground = new Button(20, 660, 40,40, undefined, FONT_AWESOME.BACKGROUND_PICTURE, -1);
        buttonBackground.Bind(this.OnClickBackground);
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

    DrawGUI(screen){
        this.items.forEach(element => {
            element.DrawObject(screen);
        });
    }

    Add(item){
        this.items.push(item);
    }

    OnClickPlay() {

    }

    OnClickStepOver() {

    }

    OnClickStop() {

    }
}