import { AbstractDrawable } from "./Base/AbstractDrawable.js";
import { COLOR } from "../System/Constants.js";
import { DrawPolygon } from "../System/SupportFunctions.js";

export class Polygon extends AbstractDrawable{

    constructor(coordinates, color=COLOR.BLACK, width=0) {
        super();
        this.coordinates = coordinates;
        this.color = color;
        this.width = width;
        this.accentColor = COLOR.WHITE;
        this.transparent = false;
        this.base = { "coords" : this.coordinates };
    }

    DrawObject(screen) {
        if(!this.transparent){
            DrawPolygon(screen, this.accentColor, this.coordinates);
        }
        DrawPolygon(screen, this.color, this.coordinates, this.width);
    }

    IsInside(position) {
    }

    ResetPosition(){
        this.coordinates = this.base.coordinates;
    }

    GetParameters(){
    }
}