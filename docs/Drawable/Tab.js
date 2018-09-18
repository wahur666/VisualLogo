import { Polygon } from "./Polygon.js";
import { COLOR } from "../System/Constants.js";

export class Tab extends Polygon {

    constructor(x, y, w, h, color = COLOR.BLACK, id = null, width = 0, transparent = true) {
        super(null, color, width);
        this.x = x;
        this.y = y;
        this.w = w;
        this.h = h;
        this.id = id;
        this.darkAccent = COLOR.GREY;
        this.lightAccent = 'rgba(200, 200, 200, 255)';
        this.transparent = transparent;
        this.selected = false;
        this.coordinates = this.CalculatePoints();
        this.base = {
            "x": this.x,
            "y": this.y,
            "h": this.h,
            "w": this.w
        }
    }

    IsInside(position) {
        return this.x <= position[0] && this.x + this.w >= position[0] && this.y <= position[1] && this.y + this.h >= position[1];
    }

    DrawObject(screen) {
        super.coordinates = this.CalculatePoints();
        if (!this.transparent) {
            if (this.selected) {
                this.accentColor = this.darkAccent;
            } else {
                this.accentColor = this.lightAccent;
            }
        }
        super.DrawObject(screen);
    }

    GetId() {
        return this.id;
    }

    CalculatePoints() {
        var points = [];
        var percentToCut = 0.2;

        var tl = [this.x, this.y];
        var tr = [this.x + this.w, this.y];
        var bl = [this.x, this.y + this.h];
        var br = [this.x + this.w, this.y + this.h];
        var edgeCut = Math.trunc(this.h * percentToCut);

        points.push([tl[0], tl[1] + edgeCut])
        points.push([tl[0] + edgeCut, tl[1]])
        points.push([tr[0] - edgeCut, tr[1]])
        points.push([tr[0], tr[1] + edgeCut])
        points.push(br)
        points.push(bl)

        return points
    }

    UpdatePoints() {
        this.coordinates = this.CalculatePoints();
    }

    ResetPositions() {
        this.y = this.base.y;
        this.h = this.base.h;
        this.UpdatePoints();
    }

}