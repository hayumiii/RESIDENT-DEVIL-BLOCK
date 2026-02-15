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
define ch = Character("Chania")
define kx = Character("Kacperix")
define ow = Character("Oliwierek")
define emo = Character("Emola")
define we = Character("Weroka")
define zuz = Character("Zuzia")
define nr = Character("Narrator", image="images/narrator-scr.png")
# Tu niby tez mozna by samo zmienialo twarze itp rozne albo voice ale to musze poczytac dalej


# The game starts here.
init python:
        def showleft(name): # mocno w lewo
            miejsce = Transform(xcenter=360)
            renpy.show(name=name, at_list=[miejsce])

        def showleft_1(name): # lekko w lewo
            miejsce = Transform(xcenter=660)
            renpy.show(name=name, at_list=[miejsce])

        def showright_1(name): # lekko w prawo
            miejsce = Transform(xcenter=1360)
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
    ch "игра создана в целах юмористических и не чтобы кого-то обижать"
    
    show chana talk1

    ch "Если ты пизда лучше не продолжай"
    show chana happy
    extend "..."  # extend by kontynuowac dialog z zmiana twarzy czyli ze poprzedni jest dalej na ekranie tlyko jakby dopisuje ta linijke i twarz zmienia
    # ale zeby zrobic nowe okienko jakby to normalnie ch
    # hanik ogarnij pls najwyzej ci wytlumacze

    show chana neutral
   
    extend "..."
   
    ch "Ты еще тут..."

    ch "Ты уверен что хочешь продолжать?"

    label wybor_1:
        menu: # Indykuje rozpoczecie wyboru 
            "Да": # Przykladowa opcja 1
                jump wybor_1a # Omija dalszy kod i przeskakuje do `label wybor_1a`
            "Я пизда": # Przykladowa opcja 2
                show chana neutral
                ch "Пока"
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

    $ renpy.music.set_volume(0.1)
    play music "horror.mp3"

    nr "Pieśń Chani w ciszy drżała, skruszona,"
    nr "Lecz zadrżała – w cieniu rozżarzona"
    nr "Za blokadę, za zdradę, w mroku narodzona"
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
    
    scene black with fade
    nr "Grupa siedzi w milczeniu. Emola zniknęła. Nikt nie wie, dlaczego."


    $ showright(name="oliwier neutral") 

    show chana talk1

    $ showleft(name="kacperix neutral")


    ch "Emola to zamknęła. Nas. Jak drzwi."
    $ showright(name="oliwier talk1") 
    ow "Może... może ktoś jej coś zrobił? Może ktoś z nas?"
    $ showright(name="oliwier neutral") 
    ch "Nie, to nie... To nie o nas chodzi. Albo może właśnie chodzi. Ale milczy. Nic nie powiedziała. Jakbyśmy zniknęli dla niej. Po prostu – hop, nie ma."
    $ showleft(name="kacperix talk1") 
    kx "Nie wierzę, że to koniec. Tak się nie kończy przyjaźń. Bez słowa?"
    $ showleft(name="kacperix neutral") 
    ch "Wiem, że nie da się, ale… Gdyby się dało. To bym pogadała."
    show chana neutral
    ch "(POV) Ona była inna. Może to lepiej że jej nie ma."

    show chana neutral 

    scene bedroom
    
    $ showright(name="oliwier talk1")

    ow "Więc co teraz..."
 
    $ showright(name="oliwier neutral")

    $ showleft(name="kacperix talk1")  

    kx "..."

    $ showleft(name="kacperix neutral")  

    show chana talk2

    ch "Zemścimy sie i odwrócimy to."

    show chana neutral

    $ showright(name="oliwier talk1")

    ow "Jak niby chcesz to zrobić?.."

    show chana talk2 

    ch "Przyzwiemy demona, który wymierzy jej karę"
    show chana happy

    $ showleft(name="kacperix talk1")  

    kx "Nie przesadzasz?"

    $ showleft(name="kacperix neutral")  

    show chana talk2

    ch "Nie. Ona musi do nas wrócić. Dla nas"

    show chana happy

    $ showright(name="oliwier talk1")

    ow "Nie wiem czy chce się w to mieszać"

    $ showright(name="oliwier neutral")
    
    show chana talk1
    
    ch "Zrobimy rytuał"

    show chana neutral
    
    $ showleft(name="kacperix talk2")  

    kx "Jak niby"

    $ showleft(name="kacperix neutral")  

    show chana talk2

    ch "Mam.. już pewny pomysł w głowie"

    show chana neutral
 
    $ showleft(name="kacperix talk1")  

    kx "A może zamiast wzywać demony zemścimy się w jakiś inny sposób?"
    
    $ showleft(name="kacperix neutral")  

    $ showright(name="oliwier talk1")

    ch "Nie znasz się na zabawie, ona musi zapłacić."

    $ showright(name="oliwier neutral")

    show chana talk2

    ow "..."
    ow "Może i nie jestem jakoś przekonany ale zaufam chanii"

    show chana happy

    $ showleft(name="kacperix talk1")  

    kx "Idziemy robić ten rytuał?"

    label choices_2:
        menu:
            "Tak":
                jump choices_2a
            "To zły pomysł...":
                jump choices_2b

    label choices_2a:
            show chana talk2
            ch "To idziemy"
            $ learned = True 
            jump choices2_common

    label choices_2b:
            show chana talk2
            ch "...Nie ma innego wyjścia"
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
                ch "Idziemy. Już nie możemy się wycofać."
                show chana happy
            
            else:
                show chana talk2
                ch "Musimy to zrobić. Ja to muszę zrobić dla spokoju"
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

    ow "To tu.."

    $ showright(name="oliwier neutral")

    show chana talk2 

    ch "Zgadza się"

    show chana talk1

    ch "A teraz.. szykujcie się"

    scene cipa with fade

    pause 2.0

    show expression glitch("chana neutral"):
        pause 1.0
        glitch("chana talk1", offset=60, randomKey=None)
        pause 0.1
        pause 1.0
        glitch("chana talk2", offset=60, randomKey=None)
        pause 0.1
        pause 1.0
        glitch("chana neutral", offset=60, randomKey=None)
        pause 0.1
        glitch("chana talk1", offset=60, randomKey=None)

    ch "Panie Boże pomóż nam"
    
    ch "By Emole ściągnąć wraz"

    ch "Suka nas zablokowała"

    $ showright(name="emola evil")

    ch "A powodu nie podała"
    hide emola evil

    ch "Więc wypowiem mądre słowa"

    show chana talk2

    ch "Niech się dzieję wola boga"

    show chana talk1

    ch "Blokada, ciemność i niekontakt"

    show chana talk2

    ch "Niech będzie z dala od nas"

    ch "I niech przyjdzie istota obiecana"

    show chana talk1

    ch "W grymuarach zapisana"

    ch "Oświecić nasze życie by.."

    show chana talk2 

    ch "Już nigdy nie spotkał nas taki czyn!"

    with Shake( (0, 0, 0, 0), 3.0, dist=30)

    hide chana talk2 with dissolve

    show diva talk

    zuz "To mnie wzywaliście?"

    hide diva talk

    scene cipa with fade

    $ showright(name="oliwier neutral") 

    $ showright_1(name="chana happy") 

    $ showleft(name="kacperix neutral")

    $ showleft_1(name="diva rizz")

    $ showright_1(name="chana talk1") 

    ch "Udało się.."

    $ showright_1(name="chana happy") 

    $ showleft_1(name="diva talk")

    zuz "A czemu miałoby się nie udać?"

    $ showright_1(name="chana talk2") 

    ch "No taka hot jesteś że aż nie z tego świata"

    $ showright_1(name="chana happy") 

    $ showright(name="oliwier talk1")

    ow "Chania to nie czas na takie rzeczy."

    $ showright(name="oliwier neutral")

    $ showleft_1(name="diva talk")

    zuz "Dlaczego mnie przywołaliście"

    $ showleft_1(name="diva neutral")

    $ showright_1(name="chana talk1")

    ch "Chcemy się na kimś zemścić"
            
    $ showright_1(name="chana neutral")

    $ showleft_1(name="diva talk")

    zuz "?"
             
    $ showleft_1(name="diva neutral")
         
    $ showleft(name="kacperix talk1")

    kx "Bo nas zablokowała"

    $ showleft(name="kacperix neutral")

    $ showleft_1(name="diva talk")

    zuz "Mhm.. słucham dalej"

    zuz "Zaintrygowaliście mnie swoim nietypowym wyborem muszę przyznać.."

    zuz "Czekajcie, a o kogo wam chodzi?"
    extend "..."

    $ showright_1(name="chana talk1")
    ch "O.."
    extend "Emole."

    scene black with dissolve
    scene black
    show diva rizz 
    zuz "Heh..."
    show diva talk
    zuz "Oni nie wiedzą w co się pakują"
    show diva rizz
    extend "..."
    show diva talk
    zuz "Ale dobrze, pomoge im"
    extend "..."
    zuz "\n Przynajmniej żeby odkryć prawdę..."
    scene black with fade
    scene cipa with fade

    $ showright(name="oliwier neutral") 

    $ showright_1(name="chana happy") 

    $ showleft(name="kacperix neutral")

    $ showleft_1(name="diva rizz")

    $ showright_1(name="chana neutral") 

    zuz "Jesteście pewni?"

    $ showright_1(name="chana talk2") 

    ch "Tak."
    $ showleft_1(name="diva talk")
    $ showright_1(name="chana neutral")

    zuz "Dobrze."

    zuz "W takim razie.."

    zuz "Potrzebuję 5-ciu rzeczy"

    zuz "Węgla z kopalni Wujek"

    zuz "Jej włosy"

    zuz "4 świeczki"

    zuz "Kości zwierzęcę"
    extend "..."
    zuz "Ale zmielone!"

    zuz "i..."

    zuz "Księge Blokady"

    zuz "Księge B̶̩̥̈́l̶͈͖̇̆ô̸̲k̵͊ͅą̸̅d̷̥́y̵̨̿͋"

    with Shake( (0, 0, 0, 0), 3.0, dist=30)

    scene black with fade
    show emola evil
    pause 1.5
    scene cipa with dissolve

    $ showright(name="oliwier neutral") 

    $ showright_1(name="chana happy") 

    $ showleft(name="kacperix neutral")

    $ showleft_1(name="diva rizz")

    $ showright_1(name="chana neutral") 

    $ showright(name="oliwier talk2")

    ow "To co najpierw"

    ch "Poczekajcie... a co to jest ta.."
    ch "Księga Blokady"

    with Shake( (0, 0, 0, 0), 3.0, dist=30)

    zuz "To jest księga z legendy krążącej w okolicy"
    zuz "Była napisana przez... samego Boga"

    $ showright_1(name="chana happy")

    ch "(pov) Blokada.. przez samego Boga?"
    extend "Coś mi tu nie gra" 

    $ showright(name="oliwier happy")

    $ showleft(name="kacperix talk2")

    kx "Dobra to włosy najłatwiejsze mi się wydaje?"

    $ showleft(name="kacperix neutral")
    hide diva rizz

    show expression glitch("diva neutral"):
        pause 1.0
        glitch("diva rizz", offset=60, randomKey=None)
        pause 0.1
        pause 1.0
        glitch("diva neutral", offset=60, randomKey=None)
        pause 0.1
        pause 1.0
        glitch("emola evil", offset=60, randomKey=None)
        pause 0.1
        glitch("diva rizz", offset=60, randomKey=None)
        pause 0.1
        pause 1.0
        glitch("diva neutral", offset=60, randomKey=None)
        pause 0.1
        pause 1.0
        glitch("emola evil", offset=60, randomKey=None)
        glitch("diva rizz", offset=60, randomKey=None)
        pause 0.1
        pause 1.0
        glitch("emola evil", offset=60, randomKey=None)
        pause 0.1
        pause 1.0
        glitch("diva neutral", offset=60, randomKey=None)


    zuz "Idźcie z bogiem dzieci..."
    zuz "Albo i bez niej."

    scene cipa with fade 


    pause 1.5

    scene szkola2 with fade 

    show chana happy

    $ showright(name="kacperix neutral")

    $ showleft(name="oliwier happy")

    show chana talk1

    ch "To jakiekolwiek pomysły macie? jak utniemy włosy Emoli?"

    show chana neutral

    $ showleft(name="oliwier talk1")

    ow "Możemy jakoś Werokę przekonać, żeby nam pomogła"

    ch "Ja sie tym zajme"
    ch "Wy idzcie"
    ch "Poszukajcie informacji o tej legendzie."

    hide oliwier talk1
    hide kacperix neutral
    hide chana neutral

    scene szkola1 with fade

    show chana neutral:
        xalign 1.0 yalign 0.0
        linear 5   xalign 0.25 yalign 0.75

    $ showleft(name="chana neutral")
    pause 1.0

    show chana neutral at center 
    with move

    ch "Gdzie ona..."

    $ showright(name="chana neutral")
    with move
    
    scene classroom1 with dissolve

    $ showleft(name="weroka talk2")
    $ showright(name="chana neutral")
    pause 1.0
    hide chana neutral
    show chana talk2
    with move
    ch "O hej weroka.!"
    $ showleft_1(name="weroka talk1")
    with move
    we "hmm?"
    ch "Potrzebuje czegoś od ciebie ważnego"
    extend ".. Ale bądź wyrozumiała"
    we "no słucham?"
    show chana neutral
    ch "..."
    show chana talk1
    ch "Emola jest w szkole?"
    $ showleft_1(name="weroka talk2")
    we ".. no tak?"
    $ showleft_1(name="weroka neutral")
    ch "Pamiętasz jak ona nas zablokowała?"
    $ showleft_1(name="weroka talk1")
    we "Nom.."
    $ showleft_1(name="weroka neutral")
    ch "heh.."
    ch "Chcemy się lekko zemścić na niej i mamy już plan.."
    $ showleft_1(name="weroka talk1")
    we "Ale po co"

    show chana happy

    ch "Nie no żartowałam! Ale czy mogłabyś mi załatwić by ona poszła do toalety na przerwie?"
    $ showleft_1(name="weroka neutral")
    we "..."
    ch "Bardzo prosze?.."
    $ showleft_1(name="weroka talk1")
    we "Troche dziwne ale dobra"
    we "Jak chcesz"
    show chana talk2
    ch "DZIEKUJEEEE!!!!"
    show chana happy    

    scene toaleta

    nr "Chańa zdecydowała się... "

    window hide
    show expression glitch("emola neutral") as emo:
        pause 1.0
        glitch("Wiem. O wszystkim wiem.", crop=True)
        xalign 0.5
        yalign 0.5
        pause 4.0
        glitch("emola neutral", offset=60, randomKey=None)
        pause 0.1
        pause 1.0
    ##scene toaleta 
    pause 5.0
    hide expression glitch("emola neutral")
    show emola neutral
    nr "..."
    emo "..."
    scene black with dissolve
    scene toaleta
    show chana neutral
    ch "Dobra... to teraz nie pozostaje mi nic innego niż czekać"
    extend "... Aż sie ona zjawi"

    scene black with fade

    nr "*30 minut później*"

    scene toaleta with fade

    show emola neutral:
        xalign 1.0 yalign 0.0
        linear 5   xalign 0.25 yalign 0.75

    show emola neutral at center
    with move

    $ showleft(name="emola neutral")
    pause 0.5

    emo "..."

    $ showright(name="chana neutral")
    with move

    emo "W końcu można odpocząć"

    $ showright(name="chana neutral")
    pause 0.5


    $ showleft(name="chana neutral")
    with move

    show chana talk1
    ch "hej emola.."

    show emola talk1
    emo "Co ty tu do cholery robisz"

    ch "cii.."

    scene wlosy with fade
    pause 0.2
    scene wlosy2 with fade
    pause 0.5
    scene szkola1 with dissolve

    $ showright(name="chana neutral")
    pause 0.5


    $ showleft(name="chana neutral")
    with move

    scene szkola2

    show oliwier talk1
    $ showright(name="chana talk1")
    $ showleft(name="kacperix neutral")

    ch "Uciekamy."

    scene bedroom with dissolve


    $ showright(name="oliwier neutral") 

    show chana talk1

    $ showleft(name="kacperix neutral")

    $ showright(name="oliwier talk1")

    ow "Masz te wlosy?"

    ch "Tak!. Udało się"

    $ showleft(name="kacperix talk1")

    kx "To co teraz?"

    ch "...Możemy iśc po--"
    ch "A czekajcie"
    ch "Co sie dowiedzieliscie o tej legendzie?"



    

















# $ showright(name="chana talk2") <-przykladowy syntax 
# Zmienimy pozniej te lewo i prawo na te itp z hania

    
    
    
     # Powrot do main menu
    # By użyc pythona do np wylaczenia gry mozna uzyc znaku `$` lub blok `python:` tak jak `label` itp.

    #$ MainMenu(confirm=False, save=True) () # Wychodzi do main menu, bez potwierdzenia i zapisując
