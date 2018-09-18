import { AbstractDrawable } from "./Base/AbstractDrawable.js";
import { IMG } from "../System/Constants.js";


export class Sprite extends AbstractDrawable {

    constructor(x = null, y = null, w = null, h = null, imgpath = IMG.PLACEHOLDER, mode = 0, index = null ) {
        super(x, y, w, h);
        this.base_rotation = 0;
        this.index = index;
        
        this.imgpath = imgpath;
        this.image = new Image();
        this.image.src = this.imgpath;

        this.loaded = false;

        this.image.onload = () => this.loaded = true;
    }

    DrawObject(screen, rotation = 0) {
        if(this.loaded){
            this.DrawRotatedImage(screen, rotation);
        }
    }

    DrawRotatedImage(screen, rotation) {
        var halfWidth = this.w / 2;
        var halfHeight = this.h / 2;

        screen.save();

        screen.translate(this.x + halfWidth, this.y + halfHeight);
        screen.rotate(rotation * Math.PI / 180)
        screen.drawImage(this.image, -halfWidth, -halfHeight, this.w, this.h);

        screen.restore();
    }

    IsInside(position) {
        return this.x <= position[0] && this.x + this.h >= position[0] && this.y <= position[1] && this.y + this.w >= position[1];
    }

}