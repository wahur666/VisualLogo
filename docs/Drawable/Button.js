import { AbstractDrawable } from "./Base/AbstractDrawable.js";
import { FONT_AWESOME, COLOR, IMG } from "../System/Constants.js";
import { Rect } from "./Rectangle.js";
import { Sprite } from "./Sprite.js";
import { TextIcon } from "./TextIcon.js";

export class Button extends AbstractDrawable {
    constructor(x = null, y = null, w = null, h = null, imgPath = IMG.PLACEHOLDER, keyCode=FONT_AWESOME.PLACEHOLDER, padding = 0) {
        super(x, y + 3, w, h);

        this.imgPath = imgPath;
        this.sprite = null;

        this.keyCode = keyCode;
        this.iconPadding = padding;
        this.textIcon = null
        
        this.textIconColor = COLOR.BLACK;

        this.buttonRect = new Rect(x, y, w, h, undefined, 1, undefined, false);
    }

    DrawObject(screen) {
        if(!this.textIcon){
            this.LoadImage();
        }
        this.buttonRect.DrawObject(screen);
        if(this.sprite){
            this.sprite.DrawObject(screen);
        }
        if(this.textIcon){
            this.textIcon.DrawObject(screen);
        }
    }

    IsInside(position){
        return this.x <= position[0] && this.x + this.h >= position[0] && this.y <= position[1] && this.y + this.w >= position[1];
    }

    Bind(funcPointer){
        this.OnClick = funcPointer;
    }

    OnClick(eventType) {
        console.log("Unbound button");
    }

    LoadImage(){
        if(this.imgPath != IMG.PLACEHOLDER) {
            this.sprite = new Sprite(this.x + 2, this.y + 2, this.w - 5, this.h + 5, this.imgPath)
        } else if (this.keyCode != FONT_AWESOME.PLACEHOLDER) {
            this.textIcon = new TextIcon(this.x + 5, this.y, this.w - 2, this.h - 5, this.keyCode, this.textIconColor);
            this.textIcon.SetPadding(this.iconPadding);
        } else {
            this.textIcon = new TextIcon(this.x + 5, this.y, this.w - 5, this.h - 5, FONT_AWESOME.PLACEHOLDER);
        }
    }

    SetAccentColor(accent) {
        this.buttonRect.SetAccentColor(accent);
    }

    SetTextIconColor(color){
        this.textIconColor = color;
    }
}