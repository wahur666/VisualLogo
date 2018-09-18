export class COLOR {

    static get WHITE() { return 'rgba(255, 255, 255, 255)' }
    static get BLACK() { return 'rgba(0, 0, 0, 255)' }
    static get RED() { return 'rgba(255, 0, 0, 255)' }
    static get GREEN() { return 'rgba(0, 255, 0, 255)' }
    static get BLUE() { return 'rgba(0, 0, 255, 255)' }
    static get CYAN() { return 'rgba(0, 255, 255, 255)' }
    static get GREY() { return 'rgba(127, 127, 127, 255)' }
    static get MAGENTA() { return 'rgba(255, 0, 255, 255)' }
    static get YELLOW() { return 'rgba(255, 236, 4, 255)' }
    static get LIGHTBLUE() { return 'rgba(168, 244, 255, 255)' }
    static get LIGHTORANGE() { return 'rgba(255, 233, 127, 255)' }
    static get KINDAORANGE() { return 'rgba(255, 128, 0, 255)' }
    static get LIGHTGRAY() { return 'rgba(238, 238, 238, 255)' }

    static get HATTER_1() { return 'rgba(211, 255, 204, 255)' } // halvany zold
    static get HATTER_2() { return 'rgba(214, 255, 248, 255)' } // halvany kek
    static get HATTER_3() { return 'rgba(196, 201, 255, 255)' } // lilaskek
    static get HATTER_4() { return 'rgba(246, 255, 196, 255)' } // halvanysarga
    static get HATTER_5() { return 'rgba(255, 251, 160, 255)' } // halvanyrozsaszin
    static get HATTER_6() { return 'rgba(255, 236, 211, 255)' } // kicsit erosebb sarga
    static get HATTER_7() { return 'rgba(255, 201, 207, 255)' } // halvanypiros
    static get HATTER_8() { return 'rgba(216, 255, 255, 255)' } // halovany nagyon kek

    static get COLOR_LIST() {
        return [this.WHITE, this.BLACK, this.RED, this.GREEN, this.BLUE, this.CYAN, this.GREY, this.LIGHTGRAY,
        this.MAGENTA, this.YELLOW, this.LIGHTBLUE, this.LIGHTORANGE, this.KINDAORANGE]
    }

    static get LOOP_COLORS() { return [this.BLACK, this.BLUE, this.RED, this.GREEN, this.CYAN, this.MAGENTA, this.KINDAORANGE] }

}


export class IMG {
    static get PLACEHOLDER() { return "./Images/icon-placeholder.png" }
    static get TURTLE() { return "./Images/turtle.png" }
    static get BEND_LEFT() { return "./Images/bendleft.png" }
    static get BEND_RIGHT() { return "./Images/bendright.png" }
    static get TURN_LEFT() { return "./Images/turnleft.png" }
    static get TURN_RIGHT() { return "./Images/turnright.png" }
    static get RED_PENCIL() { return "./Images/pencil2.png" }
    static get ICON() { return "./Images/visuallogoicon.png" }
}

export class FONT_AWESOME {
    static get SETTINGS() { return "\uF085" }
    static get LOAD() { return "\uF115" }
    static get SAVE() { return "\uF0C7" }
    static get SCREENSHOT() { return "MER" }
    static get EXIT() { return "\uF011" }
    static get PLAY() { return "\uF04B" }
    static get STEPOVER() { return "\uF051" }
    static get STOP() { return "\uF04D" }
    static get UP() { return "\uF062" }
    static get DOWN() { return "\uF063" }
    static get RIGHT() { return "\uF064" }
    static get LEFT() { return "\uF112" }
    static get PEN() { return "\uF040" }
    static get HOME() { return "\uF015" }
    static get FLOODFILL() { return "\uF1FC" }
    static get RESET() { return "\uF014" }
    static get CLEAR() { return "\uF12D" }
    static get LOOP() { return "\uF0E2" }
    static get PLACEHOLDER() { return "\uF071" }
    static get BOOKMARK() { return "\uF097" }
    static get ANGLE_DOUBLE_DOWN() { return "\uF103" }
    static get ANGLE_DOUBLE_LEFT() { return "\uF100" }
    static get ANGLE_DOUBLE_RIGHT() { return "\uF101" }
    static get ANGLE_DOUBLE_UP() { return "\uF102" }
    static get ANGLE_UP() { return "\uF106" }
    static get ANGLE_RIGHT() { return "\uF105" }
    static get ANGLE_LEFT() { return "\uF104" }
    static get ANGLE_DOWN() { return "\uF107" }
    static get LONG_UP() { return "\uF176" }
    static get LONG_DOWN() { return "\uF175" }
    static get EYE_SEE() { return "\uF06E" }
    static get EYE_NOT_SEE() { return "\uF070" }
    static get BACKGROUND_PICTURE() { return "\uF03E" }
    static get STICKY_NOTE() { return "\uF24A" }
    static get ROUND_X() { return "\uF05C" }
    static get SQUARE_X() { return "\uF2D4" }
    static get CHECK() { return "\uF00C" }
    static get CLOSE() { return "\uF00D" }
}

export class MOUSE {
    static get LMB() { return 0; }
    static get MMB() { return 1; }
    static get RMB() { return 2; }
}