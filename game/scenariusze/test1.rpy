
# imie happy -> usmiechniety
# imie neutral -> neutralny wow
# imie talk1 -> lekko otwarta morda
# imie tal2 -> mocno otwarta morda

label fabula_test_1:
    #stop music # Wylaczyc muzyke
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene white

    show chana talk1

    # These display lines of dialogue.
    # `show` by zmienić postać -> nazwa pliku bez rozszerzenia i bez "" czyli bez .jpg itp
    # `scene ...` by zmienić scenę
    # Dialogi są w formacie:
    # "Postać 1" "Dialog"

    "Chana" "Test fabuly"

    # Powrot do main menu
    # By użyc pythona do np wylaczenia gry mozna uzyc znaku `$` lub blok `python:` tak jak `label` itp.

    #$ MainMenu(confirm=False, save=True) () # Wychodzi do main menu, bez potwierdzenia i zapisując
