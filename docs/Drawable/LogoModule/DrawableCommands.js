import { Command } from "../Base/Command.js";
import { FONT_AWESOME, COLOR, IMG } from "../../System/Constants.js";
import { DrawPolygon, DrawCircle } from "../../System/SupportFunctions.js";
import { Rect } from "../Rectangle.js";

export class Forward extends Command {

    constructor(x = null, y = null, w = null, h = null, imgPath = null, mul = 1) {
        super(x, y, w, h);
        this.imagePath = imgPath;
        this.mul = mul;
        if (this.mul == 1) {
            this.keyCode = FONT_AWESOME.UP;
            this.SetKeyCodePadding(5);
        } else if (this.mul == 2) {
            this.keyCode = FONT_AWESOME.LONG_UP;
            this.SetKeyCodePadding(15);
        }

        this.mainRect.SetAccentColor(COLOR.HATTER_1);
    }

}

export class Backward extends Command {

    constructor(x = null, y = null, w = null, h = null, imgPath = null, mul = 1) {
        super(x, y, w, h);
        this.imagePath = imgPath;
        this.mul = mul;
        if (this.mul == 1) {
            this.keyCode = FONT_AWESOME.DOWN;
            this.SetKeyCodePadding(5);
        } else if (this.mul == 2) {
            this.keyCode = FONT_AWESOME.LONG_DOWN;
            this.SetKeyCodePadding(15);
        }

        this.mainRect.SetAccentColor(COLOR.HATTER_1);
    }

}

export class Right extends Command {

    constructor(x = null, y = null, w = null, h = null, imgPath = null, mul = 2) {
        super(x, y, w, h);
        this.mul = mul;
        if (this.mul == 2) {
            this.imagePath = IMG.BEND_RIGHT;
        } else if (this.mul == 6) {
            this.imagePath = IMG.TURN_RIGHT;
        }

        this.mainRect.SetAccentColor(COLOR.HATTER_2);
    }

}

export class Left extends Command {

    constructor(x = null, y = null, w = null, h = null, imgPath = null, mul = 2) {
        super(x, y, w, h);
        this.mul = mul;
        if (this.mul == 2) {
            this.imagePath = IMG.BEND_LEFT;
        } else if (this.mul == 6) {
            this.imagePath = IMG.TURN_LEFT;
        }

        this.mainRect.SetAccentColor(COLOR.HATTER_2);
    }

}

export class Home extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

        this.imagePath = imgPath;
        this.keyCode = FONT_AWESOME.HOME;
        this.SetKeyCodePadding(5);
        this.mainRect.SetAccentColor(COLOR.HATTER_3);
    }
}

export class PenDown extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);
        
        this.keyCode = FONT_AWESOME.PEN;
        this.SetKeyCodePadding(5);
        this.mainRect.SetAccentColor(COLOR.HATTER_4);
    }
}

export class PenUp extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

        this.keyCode = FONT_AWESOME.PEN;
        this.SetKeyCodePadding(5);
        this.mainRect.SetAccentColor(COLOR.HATTER_4);

        this.cross_points = [[this.x + 10, this.y + 5],
                             [this.x + 5, this.y + 10],
                             [this.x + this.w - 10, this.y + this.h - 5],
                             [this.x + this.w - 5, this.y + this.h - 10]];
    }

    DrawObject(screen){
        super.DrawObject(screen);
        DrawPolygon(screen, COLOR.RED, this.cross_points, 0);
    }
        

    SetPosition(x, y){
        super.SetPosition(x, y);
        this.cross_points = [[this.x + 10, this.y + 5],
                             [this.x + 5, this.y + 10],
                             [this.x + this.w - 10, this.y + this.h - 5],
                             [this.x + this.w - 5, this.y + this.h - 10]];
    }       
}

export class PenWidth extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);
        this.keyCode = FONT_AWESOME.PLACEHOLDER;
        
        this.pen_width = 0;
        this.mainRect.SetAccentColor(COLOR.HATTER_6);
        this.widthRect = new Rect(this.x, this.y, this.w, this.h, COLOR.BLACK);
    }

    DrawObject(screen) {
        this.mainRect.DrawObject(screen);
        this.widthRect.Extend(this.y + this.h / 2 - this.pen_width * 5, this.pen_width * 10 + 2);
        
        this.widthRect.DrawObject(screen);
    }

    Extend() {
        this.pen_width = (this.pen_width + 1) % 4;
    }

    SetPosition(x, y) {
        super.SetPosition(x, y);
        this.widthRect.SetPosition(x, y);
    }

    SetPenWidth(width) {
        this.pen_width = width;
    }
}

export class PenColor extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

        this.keyCode = FONT_AWESOME.PLACEHOLDER;

        this.colorList = COLOR.COLOR_LIST;
        this.currentColorIndex = 1;
        this.mainRect.SetAccentColor(COLOR.HATTER_6);
        this.penColor = this.colorList[this.currentColorIndex];
    }

    DrawObject(screen) {
        this.mainRect.DrawObject(screen);
        DrawCircle(screen, this.penColor, [this.x + this.w / 2, this.y + this.h /2], 15, 0);
    }

    ChangeColor() {
        this.currentColorIndex = (this.currentColorIndex + 1) % this.colorList.length;
        this.penColor = this.colorList[this.currentColorIndex];
    }

    SetColor(color) {
        this.penColor = color;
    }
}

export class FloodFill extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);
        
        this.keyCode = FONT_AWESOME.FLOODFILL;
        this.mainRect.SetAccentColor(COLOR.HATTER_3);
        super.SetKeyCodePadding(3);
    }
}


export class ShowTurtle extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

        this.keyCode = FONT_AWESOME.EYE_SEE;
        this.mainRect.SetAccentColor(COLOR.HATTER_4);
        super.SetKeyCodePadding(3);

    }
}

export class HideTurtle extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

        this.keyCode = FONT_AWESOME.EYE_NOT_SEE;
        this.mainRect.SetAccentColor(COLOR.HATTER_4);
        super.SetKeyCodePadding(3);
    }
}

export class Loop extends Command {

    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

        this.keyCode = FONT_AWESOME.LOOP;
        this.loopend = null;

        this.cycleNumber = 3;
        this.remainingCycle = this.cycleNumber;

        this.RollColor();

        this.compileInformation = {
            "compiled" : false,
            "pre_test" : false,
            "loopend_index" : -1
        };

        this.running = false;
        this.mainRect.SetAccentColor(COLOR.HATTER_5);
        super.SetKeyCodePadding(5);

        this.InitCycleDisplayMatrix();

        this.loop_id = null;
        this.ark_level = 0;
    }

    InitCycleDisplayMatrix() {
        this.cycle_display_matrix = [];
        var matix_number = [0, 0, 0,
                        0, 0, 0,
                        0, 0, 0];
        this.cycle_display_matrix.push(matix_number); //0

        var matix_number = [0, 0, 0,
                        0, 1, 0,
                        0, 0, 0];
        this.cycle_display_matrix.push(matix_number); //1

        var matix_number = [1, 0, 0,
                        0, 0, 0,
                        0, 0, 1];
        this.cycle_display_matrix.push(matix_number); //2

        var matix_number = [1, 0, 0,
                        0, 1, 0,
                        0, 0, 1];
        this.cycle_display_matrix.push(matix_number); //3

        var matix_number = [1, 0, 1,
                        0, 0, 0,
                        1, 0, 1];
        this.cycle_display_matrix.push(matix_number); //4

        var matix_number = [1, 0, 1,
                        0, 1, 0,
                        1, 0, 1];
        this.cycle_display_matrix.push(matix_number); //5

        var matix_number = [1, 0, 1,
                        1, 0, 1,
                        1, 0, 1];
        this.cycle_display_matrix.push(matix_number); //6

        var matix_number = [1, 0, 1,
                        1, 1, 1,
                        1, 0, 1];
        this.cycle_display_matrix.push(matix_number); //7

        var matix_number = [1, 1, 1,
                        1, 0, 1,
                        1, 1, 1];
        this.cycle_display_matrix.push(matix_number); //8

        var matix_number = [1, 1, 1,
                        1, 1, 1,
                        1, 1, 1];
        this.cycle_display_matrix.push(matix_number); //9
    }

    DrawObject(screen) {
        super.DrawObject(screen);
        this.DrawRemainingCycleMatrix(screen);
    }

    DrawRemainingCycleMatrix(screen) {
        var amount = 0;
        if(this.running) {
            amount = this.remainingCycle;
        } else {
            amount = this.cycleNumber;
        }
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if(this.cycle_display_matrix[amount][i * 3 + j]) {
                    var pos_x = 8 + j * 16 + this.x + 55;
                    var pos_y = 8 + i * 16 + this.y + 1;
                    DrawCircle(screen, COLOR.MAGENTA, [pos_x, pos_y], 5, 0);
                }
            }
        }
    }

    RollColor() {
        this.color = Math.floor(Math.random() * COLOR.LOOP_COLORS.length);
    }

}