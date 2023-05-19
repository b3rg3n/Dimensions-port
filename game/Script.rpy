


label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer

    $ lowplayer = player.lower()
    $ s_name = "С. Найт"
    $ m_name = "???"
    $ n_name = "Солдатик"
    $ y_name = "Проффесор"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True


    default dimensions_sroute = False
    default dimensions_mroute = False
    default dimensions_yroute = False
    default dimensions_nroute = False


    default dimensions_t1 = False
    default dimensions_t2 = False
    default dimensions_t3 = False

    $ persistent.splashchanger = False

















    call dim01




    call dim02





    call dim03


    call dim04


    call dim05


    call dim06


    call dim07


    call dim08


    if dimensions_aroute == True:
        call credits3
    elif True:
        call credits

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
