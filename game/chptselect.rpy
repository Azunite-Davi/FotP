init:
    transform customzoom:
        zoom 0.2


screen chapters:
    tag menu
    style_prefix "style 1"
    textbutton _('return') action Return()

    use game_menu(_("Chapters"), scroll="viewpoint"):
        vbox:
            spacing 100
            hbox:
                spacing 25
                imagebutton:
                    auto "chpt/prologue_%s.png"
                    action Start("prologue")
                    at customzoom 
                imagebutton:
                    auto "chpt/chapter1_%s.png"
                    action Start("chapter_1")
                    at customzoom
                    sensitive persistent.chapter_1 == True 
                imagebutton:
                    auto "chpt/chapter2_%s.png"
                    action Start("chapter_2")
                    at customzoom
                    sensitive persistent.chapter_2 == True