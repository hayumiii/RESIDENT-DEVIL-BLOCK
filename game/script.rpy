label splashscreen: # Wejscie do gry
   scene white
   pause 1.5
   play sound "kopanie.ogg"
   show a with dissolve
   pause 1.5
   hide a with dissolve
   pause 1.5
   show b with dissolve
   pause 1.5
   hide b with dissolve
   return
   stop music

# The script of the game goes in this file.

# imie happy -> usmiechniety
# imie neutral -> neutralny wow
# imie talk1 -> lekko otwarta morda
# imie tal2 -> mocno otwarta morda

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define chana = Character("Chana", image="Chana neutral", voice_tag="Chana", color="#ffffff" <- kolor imienia, mozna tez zrobic image i imie bedzie uzywane jako nazwa obrazu i bedzie obrazek maly zamiast imiona)... -> 
# czy my chcemy to robic? hanik ocen jutro
# dla chanii -> mozna to zrobic np 
#odpowiadajac na twoje pytanie kacperixie nwm czy to przejdzie vzy n lepiej imiona bo beda  sie pojawialy postacie ktorych n mamy modeli zrobionych wiec lepiej zostac przy imionach
define ch = Character("Chana")
define kx = Character("Kacperix")
define ow = Character("Oliwierek")
define emo = Character("Emola")
define we = Character("Weroka")
define zuz = Character("Zuzia")
define nr = Character("Narrator", image="images/narrator-scr.png")
# Tu niby tez mozna by samo zmienialo twarze itp rozne albo voice ale to musze poczytac dalej


# The game starts here.
init python:
        def showleft_1(name): # lekko w lewo
            miejsce = Transform(xcenter=420)
            renpy.show(name=name, at_list=[miejsce])

        def showleft(name): # mocno w lewo
            miejsce = Transform(xcenter=320)
            renpy.show(name=name, at_list=[miejsce])

        def showright_1(name): # lekko w prawo
            miejsce = Transform(xcenter=1560)
            renpy.show(name=name, at_list=[miejsce])

        def showright(name): # mocno w prawo
            miejsce = Transform(xcenter=1660)
            renpy.show(name=name, at_list=[miejsce])
label start:
    stop music # Wylaczyc muzyke
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene black bg

    show chana happy

    # These display lines of dialogue.
    # `show` by zmienić postać -> nazwa pliku bez rozszerzenia i bez "" czyli bez .jpg itp
    # `scene ...` by zmienić scenę
    # Dialogi są w formacie:
    # "Postać 1" "Dialog"
    ch "Gra powstała w celach humorystycznych i nie ma na celu nikogo urazić."
    
    show chana talk1

    ch "Jeżeli jesteś cipą to radziłabym nie kontynuować."
    show chana happy
    extend "..."  # extend by kontynuowac dialog z zmiana twarzy czyli ze poprzedni jest dalej na ekranie tlyko jakby dopisuje ta linijke i twarz zmienia
    # ale zeby zrobic nowe okienko jakby to normalnie ch
    # hanik ogarnij pls najwyzej ci wytlumacze

    show chana neutral
   
    extend "..."
   
    ch "Nadal tu jesteś..."

    ch "Napewno chcesz kontynuować?"

    label wybor_1:
        menu: # Indykuje rozpoczecie wyboru 
            "Tak": # Przykladowa opcja 1
                jump wybor_1a # Omija dalszy kod i przeskakuje do `label wybor_1a`
            "Jestem cipą": # Przykladowa opcja 2
                show chana neutral
                ch "Pa"
                jump wybor_1b
                #$ renpy.quit() # Używane by wylaczyc gre -> W DRUGIEJ OPCJI TRZEBA UZYC `JUMP` DO MIEJSCA KTORE JEST POD TYM INACZEJ KOD LECI DALEJ I WYLACZA NAWET JAK NIE POWINNO

    label wybor_1a: # Przykladowy jump, powiazanie wyboru
                show chana talk2
                ch "No to dobrze"
                $ learned = True
                jump choices1_common
    
    label wybor_1b:
                show chana neutral
                $ learned = False
                jump choices1_common
  
    label choices1_common:
                show chana neutral
                ch "..."
 
    label flags:
                if learned:
                      ch "Zapraszam"
                      jump akt1
                else:
                      show chana neutral
                      show chana talk1
                      ch "Pizda"
                      $ renpy.quit()
                      # nazwa `label` takie jak np `wybor_1b` n trzeba ustawiac pliku, samo znajduje -> pliki dawac do folderu `scenariusz`
                      return # dac bez return by przelaczylo do innej fabuly i powrocilo tu by kontynuowac -> mozeb yc do flashbackow dobrze uzyte
                      # z return jak ma juz tam zostac i bedzie budowana odtamtad kompletnie inna
                      # mozna tez zawsze uzyc `call` by powrocic do jakiegos punktu w tym pliku np fabuly sie rozdziela na nw 100 dialogow ale bedzie wspolna scenka to do jednego i pozneij znowu rozdzielic uzywajac `call` do `label`-ow ktore maja byc juz PO 
                      # wywolaniu tej scenki czyli jak redirect jest z `label scena70:` to call `scena 71` by nie zrobila sie petla   
  
    label akt1:

    #ogolnie to chcialam dac narratora vczyy cos ale nwm wsm wiec narazie pisze narrator potem sie zmieni najwyzej
 
    window hide dissolve 
    
    pause 1.0

    scene black with dissolve

    pause 1.0

    window show dissolve

    nr "Pieśń Chani w ciszy drżała, skruszona,"
    nr "Lecz zadrżała – w cieniu rozżarzona"
    nr "Za blokadę, za zdradę, za mroku"
    nr "Szept milczenia, co serce rozdziera"
    nr "Zemsta! Chani już litość odbiera!"
    nr "Zemsta, co słów nie pragnie, ni zgody"
    nr "Na Emolę, co ciszą uwięziła"
    nr "Chani w gniewie – duszę obnażyła!"   

    window hide dissolve
    
    pause 1.0

    scene bedroom

    pause 1.0

    window show dissolve

    pause 1.0

    show chana talk1
    
    ch "Chciałam zagrać i mnie zablokowała, cała historia"

    show chana neutral 
    
    $ showright(name="oliwier talk1")

    ow "I co nam do tego"
 
    $ showright(name="oliwier neutral")

    $ showleft(name="kacperix talk1")  

    kx "No rel"

    $ showleft(name="kacperix neutral")  

    show chana talk2

    ch "Zemścimy sie"

    show chana neutral

    $ showright(name="oliwier talk1")

    ow "Jak niby chcesz się na niej zemścić"

    show chana talk2 

    ch "Przyzwiemy demona, który wymierzy jej karę"
    show chana happy

    $ showleft(name="kacperix talk1")  

    kx "No super pomysł a jak chcesz to niby zrobić?"

    $ showleft(name="kacperix neutral")  

    show chana talk2

    ch "Rytuał twinków, nic ci to nie mówi?"

    show chana happy

    $ showright(name="oliwier talk1")

    ow "A my ci po co niby"

    $ showright(name="oliwier neutral")
    
    show chana talk1
    
    ch "Rytuał twinków a ja twinkiem nie jestem więc rusz głową czy coś"

    show chana neutral
    
    $ showleft(name="kacperix talk2")  

    kx "A będzie ruchanie?"

    $ showleft(name="kacperix neutral")  

    show chana talk2

    ch "Wyciskanie spermy będzie"

    show chana neutral
 
    $ showleft(name="kacperix talk1")  

    kx "A może zamiast wzywać demony zemścimy się w jakiś inny sposób?"
    
    $ showleft(name="kacperix neutral")  

    $ showright(name="oliwier talk1")

    ow "Ale pizda z ciebie ja nie mogę"

    $ showright(name="oliwier neutral")

    show chana talk2

    ch "No rel pizda"

    show chana happy

    $ showleft(name="kacperix talk1")  

    kx "No to mamy iść robić ten rytuał czy nie?"

    label choices_2:
        menu:
            "Oczywiście ze tak":
                jump choices_2a
            "Wypierdalaj jebać szatana":
                jump choices_2b

    label choices_2a:
            show chana talk2
            ch "No i sigma!"
            $ learned = True 
            jump choices2_common

    label choices_2b:
            show chana talk2
            ch "W chuju to mam"
            $ learned = False 
            jump choices2_common

    label choices2_common: 
            show chana happy
            $ showleft(name="kacperix talk1")  
            kx "To idziemy czy nie?"
            $ showleft(name="kacperix neutral")  

    
    label flags2:
            if learned:
                show chana talk2 
                ch "No przecież wybrali że tak więc idziemy"
                show chana happy
            
            else:
                show chana talk2
                ch "Nie obchodzi mnie twój wybor"
                show chana neutral
                extend "..."
                show chana talk2
                ch "Idziemy!"
                
    label egzorcyzmy:  

    scene cipa with fade

    pause 1.5

    show chana happy

    $ showright(name="oliwier neutral")

    $ showleft(name="kacperix neutral")

    $ showright(name="oliwier talk1")

    ow "To tu niby tego demona będziemy przyzywać ta?"

    $ showright(name="oliwier neutral")

    show chana talk2 

    ch "Nie niby tylko będziemy przyzywać"

    show chana talk1

    ch "Szykujcie spermę..."

    scene cipa with fade

    pause 2.0

    show chana talk1

    ch "Panie Boże kurwa pomóz"
    
    ch "Na emolę klątwę załóż"

    ch "Suka nas zablokowała"

    ch "A powodu nie podała"

    ch "Więc wypowiem mądre słowa"

    show chana talk2

    ch "Niech się dzieję wola boga"

    show chana talk1

    ch "Konik pedał i kurewki"

    show chana talk2

    ch "Lejmy sperme do konewki"

    ch "Orgia kozły i walenie"

    show chana talk1

    ch "Squirt jest jako nawodnienie"

    ch "Iść na dziwki dać dolary"

    show chana talk2 

    ch "Niech się spełnią czary mary!"

    with Shake( (0, 0, 0, 0), 3.0, dist=30)

    hide chana talk2 with dissolve

    show diva talk

    zuz "Cześć pedały"

    hide diva talk

    scene cipa with fade

    $ showright(name="oliwier neutral") 

    $ showright_1(name="chana happy") 

    $ showleft_1(name="kacperix neutral")

    show diva rizz

    $ showright_1(name="chana talk1") 

    ch "O kurwa udało się"

    $ showright_1(name="chana happy") 

    show diva talk

    zuz "No a czemu miałoby się nie udać, że niby nie istnieję tak?"

    $ showright_1(name="chana talk2") 

    ch "No taka hot jesteś że aż nie z tego świata"

    $ showright_1(name="chana happy") 

    $ showright(name="oliwier talk1")

    ow "Bo ona nie jest z tego świata geniuszko"

    $ showright(name="oliwier neutral")

    $ showleft(name="diva talk")

    zuz "Na chuj mnie przywołaliście"

    show diva neutral

    $ showright_1(name="chana talk1")

    ch "Chcemy się na kimś zemścić"
            
    $ showright_1(name="chana neutral")

    show diva talk

    zuz "Po chuj"
             
    show diva neutral
         
    $ showleft(name="kacperix talk1")

    kx "Bo nas zablokowała"

    $ showleft(name="kacperix neutral")

    show diva talk

    zuz "No to rzeczywiście zajebisty powód"

    zuz "Ale pomogę wam skoro już mnie przywołaliście..."

    zuz "Żebym mogła jej cokolwiek zrobić potrzebuję..."

    zuz "Jej włosów"

    zuz "Krwii"

    zuz "Spermy"

    zuz "Węgla z kopalni Wujek"

    zuz "Wykopanego przez Emolę bo inaczej to na chuj mi"

    show diva neutral

    $ showright_1(name="chana talk2")

    ch "Dobra ez w chuj"

    $ showright(name="oliwier talk2")

    ow "To co najpierw"

    $ showright(name="oliwier happy")

    $ showleft(name="kacperix talk2")

    kx "Włosy najłatwiejsze"

    $ showleft(name="kacperix neutral")

    show diva talk
     
    zuz "Idźcie z bogiem dzieci..."

    scene cipa with fade 

    pause 1.5

    scene szkola2 with fade 

    show chana happy

    $ showright(name="kacperix neutral")

    $ showleft(name="oliwier happy")

    show chana talk1

    ch "To jakiekolwiek pomysły JAK utniemy włosy Emoli?"

    show chana neutral

    $ showleft(name="oliwier talk1")

    ow "Możemy jakoś Werokę przekonać, żeby nam pomogła"

    

















# $ showright(name="chana talk2") <-przykladowy syntax 
# Zmienimy pozniej te lewo i prawo na te itp z hania

    
    
    
     # Powrot do main menu
    # By użyc pythona do np wylaczenia gry mozna uzyc znaku `$` lub blok `python:` tak jak `label` itp.

    #$ MainMenu(confirm=False, save=True) () # Wychodzi do main menu, bez potwierdzenia i zapisując
