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

export function DrawPolygon(canvasContext, color, pointlist, width = 0) {
    canvasContext.beginPath();
    if(width > 0){
        canvasContext.strokeStyle = color;
    } else {
        canvasContext.fillStyle = color;
    }

    canvasContext.moveTo(pointlist[0][0], pointlist[0][1]);
    if(width > 0) {
        canvasContext.lineWidth = width;
    }

    for (let index = 1; index < pointlist.length; index++) {
        const element = pointlist[index];
        canvasContext.lineTo(element[0], element[1]);
    }


    canvasContext.closePath();
    if(width == 0){
        canvasContext.fill();
    } else {
        canvasContext.stroke();
    }

}

export function DrawLines(canvasContext, color, closed, pointlist, width = 1) {
    canvasContext.beginPath();
    if(!closed){
        canvasContext.strokeStyle = color;
    } else {
        canvasContext.fillStyle = color;
    }

    canvasContext.moveTo(pointlist[0][0], pointlist[0][1]);
    if(!closed) {
        canvasContext.lineWidth = width;
    }

    for (let index = 1; index < pointlist.length; index++) {
        const element = pointlist[index];
        canvasContext.lineTo(element[0], element[1]);
    }

    if(closed){
        canvasContext.closePath();
        canvasContext.fill();
    } else {
        canvasContext.stroke();
    }

}