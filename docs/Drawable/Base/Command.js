import { AbstractDrawable } from "./AbstractDrawable.js";
import { Rect } from "../Rectangle.js";
import { TextIcon } from "../TextIcon.js";
import { Sprite } from "../Sprite.js";
import { IMG } from "../../System/Constants.js";

export class Command extends AbstractDrawable {
    constructor(x = null, y = null, w = null, h = null) {
        super(x, y, w, h);
        this.mainRect = new Rect(x, y, w, h, undefined, 1, undefined, false);
        this.sprite = null;
        this.imagePath = null;
        this.textIcon = null;
        this.keyCode = null;
        this.keyCodePad = 0;
    }

    ExecuteCommand() {
        console.log("Event didn't bound");
    }

    IsInside(position) {
        return this.x <= position[0] && this.x + this.w >= position[0] && this.y <= position[1] && this.y + self.h >= position[1];
    }

    DrawObject(screen) {
        if (! (this.sprite || this.textIcon)){
            this.LoadSprite()
        }
        this.mainRect.DrawObject(screen);
        if (this.sprite) {
            this.sprite.DrawObject(screen);
        }
        if (this.textIcon) {
            this.textIcon.DrawObject(screen);
        }
    }

    LoadSprite() {
        if (this.imagePath == null && this.keyCode != null) {
            this.textIcon = new TextIcon(this.x, this.y, this.w, this.h, this.keyCode, undefined);
            this.textIcon.SetPadding(this.keyCodePad)
            
        } else if (this.imagePath != null && this.keyCode == null) {
            this.sprite = new Sprite(this.x, this.y, this.w, this.h, this.imagePath);
        } else {
            this.sprite = new Sprite(this.x, this.y, this.w, this.h);
            console.log("Too many argument");
        }
    }
    
    SetPosition(x, y){
        this.x = x;
        this.y = y;
        this.mainRect.SetPosition(x,y);
        if(this.sprite){
            this.sprite.SetPosition(x,y);
        }

        if(this.textIcon){
            this.textIcon.SetPosition(x,y);
        }
    }

    Deltapos(position){
        return [position[0] - this.x, position[1] - this.y];
    }

    Drag(mouseposition) {
        var x = mouseposition[0] - this.delta[0];
        var y = mouseposition[1] - this.delta[1];
        this.SetPosition(x, y);
    }

    SetDelta(mouseposition){
        this.delta = this.Deltapos(mouseposition);
    }

    UnloadIcon(){
        this.textIcon = null;
    }

    Bind(function_pointer){
        this.ExecuteCommand = function_pointer;
    }

    SetAccentColor(accent){
        this.mainRect.SetAccentColor(accent);
    }

    SetKeyCodePadding(x){
        this.keyCodePad = x;
    }

}