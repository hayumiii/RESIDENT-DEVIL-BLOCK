﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene black bg

    show chana talk2

    # These display lines of dialogue.

    "Chana" "Gra powstala w celach humorystycznych i nie ma na celu nikogo urazić."
    
    show chana talk1

    "Chana" "Jeżeli jesteś cipą to radzilabym nie kontynuować."
   
    show chana happy
   
    "Chana" "..."

    "Chana" "..."
 
    show chana neutral
   
    "Chana" "..."
   
    "Chana" "Nadal tu jesteś..."

    "Chana" "Napewno chcesz kontynuować?"

    label wybor_1:
        menu:
            "Tak":
                jump wybor_1a
            "Jestem cipą":
                show chana neutral
                "Chana" "Pa"
                $ renpy.quit()

    label wybor_1a:
                show chana talk2
                "Chana" "No i super zapraszam"

    # Powrot do main menu

    $ MainMenu(confirm=False, save=True) ()
