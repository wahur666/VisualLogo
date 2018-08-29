import { Vector2 } from "../../System/SupportFunctions.js";

export class AbstractDrawable {
    constructor(x = null, y = null, w = null, h = null, vec2_pos = null, size = null) {
        if(x == null && y == null && w == null && h == null && vec2_pos == null && size == null){
            return;
        }
        if ( x != null && y != null) {
            this.x = x;
            this.y = y;
        } else if ( x == null && y == null && vec2_pos != null) {
            if (!(vec2_pos instanceof Vector2)){
                throw "vec2_pos is not Vector2 type";
            }
            this.x = vec2_pos.x;
            this.y = vec2_pos.y;
        } else {
            throw "Not enough parameter, give X and Y, or Vec2_pos";
        } 

        if (w != null && h != null) {
            this.w = w
            this.h = h
        } else if (w == null && h == null && size != null){
            if(size.length == 2){
                self.w = size[0]
                self.h = size[1]
            } else {
                throw "size is not tuple(int, int) type";
            }
        } else {
            throw "Not enough parameter, give W and H, or size=tuple(int,int)";
        }
        this.base = {
            "x" : this.x,
            "y" : this.y,
            "h" : this.h,
            "w" : this.w
        }
    }

    DrawObject(screen){
        console.log("Abstract DrawObject");
    }

    IsInside(position){
        console.log("Abstract IsInside");
    }

    SetPosition(x, y){
        this.x = x;
        this.y = y;
    }

    ResetPosition() {
        this.x = this.base.x;
        this.y = this.base.y;
        this.h = this.base.h;
        this.w = this.base.w;
    }

    GetParameters(){
        return [this.x, this.y, this.w, this.h];
    }
}