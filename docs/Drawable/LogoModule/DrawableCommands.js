import { Command } from "../Base/Command.js";
import { FONT_AWESOME, COLOR, IMG } from "../../System/Constants.js";
import { DrawPolygon } from "../../System/SupportFunctions.js";

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

    }
}

export class PenColor extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

    }
}

export class FloodFill extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

    }
}

export class Reset extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

    }
}

export class Clear extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

    }
}

export class ShowTurtle extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

    }
}

export class HideTurtle extends Command {
    constructor(x = null, y = null, w = null, h = null, imgPath = null) {
        super(x, y, w, h);

    }
}