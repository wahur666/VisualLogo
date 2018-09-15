import { AbstractDrawable } from "./Base/AbstractDrawable.js";
import { FONT_AWESOME, COLOR } from "../System/Constants.js";

export class TextIcon extends AbstractDrawable {

    constructor(x = null, y = null, w = null, h = null, keycode = FONT_AWESOME.PLACEHOLDER, color = COLOR.BLACK) {
        super(x, y + h * 0.8, w, h);

        this.keycode = keycode;
        this.text = null;
        this.pad_x = 0;
        this.color = color;
    }

    IsInside(position) {
        return this.x <= position[0] && this.x + this.h >= position[0] && this.y <= position[1] && self.y + self.w >= position[1];
    }

    DrawObject(screen) {
        screen.save();

        screen.font =  this.h - 6 + "px FontAwesome";
        screen.fillStyle =this.color;
        screen.fillText(this.keycode, this.x + this.pad_x , this.y);

        screen.restore();
    }

    SetPadding(x) {
        this.pad_x = x;
    }

    SetColor(color) {
        this.color = color;
    }

}