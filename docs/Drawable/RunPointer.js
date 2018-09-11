import { Polygon } from "./Polygon.js";
import { COLOR } from "../System/Constants.js";

export class RunPointer extends Polygon {
    constructor(x, y, w, h, color=COLOR.BLACK, width=0) {
        super(undefined, color, width);

    }

    CalculatePoints() {

    }

    SetPosition(x, y) {

    }

    IsInside(position){
        return false;
    }

    UpdatePoints() {
        
    }
}