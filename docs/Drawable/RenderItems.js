import { COLOR } from "../System/Constants.js";
import { DrawLine } from "../System/SupportFunctions.js";

export class Line {
    constructor(vec2Start = null, vec2End = null, color = COLOR.BLACK, width = 1, penDown = true) {
        this.vec2Start = vec2Start;
        this.vec2End = vec2End;
        this.color = color;
        this.width = width;
        this.penDown = penDown;
    }

    DrawObject(screen) {
        if (this.penDown) {
            DrawLine(screen, this.color, this.vec2Start, this.vec2End, this.width);
        }
    }
}

export class Node {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

export class Flood {
    constructor(vec2pos = null, color = COLOR.BLACK) {
        this.vec2pos = vec2pos;
        this.color = color;
        this.calculated = false;
        this.pixelArray = null;
    }

    DrawObject(screen) {
       
    }

}