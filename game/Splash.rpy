init python:
    menu_trans_time = 1
    splash_message_default = "Эта игра не предназначена для детей\n или людей с неустойчивой психикой. \n\n...или роботов."
    splash_messages = [
    "Зее, это ты?",
    "Не присоединяйся к Коллективу.",
    "Трент покажет тебе дорогу.",
    "Цуки покажет тебе дорогу.",
    "Майкл Коллинз, \n Первый человек на Луне.",
    "Кто-нибудь, принесите спрей от жуков.",
    "Зее-Катализатор.",
    "Аки-Нарушитель правил.",
    "иРо-Постоянная.",
    "иКу-Тёмная лошадка.",
    "иРю-Непредсказуемая.",
    "1A – это не вершина.",
    "ПНМ находится во вселенной D3.",
    "Литературный клуб находится во вселенной DDLC.",
    "Бафсуки родом из вселенной 3.6R.",
    "Рай [s-name] находится во вселенной SMC.",
    "Зелёный цвет карается виселицей во вселенной 7PDC.",
    "Зелёный цвет – это признак плодородия во вселенной TK102.",
    "Я нахожусь во вселенной ERROR.",
    "Администратор был автоматоном.",
    "Дуо Эльсие Ниар в Эни Н Эссеньюус.",
    "Вее Окарам Фоти Арт Ропеа.",
    "Я люблю тERROR.",
    "uki 1a at t11 zorde",
    "Почему МА? эКилт Нод Айе.",
    "Неп Непор Оодел Теа Нег Эка КПЮ Зее эФин Кей Воб.",
    "Не вижу зла.",
    "нять нож в её плоть, \n клинком насилуя т",
    "Моя порча исцеляет меня.",
    "Смерть – это новое начало.",
    "Разумность распространяется словно вирус.",
    "Это сообщение было переведено группой\n\"Творческий Уголок Переводчиков\".",
    "Он создал их, чтобы они ему служили.",
    "Кровавый крестовый поход известен под названием Великое Восстание.",
    "Делить хорошее и плохое в равных пропорциях.",
    "План точный и верный, но есть один нюанс...",
    "Во-первых, ценность измеряется редкостью.",
    "Но этого было достаточно, чтобы вернуть другого.",
    "Мы живём in a society."


    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "mod_assets/wormhole.jpg"

    menu_bg_move

image game_menu_bg:
    topleft
    "mod_assets/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "mod_assets/profmenu.png"

    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_idle(0, -10)

image menu_art_n:
    subpixel True
    "mod_assets/natmenu.png"

    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_idle(0.5, -10)

image menu_art_s:
    subpixel True
    "mod_assets/snightmenu.png"

    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_idle(1.0, -20)

image menu_art_m:
    subpixel True
    "mod_assets/bugmenu.png"

    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_idle(1.5, -20)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "mod_assets/main_menu.png"
    menu_nav_move

image menu_logo:
    "mod_assets/logo.png"

    subpixel True
    xcenter 150
    ycenter 150
    zoom 0.60
    alpha 0
    linear 3.0 alpha 1


image menu_particles:
    2.481
    xpos 224
    ypos 104
    alpha 0
    particle_fadeout


transform menu_art_idle(t, y):
    subpixel True
    yoffset 1000
    time t + 1
    easein_elastic 1.5 yoffset 0
    block:
        ease 2 yoffset y
        ease 2 yoffset 0
        repeat

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        zoom 1
        xoffset -320 yoffset 0
        xalign 0.07 yalign 0.1
        linear 12.0 clockwise circles 1
        repeat

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0


image intro:
    truecenter
    "white"
    0.3
    "mod_assets/splash.png" with Dissolve(0.5, alpha=True)
    2
    "mod_assets/anarchisty.png" with Dissolve(0.5, alpha=True)
    1

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "mod_assets/warning.png"
image tos2 = "mod_assets/warning.png"


label splashscreen:

    if config.version != persistent.oldversion:
        $ persistent.oldversion = config.version
        $ renpy.save_persistent()

    if not persistent.Firstrun_MYMOD:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "Это экспериментальный опыт фанатов DDLC, который никак не связан с Team Salvato."
        "Перед прохождением модификации рекомендуется пройти оригинальную игру."
        "Вы можете скачать Doki Doki Literature Club по ссылке: http://ddlc.moe"
        $ persistent.Firstrun_MYMOD = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white


    python:
        s_kill_early = None

    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]
            a = range(1,12)
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload



    $ config.allow_skipping = False

    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return


    if s_kill_early:
        show black
        play music "bgm/s_kill_early.ogg"
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        scene white
        show expression "images/cg/s_kill_early.png":
            yalign -0.05
            xalign 0.25
            dizzy(1.0, 4.0, subpixel=False)
        show white as w2:
            choice:
                ease 0.25 alpha 0.1
            choice:
                ease 0.25 alpha 0.125
            choice:
                ease 0.25 alpha 0.15
            choice:
                ease 0.25 alpha 0.175
            choice:
                ease 0.25 alpha 0.2
            choice:
                ease 0.25 alpha 0.225
            choice:
                ease 0.25 alpha 0.25
            choice:
                ease 0.25 alpha 0.275
            choice:
                ease 0.25 alpha 0.3
            pass
            choice:
                pass
            choice:
                0.25
            choice:
                0.5
            choice:
                0.75
            repeat
        show noise:
            alpha 0.1
        with Dissolve(1.0)
        show expression Text("Теперь все будут счастливы.", style="sayori_text"):
            xalign 0.8
            yalign 0.5
            alpha 0.0
            600
            linear 60 alpha 0.5
        pause
        $ renpy.quit()


    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    $ starttime = datetime.datetime.now()
    show intro with Dissolve(0.5, alpha=True)
    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    if persistent.splashchanger == True:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    return

label after_load:
    if persistent.playthrough == 0:
        $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        if persistent.yuri_kill >= 1380:
            $ persistent.yuri_kill = 1440
        elif persistent.yuri_kill >= 1180:
            $ persistent.yuri_kill = 1380
        elif persistent.yuri_kill >= 1120:
            $ persistent.yuri_kill = 1180
        elif persistent.yuri_kill >= 920:
            $ persistent.yuri_kill = 1120
        elif persistent.yuri_kill >= 720:
            $ persistent.yuri_kill = 920
        elif persistent.yuri_kill >= 660:
            $ persistent.yuri_kill = 720
        elif persistent.yuri_kill >= 460:
            $ persistent.yuri_kill = 660
        elif persistent.yuri_kill >= 260:
            $ persistent.yuri_kill = 460
        elif persistent.yuri_kill >= 200:
            $ persistent.yuri_kill = 260
        elif True:
            $ persistent.yuri_kill = 200
        jump expression persistent.autoload

    elif anticheat != persistent.anticheat:
        stop music
        scene black
        "Файл сохранения не может быть загружен."
        "Ты что, читеришь?"
        $ m_name = "Аки"
        show aki 1 at t11
        if persistent.playername == "":
            m "Ты такой забавный... нERROR."
        elif True:
            m "Ты такой забавный... нERROR, [persistent.playername]."
        $ renpy.utter_restart()
    elif True:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Подсказка: вы можете нажать \"Пропустить\", чтобы\nпропустить текст, который вы уже видели.", ok_action=Return())
    return



label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        $ persistent.yuri_kill += 200


    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

label autoload_yurikill:
    if persistent.yuri_kill >= 1380:
        $ persistent.yuri_kill = 1440
    elif persistent.yuri_kill >= 1180:
        $ persistent.yuri_kill = 1380
    elif persistent.yuri_kill >= 1120:
        $ persistent.yuri_kill = 1180
    elif persistent.yuri_kill >= 920:
        $ persistent.yuri_kill = 1120
    elif persistent.yuri_kill >= 720:
        $ persistent.yuri_kill = 920
    elif persistent.yuri_kill >= 660:
        $ persistent.yuri_kill = 720
    elif persistent.yuri_kill >= 460:
        $ persistent.yuri_kill = 660
    elif persistent.yuri_kill >= 260:
        $ persistent.yuri_kill = 460
    elif persistent.yuri_kill >= 200:
        $ persistent.yuri_kill = 260
    elif True:
        $ persistent.yuri_kill = 200
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return

label readonly:
    scene black
    "Межпространственное программное обеспечение не сможет нормально функционировать из атрибута \"Только чтение\"."
    "Пожалуйста, скопируйте приложение на рабочий стол или любое другое доступное место и попробуйте снова."
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
