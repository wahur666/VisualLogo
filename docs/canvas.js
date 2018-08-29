import { Rect } from "./Drawable/Rectangle.js";
import { COLOR } from "./System/Constants.js";
import { Polygon } from "./Drawable/Polygon.js";
import { DrawLines } from "./System/SupportFunctions.js";
import { DrawingIcon } from "./Drawable/DrawingIcon.js";


var canvas = document.querySelector('canvas');

var canvasContext = canvas.getContext("2d");
/*

canvasContext.beginPath();
canvasContext.fillStyle='rgba(255, 0, 0, 255)';
canvasContext.fillRect(40, 40, 150, 100);
canvasContext.beginPath();
canvasContext.strokeStyle="#00ff00ff";
canvasContext.rect(20, 20, 150, 100);
canvasContext.stroke();

canvasContext.beginPath();
canvasContext.strokeStyle="#0000ffff";
canvasContext.rect(200, 200, 150, 100);
canvasContext.stroke();*/

/*var rect1 = new Rect(20, 20, 150, 100, COLOR.BLUE, 2, undefined, undefined, undefined, false);
rect1.DrawObject(canvasContext);
*/
//var poly1 = new Polygon([[20,20], [20, 59], [90, 90], [150, 100], [70, 33], [27, 45]], COLOR.RED, 2);
//poly1.DrawObject(canvasContext);

var drawingIcon = new DrawingIcon(50,50,30,30,COLOR.RED, 0);
drawingIcon.DrawObject(canvasContext, 0);