label dim08:
    stop music fadeout 2.0
    scene bg blackbackground
    with dissolve_scene_full
    $ s_name = "C. Найт"
    $ n_name = "С-т Нацуки"
    $ m_name = "Д-р Баг"
    $ pm_name = "Моника Прайм"
    $ pmc_name = "[player] Прайм"
    $ ps_name = "Сайори Прайм"
    $ pn_name = "Нацуки Прайм"
    $ py_name = "Юри Прайм"
    $ bn_name = "Орда Бафсуки"
    $ dy_name = "Юлия"
    $ ds_name = "Саманта"
    $ kmc_name = "Супер [player]"
    $ km_name = "Принцесса Магнолия"
    $ ks_name = "Саиджи"
    $ ky_name = "Юрси"
    $ em_name = "Императрица Моника Прайм"
    $ emc_name = "[player] Возвышенный"
    $ rb_name = "Синий робот"
    $ rr_name = "Красный робот"
    $ ry_name = "Жёлтый робот"




































    if dimensions_aroute == False:
        "Что это только что было, игрок?"
        $ persistent.splashchanger = True
        "Я не мог говорить в червоточине, но я слышал каждое слово…"
        $ timeout_label = None
        menu:
            "Прости, [player], но фрагмент помог исправить мод." if True:
                "Я это понял, но кто вообще этот фрагмент?"
        menu:
            "Это была Моника, которую ты слышишь в червоточинах." if True:
                "Моника Прайм?"
        menu:
            "Скорее… Прайм Моника Прайм." if True:
                "Игрок, знать тебя – это самый странный и необычный опыт в моей жизни."
        menu:
            "Технически, это {i}единственный{/i} опыт в твоей жизни." if True:
                "Ну да, и не говори."
                "Обычно чернота длится покороче."
                "Что, фрагмент забыл исправить эту часть?"
        menu:
            "Я тоже не знаю. Есть идеи?" if True:
                "Ты у меня спрашиваешь? Должно быть, ты в отчаянии."
        menu:
            "Я просто хочу знать, что произойдёт дальше." if True:
                "Знаешь, это уже не просто история. Это происходит на самом деле."
        menu:
            "Поставь себя на моё место – просто смотреть очередную драму на экране." if True:
                "А я думал, что ты заботишься о нас. Причём неважно, живы мы или мертвы."
        menu:
            "Я уверен, ты тоже заботишься о твоих любимых персонажах." if True:
                "Персонажи… ага…"
                "Так я персонаж или всё-таки человек?"
                "Есть вообще разница?"
        menu:
            "Персонажи нереальны." if True:
                "Звучишь прямо как Моника Прайм."
                "А она – это просто конченный психопат."
                "Это плохая точка зрения, дружище."
            "Персонажи – это средства повествования." if True:
                "Хе-хе, тогда, я думаю, это должно значить, что в моей жизни смысл есть."
                "Может, это просто история."
                "Если и так, то тогда мы должны дать ей красивую концовку."
            "Персонажи символичны." if True:
                "Прямо как Бэтмен или Робин Гуд… Воплощение определённых черт характера."
                "Может, всё это время всё это было наоборот?"
                "Может, персонаж куда более реален, чем человек."
        "В любом случае, есть мысль об исправлении этой оплошности."
        "Если ты нажмёшь кнопку \"Исправить проблему.\", думаешь, поможет?"
    menu:
        "Исправить проблему." if True:
            scene bg mainhall
            with dissolve_scene_full

    play music mop
    if dimensions_aroute == False:
        "Хах, сработало. Мы наконец-то дома!"
        "Хотя нет, это значит, что Возвышенный тоже здесь..."
    show empress 1a zorder 2 at t41
    show sayori 2a zorder 2 at t42
    show natsuki 1f1 zorder 2 at t43
    show yulia 1a zorder 2 at t44
    if dimensions_aroute == False:
        "Ну хотя бы мы дома, все здесь, и всё хорошо, и слава тебе Господи."
    if dimensions_aroute == True:
        "Странное ощущение..."
    "Состав из четырёх человек, стоящих передо мной, выглядит печально ностальгирующе."
    show sayori 2c
    s "Должно быть, он направляется к комнате управления."
    show sayori 2b
    show yulia 1f
    dy "Только игрок знает, что он там делает."
    show sayori 2a
    show yulia 1g
    show empress 1k
    em "Ты серьёзно только что это сказала?"
    show empress 1j
    show yulia 1a
    show natsuki 1h6
    n "Разговорчики в строю."
    show natsuki 1f24
    show empress 2i
    em "Ты такая бука."
    show natsuki 1f25
    show empress 2h
    n "Так вообще-то и было задумано."
    show empress at thide
    hide empress
    show yulia at thide
    hide yulia
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    "Система громкой связи начинает потрескивать."
    emc "Добрый вечер."
    emc "Здесь за главного я."
    emc "Вы все уволены."
    show yulia 1e zorder 2 at t11
    dy "Меня вообще-то и не нанимали..."
    show yulia at thide
    hide yulia
    emc "Вы уже, наверное, заметили, что я забаррикадировал двери в главный холл."
    emc "Я бы хотел, чтобы вы там и стояли, пока я… тестирую кое-что…"
    show empress 1g zorder 2 at t11
    em "Клянусь, ещё вчера у него не было мании величия."
    show empress 1e zorder 2 at t21
    show sayori 2j zorder 2 at t22
    s "Кто бы говорил."
    show empress 2k
    em "Туше."
    show empress at thide
    hide empress
    show sayori at thide
    hide sayori
    emc "Я несколько улучшил проход под аркой. Надеюсь, вам понравится."
    emc "Теперь вместо входа в червоточину можно будет создать выход из неё."
    show natsuki 1f6 zorder 2 at t11
    n "Почему нам не пофиг, придурок?"
    show natsuki 1f7 zorder 2 at t21
    show yulia 2d zorder 2 at t22
    dy "Может, монстры из слизи?"
    show sayori 2l zorder 2 at t31
    show natsuki 1f7 zorder 2 at t32
    show yulia 2a zorder 2 at t33
    s "Я же говорила, что наши приключения ещё не закончились?"
    show sayori 2a
    show natsuki 1f24
    show yulia 2m
    n "А это обязательно должно включать монстров из слизи?.."
    show empress 2d zorder 2 at t41
    show sayori 2a zorder 2 at t42
    show natsuki 1f7 zorder 2 at t43
    show yulia 2m zorder 2 at t44
    em "О чём вы все говорите?"
    show yulia 2a
    show sayori 2j
    show empress 2c
    s "Ничего из того, что твоя межпространственная задница сможет понять."
    show natsuki 1f25
    show sayori 2a
    show empress 1f
    "Нац хихикает."
    show natsuki 1f1
    show yulia 1h
    dy "Наверное, нам нужно что-то делать."
    show yulia 1g
    show sayori 2g
    s "Да, но что именно? Дверь даже и не думает сдвинуться с места."
    show yulia at thide
    hide yulia
    show sayori at thide
    hide sayori
    show empress at thide
    hide empress
    show natsuki 1f11 zorder 2 at t11
    n "Баффи?"
    show natsuki 1f3 zorder 2 at t22
    show bhorde 3g zorder 2 at t21
    bn "Гыр-р-р?"
    show natsuki 1f5
    n "Покажи этой двери, кто тут мамочка."
    show bhorde 3y
    show natsuki 1f1
    bn "Хэ-хэ-хэ-х-х-х-х!"
    show natsuki at thide
    hide natsuki
    show bhorde at thide
    hide bhorde
    "Баффи и остальные Бафсуки мчатся к двойным дверям."
    play sound d08bufffail
    "И впервые неостановимая сила сталкивается с недвижимым объектом."
    play sound d08bufffail
    "Они продолжают крушить дверь, но безуспешно."
    show empress 1r zorder 2 at t11
    em "Полцарства за свободное перемещение…"
    show empress at thide
    hide empress
    emc "Я слышу ваше ворчание здесь."
    emc "Уверяю, вы отсюда не выберетесь."
    stop music fadeout 3.0
    emc "Начинается рубрика э-э-э-эксперименты."
    emc "Поздоровайтесь с вооружёнными силами измерения XN2."
    python:
        renpy.sound.play("mod_assets/sfx/01 Wormhole Rumble.ogg", loop=True)
    "Комната начинает трястись, арка червоточин сильно заряжается."

    show natsuki_prime 1c zorder 2 at t31
    show samantha 4j zorder 2 at t32
    show yuri_prime 2e zorder 2 at t33
    ds "Всем держаться вместе и докладывать об угрозах."
    show samantha 4i
    show yuri_prime 2c
    py "Ладно, Сэм, мы и так далеко зашли."
    show yuri_prime 2a
    show samantha 4d
    show natsuki_prime 5y
    pn "Избить побольше задир? Чёрт возьми, да."
    show natsuki_prime 5a
    "А вот и молодёжка ПНМ. Горжусь."
    show natsuki_prime at thide
    hide natsuki_prime
    show samantha at thide
    hide samantha
    show yuri_prime at thide
    hide yuri_prime
    emc "Ах, да, забыл упомянуть – это тяжело вооружённые роботы."
    show yurshi d zorder 2 at t41
    show supermc 5k zorder 2 at t42
    show magnolia 1c zorder 2 at t43
    show sayigi 3d zorder 2 at t44
    kmc "Ха-ха, этот напыщенный индюк только что-о предупредил нас, с чем мы сталкиваемся."
    show yurshi d2
    show sayigi 3x
    show supermc 5m
    ks "Да! Нам просто нужна вода, и много воды."
    show sayigi 3a
    show yurshi d
    show magnolia 2d
    km "И где именно ты предлагаешь её достать?"
    show yurshi j
    show magnolia 2e
    show supermc 2a
    ky "Оставьте это мне."
    show yurshi at thide
    hide yurshi
    show supermc at thide
    hide supermc
    show magnolia at thide
    hide magnolia
    show sayigi at thide
    hide sayigi
    "Я смотрю, куда именно Юрси направляет свой язык…"
    "Точно – система распыления."
    show supermc 3c zorder 2 at t11
    kmc "Должно срабо-отать."
    python:
        renpy.sound.play("mod_assets/sfx/08 MC Charges Fireball.ogg", loop=None)
        renpy.sound.queue("mod_assets/sfx/01 Wormhole Rumble.ogg", loop=True)
    show supermc 6l
    "Он начинает заряжать огненный шар."
    show supermc at thide
    hide supermc
    "Нужно предупредить остальных."
    show empress 1c zorder 2 at t41
    show sayori 2g zorder 2 at t42
    show natsuki 1f7 zorder 2 at t43
    show yulia 1e zorder 2 at t44
    mc "Внимание всем! Пол – это лава!"

    if dimensions_sroute == True:
        show sayori 2l
        s "[s_player], ты настоящий инфантил."
        show sayori 2e
        mc "Нет, я серьёзно, нужно убираться с пола, сейчас же!"
        show sayori 4n
        s "О! Теперь поняла!"
    if dimensions_nroute == True:
        if dimensions_t1 == True:
            show natsuki 1h7
            n "Рядовой, твои шуточки просто…"
            mc "Нет, я серьёзно, нужно убираться с пола, сейчас же!"
            show natsuki 1h3
            n "Ох… Прости, чувак."
        if dimensions_t2 == True:
            show natsuki 1h7
            n "[player], твои шуточки просто..."
            mc " Нет, я серьёзно, нужно убираться с пола, сейчас же!"
            show natsuki 1h3
            n "Ох… Прости, чувак."
        if dimensions_t3 == True:
            show natsuki 1h7
            n "[player], твои шуточки просто..."
            mc " Нет, я серьёзно, нужно убираться с пола, сейчас же!"
            show natsuki 1h3
            n "Ох… Прости."
    if dimensions_yroute == True:
        show yulia 1f
        dy "Я не знаю, что это значит, мистер [player]."
        show yulia 1e
        mc "Это значит убирайтесь с пола, сейчас же!"
        show yulia 2c
        dy "Ох, ладно, спасибо."
    if dimensions_mroute == True:
        show empress 2d
        em "[pm_player], ты совсем спятил?"
        show empress 2f
        mc " Нет, я серьёзно, нужно убираться с пола, сейчас же!"
        show empress 2l
        em "О, я поняла!"

    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    show yulia at thide
    hide yulia
    show empress at thide
    hide empress
    "Каждый находит свой островок."
    python:
        renpy.sound.play("mod_assets/sfx/08 Fireball.ogg", loop=None)
        renpy.sound.queue("mod_assets/sfx/01 Wormhole Rumble.ogg", loop=True)
    "Супер [player] делает свой ход."


    "Грохот усиливается. Арка выглядит так, словно она разорвётся на части."
    stop sound fadeout 0.5
    call rain
    stop music fadeout 5.0

    "Разбрызгиватели борются с огнём, как и было задумано."
    mc "Теперь нам просто нужно электричество!"
    show brob 1 zorder 2 at t32
    "Робот из XN2 появляется передо мной."
    play sound d08robo1
    rb "Какое значение этих… осадков."
    show rrob 1 zorder 2 at t31
    "И ещё один."
    play sound d08robo2
    rr "Тревога. Единица была похищена."
    show yrob 1 zorder 2 at t33
    "Через некоторое время их уже десятки вокруг."
    play sound d08robo3
    ry "Зелёноволосый человек. Идентифицируйте себя немедленно."
    mc "Э-э-э…"
    play sound d08robo1
    rb "Ошибка распознания. Авторизировано использование летальной силы."
    mc "Постойте, постойте, меня зовут..."
    "Я оглядываюсь в надежде на хоть какую-то идею."
    "Хм-м… а что насчёт…"
    mc "Генри Баг."
    play sound d08robo3
    ry "Сканирование."
    ry "..."
    play sound d08robo2
    ry "Ответ отрицательный. Доктор Генри Баг – это основатель межпространственного путешествия. А вы – мошенник и самозванец."
    rr "Последняя попытка."
    show brob at thide
    hide brob
    show rrob at thide
    hide rrob
    show yrob at thide
    hide yrob
    "Я вижу, что остальные тоже суетятся в попытке решить наше затруднительное положение."
    show natsuki_prime 3c zorder 2 at t31
    show samantha 4e zorder 2 at t32
    show yuri_prime 2f zorder 2 at t33
    py "[player]! Рубильник!"
    show natsuki_prime at thide
    hide natsuki_prime
    show samantha at thide
    hide samantha
    show yuri_prime at thide
    hide yuri_prime
    show bg power1 with wipeleft
    "Я замечаю главный выключатель."
    "Включено. Но как же его использовать?"
    show bg mainhall with wipeleft
    show natsuki_prime 1t zorder 2 at t31
    show samantha 1b zorder 2 at t32
    show yuri_prime 2n zorder 2 at t33
    pn "Юри! Поцелуй меня!"
    show samantha 1d
    show yuri_prime 2q
    show natsuki_prime 1z
    "Юри Прайм очень смущена от такого предложения."
    show samantha 1r
    ds "Я же говорила."
    show samantha 1q
    show natsuki_prime 1c
    pn "Вот, [player], тебе понадобится это."
    show natsuki_prime 1a
    play sound d02yuripass
    "Нацуки Прайм даёт мне нож. Неужели Юри дала ей это?"
    show natsuki_prime at thide
    hide natsuki_prime
    show samantha at thide
    hide samantha
    show yuri_prime at thide
    hide yuri_prime

    "Я поворачиваюсь и бегу к выключателю."
    show brob 1 zorder 2 at t32
    show rrob 1 zorder 2 at t31
    show yrob 1 zorder 2 at t33
    "...но мой ход предугадали заранее."
    rr "Все единицы, задействовать боевой режим."
    play sound d08weaponcharging
    "Я слышу, как все их орудия заряжаются. Нужно действовать быстро!"
    show rrob at thide
    hide rrob
    "Я пробегаю через одного робота XN2..."
    show yrob at thide
    hide yrob
    "...второго я просто силой отталкиваю в сторону."
    "Ещё один всё ещё стоит впереди."
    play sound d08robo4
    rb "Ракеты взведены. Все человекоподобные цели заблокированы."
    "Ну же, [player], не теряй насмарку!"
    show brob at thide
    hide brob

    show bg power1 with wipeleft

    "Вот оно!"
    play sound d08hackcable
    "Я взламываю кабель с помощью ножа."
    "Наверное, стоило сперва отключить питание, но не время для техники безопасности!"

    show bg power2

    "В мгновение ока кабель отрезан, и он начинает свисать вниз, к воде."
    "Чёрт, нужно же убираться с пола!"

    show bg mainhall with wipeleft
    show yrob 1 zorder 2 at t11
    "Я разворачиваюсь и вижу, как жёлтый робот направляет свою пушку прямо над головой."
    play sound d08robo3
    ry "До свидания."
    "Я отпрыгиваю к стене и схватываю коробку выключателей."

    show yrob 2 zorder 2 at t11
    play sound d08electrocuted
    ry "ОШИ-И-И-И-И-И-И-И-И-И-И-И"
    show yrob 2 at thide
    hide yrob
    play sound d08roboclunk
    "Неуклюжий робот вместе с остальными падают на землю."

    menu:
        "Попробовать выключить и включить его снова." if True:
            mc " Попробовать выключить и включить его снова."
        "Я люблю с корочкой." if True:
            mc " Я люблю с корочкой."
        "Для вас это была слишком короткая жизнь." if True:
            mc " Для вас это была слишком короткая жизнь."
        "Ребята, а что такие неживые?" if True:
            mc "Ребята, а что такие неживые?"

    "Я выключаю питание и падаю на землю."
    "Разбрызгиватели, кажется, тоже отключились."

    call rain_stop
    play music mop fadein 3.0

    if dimensions_sroute == True:
        if dimensions_t1 == True:
            show sayori 1s zorder 2 at t11
            s "Ха-ха, придурок."
        if dimensions_t2 == True:
            show sayori 1s zorder 2 at t11
            s "Ха-ха, столь очаровательный, но всё равно придурок."
        if dimensions_t3 == True:
            show sayori 1s zorder 2 at t11
            s " Ха-ха, столь очаровательный, но всё равно придурок."
    if dimensions_nroute == True:
        if dimensions_t1 == True:
            show natsuki 1f25 zorder 2 at t11
            n "Х-х-х… это было плохо."
        if dimensions_t2 == True:
            show natsuki 1f25 zorder 2 at t11
            n " Х-х-х… это было плохо."
        if dimensions_t3 == True:
            show natsuki 1f25 zorder 2 at t11
            n " Х-х-х… это было охренеть как плохо."
    if dimensions_yroute == True:
        if dimensions_t1 == True:
            show yulia 1s zorder 2 at t11
            dy "У тебя довольно странное чувство юмора."
        if dimensions_t2 == True:
            show yulia 1s zorder 2 at t11
            dy "У тебя довольно необычайное чувство юмора."
        if dimensions_t3 == True:
            show yulia 1s zorder 2 at t11
            dy "У тебя довольно необычайное чувство юмора."
    if dimensions_mroute == True:
        show empress 3k zorder 2 at t11
        em "Это было очень плоско, игрок."
        show empress 1j
        em "Плоско, но подло. Мне нравится."

    menu:
        "Запп Бренниган, к вашим услугам." if True:
            mc "Запп Бренниган, к вашим услугам."
        "Спасибо, дамы и господа, думаю, я возьму это себе в оборот." if True:
            mc "Спасибо, дамы и господа, думаю, я возьму это себе в оборот."
        "Что я ещё могу сказать? Было довольно мощно." if True:
            mc "Что я ещё могу сказать? Было довольно мощно."
        "Слишком просто. Даже не напрягся." if True:
            mc "Слишком просто. Даже не напрягся."

    if dimensions_sroute == True:
        if dimensions_t1 == True:
            show sayori 2l
            s "Я скучала по твоему каламбуру."
            show sayori 2d
            mc "Правда что ли? Я уж подумал, что у тебя выработалось сопротивление к этому."
            show sayori 2b
            s "Может быть..."
            mc "{i}Сопротивление{/i}."
            show sayori 1p
            s "О, боже…"
            show sayori at thide
            hide sayori
        if dimensions_t2 == True:
            show sayori 2l
            s "Я скучала по твоим замечательным каламбурам."
            show sayori 2d
            mc "Правда что ли? Я уж подумал, что у тебя выработалось сопротивление к этому "
            show sayori 2b
            s "Ну, может, но они мне всё ещё нравятся."
            mc "{i}Сопротивление{/i}."
            show sayori 1p
            s "О, божечки…"
            show sayori at thide
            hide sayori
        if dimensions_t3 == True:
            show sayori 2l
            s "Я скучала по твоим каламбурам, дорогой."
            show sayori 2d
            mc "Правда что ли? Я уж подумал, что у тебя выработалось сопротивление к этому."
            show sayori 2b
            s "Ну, может, и должно быть, мне стоит просто принять это и жить дальше."
            mc "{i}Сопротивление{/i}."
            show sayori 1p
            s "О, божечки…"
            show sayori at thide
            hide sayori
    if dimensions_nroute == True:
        if dimensions_t1 == True:
            show natsuki 1f20
            n "Ты меня просто убиваешь, рядовой."
            show natsuki 1f24
            mc "А я уж было подумал, что у тебя выработалось сопротивление к этому."
            show natsuki 1f25
            n "Нет-нет, ничего против подлости я не имею."
            show natsuki 1f13
            mc "{i}Сопротивление{/i}."
            show natsuki 1e24
            n "О, боже…"
            show natsuki at thide
            hide natsuki
        if dimensions_t2 == True:
            show natsuki 1f20
            n "Ты меня просто убиваешь, [player]."
            show natsuki 1f24
            mc "А я уж было подумал, что у тебя выработалось сопротивление к этому."
            show natsuki 1f25
            n "Нет-нет, ничего против подлости не имею."
            show natsuki 1f13
            mc "{i}Сопротивление{/i}."
            show natsuki 1e24
            n "О, божечки…"
            show natsuki at thide
            hide natsuki
        if dimensions_t3 == True:
            show natsuki 1f20
            n "Ты меня просто убиваешь, [player]."
            show natsuki 1f24
            mc "А я уж было подумал, что у тебя выработалось сопротивление к моему очарованию."
            show natsuki 1f25
            n "Не, ты так просто не отделаешься."
            show natsuki 1f13
            mc "{i}Сопротивление{/i}."
            show natsuki 1e24
            n "О, божечки…"
            show natsuki 1h27
            n "Ладно, забудь. Мы закончили."
            show natsuki at thide
            hide natsuki
    if dimensions_yroute == True:
        if dimensions_t1 == True:
            show yulia 1f
            dy "Ты на самом деле очень своеобразный человек."
            mc "Я уж было подумал, что у тебя выработалось сопротивление к моей своеобразности."
            show yulia 1d
            dy "Даже и не близко, мистер [player], ты настоящая редкость."
            show yulia 1e
            mc "{i}Сопротивление{/i}."
            show yulia 1q
            dy "О, боже… Я поняла."
            show yulia at thide
            hide yulia
        if dimensions_t2 == True:
            show yulia 1f
            dy "Ты на самом деле очень своеобразный человек, дорогой."
            mc "Я уж было подумал, что у тебя выработалось сопротивление к моей своеобразности."
            show yulia 1d
            dy "Даже и не близко, для меня ты бесконечно очарователен."
            show yulia 1e
            mc "{i}Сопротивление{/i}."
            show yulia 1q
            dy "О, божечки… Теперь поняла."
            show yulia at thide
            hide yulia
        if dimensions_t3 == True:
            show yulia 1f
            dy "Ты на самом деле очень своеобразный человек, дорогой."
            mc "Я уж было подумал, что у тебя выработалось сопротивление к моей своеобразности."
            show yulia 1d
            dy "Даже и не близко, для меня ты бесконечно очарователен."
            show yulia 1e
            mc "{i}Сопротивление{/i}."
            show yulia 1q
            dy "О, божечки… Теперь поняла."
            show yulia at thide
            hide yulia
    if dimensions_mroute == True:
        show empress 2k
        em "Ха-ха, скажи игроку, что он придурок."
        show empress 2d
        mc "О, он просто выбрал одну из моих шуток. [player] – это тот, с кем ты разговариваешь на текущий момент."
        show empress 2g
        em "Кажется, нужно отдать тебе должное, [pm_player]."
        mc "{i}Текущий{/i}."
        show empress 4l
        em "О, господи… Лучше бы я осталась злой."
        show empress at thide
        hide empress

    emc "Вы чё, издеваетесь? Хотя, стоит отдать вам должное."
    emc "Вы же всё-таки достаточно сыгранная команда, не так ли?"
    emc "Но твои шутки всё равно полная чушь, [player]."
    show empress 1a zorder 2 at t41
    show sayori 2j zorder 2 at t42
    show natsuki 1e1 zorder 2 at t43
    show yulia 1a zorder 2 at t44
    s "Ладно, вернёмся к придурку."
    show sayori 2g
    show empress 1n
    "Моника хихикает."
    show sayori 2l
    show empress 1m
    s "Тихо там. Юлия, есть идеи?"
    show sayori 2a
    show empress 1a
    show yulia 2w
    dy "Э-э… не хочу звучать глупо, но…"
    show yulia 2q
    show natsuki 1e7
    dy "Вы уверены, что дверь открывается наружу?"
    show natsuki 1f18
    show sayori 1n
    n "Ты издеваешься?"
    show natsuki 1f24
    "Я действительно не помню, я открывал её всего один раз, но Сайори помнить должна..."
    show sayori 1p
    show yulia 2d
    show natsuki 1f25
    show empress 1l
    s "Я, э-э… чёрт."
    show empress at thide
    hide empress
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    show yulia at thide
    hide yulia
    "Сайори медленно открывает дверь..."
    emc "Что, правда? Ох, ради всего святого..."
    emc "Ладно, неважно, увидимся в комнате управления."

    scene bg tunnel
    with wipeleft_scene

    emc "Ах, комната управления, комната управления… Неплохое эхо здесь, не так ли?"
    mc "Мужик, ты когда-нибудь заткнёшься?"
    if dimensions_sroute == True:
        show sayori 2d zorder 2 at t11
        s "Я ничего говорить не стану."
        "Я изо всех сил сопротивляюсь ответить."
        show sayori at thide
        hide sayori
    if dimensions_nroute == True:
        show natsuki 1f25 zorder 2 at t11
        n "Я ничего говорить не стану."
        "Я изо всех сил сопротивляюсь ответить."
        show natsuki at thide
        hide natsuki
    if dimensions_yroute == True:
        show yulia 1q zorder 2 at t11
        dy "Я ничего говорить не стану."
        "Я изо всех сил сопротивляюсь ответить."
        show yulia at thide
        hide yulia
    if dimensions_mroute == True:
        show empress 1n zorder 2 at t11
        em "Я ничего говорить не стану."
        "Я изо всех сил сопротивляюсь ответить."
        "А ещё я упустил возможность пошутить про сопротивление. Блин."
        show empress at thide
        hide empress
    emc "Ну же, глубоко внутри ты хочешь стать мной."
    emc "Со всей этой мощью, со всей уверенностью."
    emc "Это явно ново для тебя. Но придёт время, и ты привыкнешь."
    mc "Да заткнись ты уже!"
    show sayori 2a zorder 2 at t11
    s "Как ты сам раньше говорил, этот монстр – не ты."
    if dimensions_sroute == True:
        if dimensions_t1 == True:
            mc "Я знаю. Спасибо, дружище."
            show sayori 1d
            s "Всегда пожалуйста."
        if dimensions_t2 == True:
            mc "Я знаю. Спасибо, Сай."
            show sayori 1d
            s "Всегда пожалуйста, дорогой."
        if dimensions_t3 == True:
            mc "Я знаю. Спасибо, дорогая."
            show sayori 1y
            s "Всегда пожалуйста, хе-хе."
    if dimensions_sroute == False:
        mc "Я знаю. Спасибо, Сайори."
        show sayori 1d
        s "Всегда пожалуйста, дружочек."
    show sayori at thide
    hide sayori
    "Ну вот, опять всё заново."
    stop music fadeout 2.0

    scene bg control
    with wipeleft_scene

    show exalted 2k zorder 2 at t11
    play music thecall fadein 1.0
    emc "Я так рад, что вы справились."
    show exalted 1m
    if dimensions_sroute == True:
        s "Но ты же только что изо всех сил пытался нас остановить..."
    if dimensions_nroute == True:
        n "Но ты же только что изо всех сил пытался нас остановить..."
    if dimensions_yroute == True:
        dy "Но ты же только что изо всех сил пытался нас остановить..."
    if dimensions_mroute == True:
        em "Но ты же только что изо всех сил пытался нас остановить..."
    show exalted 1q
    emc "Эм… Так говорят..."
    show exalted 1v
    n "Мы можем уже просто подраться и закончить с этим?"
    dy "Да, эта игра в кошки-мышки исчерпала себя ещё сотни лет назад."
    show exalted 1s
    emc "Ну ладно."
    if dimensions_sroute == True:
        s "Расслабьтесь, ребята, он мой."
        show exalted 2k
        emc "Ой, да ладно! Начинается веселье."
        "Сайори бросается за ним на полной скорости и{nw}"
    if dimensions_nroute == True:
        n " Расслабьтесь, ребята, он мой."
        show exalted 2k
        emc "Ой, да ладно! Начинается веселье."
        "Нацуки бросается за ним на полной скорости и{nw}"
    if dimensions_yroute == True:
        dy "Расслабьтесь, ребята, он мой."
        show exalted 2k
        emc "Ой, да ладно! Начинается веселье."
        "Юлия бросается за ним на полной скорости и{nw}"
    if dimensions_mroute == True:
        em " Расслабьтесь, ребята, он мой."
        show exalted 2k
        emc "Ой, да ладно! Начинается веселье."
        "Моника бросается за ним на полной скорости и{nw}"

    scene bg blackbackground
    stop music
    play sound tinitus
    if dimensions_aroute == True:
        "..."
        a "Значит, мы приближаемся к старой концовке."
        a "Я сделала титульный лист, чтобы мы смогли попасть на новый контент."
        amc "Аки, откуда вообще взяться этому новому контенту?"
        a "От меня, балда. Я практиковалась в мододельстве."
        a "И я даже смогла сыграть на пианино!"
        a "Знаю, я не так хороша в мододельстве, как Чифф и его Измерения 5, но это сделано с любовью."
        a "Оно довольно короткое, но оно того стоит!"
        if dimensions_mroute == True:
            amc "С любовью?"
            a "О-о… ты знаешь, что я имела в виду!"
            a "Эй, и, ну... я опять запамятовала."
            a "Призналась ли доктор Баг в любви к тебе в Измерениях 5?"
            menu:
                "Да." if True:
                    $ love_original = True
                    a "О-о-о, как это мило. Если бы я только это помнила."
                "Нет." if True:
                    $ love_original = False
                    a "О-о-о, какая жалость. Это было бы лучшим моментом в руте для всех фанатов всех Моник, хе-хе."
    elif True:
        "А-а-а-а… вот дерьмо…"
        if dimensions_sroute == True:
            "Сайори толкнула меня плечом, и я отправился в полёт к главному пульту."
        if dimensions_nroute == True:
            "Нацуки толкнула меня плечом, и я отправился в полёт к главному пульту."
        if dimensions_yroute == True:
            "Юлия толкнула меня плечом, и я отправился в полёт к главному пульту."
        if dimensions_mroute == True:
            "Моника толкнула меня плечом, и я отправился в полёт к главному пульту."
        "Я чувствую, как что-то влажное стекает по моей руке."
        "Это… это кровь."
        "Я чувствую себя очень ослабленным."
        "Я слышу голоса, бледные, но явно напуганные."
        "О боже, Возвышенный, я не могу позволить ему навредить им..."
        "Но я не могу двигаться..."
        "Чем больше времени проходит, тем сложнее это всё осознавать."
        menu:
            "Держись, [player]." if True:
                "Я пытаюсь..."
        "Долгие минуты проходят, пока я попеременно прихожу в сознание и отключаюсь."
        if lowplayer == "думгай" or lowplayer == "палачрока" or lowplayer == "doomguy" or lowplayer == "doomslayer":
            "Постепенно мною начинает овладевать горяченный бред."

            stop music fadeout 2.0
            scene bg blackbackground
            with dissolve_scene_full

            "Я чувствую необходимость…"
            "Нужду рвать..."
            "...и метать!"

            scene bg hell
            play music dgmus

            mc "Где он?"
            play sound d03cocking
            show dg_reload
            mc "Где этот чёртов демон?!"
            "Я чувствую чьё-то присутствие."
            "Отвратительный зверь наконец-то предстал передо мной."

            scene bg hellcow with dissolve
            show dg_aim

            mc "Мистер Коровка."
            mc "Наконец-то мы встретились."
            mc "Приготовься встретить своего {i}\"Переведено и редактировано во избежание нарушения авторских прав\"{/i}!"
            hide dg_reload
            play sound d04thirdshot
            show dg_shoot
            "..."

            scene bg hell with dissolve
            show dg_aim

            mc "Именно, демоническое отродье!"
            "Что-то ещё двигается."

            scene bg hellcow with dissolve
            show dg_aim

            mc "Ещё больше вас!"
            mc "Ладно!"
            mc "Посмотрим, как вам понравится это!"
            hide dg_aim
            play sound d04thirdshot
            show dg_shoot
            "..."
            mc "Чёрт, эта штука тяжёлая!"
            hide dg_shoot
            play sound d03cocking
            show dg_reload
            mc "Нужно перезарядиться!"
            mc "Ладно, попробуем ещё раз, не так ли?"

            $ consolehistory = []
            call updateconsole ("-", "Наверное, это хорошая мысль...")
            call updateconsole ("-", "Подождать, если ты хочешь услышать...")
            call updateconsole ("-", "Всю музыку.")
            $ pause(2)
            call hideconsole

            mc "УМРИ, ДЕМОНЮГА!"
            hide dg_reload
            play sound d04thirdshot
            show dg_shoot
            "..."

            scene bg hell with dissolve
            show dg_aim
            mc "Ха-ха, верно, вы, придурки, и рядом не стоите с моими бочками, полными любви."
            mc "Вы пожалеете о том дне, когда решили связаться с единственным и неповторимым Палачом Человеком Мужиком Рока!"


            stop music fadeout 2.0
            scene bg blackbackground
            with dissolve_scene_full

            "Горячка рассеивается."
            "Это было очень странно..."

        "Что я пропустил? Все ли в порядке?"
        "Я нахожу в себе силы открыть глаза."

    play music rubble



    if dimensions_sroute == True:
        show bg ch08s1
        with dissolve
        mc "С..."
        s "[s_player]! Нет, нет, нет, нет."
        mc "Не… могу…"
        mc "Думаю… хватит…"
        "Возвышенный скован в дальнем конце комнаты."
        "Моника надёжно связала его."
        s "Нет, ты не можешь умереть просто так, [s_player], ты обещал."
        s "Ты будешь со мной навсегда, ты помнишь?"
        if dimensions_t1 == True:
            mc "Не… могу…"
            show bg ch08s2
            s "Это нечестно. Ты остаёшься, ты слышишь?"
            s "Ты будешь жить. Ты будешь жить. Ты будешь жи{nw}"
        if dimensions_t2 == True:
            mc "Люблю… тебя..."
            show bg ch08s2
            s "Даже не смей, [s_player], ты остаёшься, ты слышишь?"
            s " Ты будешь жить. Ты будешь жить. Ты будешь жи{nw}"
        if dimensions_t3 == True:
            mc "Люблю… тебя..."
            show bg ch08s2
            s "Даже не смей, [s_player], ты остаёшься, ты слышишь?"
            s " Ты будешь жить. Ты будешь жить. Ты будешь жи{nw}"
        mc "Сайори."
        "Я беру её за руку из последних сил."
        mc "Нам же… было… весело?"
        s "С недавних пор – нет! Дерьмо бросалось всеми из каждого вентилятора."
        s "Боже, я не готова к этому, никогда не буду."
        mc "Ты сильная."
        "Я показываю на остальных собравшихся рядом."
        mc "И… у тебя есть команда."
        show bg ch08s4
        s "Знаю, но я нуждаюсь в тебе. И всегда нуждалась в тебе"
        show bg ch08s3
        "Выражение лица Сайори резко меняется с грустного на решительное."
        "До боли знакомое чувство, то же самое я чувствовал к Парадайз Сайори."
        mc "Даже… не думай."
        s "Я могу спасти тебя снова."
        mc "Никаких… изменений. Ты же говорила."
        show bg ch08s1
        s "Но я должна!"
        mc "На этот раз… я спасу тебя."
        mc "Возвышенный… должен быть… остановлен."
        show bg ch08s3
        "Она на пару секунд остановилась в задумчивости."
        s "Как… я не знаю, куда идти отсюда."
        menu:
            "Помни меня." if True:
                mc "Воспоминания… будут жить вечно… пока ты о них помнишь."
                s "Я буду помнить тебя до тех пор, пока сама не умру, [s_player]."
                if dimensions_t1 == True:
                    mc "Ты лучший... друг, который…"
                if dimensions_t2 == True:
                    mc "Ты – любовь... Всей моей жизни..."
                if dimensions_t3 == True:
                    mc " Ты – любовь... Всей моей жизни..."
            "Забудь меня." if True:
                mc "Ты должна… позволить мне умереть."
                s "Нет. Я не могу. Я не буду. Ты заслуживаешь лучшего."
                mc "Поебать… на то, что я заслуживаю."
                if dimensions_t1 == True:
                    mc "Ты заслуживаешь лучшую... жизнь."
                if dimensions_t2 == True:
                    mc "Я хочу… чтобы ты продолжала жить... любовь моя..."
                if dimensions_t3 == True:
                    mc "Я хочу… чтобы ты продолжала жить... любовь моя..."

        stop music fadeout 7.0
        scene bg blackbackground
        with dissolve_scene_full
        "Мои последние мысли – о ней... а затем..."
        "..."
        "..."
        n "Мне жаль, Сайори, но он умер."
        dy "Мы больше ничего не сможем для него сделать."
        em "Ну… вообще-то…"
        em "Может, [player] и умер… Но лучшая его часть продолжает жить..."
        s "Игрок?... Нет, это явно не лучшая его часть..."
        em "Это всё, что я могу предложить. Что думаете?"
        s "Я… э-э… Ладно, делай, что хочешь."
        em "Ладно… Давай посмотрим…"
        em "Хм-м, дайте мне пару секунд."
        em "Вот и всё. Это должно сработать."
        em "Открой свои глаза."
        if dimensions_aroute == True:
            jump dim09f
            return
        menu:
            "Я исправлю прошлое." if True:
                show bg sreveal
                emc "Есть способ. Мне будет нужна твоя помощь, Сайори."
                show bg dimensions
                "..."
            "Я освобожу тебя." if True:
                show bg sreveal
                emc " Есть способ. Мне будет нужна твоя помощь, Юлия."
                show bg dimensions
                "..."
            "Я спасу погибших." if True:
                show bg sreveal
                emc " Есть способ. Мне будет нужна твоя помощь, Нац."
                show bg dimensions
                "..."
            "Я продолжу исследование." if True:
                show bg sreveal
                emc "Единственный путь – только вперёд. Прямо как и хотела доктор Баг."
                show bg dimensions
                "..."



    if dimensions_nroute == True:
        show bg ch08n2
        with dissolve
        mc "Н..."
        n "[player]! Чёрт возьми!"
        mc "Не… могу…"
        mc "Думаю… хватит…"
        "Возвышенный скован в дальнем конце комнаты."
        "Моника надёжно связала его."
        show bg ch08n1
        n "Нет, солдат, ты ни за что не умрёшь. Ну же, борись!"
        n "Чёрт возьми, я не понесу ответственность за то, что я тебя тоже убила! Оставайся со мной!"
        if dimensions_t1 == True:
            mc "Не… могу…"
            n "Нет, ты не можешь сдаться! Ну же, рядовой, борись, чёрт возьми!"
            n "Ты будешь жить. Ты будешь жить. Ты будешь жи{nw}"
        if dimensions_t2 == True:
            mc "Не… могу…"
            n "Нет, ты не можешь сдаться! Ну же, [player], борись, чёрт возьми!"
            n "Ты будешь жить. Ты будешь жить. Ты будешь жи{nw}"
        if dimensions_t3 == True:
            mc "Люблю… тебя…"
            n "Даже и не думай, [player], ты не можешь просто сдаться! Борись, чёрт возьми!"
            mc "Не… могу…"
            n "Нет, ты не можешь сдаться! Ну же, рядовой, борись, чёрт возьми!"
            n "Ты будешь жить. Ты будешь жить. Ты будешь жи{nw}"
        mc "Нац."
        "Я беру её за руку из последних сил."
        mc "Ты спасла меня... А остальное... неважно…."
        n "Что я вообще буду делать без тебя? Может, поговорить с отцом?"
        n "Боже, я не должна была это спрашивать у тебя, это уж слишком."
        mc "Ты сильная."
        "Я показываю на остальных собравшихся рядом."
        mc "И… у тебя есть команда."
        n "Знаю, но я нуждаюсь в тебе. Ты же мой герой."
        show bg ch08n2
        "Выражение лица Нацуки резко меняется с грустного на решительное."
        mc "Что… ты затеяла?.."
        n "Наша миссия – помогать людям, ведь так?"
        mc "Иди спаси кого-то ещё… не меня… ладно?"
        n "Или ты просто можешь остаться, [player], ты делаешь меня лучше."
        mc "У тебя… всё получится, Нац… просто… не прячься."
        mc "Выбрось… маску."
        " Она на пару секунд остановилась в задумчивости."
        n "Ладно. Я вообще могу тебе как-то помочь? Тебе удобно?"
        menu:
            "Бороться." if True:
                mc "Нахрен удобства… Я сражаюсь до конца."
                n "Тогда я тоже сражаюсь. Ну же, [player], просто дыши!"
                if dimensions_t1 == True:
                    mc "Было… честью…"
                if dimensions_t2 == True:
                    mc "Не могу просить...лучшего…"
                if dimensions_t3 == True:
                    mc "Я люблю тебя… очень сильно… я бы пободался с игроком..."
            "Отдохнуть." if True:
                mc "Просто… Поговори со мной."
                mc "Твой голос… такой мягкий."
                n "Ладно. Тс-с-с-с… Всё в порядке… Я здесь."
                if dimensions_t1 == True:
                    mc "Спасибо… сержантик..."
                if dimensions_t2 == True:
                    mc "Спасибо… Нацуки..."
                if dimensions_t3 == True:
                    mc "Спасибо… Нац..."

        stop music fadeout 7.0
        scene bg blackbackground
        with dissolve_scene_full
        "Мои последние мысли – о ней… а затем…"
        "..."
        "..."
        s "Мне жаль, Нацуки, но он умер."
        dy "Мы больше ничего не сможем для него сделать."
        em "Ну… вообще-то…"
        em "Может, [player] и умер… Но лучшая его часть продолжает жить..."
        n "Игрок?... Нет, это явно не лучшая его часть..."
        em "Это всё, что я могу предложить. Что думаете?"
        n "Я… э-э… Ладно, делай, что хочешь."
        em "Ладно… Давай посмотрим…"
        em "Хм-м, дайте мне пару секунд."
        em "Вот и всё. Это должно сработать."
        em "Открой свои глаза."
        if dimensions_aroute == True:
            jump dim09f
            return
        menu:
            "Я исправлю прошлое." if True:
                show bg nreveal
                emc "Есть способ. Мне будет нужна твоя помощь, Сайори."
                show bg dimensions
                "..."
            "Я освобожу тебя." if True:
                show bg nreveal
                emc " Есть способ. Мне будет нужна твоя помощь, Юлия."
                show bg dimensions
                "..."
            "Я спасу погибших." if True:
                show bg nreveal
                emc " Есть способ. Мне будет нужна твоя помощь, Нац."
                show bg dimensions
                "..."
            "Я продолжу исследование." if True:
                show bg nreveal
                emc "Единственный путь – только вперёд. Прямо как и хотела доктор Баг."
                show bg dimensions
                "..."



    if dimensions_yroute == True:
        show bg ch08y1
        with dissolve
        mc "Ю..."
        dy "[player]! Мне так жаль."
        mc "Не… могу…"
        mc "Думаю… хватит…"
        "Возвышенный скован в дальнем конце комнаты."
        "Моника надёжно связала его."
        show bg ch08y2
        dy "Нет, ты не можешь умереть, [player], мы выберемся отсюда."
        show bg ch08y3
        dy "Мы обязательно увидим солнце, помнишь?"
        if dimensions_t1 == True:
            mc "Не… могу…"
            dy "Мне неведомо понятие смерти. Она же не неизбежна?"
            dy "Ты будешь жить. Ты будешь жить. Ты будешь жи{nw}"
        if dimensions_t2 == True:
            mc "Люблю… тебя…"
            dy "Мне неведомо понятие смерти. Она же не неизбежна?"
            dy "Ты будешь жить. Ты будешь жить. Ты будешь жи{nw}"
        if dimensions_t3 == True:
            mc "Люблю… тебя…"
            dy "Мне неведомо понятие смерти. Она же не неизбежна?"
            dy "Ты будешь жить. Ты будешь жить. Ты будешь жи{nw}"
        mc "Юлия."
        show bg ch08y4
        "Я беру её за руку из последних сил."
        mc "Продолжай путь… выберись… ради меня…"
        dy "Но это был наш план. Наше совместное путешествие. Я не хочу идти одной."
        dy "Я даже не знаю, смогу ли я. Ты всё время выполнял все задачи."
        mc "Ты сильная."
        "Я показываю на остальных собравшихся рядом."
        mc "И… у тебя есть команда. Это и твоя команда тоже."
        dy "Знаю, но именно тебе я обещала. Ты – моя искра."
        show bg ch08y3
        "Юлия закрывает глаза со взглядом, полным уверенности."
        mc "Что… ты затеяла?"
        show bg ch08y4
        dy "Профессор. Неужели это именно то, что ты чувствовал, когда потерял её?"
        mc "Наверное..."
        dy "Тогда прости, что заставила пройти через это испытание и тебя."
        mc "Ты меня тоже… прости."
        mc "У тебя должно быть всё… хорошо, Юлия."
        "Она на пару секунд остановилась в задумчивости."
        dy "Куда бы ты не пошёл, найди её. Твои чувства будут потрачены впустую на этом ржавом ведре."
        if dimensions_t1 == True:
            menu:
                "Спасибо." if True:
                    mc "Я… ценю это..."
                    dy "Удачи тебе, куда бы ты не отправился."
                    mc "Тебе… тоже… друг"
                "Ты и есть то ржавое ведро, которому я обещал." if True:
                    mc "Ты и есть… ржавое ведро… которому я… ох…"
                    dy "О, мистер [player], не заставляй меня, это тяжело."
                    mc "Я знаю… но спасибо тебе… друг мой…"
        if dimensions_t2 == True:
            menu:
                "Спасибо." if True:
                    mc "Я… ценю это..."
                    dy "Удачи тебе, куда бы ты не отправился."
                    mc "Тебе… тоже… мой ангел…"
                "Ты и есть то ржавое ведро, в которое я влюбился." if True:
                    mc "Ты и есть… ржавое ведро… в которое я… ох…"
                    dy "О, мистер [player], не заставляй меня, это тяжело."
                    mc "Я знаю… но спасибо тебе… Юлия…"
        if dimensions_t3 == True:
            menu:
                "Спасибо." if True:
                    mc "Я… ценю это..."
                    dy "Удачи тебе, куда бы ты не отправился."
                    mc "Тебе… тоже… мой механический ангел…"
                "Ты и есть то ржавое ведро, в которое я влюбился." if True:
                    mc "Ты и есть… ржавое ведро… в которое я… ох…"
                    dy "О, мистер [player], не заставляй меня, это тяжело."
                    mc "Я знаю… но спасибо тебе… Юлия…"


        stop music fadeout 7.0
        scene bg blackbackground
        with dissolve_scene_full
        "Мои последние мысли – о ней… а затем…"
        "..."
        "..."
        n "Мне жаль, Юлия, но он умер."
        s "Мы больше ничего не сможем для него сделать."
        em "Ну… вообще-то…"
        em "Может, [player] и умер… Но лучшая его часть продолжает жить..."
        dy "Игрок?... Нет, это явно не лучшая его часть..."
        em "Это всё, что я могу предложить. Что думаете?"
        dy "Я… э-э… Ладно, делай, что хочешь."
        em "Ладно… Давай посмотрим…"
        em "Хм-м, дайте мне пару секунд."
        em "Вот и всё. Это должно сработать."
        em "Открой свои глаза."
        if dimensions_aroute == True:
            jump dim09f
            return
        menu:
            "Я исправлю прошлое." if True:
                show bg yreveal
                emc "Есть способ. Мне будет нужна твоя помощь, Сайори."
                show bg dimensions
                "..."
            "Я освобожу тебя." if True:
                show bg yreveal
                emc " Есть способ. Мне будет нужна твоя помощь, Юлия."
                show bg dimensions
                "..."
            "Я спасу погибших." if True:
                show bg yreveal
                emc " Есть способ. Мне будет нужна твоя помощь, Нац."
                show bg dimensions
                "..."
            "Я продолжу исследование." if True:
                show bg yreveal
                emc "Единственный путь – только вперёд. Прямо как и хотела доктор Баг."
                show bg dimensions
                "..."



    if dimensions_mroute == True:
        show bg ch08m1
        with dissolve
        mc "M..."
        em "[pm_player]! О, нет..."
        mc "Не… могу... двигаться..."
        mc "Думаю… хватит…"
        "Возвышенный скован в дальнем конце комнаты."
        "Сайори надёжно связала его."
        em "Может, я и влюблена в игрока, но знаешь, ты мне тоже нравишься."
        em "Так что я не хочу терять и тебя тоже. Пожалуйста, будь в порядке."
        mc "Не... могу..."
        show bg ch08m2
        em "Это нечестно. Ты остаёшься, слышишь?"
        show bg ch08m3
        em "Ты будешь жить. Ты будешь жить. Ты будешь жи{nw}"
        mc "Моника."
        show bg ch08m4
        "Я беру её за руку из последних сил."
        mc "Добро… пожаловать… в ПНМ."
        mc "Это твой… шанс измениться."
        em "O, [pm_player], я изменюсь, я клянусь."
        em "Но я не знаю, примут ли меня другие..."
        mc "Ты не такая… чтобы… просто сдаться."
        "Я показываю на остальных собравшихся рядом."
        mc "Они… узнают тебя… в конце концов."
        em "Знаю, но я нуждаюсь в тебе. И всегда нуждалась."
        em "В обоих из них."
        show bg ch08m3
        "Выражение лица Моники резко меняется с грустного на решительное."
        "До боли знакомое чувство, то же самое я чувствовал к Парадайз Сайори."
        mc "Даже… не думай об этом."
        em "Я бы могла возродить тебя в моей вселенной."
        mc "Нет… это говорит… старая Моника."
        show bg ch08m4
        em "Но я должна! Я же люблю тебя."
        mc "Я спасу тебя… в этот раз."
        mc "Доверься мне…"
        "Она на пару секунд остановилась в задумчивости."
        em "Почему ты помог мне, [player]? Я этого не заслужила."
        menu:
            "В тебе есть ещё хорошее." if True:
                $ dimensions_t1 = True
                $ dimensions_t2 = False
                mc "Всё ещё… время, чтобы… сделать хорошее..."
                em "Я это сделаю, я клянусь. Ради тебя. Всё ради тебя."
                mc "Ты уже… на пути…"
                mc "Ты становишься… доктором Баг..."
            "Я люблю тебя." if True:
                $ dimensions_t1 = False
                $ dimensions_t2 = True
                mc "Я… люблю тебя…"
                em "Ты… любишь меня? Но это безумие."
                em "Ты любил Её? А я Её убила…"
                mc "Ты… И ЕСТЬ… Доктор"

        stop music fadeout 7.0
        scene bg blackbackground
        with dissolve_scene_full
        "Мои последние мысли – о ней… а затем…"
        "..."
        "..."
        n "Мне жаль, Моника, но он умер."
        dy "Мы больше ничего не сможем для него сделать."
        em "Ну… вообще-то…"
        em "Может, [player] и умер… Но лучшая его часть продолжает жить..."
        s "Игрок?... Нет, это явно не лучшая его часть..."
        em "Это всё, что я могу предложить. Что думаете?"
        s "Я… э-э… Ладно, делай, что хочешь."
        em "Ладно… Давай посмотрим…"
        em "Хм-м, дайте мне пару секунд."
        em "Вот и всё. Это должно сработать."
        em "Открой свои глаза."
        if dimensions_aroute == True:
            jump dim09f
            return
        menu:
            "Я исправлю прошлое." if True:
                show bg mreveal
                emc "Есть способ. Мне будет нужна твоя помощь, Сайори."
                show bg dimensions
                "..."
            "Я освобожу тебя." if True:
                show bg mreveal
                emc " Есть способ. Мне будет нужна твоя помощь, Юлия."
                show bg dimensions
                "..."
            "Я спасу погибших." if True:
                show bg mreveal
                emc " Есть способ. Мне будет нужна твоя помощь, Нац."
                show bg dimensions
                "..."
            "Я продолжу исследование." if True:
                show bg mreveal
                emc "Единственный путь – только вперёд. Прямо как и хотела доктор Баг."
                show bg dimensions
                "..."


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
