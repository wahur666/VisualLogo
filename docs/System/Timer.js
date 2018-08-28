export class Timer {
    constructor() {
        this.counter = 0;
    }

    wait(sec) {
        this.counter = sec * 60;
    }

    tick() {
        if(this.counter > 0){
            this.counter -= 1;
        }
    }

    is_waiting(){
        return this.counter != 0;
    }

    stop(){
        this.counter = 0;
    }
}