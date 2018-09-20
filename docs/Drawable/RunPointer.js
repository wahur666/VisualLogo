import { Polygon } from "./Polygon.js";
import { COLOR } from "../System/Constants.js";

export class RunPointer extends Polygon {
    constructor(x, y, w, h, color=COLOR.BLACK, width=0) {
        super(undefined, color, width);
        this.x = x;
        this.y = y;
        this.w = w;
        this.h = h;
        this.base_coordinates = this.CalculatePoints();
        this.coordinates = this.CalculatePoints();
        this.transparent = true;
        this.base = {
            "x": this.x,
            "y": this.y,
            "h": this.h,
            "w": this.w
        };
    }

    CalculatePoints() {
        var points = [];

        var p1 = [this.x + this.w / 2, this.y];
        var p2 = [this.x - this.w / 2, this.y - this.h / 2];
        var p3 = [this.x - this.w / 2, this.y + this.h / 2];

        points.push(p3);
        points.push(p1);
        points.push(p2);

        return points;
    }

    SetPosition(x, y) {
        this.x = x;
        this.y = y;
        this.UpdatePoints();
    }

    IsInside(position){
        return false;
    }

    UpdatePoints() {
        this.coordinates = this.CalculatePoints();
    }
}