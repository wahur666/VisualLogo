import { Rect } from "./Rectangle.js";
import { COLOR, FONT_AWESOME } from "../System/Constants.js";
import { Button } from "./Button.js";

export class GUI {
    constructor(application_core){
        this.application_core = application_core;
        this.items = [];
        this.Initialize();
    }

    Initialize() {
        this.drawingWindow = new Rect(20, 20, 630, 600, COLOR.BLACK, 1, undefined, undefined, undefined, false);
        this.Add(this.drawingWindow);

        var buttonPlay = new Button(380, 640, 60, 60, undefined, undefined, undefined, FONT_AWESOME.PLAY, 5);
        buttonPlay.Bind(this.OnClickPlay);
        buttonPlay.SetAccentColor(COLOR.HATTER_1);
        this.Add(buttonPlay);

        var buttonStepOver = new  Button(450, 640, 60, 60, undefined, undefined, undefined, FONT_AWESOME.STEPOVER, 10);
        buttonStepOver.Bind(this.OnClickStepOver);
        buttonStepOver.SetAccentColor(COLOR.HATTER_4);
        this.Add(buttonStepOver);

        var buttonStop = new Button(520, 640, 60, 60, undefined, undefined, undefined, FONT_AWESOME.STOP, 4);
        buttonStop.Bind(this.OnClickStop);
        buttonStop.SetAccentColor(COLOR.HATTER_7);
        this.Add(buttonStop);

        var buttonReset = new Button(590, 640, 60, 60, undefined, undefined, undefined, FONT_AWESOME.RESET, 4);
        buttonReset.Bind(this.OnClickReset);
        buttonReset.SetAccentColor(COLOR.HATTER_8);
        this.Add(buttonReset);

        var buttonBackground = new Button(20, 660, 40,40, undefined, undefined, undefined, FONT_AWESOME.BACKGROUND_PICTURE, -1);
        buttonBackground.Bind(this.OnClickBackground);
        this.Add(buttonBackground);
    }

    DrawGUI(screen){
        this.items.forEach(element => {
            element.DrawObject(screen)
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