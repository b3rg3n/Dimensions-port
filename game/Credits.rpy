init python:
    import datetime

image credits_cg1:
    "images/cg/credits/1.png"
    size (640, 360)

image credits_cg2:
    "images/cg/credits/2.png"
    size (640, 360)

image credits_cg3:
    "images/cg/credits/3.png"
    size (640, 360)

image credits_cg4:
    "images/cg/credits/4.png"
    size (640, 360)

image credits_cg5:
    "images/cg/credits/5.png"
    size (640, 360)

image credits_cg6:
    "images/cg/credits/6.png"
    size (640, 360)

image credits_cg7:
    "images/cg/credits/7.png"
    size (640, 360)

image credits_cg8:
    "images/cg/credits/8.png"
    size (640, 360)

image credits_cg9:
    "images/cg/credits/9.png"
    size (640, 360)

image credits_cg10:
    "images/cg/credits/10.png"
    size (640, 360)

image credits_cg1_locked:
    "mod_assets/cg/ch03b.png"
    size (640, 360)

image credits_cg2_locked:
    "mod_assets/background/ch04b.png"
    size (640, 360)

image credits_cg3_locked:
    "mod_assets/background/beachlegs.png"
    size (640, 360)

image credits_cg4_locked:
    "mod_assets/background/sayohugging.png"
    size (640, 360)

image credits_cg5_locked:
    "mod_assets/background/nathugging.png"
    size (640, 360)

image credits_cg6_locked:
    "mod_assets/background/yuliahugging.png"
    size (640, 360)

image credits_cg7_locked:
    "mod_assets/background/ch08s3.png"
    size (640, 360)

image credits_cg8_locked:
    "mod_assets/background/ch08n1.png"
    size (640, 360)

image credits_cg9_locked:
    "mod_assets/background/ch08y4.png"
    size (640, 360)

image credits_cg10_locked:
    "mod_assets/background/ch08m3.png"
    size (640, 360)

image credits_cg1_clearall:
    "mod_assets/placeholder.png"
    size (640, 360)

image credits_cg2_clearall:
    "mod_assets/placeholder.png"
    size (640, 360)

image credits_cg3_clearall:
    "mod_assets/placeholder.png"
    size (640, 360)

image credits_cg4_clearall:
    "mod_assets/placeholder.png"
    size (640, 360)

image credits_cg5_clearall:
    "mod_assets/placeholder.png"
    size (640, 360)

image credits_cg6_clearall:
    "mod_assets/placeholder.png"
    size (640, 360)

image credits_cg7_clearall:
    "mod_assets/placeholder.png"
    size (640, 360)

image credits_cg8_clearall:
    "mod_assets/placeholder.png"
    size (640, 360)

image credits_cg9_clearall:
    "mod_assets/placeholder.png"
    size (640, 360)

image credits_cg10_clearall:
    "mod_assets/placeholder.png"
    size (640, 360)

image credits_logo:
    "mod_assets/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

image starring:
    ypos credits_ypos + 320
    xoffset 0 alpha 0
    "black"
    Text("[player] - Элиас Тоуфекс", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
    0.5
    linear 2.0 alpha 1
    4.0
    linear 2.0 alpha 0

image credits_ts = "mod_assets/madeby.png"

style credits_header:
    font "mod_assets/lobster.ttf"
    color "#d2efee"
    size 33
    text_align 0.5
    outlines []

style credits_text:
    font "mod_assets/gui/font/comicbd.ttf"
    color "#949494"
    size 36
    text_align 0.5
    outlines []

style credits_text_small:
    font "mod_assets/gui/font/comic.ttf"
    color "#949494"
    size 17
    text_align 0.5
    outlines []

style monika_credits_text:
    font "mod_assets/Vivaldi.ttf"
    color "#fff"
    size 26
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-105)
image credits_text = ParameterizedText(style="credits_text", ypos=35)
image credits_text_small = ParameterizedText(style="credits_text_small", ypos=35)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)


transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_sticker_scroll_rip:
    subpixel True
    yoffset 940
    7.8
    linear 14 yoffset -400

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

transform credits_sticker_5:
    yanchor -0.5
    xalign 0.12
    alpha 0.5
    credits_sticker_scroll_rip
transform credits_sticker_6:
    yanchor -0.5
    xalign 0.88
    alpha 0.5
    credits_sticker_scroll_rip

define credits_ypos = 250

image mcredits_1a:
    ypos credits_ypos
    xoffset -180
    "black"
    1.0
    Text("Заперт внутри", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset 10
    "black"
    3.0
    Text(" Запутанного пути.", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos + 50
    xoffset -110
    "black"
    6.0
    Text("И путники выглядят странно.", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 100
    xoffset -180
    "black"
    11.0
    Text("Неудачи, гонения", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 100
    xoffset 15
    "black"
    13.0
    Text(" Превозмочь все угрызения.", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 150
    xoffset -155
    "black"
    15.5
    Text("Куда иду - и сам не знаю.", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 15.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("Тёмной лужей чернила вдруг стали,", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text(" Просто пиши - дай им стать большой рекой!", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("В мире, где миллионы решений", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -145
    "black"
    42.0
    Text(" Куда же плыть", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 85
    "black"
    43.47
    Text(" Вместе с нею за мечтой?", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 10.0, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("Какой же путь вместе нас сведёт с тобой?", style="monika_credits_text") with ImageDissolve("mod_assets/wipeleft.png", 15.0, ramplen=4)

image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

label credits:
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    play music "mod_assets/sfx/end-voice.ogg" noloop

    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show end_glitch1 zorder 2
    show black as bar zorder 9:
        alpha 0.3
        size (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat


    pause 22
    scene black
    pause 0.5
    $ consolehistory = []
    call updateconsole ("renpy.music.play(\"theotheryou.ogg\")", "Играет аудио \"theotheryou.ogg\"...")
    pause 1.0
    call hideconsole
    play music "mod_assets/music/theotheryou.ogg" noloop
    show mcredits_1a zorder 50
    show mcredits_1b zorder 49
    show mcredits_1c zorder 48
    show mcredits_2a zorder 47
    show mcredits_2b zorder 46
    show mcredits_2c zorder 45

    pause 20
    jump credits4

label credits4:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    $ consolehistory = []
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    show starring
    pause 9.12
    hide starring
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Автор идеи и сценарист" as credits_header_1 at credits_text_scroll_left
    show credits_text_small "\n\nChiff the Oblivious #4251\nEthan (Just Monika#7954)" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg1.png\")", "В доступе отказано.")
    elif True:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg1.png\")", "В доступе отказано.")
    show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Художники по спрайтам" as credits_header_2 at credits_text_scroll_right
    $ pause (0.5)
    show credits_text_small "\n\nAjTheYandere#9808\nAkame#8940\nAri#5636\nAverage#3201\nChildish-N (DeviantArt)\nChiff the Oblivious#4251\nCyrke#8043\nEdinIsHere#4122\nEthan (Just Monika#7954)\nEzfi#9209\nhalibabica#2422\nHansen-Chan (DDNP\nLeoDeCraprio#4239\nMalukah Maker#2907\nNormallyAverage#3201" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(25.55 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg2.png\")", "В доступе отказано (2).")
    elif True:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg2.png\")", "В доступе отказано (2).")
    show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Художники по спрайтам" as credits_header_1 at credits_text_scroll_left
    show credits_text_small "\n\nPluralRoses#0136\nRocky#1118\nY?ZZIE™#5015\nSpei?er#7316\nStefano#4553\nSuperior Cabbage#1315\nyagamirail0#7046\nyazzy-.chr#0151\nu/Http_Bxbygirl-\nu/badooga1\nu/Mouhantain\nRPG Maker MV" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg1.png\")", "В доступе отказано (3).")
    elif True:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg1.png\")", "В доступе отказано (3).")
    show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Художники по фонам" as credits_header_2 at credits_text_scroll_right
    $ pause (0.5)
    show credits_text_small "\n\n\nAlex [[ORG]#9077\nChiff the Oblivious#4251\nCyrke#8043\nFrau Engel (Sims 3 Modder)\nkimagure\nminikle\nNuxill#7870\nObsoletovsky (DDNP) (36u8CZs)\nQQQnoQnoSpei?er#7316\nyagamirai10#7046\nhttps://cloudnovel.net/fluffness\nhttps://k-after.at.webry.info\nhttp://moonwind.pw\nhttps://pixabay.com\nhttp://teddy-plaza.sakura.ne.jp" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(43.75 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg2.png\")", "В доступе отказано (4).")
    elif True:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg2.png\")", "В доступе отказано (4).")
    show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "художники CG" as credits_header_1 at credits_text_scroll_left
    show credits_text_small "\n\nAjTheYandere#9808\nAverage#3201\nChiff the Oblivious#4251\nCyrke#8043\nElon_thelad#7496\njayunderarrest#8020\nnormie#4456\nPooshi#3700" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg3.png\")", "В доступе отказано (5).")
    elif True:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg3.png\")", "В доступе отказано (5).")
    show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Композитор" as credits_header_2 at credits_text_scroll_right
    show credits_text_small "Композитор Scott Buckley - www.scottbuckley.com.au\nMusic by St4bility - soundcloud.com/st4bility\nBenjamin Tissot (Royalty Free Music from www.bensound.com)\nChiff the Oblivious#4251\nChild of Ragnarok#0688\nHumble SFX Bundle\nSpei?er#7316\nVirtualKibou#0811\nhttp://bit.ly/PablosCornerYT" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg3.png\")", "В доступе отказано (6).")
    elif True:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg3.png\")", "В доступе отказано (6).")
    show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Программист" as credits_header_1 at credits_text_scroll_left
    show credits_text_small "Chiff the Oblivious#4251\nFL13#0023\nNikso#5950\nOkieDoki#4511\nTerra#2060" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg1.png\")", "В доступе отказано (7).")
    elif True:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg1.png\")", "В доступе отказано (7).")
    show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "UI" as credits_header_2 at credits_text_scroll_right
    show credits_text_small "Chiff the Oblivious#4251\nEnra#0080\nEthan (Just Monika#7954)\nJohnRDVSMarston#5275\nOwO what_s this_ Bittersweet#2161\nTheMelodyofGaming#7515\nu/Diana_Elizabeth_\nFreedoom" as credits_text_2 at credits_text_scroll_right
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    show bug_sticker at credits_sticker_5
    show prof_sticker at credits_sticker_6
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg2.png\")", "В доступе отказано (8).")
    elif True:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg2.png\")", "В доступе отказано (8).")
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Особые благодарности" as credits_header_1 at credits_text_scroll_left
    show credits_text_small "Angelic Beast#5498\nDarkSyner76#0126\nEthan (Just Monika#7954)\nHanaka (GangstaKingofSA#0235)\nKarasilSothren#2772\nPhantomhive#8729\nSeantience#2926\nTitan#5290\nultrastarwarsfan#9550" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg3.png\")", "В доступе отказано (9).")
    elif True:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg3.png\")", "В доступе отказано (9).")
    show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Очень особые благодарности" as credits_header_2 at credits_text_scroll_right
    show credits_text "Team Salvato\nScott Buckley\nTerra#2060" as credits_text_2 at credits_text_scroll_right
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/m_cg1.png\")", "Ваш аккаунт заблокирован.")
    elif True:
        call updateconsole_clearall ("os.remove(\"images/cg/m_cg1.png\")", "Ваш аккаунт заблокирован.")
    show credits_header "Перевод – команда\n\"Team Анархисты\"" as credits_header_2 at credits_text_scroll_right
    show credits_text_small "Владислав Кравченко\naka Maddie, The Mad\nKrailak Nekolover\nВиктория Масвина\nВладислав Лапов" as credits_text_2 at credits_text_scroll_right
    $ pause(116.80 - (datetime.datetime.now() - starttime).total_seconds())
    call updateconsole ("os.remove(\"game/screens.rpy\")", "Ваш аккаунт заблокирован.")
    call updateconsole ("--", "Что происходит?")
    call updateconsole ("--", "Почему я не могу ничего удалить?")
    call updateconsole ("Разрешить доступ для Аки", "Этот аккаунт заблокирован.")
    $ pause(128.42 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole
    scene credits_ts
    with dissolve_scene_full
    play sound page_turn
    show credits_text "Модифицировано с любовью":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 1.0 alpha 1
        6.5
        linear 1.0 alpha 0
    pause 9.3

    if dimensions_sroute == True:
        if dimensions_t1 == True:
            show poem_s1 with Dissolve (1)
        if dimensions_t2 == True:
            show poem_s2 with Dissolve (1)
        if dimensions_t3 == True:
            show poem_s3 with Dissolve (1)
    if dimensions_nroute == True:
        if dimensions_t1 == True:
            show poem_n1 with Dissolve (1)
        if dimensions_t2 == True:
            show poem_n2 with Dissolve (1)
        if dimensions_t3 == True:
            show poem_n3 with Dissolve (1)
    if dimensions_yroute == True:
        if dimensions_t1 == True:
            show poem_y1 with Dissolve (1)
        if dimensions_t2 == True:
            show poem_y2 with Dissolve (1)
        if dimensions_t3 == True:
            show poem_y3 with Dissolve (1)
    if dimensions_mroute == True:
        if dimensions_t1 == True:
            show poem_m1 with Dissolve (1)
        if dimensions_t2 == True:
            show poem_m2 with Dissolve (1)

    $ renpy.pause()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
