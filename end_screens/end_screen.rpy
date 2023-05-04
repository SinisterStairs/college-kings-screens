screen end_screen(support_link=""):
    tag end_screen
    modal True
    style_prefix "end_screen"

    add "end_screen_background"

    textbutton "COLLEGE KINGS EPISODE 4 IS CURRENTLY IN DEVELOPMENT":
        text_style "end_screen_title"
        xalign 0.5
        ypos 100
        # action OpenURL("steam://openurl/https://store.steampowered.com/app/2267960/College_Kings_2__Episode_3_Back_To_Basics/")

    hbox:
        align (0.5, 1.0)
        yoffset -25
        xfill True

        vbox:
            xpos 50
            ysize 500

            hbox:
                align (0.5, 0.5)
                spacing 25

                text "Get the latest updates on our Discord" style "end_screen_large_text" yalign 0.5
                
                imagebutton:
                    idle "discord_idle"
                    action OpenURL("https://discord.gg/collegekings")
                    yalign 0.5 

            hbox:
                align (0.5, 1.0)
                spacing 100

                imagebutton:
                    idle "main_menu_idle"
                    hover "main_menu_hover"
                    action MainMenu()

                imagebutton:
                    idle "team_idle"
                    hover "team_hover"
                    action Show("team_credits")
                    yalign 0.5

        frame:
            background "end_screen_frame_background"
            xysize (910, 500)
            padding (50, 50)
            align (1.0, 0.5)

            vbox:
                yalign 1.0
                spacing 15

                text "CHECK OUT OUR NEW GAME: UNSCRIPTED" style "end_screen_header"

                text "{b}Calling all CK lovers!{/b}\n\nWe are beyond excited to share our new game Unscripted with our community and we don't want you to miss out. Play the lead in a romantic comedy where you decide the fate of your relationships. Love, sex and a ton of hilarious adventures await! If you love College Kings, you'll love Unscripted, so come join the ride and get the game as soon as it's out!"

                hbox:
                    xalign 0.5
                    spacing 15

                    add "steam_logo" yalign 0.5
                    
                    textbutton "STEAM":
                        action OpenURL("steam://openurl/https://store.steampowered.com/app/2156300/Unscripted/")
                        yalign 0.5
                        
                    add "gui/common/arrow.webp" yalign 0.5

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    on "replace" action SetVariable("quick_menu", False)
    on "replaced" action SetVariable("quick_menu", True)
