import { COLOR } from "../../System/Constants.js";
import { Line } from "../RenderItems.js";

export class Turtle {
    constructor() {
        [this.pos_x, this.pos_y] = [315, 300];
        this.base = {
            "x" : this.pos_x,
            "y" : this.pos_y
        };
        this.rotation = 0;
        this.show_turtle = true;
        this.pen_color = COLOR.BLACK;
        this.pen_down = true;
        this.pen_width = 1;
        this.distortion = 0;
        
        this.lines = [];

        this.boundaries = {
            "top" : null,
            "bot" : null
        };
    }

    SetBoundaries() {
        
    }

    Forward(distance = 20) {
        var [start_x, start_y] = [this.pos_x, this.pos_y];
        [this.pos_x, this.pos_y] = this.Move(1, distance);
        this.NormalizeMovement();
        var [end_x, end_y] = [this.pos_x, this.pos_y];
        line_o = new Line();
    }

    Backward(distance = 20) {

    }

    Right(angle = 90) {
        
    }
    
    Move() {

    }

    NormalizeMovement(){

    }
}