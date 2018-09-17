import { ApplicationCore } from "./VisualLogo.js";

var canvas = document.querySelector('canvas');
var applicationCore = new ApplicationCore(canvas);

function mainLoop(){
    applicationCore.Run();
    requestAnimationFrame(mainLoop);
}

mainLoop();