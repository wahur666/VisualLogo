import { ApplicationCore } from "./VisualLogo.js";


var canvas = document.querySelector('canvas');

var canvasContext = canvas.getContext("2d");
var canvasRect = canvas.getBoundingClientRect();
var mouseDown = false;

canvas.addEventListener("mousedown", function(event) {
    mouseDown = true;
    console.log(event.button);
}, false);

canvas.addEventListener("mouseup", function(event) {
    console.log(event.button);
    mouseDown = false;
}, false);

canvas.oncontextmenu = function (e) {
    e.preventDefault();
};

canvas.addEventListener("wheel", function(event) {
    console.log(event.deltaY);
}, false);

canvas.addEventListener("mousemove", function(event){
    if(mouseDown){
        console.log(Math.round((event.clientX - canvasRect.left) / (canvasRect.right - canvasRect.left) * canvas.width),
                    Math.round((event.clientY - canvasRect.top) / (canvasRect.bottom - canvasRect.top) * canvas.height))
    }
}, false);


var applicationCore = new ApplicationCore(canvas);

function mainLoop(){
    applicationCore.Run();
    requestAnimationFrame(mainLoop);
}

mainLoop();