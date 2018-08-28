export class Vector2 {
    constructor(x, y){
        this.x = x;
        this.y = y;
    }
}

export function MoveElementList(list, element, index) {
    list.splice(list.indexOf(element), 1);
    list.splice(index, 0, element);
    return list;
}

export function DrawRect(canvasContext, color, x, y, w, h, width = 0) {
    canvasContext.beginPath();
    if(width == 0){
        canvasContext.fillStyle=color;
        canvasContext.fillRect(x, y, w, h);
    } else {
        canvasContext.lineWidth = width;
        canvasContext.strokeStyle=color;
        canvasContext.rect(x, y, w, h);
        canvasContext.stroke();
    }
}