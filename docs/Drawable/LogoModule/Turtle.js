import { COLOR } from "../../System/Constants.js";
import { Line, Flood } from "../RenderItems.js";

export class Turtle {
    constructor() {
        [this.pos_x, this.pos_y] = [315, 300];
        this.base = {
            "x": this.pos_x,
            "y": this.pos_y
        };
        this.rotation = 0;
        this.show_turtle = true;
        this.pen_color = COLOR.BLACK;
        this.pen_down = true;
        this.pen_width = 1;
        this.distortion = 0;

        this.lines = [];

        this.boundaries = {
            "top": null,
            "bot": null
        };
    }

    Forward(distance = 20) {
        var [start_x, start_y] = [this.pos_x, this.pos_y];
        [this.pos_x, this.pos_y] = this.Move(1, distance);
        this.NormalizeMovement();
        var [end_x, end_y] = [this.pos_x, this.pos_y];
        var line_o = new Line([start_x + this.distortion, start_y + this.distortion], [end_x + this.distortion, end_y + this.distortion],
            this.pen_color, this.pen_width, this.pen_down);
        this.lines.push(line_o);
    }

    Backward(distance = 20) {
        var [start_x, start_y] = [this.pos_x, this.pos_y];
        [this.pos_x, this.pos_y] = this.Move(-1, distance);
        this.NormalizeMovement();
        var [end_x, end_y] = [this.pos_x, this.pos_y];
        var line_o = new Line([start_x + this.distortion, start_y + this.distortion], [end_x + this.distortion, end_y + this.distortion],
            this.pen_color, this.pen_width, this.pen_down);
        this.lines.push(line_o);
    }

    Right(angle = 90) {
        this.rotation += angle;
        this.rotation %= 360;
    }

    Left(angle = 90) {
        this.rotation -= angle;
        this.rotation %= 360;
    }

    Home() {
        var [start_x, start_y] = [this.pos_x, this.pos_y];
        [this.pos_x, this.pos_y] = [this.base.x, this.base.y];
        var [end_x, end_y] = [this.pos_x, this.pos_y];
        var line_o = new Line([start_x + this.distortion, start_y + this.distortion], [end_x + this.distortion, end_y + this.distortion],
            this.pen_color, this.pen_width, this.pen_down);
        this.lines.push(line_o);
    }

    PenDown() {
        this.pen_down = true;
    }

    PenUp() {
        this.pen_down = false;
    }

    Width(size) {
        this.pen_width = size;
    }

    Color(color) {
        this.pen_color = color;
    }

    Fill() {
        var flood = new Flood([this.pos_x, this.pos_y], this.pen_color);
        this.lines.push(flood);
    }

    Reset() {
        [this.pos_x, this.pos_y] = [this.base.x, this.base.y];
        this.lines = [];
        this.rotation = 0;
        this.pen_color = COLOR.BLACK;
        this.pen_width = 3;
        this.pen_down = true;
        this.show_turtle = true;
    }

    Clear() {
        this.lines = []
    }

    ShowTurtle() {
        this.show_turtle = true;
    }

    HideTurtle() {
        this.show_turtle = false;
    }

    Move(direction, distance) {
        return [Math.trunc(Math.round(this.pos_x + (distance * Math.cos(Math.PI / 180 * this.rotation)) * direction)),
        Math.trunc(Math.round(this.pos_y + (distance * Math.sin(Math.PI / 180 * this.rotation)) * direction))];
    }

    Debug() {
        console.log(this.pos_x, this.pos_y);
        console.log(this.rotation);
    }


    GetTurtleInformationToRender() {
        return [[this.pos_x, this.pos_y], this.rotation, this.show_turtle]
    }

    GetLinesForRenderer() {
        return this.lines
    }

    SetDistortion(amount) {
        this.distortion = amount;
    }

    SetBoundaries(top, bot) {
        this.boundaries.top = top;
        this.boundaries.bot = bot;
    }

    NormalizeMovement() {
        if (this.boundaries.top != null && this.boundaries["bot"] != null) {
            if (this.pos_x < this.boundaries.top[0]) {
                this.pos_x = this.boundaries.top[0];
            }
            if (this.pos_x > this.boundaries.bot[0]) {
                this.pos_x = this.boundaries.bot[0];
            }
            if (this.pos_y < this.boundaries.top[1]) {
                this.pos_y = this.boundaries.top[1];
            }
            if (this.pos_y > this.boundaries.bot[1]) {
                this.pos_y = this.boundaries.bot[1];
            }

        }
    }

}