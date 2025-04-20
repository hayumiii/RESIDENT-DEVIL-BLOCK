
label splashscreen: # Wejscie do gry
   play sound "kopanie.ogg"
   scene white
   pause 1.5
   show a with fade
   pause 1.5
   hide a with dissolve
   pause 1.5
   show b with fade
   pause 1.5
   hide b with dissolve
   return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen") - > Nie uzywamy tego narazie
# dla chanii -> mozna to zrobic np 
#define chana = Character("Chana", image="Chana neutral", voice_tag="Chana")
# Tu niby tez mozna by samo zmienialo twarze itp rozne albo voice ale to musze poczytac dalej


# The game starts here.


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene black bg

    show chana talk2

    # These display lines of dialogue.
    # `show` by zmienić postać -> nazwa pliku bez rozszerzenia i bez "" czyli bez .jpg itp
    # `scene ...` by zmienić scenę
    # Dialogi są w formacie:
    # "Postać 1" "Dialog"

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
        menu: # Indykuje rozpoczecie wyboru 
            "Tak": # Przykladowa opcja 1
                jump wybor_1a # Omija dalszy kod i przeskakuje do `label wybor_1a`
            "Jestem cipą": # Przykladowa opcja 2
                show chana neutral
                "Chana" "Pa"
                $ renpy.quit() # Używane by wylaczyc gre -> W DRUGIEJ OPCJI TRZEBA UZYC `JUMP` DO MIEJSCA KTORE JEST POD TYM INACZEJ KOD LECI DALEJ I WYLACZA NAWET JAK NIE POWINNO

    label wybor_1a: # Przykladowy jump, powiazanie wyboru
                show chana talk2
                "Chana" "No i super zapraszam" # Kod sie po tym kontynuuje

    # Powrot do main menu
    # By użyc pythona do np wylaczenia gry mozna uzyc znaku `$` lub blok `python:` tak jak `label` itp.

    $ MainMenu(confirm=False, save=True) () # Wychodzi do main menu, bez potwierdzenia i zapisując
