import { COLOR } from "./System/Constants.js";
import { Turtle } from "./Drawable/LogoModule/Turtle.js";
import { GUI } from "./Drawable/GUI.js";
import { DrawRect } from "./System/SupportFunctions.js";

export class ApplicationCore {

    constructor(canvas) {
        this.canvas = canvas;
        this.background_color = COLOR.LIGHTGRAY;
        this.background_color_index = 7;
        this.screen = canvas.getContext("2d");

        this.version = "1.2.3";
        
        this.logoCore = new Turtle();
        this.logoCore.SetBoundaries([20, 20], [650, 620])

        this.gui = new GUI(this);

    }

    Run() {
        DrawRect(this.screen, this.background_color, 0, 0, this.canvas.width, this.canvas.height, 0);
        this.gui.DrawGUI(this.screen);

    }

    Debug() {
        this.logoCore.Debug();
        this.logoCore.Forward();
        this.logoCore.Forward();
        this.logoCore.Debug();
    }

    

}