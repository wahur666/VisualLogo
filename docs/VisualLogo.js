import { COLOR } from "./System/Constants.js";
import { Turtle } from "./Drawable/LogoModule/Turtle.js";
import { GUI } from "./Drawable/GUI.js";

export class ApplicationCore {

    constructor(screen) {
        this.background_color = COLOR.LIGHTGRAY;
        this.background_color_index = 7;
        this.screen = screen;

        this.version = "1.2.3";
        
        this.logoCore = new Turtle();
        this.logoCore.SetBoundaries([20, 20], [650, 620])

        this.gui = new GUI(this);

        this.gameExit = false;

    }

    Exit(){
        this.gameExit = true;
    }

    Run() {

    }

    Debug() {
        this.logoCore.Debug();
        this.logoCore.Forward();
        this.logoCore.Forward();
        this.logoCore.Debug();
    }

    

}