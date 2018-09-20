import { COLOR } from "../System/Constants.js";
import { Polygon } from "./Polygon.js";
import { DrawLines } from "../System/SupportFunctions.js";

export class DrawingIcon extends Polygon{

    constructor(x, y, w, h, color=COLOR.BLACK, width=0){
        super([], color, width);
        this.x = x; 
        this.y = y;
        this.w = w;
        this.h = h;
        this.base_coordinates = this.CalculatePoints();
        this.coordinates = this.CalculatePoints();
        this.base_rotation = 0;
        this.transparent = true;
        this.base = {
            "x": this.x,
            "y": this.y,
            "h": this.h,
            "w": this.w
        };
    }

    SetPosition(x, y){
        this.x = x;
        this.y = y;
        this.UpdatePoints();
    }

    DrawObject(screen, rot){
        this.RotateToAngle(rot);
        super.DrawObject(screen);
        
        DrawLines(screen, COLOR.BLACK, false, this.coordinates, 1);
    }
    
   
    ResetPosition() {
        this.x = this.base.x;
        this.y = this.base.y;
        this.base_rotation = 0;
        this.UpdatePoints();
    }

    IsInside(position){
        return false;
    }

    UpdatePoints(){
        this.base_coordinates = this.CalculatePoints();
    }

    CalculatePoints(){
        var points = [];

        var origo = [this.x, this.y];
        var p1 = [this.x + this.w / 2, this.y];
        var p2 = [this.x - this.w / 2, this.y - this.h / 2];
        var p3 = [this.x - this.w / 2, this.y + this.h / 2];
    
        points.push(origo);
        points.push(p3);
        points.push(p1);
        points.push(p2);
        points.push(origo);
        
        return points;
    }
    
    RotateToAngle(angle) {
        var rot_diff = angle - this.base_rotation;
        this.coordinates = [];
        
        for (const element of this.base_coordinates) {
            var sf = Math.sin(Math.PI / 180 * rot_diff);
            var cf = Math.cos(Math.PI / 180 * rot_diff);
            var x = element[0] - this.base_coordinates[0][0];
            var y = element[1] - this.base_coordinates[0][1];
            
            var new_x = Math.trunc(Math.round(x * cf - y * sf)) + this.base_coordinates[0][0];
            var new_y = Math.trunc(Math.round(x * sf + y * cf)) + this.base_coordinates[0][1];
            this.coordinates.push([new_x, new_y]);
        }
    }
}