import { AbstractDrawable } from "./Base/AbstractDrawable.js";
import { COLOR } from "../System/Constants.js";
import { DrawRect } from "../System/SupportFunctions.js";

export class Rect extends AbstractDrawable {

    constructor( x = null, y = null, w = null, h = null, color=COLOR.BLACK, width = 0, movable = false, vec2_pos = null, size = null, transparent = true) {
        super(x, y, w, h, vec2_pos, size);
        this.delta = [0, 0];
        this.color = color;
        this.width = width;
        this.movable = movable;
        this.transparent = transparent;
        this.accentColor = COLOR.WHITE;
        this.Clickable = true;
    }
    
    DrawObject(screen) {
        if(!this.transparent){
            DrawRect(screen, this.accentColor, this.x, this.y, this.w, this.h);
        }
        DrawRect(screen, this.color, this.x, this.y, this.w, this.h, this.width);
    }

}