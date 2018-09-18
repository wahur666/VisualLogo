import { Turtle } from "./Drawable/LogoModule/Turtle.js";
import { GUI } from "./Drawable/GUI.js";

export class ApplicationCore {

    constructor(canvas) {
        this.canvas = canvas;
        this.version = "1.2.3";

        this.logoCore = new Turtle();
        this.logoCore.SetBoundaries([20, 20], [650, 620])

        this.gui = new GUI(this);
        
        this.SetupHandlers();
    }

    SetupHandlers() {
        this.canvas.oncontextmenu = function (e) {
            e.preventDefault();
        };

        this.canvas.addEventListener("mousedown", (event) => this.MouseHandler(event), false);

        this.canvas.addEventListener("mouseup", (event) => this.MouseHandler(event), false);

        this.canvas.addEventListener("wheel",  (event) => this.MouseHandler(event), false);

        this.canvas.addEventListener("mousemove", (event) => this.MouseHandler(event), false);

        this.canvas.addEventListener("mouseout", (event) => this.MouseHandler(event), false);

        window.addEventListener("keydown", (event) => this.KeyboardHandler(event), false);
        
        window.addEventListener("keyup", (event) => this.KeyboardHandler(event), false);

    }

    MouseHandler(event) {
        this.gui.MouseHandler(event);
    }

    KeyboardHandler(event) {
        this.gui.KeyboardHandler(event);
    }

    Update() {
        this.gui.DrawGUI();
    }

    Debug() {
        this.logoCore.Debug();
        this.logoCore.Forward();
        this.logoCore.Forward();
        this.logoCore.Debug();
    }

}