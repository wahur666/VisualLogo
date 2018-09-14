import { AbstractDrawable } from "./Base/AbstractDrawable.js";
import { COLOR } from "../System/Constants.js";
import { DrawRect } from "../System/SupportFunctions.js";

export class Rect extends AbstractDrawable {

    constructor(x = null, y = null, w = null, h = null, color = COLOR.BLACK, width = 0, movable = false, vec2_pos = null, size = null, transparent = true) {
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
        if (!this.transparent) {
            DrawRect(screen, this.accentColor, this.x, this.y, this.w, this.h, 0);
        }
        DrawRect(screen, this.color, this.x, this.y, this.w, this.h, this.width);
    }

    IsInside(position) {
        return this.x <= position[0] && this.x + this.h >= position[0] && this.y <= position[1] && self.y + self.w >= position[1];
    }

    DeltaPos(position) {
        return [position[0] - this.x, position[1] - this.y];
    }

    Drag(mousePosition) {
        this.x = mousePosition[0] - this.delta[0];
        this.y = mousePosition[1] - this.delta[1];
    }

    SetDelta(mousePosition) {
        this.delta = this.DeltaPos(mousePosition);
    }

    IsMovable() {
        return this.movable;
    }

    Extend(y, h) {
        this.y = y;
        this.h = h;
    }

    SetAccentColor(accent) {
        this.accentColor = accent;
    }

}