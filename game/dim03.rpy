label dim03:
    stop music fadeout 2.0
    scene bg blackbackground
    with dissolve_scene_full
    $ m_name = "Д-р Баг"
    $ s_name = "С. Найт"
    $ n_name = "С-т Нацуки"
    $ y_name = "Проф. Юри"
    $ pm_name = "Моника Прайм"
    $ ps_name = "Сайори Прайм"
    $ py_name = "Юри Прайм"
    $ pn_name = "Нацуки Прайм"
    $ pmc_name = "[player] Прайм"
    $ bm_name = "Граф Моникула"
    $ by_name = "Йерри"
    $ bn_name = "Орда Бафсуки"














    y "Ну же, [player], вставай."
    mc "Ух... я в порядке."

    scene bg ruined
    with dissolve_scene_full

    play music kansas
    show yuri 1g zorder 2 at t11
    "Когда ко мне вернулось зрение, я понял, что мы находимся в знакомой комнате."
    mc "А где остальные?"
    show yuri 1h
    y "Здесь только мы вдвоём. Скорее всего, генератор был неисправен."
    show yuri 1g
    mc "Прежде чем беспокоиться о чём-либо, нужно сначала понять, где мы вообще находимся."
    show yuri 1h
    y "Конечно."
    show yuri 1e
    "Юри выглянула в окно."
    show yuri 1f
    y "Эм-м... [player]..."
    show yuri 1g
    mc "Что такое?"
    show yuri 1f
    y "Ты... должен это увидеть."
    stop music fadeout 2.0
    "Я выглянул в окно..."

    scene bg pripyatwindow
    with wipeleft_scene
    play music ash

    "..."
    mc "Вау."
    y "Это Припять. Почему мы именно в Припяти?!"
    mc "Разве это не заброшенное радиоактивное место?"
    y "В нашей реальности это так. Не уверена, что здесь произошло, но здесь всё выглядит хуже..."
    y "Мы должны изучить местность. Это место может быть сокровищницей научных находок."
    y "Ох... когда мы встретим остальных, конечно."
    ps "Э-э-э... Привет?"

    scene bg ruined
    with wipeleft_scene

    show sayori_prime 1b zorder 2 at t21
    show yuri 2b zorder 2 at t22
    "Юри с изумлением смотрит на Сайори из Литературного клуба."
    y "Невероятно! Это мисс Найт, только... другая."
    y "Какой твой любимый цвет?"
    show sayori_prime 3h
    ps "Кто вы?! И где мы находимся?!"
    show sayori_prime 4p
    ps "ЧТО ЗДЕСЬ ПРОИСХОДИТ?!"
    show yuri 1a
    "Конечно, было здорово наблюдать, как Юри самовыражается, но я показал ей жестом отступить."
    mc "Мы до конца не уверены, где находимся."
    show sayori_prime 4m
    ps "Что ты с ним сделал?!"
    show yuri 1l
    y "Сайори, мы... все... из другого измерения."
    show yuri 1g
    mc "Мы знаем об этом месте не больше, чем ты."
    mc "Мы только что сюда прибыли."
    show sayori_prime 3p
    ps "Где он?!"
    show sayori_prime 1w
    "Сайори из другого измерения расплакалась."
    show yuri 2u
    y "Иди сюда."
    show sayori_prime 1v at t42
    show yuri 1s at t43
    "Неожиданно Юри заключила Сайори в свои объятья."
    show sayori_prime at thide
    hide sayori_prime
    show yuri at thide
    hide yuri
    show natsuki 1g3 zorder 2 at t11
    n "Юри, вот ты где."
    "Нацуки вошла, а за нею и мой двойник."
    show natsuki 1e1
    n "Могу я присоединиться?"
    show natsuki 1e1 zorder 2 at t42
    show yuri 1s zorder 2 at t43
    "Действительно, её тоже обняли."
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show mc2 1c zorder 2 at t11
    pmc "Сайори!"
    show mc2 1c zorder 2 at t21
    show sayori_prime 4r zorder 2 at t22
    ps "Ты в порядке!"
    show mc2 1a zorder 2 at t42
    show sayori_prime 1q zorder 2 at t43
    "Он обнял её. Можно и я с кем-нибудь обнимусь?"
    show mc2 2d
    "Другой [player] посмотрел мне в глаза, возможно, думая о том же."
    "Ладно, это довольно странно."
    show mc2 at thide
    hide mc2
    show sayori_prime at thide
    hide sayori_prime
    show natsuki 1g3 zorder 2 at t21
    show yuri 1f zorder 2 at t22
    n "Устройство в порядке?"
    y "Оно работает исправно, но оно не отправляет нас домой."
    n "Также исправно."
    show yuri 1h
    y "Похоже, что погрешность составляет 100 вселенных."
    y "Так что мы можем пробовать до тех пор, пока не получится."
    show natsuki 1h6
    n "И это значит, что попасть во вселенную с этими монстрами из слизи возрастает... Отлично..."
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show mc2 3d zorder 2 at t21
    show sayori_prime 1k zorder 2 at t22
    "Другой [player], кажется, объясняет что-то Сайори."
    "Это должно помочь."
    show mc2 at thide
    hide mc2
    show sayori_prime at thide
    hide sayori_prime
    show natsuki 1e7 zorder 2 at t21
    show yuri 2c zorder 2 at t22
    y "С другой стороны, у нас будет большое количество образцов для анализа."
    show natsuki 1g5
    n "Профессор, тебе, возможно, покажется это хорошей идеей, но у меня нет патронов на 100 прыжков."
    show yuri 1a
    y "Хмм, хорошая мысль. Доктор Баг может помочь уменьшить круг поиска."
    show natsuki 1g11
    n "Тогда давайте отыщем её."
    show natsuki 1h24
    n "Снова."
    show yuri 1f
    y "Готовы отправиться в путь?"
    show mc2 3g zorder 2 at t41
    show sayori_prime 3l zorder 2 at t42
    show natsuki 1e7 zorder 2 at t43
    show yuri 1i zorder 2 at t44
    "Все закивали."

    scene bg pripyat
    with dissolve_scene_full

    show natsuki 1h3 zorder 2 at t21
    show yuri 1e zorder 2 at t22
    n "Ну, их здесь нет. Давайте обойдём территорию."
    show natsuki 1h7
    show yuri 1f
    y "Или мы можем разделиться?"
    show yuri 1g
    show natsuki 1g24
    n "Ой, да ладно, ты же знаешь, что именно в такие моменты появляются монстры из слизи."
    show yuri 1c
    y "Ты видела признаки присутствия монстров?"
    show yuri 1b
    y "Самое странное, что ты видела до сих пор - это себя с розовыми волосами."
    show natsuki 1g14
    show yuri 1a
    n "{i}До сих пор...{/i}"
    show mc2 2d zorder 2 at t31
    show natsuki 1g1 zorder 2 at t32
    show yuri 1a zorder 2 at t33
    pmc "Прошу прощения, сержант."
    show natsuki 1h25
    n "Привет, красавчик."
    "Воу, он довольно быстро покорил её сердце."
    "Очаровательный засранец."
    show mc2 4f
    pmc "Я н-не знаю правил для таких... вещей."
    pmc "Он опасен? Если... я рядом?"
    "Он обо мне сейчас?"
    show natsuki 1h3
    n "Ты не того спрашиваешь. Юри?"
    show natsuki 1h1
    show yuri 1k
    y "Все копии, которых я видела за время путешествий по измерениям, не имели проблем при встрече с их двойниками."
    show yuri 1n
    show natsuki 1h26
    mc "Ты сказала мне, что основываешь эту идею на научной фантастике..."
    show natsuki 1h1
    show yuri 1t
    y "Хмф... Я надеялась, что ты забыл об этом."
    show yuri 1u
    show natsuki 1e25
    show mc2 2q
    n "Только не лезьте целоваться, мы будем в порядке."
    show mc2 2y
    pmc "Спасибо... наверное..."
    show mc2 at thide
    hide mc2
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show sayori_prime 5d zorder 2 at t11
    ps "Эй, [player]. Извини, что сорвалась."
    show sayori_prime 5c
    ps "Ситуация была очень запутана, но это не оправдывает меня."
    mc "Не волнуйся об этом."
    mc "На твоём месте я бы тоже разозлился."
    show sayori_prime 5b
    ps "Хе-хе. Ты будешь удивлён, но я пропустила кексы!"
    show sayori_prime 5a zorder 2 at t21
    show mc2 5s zorder 2 at t22
    pmc "Я не..."
    show sayori_prime at thide
    hide sayori_prime
    show mc2 at thide
    hide mc2
    show natsuki 2d2 zorder 2 at t11
    n "Тихо, поблизости наблюдаются признаки жизни."
    show natsuki 2d5
    n "Смотрите в оба."

    stop music fadeout 2.0
    scene bg pripyatlobby
    with dissolve_scene_full
    play music lobby fadein 0.5

    n "Есть кто дома?"
    show monika 1a zorder 2 at t11
    m "А-ха! Привет ещё раз."
    show monika 1j
    m "Угадайте кого я нашла!"
    show monika 1a zorder 2 at t21
    show monika_prime 2i zorder 2 at t22
    pm "Отвали от меня!"
    show monika 3a
    m "На этот раз ты проиграла, М."
    show monika_prime 2r
    pm "Гра-ах!"
    pm "Я не поняла, ты должна сейчас плавиться."
    show monika at thide
    hide monika
    show monika_prime at thide
    hide monika_prime
    show sayori_prime 4w zorder 2 at t11
    ps "Что ты делаешь?"
    ps "Отпусти её!"
    show sayori_prime 1j zorder 2 at t21
    show natsuki 1h24 zorder 2 at t22
    n "Это из-за неё мы в таком положении!"
    show natsuki 1h6
    n "Эта сучка связала доктора Баг и заперла её в шкафу."
    show sayori_prime 1v
    "Сайори отшатнулась от этих слов."
    show sayori_prime 1u
    ps "Просто... не делай ей больно."
    ps "Она - мой друг."
    show sayori_prime at thide
    hide sayori_prime
    show natsuki at thide
    hide natsuki
    show monika 1a zorder 2 at t21
    show monika_prime 2i zorder 2 at t22
    m "Не собиралась, и я думаю, тебе понравится, что она скажет, Сайори."
    pm "Хмф."
    show monika 1h
    m "Давай, скажи это."
    show monika_prime 5b
    pm "Аргх, ладно."
    show monika_prime 2q
    pm "Я использовала вас, чтобы [player] был только со мной. Клуб - это ловушка."
    show monika at thide
    hide monika
    show monika_prime at thide
    hide monika_prime
    show sayori_prime 2o zorder 2 at t11
    ps "Ч-что ты имеешь в виду? Ловушка? Но почему?"
    show sayori_prime at thide
    hide sayori_prime
    show monika 1h zorder 2 at t21
    show monika_prime 1r zorder 2 at t22
    pm "Я хотела влюбить его в меня."
    show monika_prime 1p
    pm "Я знала, что он выберет меня. Он был другим."
    show monika at thide
    hide monika
    show monika_prime at thide
    hide monika_prime
    show sayori_prime 2v zorder 2 at t21
    show mc2 2j zorder 2 at t22
    pmc "Что? Ты? Но это бессмысленно, я не твоего уровня."
    pmc "И даже тогда ты практически не разговаривала со мной..."
    show sayori_prime at thide
    hide sayori_prime
    show mc2 at thide
    hide mc2
    show monika 1h zorder 2 at t21
    show monika_prime 1o zorder 2 at t22
    pm "Хотя на этот раз я не испытываю к тебе такого чувства."
    show monika_prime 1m
    pm "Сейчас меня больше интересует твой двойник."
    "Я сглатываю."
    show monika_prime 5a
    pm "Смотри. Это сложно?"
    show monika at thide
    hide monika
    show monika_prime at thide
    hide monika_prime
    show natsuki 1h23 zorder 2 at t21
    show yuri 1e zorder 2 at t22
    n "Это не трудно!"
    show natsuki 1h7
    show yuri 2f
    y "Это не объясняет того, что первой мыслью при виде доктора Баг было похитить её."
    show yuri 2h
    y "Это выглядит будто... ты уже знала о мультивселенной раньше..."
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show monika 1h zorder 2 at t21
    show monika_prime 5a zorder 2 at t22
    pm "Разве ваш [player] не рассказал вам?"
    show monika_prime 1n
    pm "Ах, конечно нет."
    show monika_prime 4k
    pm "Я стёрла его память."
    show monika_prime 1k
    mc "Что? Как?"
    show monika_prime 1a
    show monika 2g
    m "Она говорила о том, что не может изменить код, когда я её поймала."
    show monika at thide
    hide monika
    show monika_prime at thide
    hide monika_prime
    show sayori_prime 2o zorder 2 at t11
    ps "Ты что, волшебник?"
    show sayori_prime at thide
    hide sayori_prime
    show monika 1d zorder 2 at t21
    show monika_prime 5a zorder 2 at t22
    pm "Ха-ха нет, моя дорогая, когда мы вернулись домой, это измерение уже было нереальным."
    pm "Мы были персонажами визуальной новеллы под названием \"Литературный клуб Тук-Тук\"."
    show monika at thide
    hide monika
    show monika_prime at thide
    hide monika_prime
    show mc2 5w zorder 2 at t11
    pmc "Нереальным? Да ну..."
    pmc "С меня хватит этого грёбанного кошмара."
    show mc2 1s
    pmc "Через несколько секунд я проснусь... 3... 2..."
    show mc2 at thide
    hide mc2
    show monika 1f zorder 2 at t21
    show monika_prime 5a zorder 2 at t22
    pm "Это один из симуляторов свиданий, представленных в моде."
    show monika_prime 4l
    pm "Или было таким… до того, как я изменила его."
    show monika 2n
    m "Признайся, это объясняет такую привязанность девочек к тебе..."
    show monika at thide
    hide monika
    show monika_prime at thide
    hide monika_prime
    show natsuki 1f3 zorder 2 at t11
    n "Так, это место реальное? Наш дом?"
    show natsuki at thide
    hide natsuki
    show monika 1c zorder 2 at t21
    show monika_prime 3n zorder 2 at t22
    pm "Очевидно, что я не могу пробраться в код, иначе я бы давно стёрла эту менее привлекательную Монику."
    show monika_prime 1m
    show monika 2h
    m "..."
    show monika_prime 1l
    pm "Что?"
    show monika 2i
    m "Продолжай."
    show monika 2h
    show monika_prime 1d
    pm "Я не думаю, что мы сейчас в игре."
    show monika_prime 1m
    pm "Извини, но я не знаю о вашем доме. Не была там."
    show monika_prime 1d
    mc "Подожди обвинять... Нацуки..."
    show monika at thide
    hide monika
    show monika_prime at thide
    hide monika_prime
    show natsuki 1f3 zorder 2 at t11
    mc "А разве мой двойник из визуальной новеллы не заигрывал с тобой раньше?"
    show natsuki 1h6
    n "Прошу прощения?"
    show natsuki 1h7 zorder 2 at t21
    show mc2 1d zorder 2 at t22
    pmc "Ох, я, кажется, понимаю, о чём он."
    pmc "Ты строила мне глазки, как только я появился."
    show mc2 1g
    pmc "Как и моя Нацуки мне."
    show mc2 1b
    show natsuki 1f15
    n "Ну, какую бы порчу ты на меня не навела, я не планировала кусаться..."
    show natsuki 1f7 zorder 2 at t31
    show mc2 1d zorder 2 at t32
    show yuri 1h zorder 2 at t33
    y "Это увеличивает шанс того, что мы всё ещё в игре."
    show yuri 1n
    show natsuki 1e24
    n "Господи! Неужели это так важно?!"
    show yuri 1f
    show natsuki 1e23
    n "Сейчас мы потеряли одного члена ПНМ и двух возможных попутчиков."
    show natsuki 1e6
    n "Мы находимся в неизвестной вселенной, не имея понятия, что здесь происходит."
    n "Мы не можем попасть домой."
    show natsuki 1h24
    n "А вы все рассуждаете о какой-то глупой философской абракадабре о том, существуем мы или нет..."
    show natsuki at thide
    hide natsuki
    show mc2 at thide
    hide mc2
    show yuri at thide
    hide yuri
    show monika 1f zorder 2 at t21
    show monika_prime 1i zorder 2 at t22
    m "Нац..."
    show monika at thide
    hide monika
    show monika_prime at thide
    hide monika_prime
    show natsuki 1h17 zorder 2 at t21
    show yuri 1e zorder 2 at t22
    n "Простите, босс, но я думаю, что наш главный приоритет - выполнение миссии."
    show natsuki 1e14
    show yuri 2f
    y "Как бы я сейчас не была удивлена этой ситуацией, она права."
    y "Нужно возвращаться домой."
    show yuri 1k
    show natsuki 1e13
    n "Именно, а остальное может подождать."
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri

    show monika 2i zorder 2 at t21
    show monika_prime 1c zorder 2 at t22
    m "Справедливо... в таком случае..."
    m "Моника, я до сих пор не могу понять, но..."
    show monika 1d
    m "Поскольку ты – это я, я уверена, что ты сдержишь своё слово."
    show monika 3a
    m "Как насчёт перемирия? До того момента, пока мы не выйдем из этой ситуации."
    show monika 1a
    show monika_prime 1d
    pm "Я думаю, в плане пленения мы квиты."
    show monika_prime 2a
    pm "Ладно, Баг. Я буду вести себя наилучшим образом."
    show monika at thide
    hide monika
    show monika_prime at thide
    hide monika_prime
    show sayori_prime 4f zorder 2 at t11
    ps "{i}Мы{/i} в том числе."
    show sayori_prime 2f zorder 2 at t21
    show mc2 3d zorder 2 at t22
    pmc "Сайори..."
    show sayori_prime 2d
    show mc2 3a
    ps "Но ты не сможешь помириться со своими друзьями."
    "Ей определённо место в Литературном клубе."
    show sayori_prime at thide
    hide sayori_prime
    show mc2 at thide
    hide mc2
    show monika 1a zorder 2 at t21
    show monika_prime 2h zorder 2 at t22
    m "Сейчас наша цель – пропавшие."
    show monika_prime 2r
    pm "Ага, Юри Прайм, Нацуки Прайм и... ваша Сайори, я полагаю?"
    show monika at thide
    hide monika
    show monika_prime 2h zorder 2 at t21
    show yuri 1r zorder 2 at t22
    y "Прайм? Вы думаете, ваша вселенная самая важная?"
    show monika_prime 2m
    y "Даже если мы теперь знаем, что это всего лишь игра?"
    show monika_prime 2n
    pm "Ну, нет, но там я была практически богом."
    show yuri at thide
    hide yuri
    show monika_prime 4b zorder 2 at t11
    pm "Знаешь, [pm_player], изначально в клубе было шесть девочек, но я удалила их."
    show monika_prime 3l
    pm "И если бы я забыла ключи, я могла бы просто пройти сквозь двери."
    show monika_prime 1j
    pm "Было здорово."
    show mc2 4d zorder 2 at t31
    show natsuki 1g25 zorder 2 at t32
    show monika_prime 1i zorder 2 at t33
    n "Эй, злая божественная леди, следуй за моим главным героем из видеоигры, вот тебе амулет или что там ещё, и помоги нам найти что-нибудь, где можно расположиться."
    show natsuki 1g10
    n "У Юри болит спина."
    show mc2 at thide
    hide mc2
    show natsuki at thide
    hide natsuki
    show monika_prime 1h zorder 2 at t21
    show sayori_prime 4q zorder 2 at t22
    ps "И если вы найдёте что-нибудь вкусное, помните, что вы должны мне."
    show monika_prime 2q
    pm "Ух..."
    show monika_prime at thide
    hide monika_prime
    show sayori_prime at thide
    hide sayori_prime
    show monika 1d zorder 2 at t11
    m "[player], можно тебя на минутку?"
    mc "Конечно."
    "Доктор Баг ждёт, пока все покинут комнату."
    show monika 1o
    "..."
    show monika 2f
    m "Я солгала, что доверяю ей."
    show monika 2g
    m "Я начала уставать, и мне нужно было что-то придумать, пока она не сбежала."
    mc "О, чёрт. Почему ты говоришь это мне, а не Юри?"
    show monika 2p
    m "Если [player] Прайм действительно может наложить порчу на других девочек, то нам конец, если он встанет на сторону другой Моники."
    show monika 1r
    m "Так что у меня нет выбора, кроме как довериться тебе."
    show monika 1f
    m "Возможно, вы не сильно преуспели в сохранении пространственно-временного континуума, но мы давно это прошли."
    m "Мне нужно, чтобы ты..."

    stop music fadeout 2.0

    show monika 1g
    "Грохоты снаружи прервали наш разговор."
    m "Хочу ли я знать причину звука?"
    "Нацуки вбегает обратно в фойе."
    show monika 1f zorder 2 at t21
    show natsuki 1e2 zorder 2 at t22
    n "Что бы это ни было, это не хорошо."
    show monika at thide
    hide monika
    show natsuki at thide
    hide natsuki
    "Грохот становился громче и перешёл в отчётливые удары."
    "Шаги?"
    "Не может быть..."
    "Но прежде чем нас достигает сущность, дверь распахивается и внутрь вбегают три человека."
    show yuri_prime 2p zorder 2 at t31
    show sayori 4m zorder 2 at t32
    show natsuki_prime 1p zorder 2 at t33
    play sound d03lobbyentrance
    play music brawl

    py "А-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а!!!"
    pn "Мы все умрём!"
    s "Бегите!"
    show yuri_prime at thide
    hide yuri_prime
    show sayori at thide
    hide sayori
    show natsuki_prime at thide
    hide natsuki_prime
    show natsuki 1e2 zorder 2 at t11
    n "Что это такое?!"
    show natsuki at thide
    hide natsuki
    show sayori 4m zorder 2 at t11
    s "Я СКАЗАЛА БЕГИТЕ!"
    show sayori at thide
    hide sayori
    "Не желая спорить с этим советом, я начинаю бежать в противоположном направлении."
    play sound d03fallover
    "...и тут же спотыкаюсь о какие-то обломки."
    show natsuki 1f6 zorder 2 at t11
    n "Шевелись, друг, ты слышал даму."
    "Нацуки отстала от остальных, чтобы прикрыть меня."
    mc "Чёрт побери, прости."
    show natsuki 1f5
    n "Не извиняйся, просто уноси ноги."

    scene bg pripyat
    with wipeleft_scene

    "Чувство страха нарастает, когда мы возвращаемся на разрушенные улицы Припяти."
    "Глухой стук был не только позади нас. Он раздался повсюду."
    show natsuki 2e2 zorder 2 at t11
    n "Держись за мной, [player]. Я бы не хотела тебя случайно застрелить."
    play sound d03cocking
    show natsuki 2e5
    n "Но не смотри на мою задницу, гад."
    "По крайней мере, остальные спаслись."
    mc "Возможно, лучше сэкономить две пули."
    show natsuki 2e6
    n "Блин, спасибо за доверие..."
    "Мрачные фигуры появились во мраке."
    mc "Привет?"
    show natsuki 2e4
    n "А-а-а-а, что это за хрень?"
    show natsuki at thide
    hide natsuki
    "Когда я получил ответ, я разрывался между криком и смехом."

    show bhorde 5a zorder 2 at t11
    bn "Гр-р-а-а-а-а! Блё-ё-ё-ё-ё! Гр-ра-аргх!"
    "Орда Бафсуки остановилась по периметру вокруг меня и сержанта."
    show natsuki 3a1 zorder 2 at t33
    show bhorde 5a zorder 2 at t31
    n "...нет."
    n "Только... не это."
    n "Я уже устала от этих вселенных и моих нелепых двойников!"
    "Оказывается, Нацуки Прайм ещё не {i}настолько{/i} странная..."
    show natsuki 3a2
    bn "Бла-ар-р-рг-гх???"
    mc "Хах, у них даже волосы розовые."
    show natsuki 3a5
    n "Чувак, серьёзно... что нам делать?"
    mc "Они выглядят растерянными. Может кинуть палку или ещё что-нибудь?"
    show natsuki 3a6
    n "...Ты пытаешься убить нас?"
    show natsuki 3a3
    n "Если бы кто-то бросил в меня палку, я бы выстрелила ему в лицо."
    "Напомните мне {i}никогда{/i} её не злить."
    mc "Ладно, ладно, тогда попробуй... представить себя на их месте?"
    show natsuki 3a1
    n "Да, это просто фантастический совет."
    show natsuki 3a5
    n "Мы окружены толпой моих двойников, которые хотят нас съесть, а ты хочешь, чтобы я представила себя на их месте."
    bn "Р-Р-Р-А-А-А-А-А!"
    mc "Они взволнованы. Сейчас или никогда."
    play sound d03firing
    show natsuki 3b2
    "Нацуки сделала предупредительный выстрел."
    show natsuki 3a2
    bn "Хур-р р-а-а-у-у-у-у-у ух-х...."
    "По крайней мере, мы выиграли время."
    "Итак, наш план..."

    menu:
        "Враждебность.":
            mc "Единственный выход отсюда - пробиться через них."
            show natsuki 2e1
            n "Но я не могу их убить..."
            n "Они... это я...."
            show natsuki 2e2
            n "К тому же, я не люблю стрелять первой."
            mc "Есть предложения, как избавиться от них?"
            bn "Гр-р-р-р-р."
            show natsuki 2e6
            n "Хм-м-м… В самый раз, чтобы расчистить путь."
            n "Нам нужно поторопиться и быстро спрятаться."
            mc "Понял."
            show natsuki 2e2
            n "На счёт три."
            "Имелось в виду НА три или ПОСЛЕ трёх?"
            n "Раз."
            show natsuki 2e1
            n "Два."
            show natsuki 2e4
            n "Три!"
            play sound d03tackle
            show natsuki 2e4 at t32
            "Нац несётся со всей скоростью на самую маленькую Бафсуки, заставленную врасплох подкатом."
            "Я вроде как ожидал увидеть пламенный след на земле."
            bn "Гр-р-р? Гра-а-а-а-а-а!"
            show natsuki 2e3
            n "Вперёд!"
            play sound d03tackle
            "Ей удалось превратить ничего не подозревающую Бафсуки в живой щит, об который наваливаются все остальные."
            mc "Я погляжу, она склонна к ближнему бою."
            show bhorde at thide
            hide bhorde
            show natsuki zorder 2 at thide
            hide natsuki
            "Мы выбираемся и бежим, пока стук не дойдёт вне зоны слышимости."
            stop music fadeout 2.0
            show natsuki 1f3 zorder 2 at t11
            n "Фух, больше так не делай, пожалуйста."
            show natsuki 1f1
            n "Бедные создания, явно не самые умные на свете, но они определённо тяжёлые."
            show natsuki at thide
            hide natsuki
        "Бегство.":
            mc "Есть какой-то способ, чтобы отвлечь их и проскользнуть мимо?"
            show natsuki 2e1
            n "Хм-м… Может, я могу использовать что-то, что есть общее у всех нас."
            mc "Что?"
            show natsuki 2e3
            n "Если расскажешь хоть кому-нибудь, я клянусь, тебе не поздоровится."
            mc "Мамой клянусь."
            show natsuki 2e2
            n "Да… Готова поставить что-угодно, что им это понравится."
            "Она тянется к своему заднему карману и достаёт что-то, что при рассмотрении оказывается…"
            mc "Манга?"
            bn "Гы-а-а-а??"
            show natsuki 2e6
            n "Помнишь ту часть, в которой я прикончу тебя?"
            show natsuki 2e5
            mc "Уж лучше ты, чем они."
            "Она бросает помятую копию в самую большую группу."
            "Другие начинают роиться вокруг неё, галдя и становясь в некое подобие узора."
            bn "Ы-а-а-а-г-х-х!"
            show natsuki 2e1
            n "Ох, теперь мне даже жаль, что я это сделала."
            n "Бедная девчушка завтра вся будет покрыта в синяках."
            bn "Р-р-р-р-р-а-а-а-а-а-а-а-х-х!!!"
            show natsuki 2e2
            mc "Что ж, пора сваливать отсюда."
            stop music fadeout 2.0
            n "Ох, да, конечно. Хотя постой, мне кажется, я знаю, куда подевались остальные."
            show bhorde 5a at thide
            hide bhorde
            show natsuki at thide
            hide natsuki
        "Дипломатия.":
            mc "Это может прозвучать глупо, но давай попробуем поговорить с ними."
            show natsuki 2e6
            n "О-о чём именно?"
            mc "Ну, что бы ты хотела услышать от щуплой копии себя?"
            show natsuki 2e1
            "Она думает пару секунд, а затем поворачивается к орде."
            show natsuki 2e2
            n "Да здравствует могучая Орда Бафсуки!"
            "Она делает реверанс, а затем встречает их с почитающим взглядом."
            bn "Хы-ы-ых. Гырх хырх хры-а-а-а-а."
            mc "Кажется, это работает!"
            "Они поворачивают взгляды на меня, несущиеся и рычащие зубами."
            show natsuki 2e5
            n "Тише ты! Ты что, не знаешь, с кем ты говоришь?"
            show natsuki 2e6
            n "Леди такой… э… фигуры требуют уважения!"
            "Ну, поехали…."
            mc "В-в таком с-случае… да здравствуют все… Нацуки..."
            "Они начинают расходиться, явно польщены нашим поклонением."
            show bhorde 5a at thide
            hide bhorde
            show natsuki 1f4 zorder 2 at t11
            n "Хах, у тебя пока ещё есть надежда, рядовой."
            stop music fadeout 2.0
            mc "Я не помню, чтобы я подписывался на это."
            show natsuki 1f1
            n "Ладно, нужно сваливать отсюда."
            show natsuki 1f25
            n "И, ты знаешь, я была бы не против, чтобы время от времени мне поклонялись чуть больше."
            show natsuki at thide
            hide natsuki

    play music ash fadein 1.0
    "Мы прогуливаемся ещё несколько минут, прежде чем мы успеваем заметить и других."
    "Знакомые лица, но это явно не те, что я ожидал увидеть."
    show monika_prime 2a zorder 2 at t21
    show mc2 1b zorder 2 at t22
    pm "Ну и ну, вот это командная работа. Я бы помогла, но, ты знаешь."
    pm "У меня нет способностей."
    mc "Как для того, кто постоянно говорит о способностях, я действительно ни разу не видел ни одну из них."
    pm "И молись, чтобы никогда и не увидел. Спроси другого тебя, он тебе расскажет."
    show mc2 4d
    pmc "Я тоже никогда не видел, чтобы ты использовала свои способности..."
    show monika_prime 3l
    pm "Не тебя, балда, – игрока. Ну, того, кто сделал это решение вместо тебя."
    show monika_prime 1a
    mc "Значит, мы всё ещё в игре?"
    show monika_prime at thide
    hide monika_prime
    show mc2 at thide
    hide mc2
    show natsuki 2c6 zorder 2 at t11
    n "Не подстрекай её…"
    show natsuki at thide
    hide natsuki

    show monika_prime 2d zorder 2 at t21
    show mc2 4d zorder 2 at t22
    pm "Ну вообще, я уже не так уверена, что нужно делать сейчас. Измерения всё усложняют."
    pm "Всё, что я знаю, так это то, что игрок использует генератор червоточин, чтобы иметь доступ к текущим мирам."
    show monika_prime at thide
    hide monika_prime
    show mc2 at thide
    hide mc2
    show natsuki 2d5 zorder 2 at t11
    n "Всё, что мы знаем, так это то, что ты иногда несёшь полнейшую херню, леди."
    show natsuki at thide
    hide natsuki
    show monika_prime 4j zorder 2 at t21
    show mc2 4d zorder 2 at t22
    pm "Хорошо, тогда приступим?"
    show mc2 4z
    pmc "А нам действительно стоит это делать?"
    show mc2 1s
    pm "Игрок, можешь, пожалуйста сделать так, чтобы [pm_player] сказал \"Моника – лучшая\"?"

    menu:
        "Сказать \"Моника – лучшая\" как положено.":
            show monika_prime 1l
            mc "Моника – лучшая."
            show monika_prime 1n
            "Нац легонько пихает меня по плечу."
            show monika_prime at thide
            hide monika_prime
            show mc2 at thide
            hide mc2
            show natsuki 2c1 zorder 2 at t11
            n "Ты бы лучше не валял дурака..."
            mc "Так я и не валяю! Кто-то контролирует меня!"
            show natsuki at thide
            hide natsuki
            show monika_prime 1m zorder 2 at t21
            show mc2 1b zorder 2 at t22
            pm "Я же говорила. Хорошо, игрок, любовь моя: мы всё ещё в игре?"
            mc "Я играю в игру, но в главном меню был дисклеймер об использовании экспериментальной технологии червоточин."
            show mc2 1d
            pmc "То есть, мы не имеем ни малейшего понятия."
            show mc2 1b
            show monika_prime 3l
            pm "Кстати говоря, наконец-то рада встрече, так сказать."
            mc "Одна из причин, по которым я установил этот мод – это вернуть тебя."
            show monika_prime 1g
            pm "Вернуть? А я куда-то уходила?"
            show monika_prime 1e
            pm "Хотя, это мило с твоей стороны."
            show monika_prime 1i
            mc "Ты удалила игру."
            show monika_prime at thide
            hide monika_prime
            show mc2 at thide
            hide mc2
            show natsuki 2d4 zorder 2 at t11
            n "Пожалуйста, [player], ты можешь перестать? Ты меня пугаешь."
            show natsuki 2c5
            mc "ИГРОК ЗАСТАВЛЯЕТ МЕНЯ ГОВОРИТЬ. ЭТО РЕАЛЬНО!!!"
            show natsuki at thide
            hide natsuki
            show monika_prime 2l zorder 2 at t21
            show mc2 1b zorder 2 at t22
            pm "Успокойся, [player], он не причинит тебе вреда."
            show monika_prime 1m
            pm "Любовь моя, может, не бери контроль над ним так, чтобы он мог узреть будущее?"
            mc "Лучше бы не узрел…"
            show monika_prime at thide
            hide monika_prime
            show mc2 at thide
            hide mc2
            show natsuki 2c5 zorder 2 at t11
        "Поговорить напрямую с ГГ.":
            "Голос в моей голове говорит \"Привет\"."
            mc "А-А-А-А-А-А!"
            show monika_prime at thide
            hide monika_prime
            show mc2 at thide
            hide mc2
            show natsuki 2c2 zorder 2 at t11
            n "Ты в порядке?"
            mc "Он только что заговорил со мной. Да что же это такое?!"
            "Голос говорит, чтобы ты не пугался, и что он не причинит никакого вреда."
            show natsuki at thide
            hide natsuki
            show monika_prime 1d zorder 2 at t21
            show mc2 1b zorder 2 at t22
            mc "Моника, я думаю, что я сам уладил то, что ты хотела мне сказать..."
            show monika_prime 2d
            pm "Но мы прошли через столько всего, игрок!"
            show monika_prime 2g
            pm "И ты знаешь, что я люблю тебя!"
            show monika_prime at thide
            hide monika_prime
            show mc2 at thide
            hide mc2
            show natsuki 2c6 zorder 2 at t11
            n "Хочешь, чтобы я застрелила её?"
            show natsuki at thide
            hide natsuki
            show monika_prime 2g zorder 2 at t21
            show mc2 1b zorder 2 at t22
            mc "Голос говорит, что ты удалила игру, ещё тогда, когда [player] Прайм был под его контролем."
            show monika_prime 1q
            pm "С чего бы я это делала? Может, это была другая Моника?"
            show monika_prime 1p
            pm "Ну, знаешь, та, которая не любила тебя так сильно, разумеется."
            show monika_prime at thide
            hide monika_prime
            show mc2 at thide
            hide mc2
            show natsuki 2c5 zorder 2 at t11
            n "Ладно, я стреляю."
            mc "Нац, пожалуйста, дай мне хотя бы минутку, чтобы всё обработать..."
        "Ничего не делать.":
            "Ничего не происходит, и я выгляжу растерянно."
            show monika_prime at thide
            hide monika_prime
            show mc2 at thide
            hide mc2
            show natsuki 2c5 zorder 2 at t11
            n "...Итак..."
            show natsuki 2d6
            n "Моника, ты собираешься шевелить ногами?"
            show natsuki at thide
            hide natsuki
            show monika_prime 2g zorder 2 at t21
            show mc2 1b zorder 2 at t22
            pm "Ну, я считала, что он сделает {i} хоть что-то{/i}."
            show mc2 1e
            pmc "И в общем-то, это ничего не доказывает."
            show mc2 1b
            show monika_prime 2f
            pm "Итак, по какой-то причине игрок не хочет... {i}играть{/i}, но ты был под контролем до этого."
            mc "Когда это?"
            show monika_prime 3j
            pm "Только что, во время твоего забега с ордой."
            show monika_prime 1m
            pm "Так это был не ты, кто придумал столь замечательный план. Это был мой обожаемый игрок."
            mc "Да ты что, я же это придумал..."
            show mc2 5h
            pmc "Подождите секундочку, я, кажется, знаю..."
            show mc2 5i
            pmc "[player], у тебя не было никаких... летающих прямоугольников в твоём сознании?"
            show monika_prime at thide
            hide monika_prime
            show mc2 at thide
            hide mc2
            show natsuki 2c1 zorder 2 at t11
            n "Можно я просто скажу... Что?"
            show natsuki at thide
            hide natsuki
            show monika_prime 1a zorder 2 at t21
            show mc2 5h zorder 2 at t22
            pmc "Один из них сделал такой пиликающий звук, и это был тот выбор, который ты сделал?"
            show mc2 5b
            show monika_prime 3d
            pm "Звучит так, как будто ты описываешь меню в игре."
            "Ах да, этот знакомый до боли концепт."
            show monika_prime at thide
            hide monika_prime
            show mc2 at thide
            hide mc2
            show natsuki 2d2 zorder 2 at t11
            n "Или какую-то серьёзную детскую психологическую травму."
            show natsuki 2c5
            mc "Вообще-то, у Прайма и у меня было разное детство."
            show natsuki at thide
            hide natsuki
            show monika_prime 2k zorder 2 at t21
            show mc2 3b zorder 2 at t22
            pm "Ну, пока мы на одной волне, всё замечательно."
            show monika_prime 2o
            pm "Но я бы очень хотела, чтобы моя любовь хотя бы заглянула на секундочку. Ах..."
            show monika_prime at thide
            hide monika_prime
            show mc2 at thide
            hide mc2
            show natsuki 2c5 zorder 2 at t11

    n "Итак, позволь спросить прямо, Моника."
    n "Ты влюблена… в бога?"
    show natsuki 2c6
    n "Ты не считаешь, что это как минимум... странно?"
    show natsuki at thide
    hide natsuki
    show monika_prime 2l zorder 2 at t21
    show mc2 3b zorder 2 at t22
    pm "Забавно слышать это от цундере-солдатки, затаившую обиду на орду из самих себя."
    show monika_prime at thide
    hide monika_prime
    show mc2 at thide
    hide mc2
    show natsuki 2d3 zorder 2 at t11
    n "Ну, твой любовник – это тот, кто сделал меня мной."
    show natsuki at thide
    hide natsuki
    show monika_prime 2i zorder 2 at t21
    show mc2 3b zorder 2 at t22
    pm "Я так не думаю. Они не сделали наши миры. Например, мой мир был создан Team Salvato."
    show mc2 4h
    pmc "Это бог всех богов?"
    mc "В любой другой момент я бы мог подумать, что это безумная идея, но сейчас... да, это имеет смысл."
    show monika_prime 1k
    pm "Просто прими это и живи дальше, розоволосая, пока не стало хуже."
    show monika_prime at thide
    hide monika_prime
    show mc2 at thide
    hide mc2
    show natsuki 2c3 zorder 2 at t11
    "Лицо Нацуки морщится в отвращении."
    show natsuki 2e6
    n "Ну что же, хорошо. А как насчёт..."
    show natsuki 3a5
    n "У меня есть пушка."
    show natsuki at thide
    hide natsuki
    show monika_prime 3l zorder 2 at t21
    show mc2 3b zorder 2 at t22
    pm "Ты такая милая."
    show monika_prime at thide
    hide monika_prime
    show mc2 at thide
    hide mc2
    show natsuki 3a6 zorder 2 at t11
    play sound d03cocking
    n "Она заряжена."

    stop music fadeout 2.0
    scene bg pripyatlobby
    with dissolve_scene_full
    play music lobby fadein 0.5

    show natsuki 1f3 zorder 2 at t11
    n "Кажется, они вернулись."
    show natsuki 1f1 zorder 2 at t22
    show yuri 1a zorder 2 at t21
    y "Нет, тебе не кажется."
    show natsuki 1h4
    n "Пхех, эй, профессор, что я могу сказать? Я знаю, о чём ты думаешь."
    show yuri_prime 1e zorder 2 at t31
    show yuri 1a zorder 2 at t32
    show natsuki 1f1 zorder 2 at t33
    py "Возможно, ты посчитаешь это странным..."
    show yuri_prime at thide
    hide yuri_prime
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    show sayori 4r zorder 2 at t11
    s "Ты вернулся!"
    play sound d03hug
    "Сайори бежит и обнимает меня."
    show sayori 4d
    mc "Хах, так тебе тоже нравятся обнимашки."
    show sayori 1b
    s "Тоже? Ты обнимался с кем-то ещё?"
    show sayori 1b zorder 2 at t21
    show natsuki 1f25 zorder 2 at t22
    n "На меня не смотри. Я просто кричу и каратирую."
    show natsuki at thide
    hide natsuki
    show sayori 1a zorder 2 at t11
    mc "Наши двойники."
    s "Ах, нет ничего лучше, чем лёгкое чувство дежавю."
    "Было бы очень здорово не думать о Матрице после того диалога с Моникой."
    show sayori 2d
    s "Очень хорошо, что ты вернулся."
    mc "Ты знаешь, а мне начинает нравиться наш странный контингент."
    show sayori 2q
    s "Я рада, хе-хе."
    show monika 1a zorder 2 at t11
    show sayori at thide
    hide sayori
    m "Добро пожаловать, ребята. Кажется, нам ещё многое предстоит сделать."
    show monika 1a zorder 2 at t21
    show natsuki 1f3 zorder 2 at t22
    n "Можешь сказать это ещё раз."
    show natsuki at thide
    hide natsuki
    show monika 3a zorder 2 at t11
    m "У нас есть хорошие новости для всех вас."
    m "Нашему другу из другой вселенной, Нацуки Прайм, удалось договориться о перемирии с ордой."
    show monika 1a
    mc "Это... замечательно. Но как?"
    show monika 1j zorder 2 at t21
    show yuri_prime 1b zorder 2 at t22
    py "С помощью еды."
    show monika 1a
    py "Так что теперь она в другой вселенной, ищет, из чего бы ей готовить."
    show yuri_prime 1a
    mc "Профессор, мне это напомнило кое-что..."
    show monika at thide
    hide monika
    show yuri_prime at thide
    hide yuri_prime
    show yuri 1f zorder 2 at t11
    mc "Я забыл вернуть тебе твой нож."
    show yuri 1a zorder 2 at t21
    show yuri_prime 3p zorder 2 at t22
    play sound d02yuripass
    "Я возвращаю ей нож, в то время как Юри Прайм смотрит в ужасе."
    show yuri_prime 3n
    show yuri 1f
    y "Что?"
    show yuri_prime 3o
    show yuri 1e
    py "Я... позже расскажу."
    show yuri at thide
    hide yuri
    show yuri_prime at thide
    hide yuri_prime
    show natsuki 1f3 zorder 2 at t11
    n "У меня тоже есть новости для всех вас."
    show natsuki 1e7 zorder 2 at t22
    show mc2 3d zorder 2 at t21
    pmc "Боюсь, мы все действительно просто игровые персонажи."
    show mc2 3b
    mc "Да, и только игрок реален."
    show natsuki 1e3
    n "Это как бог, и Моника влюблена в него."
    show mc2 3d zorder 2 at t31
    show natsuki 1e7 zorder 2 at t32
    show monika_prime 1n zorder 2 at t33
    pm "А почему нет?"
    show mc2 at thide
    hide mc2
    show natsuki at thide
    hide natsuki
    show monika_prime at thide
    hide monika_prime
    show yuri 1h zorder 2 at t11
    y "Может, потому что всё, что когда-нибудь происходило с тобой – это их вина?"
    "Это было жутко."
    show yuri 1k zorder 2 at t21
    show mc2 3d zorder 2 at t22
    pmc "О, нет, это уже всё в прошлом. Игрок – это просто немножко перебивающий всех придурок."
    show yuri 2y5
    show mc2 3j
    y "О, ну в таком случае, я бы с удовольствием продолжила говорить с тобой об этом!"
    "Тише, Юри, не заводись."
    show yuri at thide
    hide yuri
    show mc2 at thide
    hide mc2
    show monika 2d zorder 2 at t11
    m "Хах. И хотя я уверена, что это своего рода откровение, это всё ещё никак не влияет на наше текущее положение дел."
    m "Нам нужно найти хорошее место для генератора червоточин и выбраться из этого измерения."
    show monika 4a
    m "Кажется, основной холл может быть весьма кстати."
    show monika 2a zorder 2 at t21
    show yuri 1a zorder 2 at t22
    y "Согласна."
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    show natsuki 1g7 zorder 2 at t11
    n "Эй, [player], хочешь пойти и поразведать?"
    mc "Ты уверена?"
    show natsuki 1h3
    n "Ну да, не то, чтобы ты был всемогущий герой, избранный игроком..."
    mc "А я только начал думать, что я тебе нравлюсь."
    show natsuki 1g26
    n "Ты реально бестолковый."
    show sayori 2d zorder 2 at t21
    show natsuki 1g1 zorder 2 at t22
    s "Позаботься о нём, хорошо?"
    mc "Я в порядке, мам."
    show sayori 2l
    show natsuki 1e26
    n "Я верну его до 11 вечера."
    show sayori 1a
    show natsuki 1g1
    s "Хех, ты бы поверила, что он был напуган тобой?"
    show natsuki 1e6
    n "Ну, я и так достаточно ужасающая."
    show natsuki 1e24
    show sayori 4h
    "Она издаёт первобытный рёв."
    show natsuki 1f26
    show sayori 1p
    mc "Надеюсь, что здесь нет никаких Бафйори."
    show sayori 2l
    s "Ха, а я всегда считала, что мой двойник был бы славянином."
    mc "Если мы будем переходить через достаточное количество измерений, я уверен, что мы найдём то, в котором ты будешь богом репа."
    show natsuki 1f1
    show sayori 2a
    s "А то ты не знаешь. Мой литературный двойник показал мне парочку приёмов."
    show sayori_prime 1l zorder 2 at t31
    show sayori 2r zorder 2 at t32
    show natsuki 1f1 zorder 2 at t33
    ps "Э-хе-хе..."
    show sayori_prime at thide
    hide sayori_prime
    show sayori at thide
    hide sayori
    show natsuki 1h26 zorder 2 at t11
    n "Ну же, рядовой, ты же хотел надрать межпространственные задницы."
    show natsuki 1h20
    "Я никогда не искуплю свою вину, не так ли?"

    stop music fadeout 2.0
    scene bg pripyat
    with dissolve_scene_full
    play music ash

    mc "Признайся, ты просто хотела провести больше времени со мной."
    show natsuki 1f7 zorder 2 at t11
    n "С чего бы вдруг мы стали настолько уверены в себе?"
    show natsuki 1f1
    n "Я бы поиздевалась над тобой за попытку заигрывать, но я считаю, что ты заслужил небольшой перерыв."
    mc "Примерно так же, как я узнал, что мы все вымышленные, ладно?"
    show natsuki 1f3
    n "Мы всё ещё реальны. И наши двойники тоже."
    n "Ты бы лучше помнил о том, если мы попадём в передрягу."
    show natsuki 1e1
    n "Знаешь, я на самом деле рада, что Нацуки удалось решить все дела с крупышами."
    show natsuki 1f17 "Во всех измерениях, в которых мы оказываемся, я бы хотела помогать людям."
    mc "Ты слишком миролюбива как для леди с пушкой."
    show natsuki 1h25
    n "Оу, так теперь я \"леди\"?"
    show natsuki 1f24
    n "И если я ношу пушку, то это не значит, что я хочу использовать её."
    show natsuki 1f17
    n "Хм-м-м..."
    "Я чувствую, что она что-то недоговаривает..."

    menu:
        "Обратиться к ней грубо.":
            mc "Ладно, сержантик, что нужно сделать, чтобы быть боевым пацифистом?"
            show natsuki 1h2
            n "Да ладно, я думаю, ты и так знаешь."
            show natsuki 1h3
            n "Желание иметь значение. Защита своей страны..."
            mc "И?"
            show natsuki 1g24
            n "И… большая страсть к тому, чтобы некоторые события моей жизни, когда я была ещё ребёнком, никогда не произошли снова."
            mc "О, чёрт... Семья?"
            n "Да, скажем, разногласия с отцом. Пока на этом остановимся."
            mc "Справедливо. Но, знаешь, если хочешь поговорить, я здесь."
            show natsuki 1e26
            n "Эй, не расслабляйся."
            show natsuki 1f1
            mc "Даже и не мечтал."
        "Обратиться к ней мягко.":
            mc "Нац, что-то не так?"
            show natsuki 1e3
            n "Ты о чём?"
            mc "Ну, не могу не заметить, что этот имидж, с которым ты таскаешься, есть не более, чем просто щит."
            show natsuki 1f3
            n "А ты хорош."
            mc "Нет, я не хочу давить, но что бы это ни было, это разъедает тебя."
            show natsuki 1e17
            n "Ну да, но некоторый груз не так лёгок, как тебе кажется."
            mc "Я знаю, и я даже не спрашиваю."
            show natsuki 1e19
            mc "У нас есть что-то вроде взаимопонимания, и поэтому я подумал, что ты могла бы довериться и подтолкнуть немного от всей этой тяжести."
            show natsuki 1e14
            mc "Мне не нравится смотреть, как мои друзья страдают."
            show natsuki 1f25
            n "Ты слишком подлый, ты знаешь это?"
            show natsuki 1f1
            mc "Это не подло, если это честно."
            show natsuki 1f24
            n "Больше похоже на какой-то низкобюджетный диалог в романтической комедии."
            show natsuki 1f25
            n "Не волнуйся, просто будь рядом, и я скажу тебе."
            show natsuki 1h21
            n "Ну а сейчас, давай лучше сфокусируемся на том, чтобы выбраться в место безопаснее, пожалуйста."
            show natsuki 1f1
            mc "Ну конечно, тебе нужно привносить логику..."
        "Ничего не делать.":
            show natsuki 1f25
            mc "О да, такая столь кровожадная леди."
            show natsuki 1f23
            n "Пф-ф-ф, ты ещё даже ничего не видел."
            mc "Обещаешь?"
            show natsuki 1e26
            n "Тихо, мальчик."
            mc "Хе-хе, тебе кто-нибудь говорил, что ты буквально королева издевательств?"
            show natsuki 1f4
            n "О, да всё время. Если бы не мой статус, люди бы называли меня Королева Нацуки."
            mc "Ну, никогда не знаешь, может, мы найдём соответствующую корону из щебня."
            show natsuki 1h5
            n "Королевы издевательств не носят обычные короны из щебня."
            mc "Ох, конечно, Ваше величество."
            show natsuki 1f25
            n "Для тебя – товарищ сержант."
            show natsuki 1f1
            mc "Так точно, трщсржант."

    show natsuki 1e3
    n "Похоже, это именно то место, о котором говорила Доктор Баг."
    n "Кажется, путь чист."
    show natsuki 1e7
    mc "Получается, нам нужно просто ждать здесь, пока они все не поднимутся и будут готовы идти?"
    show natsuki 1e3
    n "Нет, другалёчек, нам нужно вернуться обратно."
    show natsuki 1e7
    "Даже не знаю, может, \"другалёчек\" - это что-то милое? Хм-м-м..."
    mc "Я не настолько привык к ходьбе, как ты."
    show natsuki 1h4
    n "Ты должен записаться. Самая лучшая тренировка в жизни."
    show natsuki 1h1
    mc "Нет, знаешь, я немного занят пребыванием в другом измерении и всё такое."
    show natsuki 1g6
    n "Конечно, д{nw}"
    hide natsuki
    show monicula 2b zorder 2 at t11
    stop music fadeout 2.0
    play sound d03trap
    bm "Ага, попались!"
    show monicula 2b
    "Очередная Моникообразная личность, которой удалось устроить засаду с помощью какого-то гаджета."
    show monicula 2a zorder 2 at t21
    show natsuki 1e23 zorder 2 at t22
    n "Нет... Чёрт возьми..."
    show monicula 1a
    show natsuki 1e24
    bm "О, ты ОБЯЗАТЕЛЬНО СПРАВИШЬСЯ с этим!"
    show monicula 2i
    bm "Подождите, разве я вас знаю?"
    mc "Ура... Моника из Припяти..."
    show monicula 1f
    bm "Как вы... вообще... знаете моё имя?"
    show natsuki 1e2
    n "Ни слова!"
    show natsuki 1e6
    "Да, я знаю, некая другая Моника не позволила бы мне сбежать с одним и тем же дважды."
    mc "У тебя... на бейджике написано."
    show monicula 2p
    "Моника из Припяти смотрит вниз, искренне надеясь заметить пресловутый бейджик."
    show monicula 1g
    bm "Что за?.. Оу..."
    show natsuki 1e4
    n "А ты не очень сообразительная, не находишь?"
    show monicula 2c
    play sound d03knockout
    show natsuki 1e22
    "И вот так, Моника из Припяти выбивает в ловушке землю из-под ног."

    scene bg blackbackground
    with dissolve_scene_full

    if dimensions_aroute == True:
        "..."
        amc "Это действительно необходимо?"
        a "Боюсь, что да. Историю жителей измерения D3 необходимо разыграть именно таким образом."
        a "Должно быть, это то же самое, что и в твой первый раз."
        amc "А не изменилось ли что-то, когда ты говорила со мной в шкафу?"
        a "Ты и я находимся не внутри Великой Симуляции."
        a "И пока об этом не знает никто, кроме нас с тобой, всё хорошо."

    "..."
    by "ПРОСЫПАЙСЯ, ЧЁРТ ВОЗЬМИ!"
    "Юри будит меня снова. Похоже, это уже вошло в привычку."
    "Но что это она там делает?"
    "Подождите, это же не Юри..."

    scene bg torture
    with wipeleft_scene

    show yerri 1d zorder 2 at t11
    play music yerri
    "Странно, но этот человек из Припяти бейджик таки надел."
    show yerri 1b
    by "Ну же, нужно выбираться отсюда!"
    mc "Ух, где мы вообще на этот раз?"
    show yerri 1f
    by "Поместье графа Моникулы. И что значит \"на этот раз\"?"
    mc "Графа..."
    show yerri 1i
    by "Моникулы, и нет, она не вампир. Она просто сумасшедший учёный, которой очень нравится похищать случайных прохожих."
    "Сумасшедший учёный, да? Больше похоже на Баг, чем на Прайм."
    show yerri 1k
    by "...а затем сращивать их в сверхсильные армии клонов."
    "А хотя, в общем-то, неважно..."
    mc "Так значит, вот откуда появились все эти Бафсуки?"
    show yerri 1d
    by "Да, и судя по всему, твой дружок – следующий на плаху."
    mc "Ох, Нац..."
    "Я вижу её, сидящую без сознания в углу клетки."
    show yerri 1b
    by "Есть план, но мне будет нужна твоя помощь."
    mc "Итак, что тебе нужно?"
    show yerri 1p
    by "А-а-а! Пожалуйста, помоги мне, ты мне нужен!"
    mc "Ладно, леди, успокойся. Я тоже хочу выбраться отсюда..."
    show yerri 4r
    by "Чёрт возьми, или ты помогаешь мне, или я распотрошу тебя прямо сейчас!!!"
    mc "Ох, чёрт, я сказал, что я хотел бы! НАЦ!"
    mc "НАЦ?!!!"
    show yerri at thide
    hide yerri
    show natsuki 1d3 zorder 2 at t44
    n "Хм-м... Оу?"
    show natsuki 1a2
    n "[player]!"
    mc "Не желаешь помочь?"
    show natsuki at thide
    hide natsuki
    show yerri 3y5 zorder 2 at t11
    by "Она тебе не поможет. Она тебя не заполучит. Ты – мой, и я сделаю с тобой, что бы я ни пожелала!"
    show yerri 3y1
    by "Видишь ли, план состоит в том, что… ты предложишь себя как ритуал Моникуле в обмен за мою свободу."
    show yerri at thide
    hide yerri
    show natsuki 1a2 zorder 2 at t44
    n "Держись, я иду!"
    play sound d03picklock
    "Я вижу, как Нац возится с замком, пока я пячусь к стене."
    show natsuki at thide
    hide natsuki
    show yerri 4y1 zorder 2 at t11
    mc "Но ведь это... даже не имеет никакого смысла? Я и так в заточении."
    show yerri 4y7
    by "Ты думаешь, что я беспокоюсь за тебя? Всё, что имеет смысл – это текущий момент."
    show yerri 4y4
    by "ТЫ и Я."
    show yerri 4y2
    by "В вечной..."
    show yerri 4y3
    by "АГОНИИ!"
    mc "Пожалуйста, нет!"
    play sound d03knockknife
    show yerri at thide
    hide yerri
    "Мне удалось выбить нож из рук Йерри, выигрывая немного времени для Нац."
    show natsuki 1a6 zorder 2 at t44
    play sound d03picklock
    n "Чёрт возьми, Юри, я клянусь, если ты не прекратишь ПРЯМО СЕЙЧАС, я надеру тебе задницу."
    show natsuki at thide
    hide natsuki
    show yerri 3p zorder 2 at t11
    by "Кто. БЛЯТЬ. Такая. Юри?!?!?"
    mc "Ну спасибо, ты только что разозлила её..."
    show yerri 3y7
    by "Нет! Я просто в экстазе! А-ха-ха-ха-ха-ха!"
    "Пожалуй, это самый неуравновешенный человек во всём свете."
    show yerri at thide
    hide yerri
    show natsuki 1a23 zorder 2 at t44
    play sound d03picklock
    n "Да мне всё равно. У тебя не получится навредить ему. Он мне нравится живым."
    show natsuki at thide
    hide natsuki
    show yerri 4x zorder 2 at t11
    by "Живой, мёртвый – какая вообще разница, если ты всё равно не можешь ничего не чувствовать?"
    show yerri 4x zorder 2 at t21
    show natsuki 1a15 zorder 2 at t22
    play sound d03breakin
    "Нац врывается через дверь..."
    "Однако прежде чем она успевает сделать хоть что-то, Йерри поднимает нож к своей глотке."
    show natsuki 1a11
    show yerri 5y2
    stop music
    play sound d03cutthroat
    "..."
    show natsuki 1a16
    show yerri 6y2
    "......"
    play sound d03lobbyentrance
    show yerri at thide
    hide yerri
    "........."
    show natsuki 1b21 zorder 2 at t11
    mc "Ох-х-х, ну и жуть..."
    play music dfsocean fadein 4.0
    show natsuki 1d13
    n "Ты в порядке?"
    mc "Очередная психологическая травма на всю оставшуюся жизнь, но в целом да. А ты?"
    show natsuki 1b19
    n "Я в порядке, но не имею ни малейшего понятия, куда Моникула спрятала пушку."
    mc "При условии, что часть про \"графа Моникулу\" не была бредом Йерри."
    show natsuki 1b24
    n "Ну, {i}кто-то же{/i} выбил нас."
    show natsuki 1b15
    n "И ради всего святого, как у этой ненормальной есть хоть что-то, что роднит её с нашей Юри?"
    mc "Нужно не спускать с неё глаз. Даже одна крохотная капля кошмарно заряженной Йерри – это слишком."
    mc "И... чёрт... Ну, теперь мы знаем, что у неё есть нож."
    show natsuki 1b21
    n "Вот дерьмо… Я только что вспомнила. Юри Прайм очень странно отреагировала на нож профессора."
    show natsuki 1b14
    n "Может, она прольёт свет на это."
    mc "Хорошо мыслишь. Хотя пока мы застряли тут, это всё пустая трата времени."
    show natsuki 1a24
    n "Я... рада, что с тобой всё хорошо."
    "Если бы я не знал её лучше, могло прозвучать так, как будто она заботится обо мне."
    show natsuki 1d25
    n "Значит так, рядовой, несёмся к двери через три..."
    n "Два..."
    n "Один..."

    scene bg npp
    with wipeleft_scene
    play sound d03lobbyentrance
    mc "Наружу!"
    stop music fadeout 2.0
    show natsuki 1d2 zorder 2 at t11
    n "Да, давай вернёмся назад, быстро. Нам нужно предупредить всех остальных."
    hide natsuki
    show monicula 1a zorder 2 at t11
    play music count
    bm "Неужто вы думали, что всё будет настолько просто?"
    bm "О, привет, [player], я знала, что узнаю тебя."
    show monicula 1a zorder 2 at t32
    show bhorde 5a as horde1 zorder 1 at t31
    show bhorde 5a as horde2 zorder 1 at t33
    bn "Хыр-р-р-р гыр-р-р-р."
    bm "Надеюсь, что вам понравится в кругу моих друзей."
    show monicula at thide
    hide monicula
    hide horde1
    hide horde2
    show natsuki 1a2 zorder 2 at t11
    n "[player], Бафсуки! Это наш шанс!"
    mc "И впрямь. Есть что-нибудь съестное?"
    show natsuki 1a7
    n "Полевое питание, если это вообще считается."
    "Я замечаю что-то отражающееся на постаменте."
    mc "Твоя пушка!"
    mc "Ладно, я понял, делай что хочешь."
    show natsuki 1a4
    n "Итак... Кто тут голоден?"
    play sound d03ration
    "Она трясёт пакетиком, лишь отдалённо напоминающим еду."
    show natsuki 1a4 zorder 1 at t21
    show bhorde 1a zorder 1 at t22
    bn "Хм-м-м?"
    "Одна из Бафсуки ковыляет сюда. Она выглядит заинтересованной."
    show natsuki at thide
    hide natsuki
    show bhorde at thide
    hide bhorde
    show monicula 2l zorder 2 at t11
    bm "Ха-ха, ты думаешь, что они предадут меня, если ты соблазнишь их едой?"
    hide monicula
    show natsuki 1c25 zorder 2 at t11
    n "Нет, но я надеюсь, что кто-то уже это сделал."
    play sound d03grabbing
    "Я берусь за пушку Нацуки и хватаю связку ключей на брелоке."
    "В хозяйстве пригодится."
    hide natsuki
    show monicula 1d zorder 2 at t11
    bm "Кто?"
    hide monicula
    show natsuki 1a4 zorder 2 at t11
    n "Я!"
    show natsuki 1a4 zorder 2 at t32
    show bhorde 1a as horde1 zorder 1 at t31
    "Одна за одной, Бафсуки сменяют воюющую сторону, в то время как Нац продолжает раздавать еду."
    show bhorde 1a as horde2 zorder 1 at t33
    "Лишь пара-тройка из них остаются верны Моникуле."
    show natsuki 1d25
    n "Итак, подружаня, – два правила."
    play sound d03throwgun
    "Я бросаю ей пушку."
    show natsuki 2d5
    n "Первое – ты даёшь мне и моему другу спокойно уйти."
    show natsuki 2d6
    n "Второе – Бафсуки идут с нами."
    mc "Чего?"
    show natsuki at thide
    hide natsuki
    hide horde1
    hide horde2
    show monicula 2l zorder 2 at t11
    bm "Как насчёт того, чтобы \"нет\"? Ты, наверное, сумасшедшая, если ты думаешь, что мы заключим такую сделку."
    show monicula at thide
    hide monicula
    show natsuki 2e5 zorder 2 at t32
    show bhorde 1a as horde1 zorder 1 at t31
    show bhorde 1a as horde2 zorder 1 at t33
    play sound d03cocking
    n "Ладно."
    play sound d03firing
    "Нац делает предупредительный выстрел в воздух над головой Моникулы."
    "Моникула взвизгивает и бежит."
    show natsuki 1f1
    bn "Р-р-р-р-а-а-а!"
    show natsuki 1f6
    n "Бафсуки, в атаку!"
    hide horde1
    hide horde2
    show natsuki 1f3 zorder 2 at t11
    "Это невообразимое и одновременно удивительное зрелище, как они штурмуют по полю сквозь бетон."
    "Они и Моникула исчезают за горизонтом."
    "Нац горделиво стоит."
    mc "Они идут с нами?"
    stop music fadeout 2.0
    show natsuki 1f23
    n "Я же не оставила тебя позади, не так ли?"
    n "Да, они идут с нами."
    play music talking
    mc "Просто..."
    show natsuki 1f24
    n "Они – это я. Они чуть более простые и намного более коренастые, но это действительно тоже я."
    show natsuki 1f7
    n "Я не могу просто оставить их в этой адской дыре."
    mc "Хорошо, я понял. Хотя, Баг и Моника Прайм не совсем похожи."
    show natsuki 1f6
    n "И правда. Не доверяю я этой ведьме."
    mc "Доктор Баг внушает большее доверие?"
    show natsuki 1e7
    n "Ну да, конечно... {i}Ты{/i} внушаешь большее доверие."
    n "Почему?"
    show natsuki 1g25
    n "Потому что у тебя хватило яиц ответить на мою чушь."
    show natsuki 1e1
    n "Ладно, самое время поворачивать обратно."
    n "Скорее всего, они последуют за нами за едой."
    mc "Нац, я хочу сказать..."
    show natsuki 1e7
    n "Что?"

    menu:
        "Долг.":
            mc "Было честью работать с вами, Сержант."
            show natsuki 1h3
            n "А ты что, уже уходишь?"
            mc "Нет, просто я не могу объяснить, что Йерри сделала с моим разумом, и мне просто хотелось, чтобы ты знала."
            mc "Ну, знаешь, пока я всё ещё могу..."
            show natsuki 1f1
            n "Тогда даю слово, что никто не посмеет сделать {i}это{/i} с тобой."
            mc "Спасибо, трщ сержант. И знаешь, я могу рассмотреть предложение записаться."
            show natsuki 1f4
            n "Ты же знаешь, что я просто глумлюсь над тобой?"
            mc "Ну, теперь да, и в этом и состоит моя жалоба."
            show natsuki 1e20
            n "А ещё хочу заметить, что сегодня мы настолько далеко ушли от повестки, насколько это вообще возможно."
            mc "Это и так понятно."
        "Дружба.":
            mc "Хочешь верь, хочешь нет, но в те моменты, когда мы не попали в засаду или нас не похитили, мне было приятно работать вместе."
            show natsuki 1h20
            n "А ты довольно сентиментален, не так ли?"
            show natsuki 1f9
            mc "Я знаю, что ты прикроешь меня, а я – тебя."
            show natsuki 1f8
            n "Думаю, это не самая плохая договорённость."
            mc "И обоюдные издевательства у нас на высшем уровне."
            show natsuki 1h25
            n "Да, на меня иногда снисходит озарение."
            mc "Я чрезвычайно рад нашему знакомству, Нац."
            show natsuki 1h24
            n "Боже, ещё хотя бы капля подлости, и мы начнём привлекать крыс."
            show natsuki 1e26
            mc "Если мы не справимся с какими-то крысами после сегодняшнего, то значит, что-то идёт не так."
        "Сложно определить.":
            mc "Уверен, ничего такого, что ты бы не нашла слишком подлым."
            show natsuki 1h26
            n "Продолжай, мне вообще... нравятся подлые люди."
            mc "У нас был целый шквал самых разных эмоций, и я бы с удовольствием искал дополнительных приключений с тобой."
            show natsuki 1f20
            n "Ладно, удовлетворительно."
            show natsuki 1e15
            n "Подожди, ты же не собираешься сделать мне предложение?"
            show natsuki 1e13
            n "Потому что, ну, я замужем за своей работой, ладно?"
            mc "Ха-ха, какое клише. Но это и так очевидно, что у нас есть какая-то связь между нами, и это чуть больше, чем просто дружба."
            show natsuki 1f20
            n "Как скажешь. Вот я думала, что мы просто две старые девы, переродившиеся, чтобы спорить друг с другом на веки вечные."
            mc "Согласен."
            show natsuki 1f1
            n "Я тоже."
            "Нац целует меня в щёку."
            mc "А мне казалось, старые девы не делают этого..."
            show natsuki 1f26
            n "Тогда это какие-то неправильные старые девы."

    "Бафсуки возвращаются, и одна из них, одетая в броню, идёт к нам."
    show natsuki 1e3 zorder 2 at t21
    show bhorde 2f zorder 2 at t22
    n "О, привет... я. Как ты смотришь на то, чтобы присоединиться к нам?"
    "Грубость в голосе Нацуки постепенно исчезает. Ясное дело, что это просто постановка."
    show bhorde 2c
    bn "Хыр-р-р?"
    show natsuki 1g1
    n "Не беспокойся, мы позаботимся о тебе."
    mc "Как-нибудь..."
    show bhorde 21
    show natsuki 1g26
    bn "А-а-а..."
    "Странно видеть его улыбающегося. Здесь это уже более {i}она{/i}, чем {i}оно{/i}."
    mc "Ты же раньше была человеком?"
    show bhorde 2s
    bn "Гры-ы-ы... Хр."
    show natsuki 1e3
    n "Может быть, у нас получится восстановить тебя до исходного состояния."
    show bhorde at thide
    hide bhorde
    "Бафсуки карабкаются вместе в одно целое, и многорукое нечто ступает вперёд."
    show bhorde 4r zorder 2 at t22
    show natsuki 1e1
    bn "С-спа-а... а-а-с..."
    show bhorde 4u
    "Оу, они умеют говорить."
    show natsuki 1e20
    n "В любое время, дружище."
    show natsuki 1h1
    n "Ладно, пора идти обратно. Баг, скорее всего, готовится к следующему этапу."

    stop music fadeout 2.0
    scene bg pripyatlobby
    with dissolve_scene_full

    show sayori 4w zorder 2 at t21
    show bhorde 45 zorder 2 at t22
    play music lobby fadein 0.5
    s "A-a-a-a-a!"
    mc "Всё в порядке, они с нами."
    show bhorde 43
    bn "Ку-у-у-у."
    show sayori 1v zorder 2 at t31
    show bhorde 4g zorder 2 at t32
    show natsuki 1f20 zorder 2 at t33
    n "И они безобидные, честно."
    mc "Прямо как ты, хе-хе."
    show natsuki 1h23
    n "Если хочешь, чтобы я показала, я сломаю тебе руку."
    show sayori 1i
    s "Эй, это вовсе необязательно!"
    show bhorde at thide
    hide bhorde
    show natsuki at thide
    hide natsuki
    show sayori 1b zorder 2 at t21
    show monika_prime 1a zorder 2 at t22
    pm "Так что, мы идём?"
    show sayori 1c
    s "Зависит от Доктора Баг. Ты её не видела?"
    show sayori 1b
    pm "В последний раз она была у бокового входа."
    show sayori at thide
    hide sayori
    show monika_prime at thide
    hide monika_prime
    show natsuki 1a1 zorder 2 at t11
    n "[player], найди её, я тем временем озвучу все инструкции."
    show natsuki at thide
    hide natsuki
    show monika_prime 1a zorder 2 at t11
    pm "Я пойду с тобой. У нас даже не было возможности нормально побеседовать."
    mc "Ладно, да… Я бы не был против..."
    show monika_prime 2h
    pm "Да ладно, [player], не будь таким ворчливым, сержант сильно повлияла на тебя."
    "Ой, Моника, иди ты куда подальше..."
    show monika_prime 1a
    pm "Я собиралась рассказать тебе о песне, которую я писала для игрока."
    pm "Я всё ещё новичок, но это приходит со временем. А ты играешь на каком-то инструменте?"
    "Серьёзно?"
    mc "На гитаре, и недавно начал баловаться с пианино, а что?"
    show monika_prime 1b
    pm "Это же просто замечательно! Я тоже играю на пианино, и быть может, мы бы когда-нибудь сыграли дуэтом."

    show monika_prime 1c zorder 2 at t21
    show sayori 3d zorder 2 at t22
    s "О-о, а мы можем сыграть трио?"
    "Сайори решает вклиниться в беседу."
    show sayori 1a
    s "Я играю на укулеле."
    "Я даже не давал согласие на дуэт..."
    show monika_prime 2c
    pm "Ну... если ты настаиваешь..."
    show monika_prime at thide
    hide monika_prime
    show sayori at thide
    hide sayori

    scene bg pripyatcorridor
    with wipeleft_scene

    "Мы трое идём по коридору вместе в неловкой тишине."
    "Я так устал от ходьбы. Может, Моника принесла пару стульев..."
    "Мы дошли до бокового входа."
    "Но... здесь никого..."
    mc "Моника, где она{nw}"
    stop music fadeout 2.0
    play sound d03monihit
    "Что-то очень тяжёлое стукнуло меня по голове."
    show sayori 4c zorder 2 at t11
    s "[s_player]! Будь ты проклята, Моника! А-а-а..."
    show sayori at thide
    hide sayori
    play sound d03monithrow
    "С тем, как я ползу вниз по полу, я вижу, как Моника швыряет Сайори к стене."
    show monika_prime 1d zorder 2 at t11
    pm "Я дико извиняюсь за это, но видишь ли, мне действительно нужно обратно домой."
    show monika_prime 1a
    pm "И я не могу никому позволить встать у меня на пути. Даже тебе, любовь моя."
    pm "Без обид?"
    mc "Бляяяяяяя{nw}"
    show monika_prime 4l
    pm "Ну, ну, это не самое подходящее время для ругательств."
    show monika_prime at thide
    hide monika_prime
    "Сайори неподвижна."
    "Я хочу помочь, но я чувствую, как мир.. ускользает...... от меня......"
    scene bg blackbackground
    with dissolve_scene_full

    "..."
    if dimensions_aroute == True:
        amc "Так что именно должно будет произойти?"
        amc "Часть тебя умрёт или что?"
        a "Думай об этом, как о некой передаче энергии."
        a "Когда Доктор Баг умрёт, она воссоединится с моим духом."
        amc "Ты веришь в духов?"
        a "Для такой сущности, как я, это просто такое же хорошее слово, как и любое другое."
        a "А дух я на самом деле или нет, я не могу сказать точно."
    else:

        pm "Чудесно!"
        pm "В таком случае, мы займёмся тем же и завтра."
        pm "Может, ты даже научился чему-то у своих друзей."
        pm "Так что твои стихи станут только лучше!"
        m "Действительно, ананасы..."
    "..."
    s "[s_player]! Вставай, ты мне нужен!"

    scene bg pripyatcorridor
    with dissolve_scene_full
    play sound d03pickup
    play music bugging
    show sayori 1w zorder 2 at t11
    s "Не уходи от меня снова."
    mc "Я в порядке… а что произошло?"
    show sayori 4w
    s "Это Моника, мы должны остановить её!"
    mc "Ох, чёрт, генераторы! Ты поищешь Юри, я найду Баг."
    show sayori 1j
    s "Принято."
    show sayori at thide
    hide sayori
    "Я вбегаю обратно тем же путём, и обнаруживаю странные лица остальных."

    scene bg pripyatlobby
    with wipeleft_scene

    show mc2 3a zorder 2 at t21
    show natsuki 1g3 zorder 2 at t22
    mc "Где Доктор Баг?!"
    show mc2 4d
    pmc "А ты разве не пошёл искать её?"
    mc "Чёрт… Нац, мне нужно, чтобы ты заняла оборону. Моника пошла во все тяжкие."
    show natsuki 1h6
    n "Принято. Всем внимание!"
    show mc2 at thide
    hide mc2
    show natsuki at thide
    hide natsuki
    "Я продолжаю рыскать по зданию, безуспешно обходя комнату за комнатой."

    scene bg pripyatcorridor2
    with wipeleft_scene

    show monika_prime 1k zorder 2 at t11
    pm "А, вот ты где!"
    show monika_prime 1a
    "Моника возникает из комнаты c самодовольной ухмылкой."
    show monika_prime 3a
    pm "Вот, я подумала, что ты захочешь сказать пока."
    "Она отошла так, что я теперь вижу комнату."
    show monika_prime at thide
    hide monika_prime
    "О, господи, Доктор Баг!"
    "Я вбегаю в комнату, тем самым позволяя Монике сбежать."

    scene bg ch03a
    with wipeleft_scene

    m "[player]... Ах-х-х..."
    mc "Нет, нет, нет, что же мне теперь делать?! Я не помню тренировку про первую помощь."

    scene bg ch03b

    m "Н-нет, я не тот д-доктор..."
    mc "Сейчас не время шутить! Мне нужно знать, как помочь тебе."

    scene bg ch03a

    m "Нет, с меня хватит. Другая я – вот кому н-нужна помощь."
    mc "Она только что проткнула тебя насквозь, и не говори так, чёрт возьми!"
    mc "ЭЙ! КТО-НИБУДЬ РЯДОМ?!"
    m "У н-неё есть генератор. Можешь использовать его как п-п-пункт н-назначения..."
    m "Помоги Юр... Юри... Она тяжело это воспримет... Ах..."
    mc "Пожалуйста... Пожалуйста, не уходи. Ты же лучшая из нас."

    scene bg ch03b

    m "Просто...... с-сделай...... что... нужно."

    scene bg ch03c

    "Огонёк в её глазах угасает, отныне и навсегда."

    menu:
        "Злость.":
            mc "Моника, чёртов ты кусок дерьма! Я убью тебя за это!"
            "Я вскарабкиваюсь на ноги и поднимаю кусок стекла с пола."

            scene bg pripyatcorridor2
            with dissolve_scene_full

            "Но прежде, чем я начинаю бежать, Сайори и Юри входят внутрь."
            show sayori 4m zorder 2 at t21
            show yuri 2f zorder 2 at t22
            s "Ты в порядке... ох... о, боже мой..."
            show sayori 4v
            y "[player], положи стекло на место."
            "Я смотрю вниз и осознаю, что моя рука кровоточит, пока я держу его в руках."
            mc "Она… она убила Баг… я… должен её остановить."
            show sayori 1u
            s "Прекрати, [s_player], ты нам нужен трезво мыслящим!"
            show yuri 1w
            y "Позволь я это заберу."
            "Юри встаёт и медленно вытягивает стекло из моей руки."
            show yuri 2m
            y "Нужно быть сильными для неё."
            "Я только забыл о нашем испуге по поводу здравомыслия профессора, как она теперь держит этот окровавленный кусок стекла..."
            mc "Просто скажи мне, что генератор всё ещё у тебя."
            show yuri 2f
            y "Да, но скорее всего, Моника Прайм украла второй."
            show sayori 1k
            s "Моника, мне так жаль."
            "Сайори наклоняется и закрывает глаза Доктора Баг."
            mc "Она сказала, что мы можем использовать генератор в качестве пункта назначения."
            show yuri 2h
            y "Так вот как, теперь мы можем идти за Моникой Прайм."
            show sayori 1v
            s "Ты уверена, что это хорошая идея?"
            mc "Мы должны знать, почему. Она хотя бы нам скажет."
            show yuri 2t
            "Юри смотрит на меня с беспокойством."
            y "Нам лучше поторопиться. Боюсь, что нет времени на траур, если мы хотим наверстать упущенное."
        "Грусть.":
            mc "Что же нам делать без вас?"

            scene bg blackbackground
            with dissolve_scene_full

            "Я закрыл доктору Баг глаза."

            scene bg pripyatcorridor2
            with dissolve_scene_full

            mc "Это была твоя миссия, и мы тебя подвели."
            mc "Я подвёл тебя. Я даже не должен быть здесь."
            show sayori 4m zorder 2 at t21
            show yuri 2f zorder 2 at t22
            "Сайори и Юри входят в комнату."
            "На лице Сайори страх и шок. У Юри ноль эмоций."
            show sayori 1v
            s "Д-да, ты права. Мне очень жаль, Моника."
            show yuri 2h
            y "Доктор Баг настаивала на том, чтобы мы продолжали."
            show sayori 1u
            show yuri 2e
            mc "Боже, Юри, неужели тебе все равно? У твоего местного двойника было много эмоций, а у тебя их просто нет."
            show yuri 2l
            "Оглядываясь назад, это было действительно жестоко, но я так не думаю."
            show yuri 1f
            y "Я забочусь, но я не могу позволить себе показать это. Она сейчас рассчитывает на нас."
            show sayori 2k
            s "Генератор червоточин пропал. Моника Прайм, должно быть, взяла его."
            show yuri 1h
            y "Я думаю, что лучше проследить за ней с нашим генератором."
            mc "Доктор Баг согласилась на это."
            show sayori 2u
            show yuri 2t
            y "Прости меня, [player], но нам нужно двигаться."
            "Я отдаю последние почести, и мы уходим."
        "Стоицизм.":
            mc "Хорошо."
            "Я без понятия, как это могло произойти."
            mc "Спи спокойно, Моника Баг."

            scene bg blackbackground
            with dissolve_scene_full

            "Я закрыл ей глаза. Сайори и Юри входят в комнату. На лице Сайори виден шок и горе. Юри без эмоций."

            scene bg pripyatcorridor2
            with dissolve_scene_full

            show sayori 4w zorder 2 at t21
            show yuri 2e zorder 2 at t22
            s "Мне очень жаль, Моника."
            show yuri 2f
            show sayori 4v
            y "Взяла ли Моника Прайм генератор червоточин?"
            "Спокойно, занимайтесь своими делами."
            show yuri 2e
            mc "Боюсь, что да. Кстати, профессор, нам с тобой надо поговорить."
            show sayori 1u
            s "Нам {i}действительно{/i} стоит об этом говорить?"
            show yuri 1t
            mc "Это не важно. Нац и я наткнулись на твоего двойника из этого измерения - Йерри."
            mc "Она была невероятно психически нестабильна и покончила с собой после угроз убийством."
            mc "Мне нужно знать, стоит ли нам беспокоиться."
            show yuri 2f
            y "[player], должно быть, я поражаю тебя своими эмоциями."
            "Юри стояла как картонная кукла."
            mc "Нет, прямо сейчас ты этого не делаешь."
            show yuri 2h
            y "Тогда у нас сейчас большие проблемы."
            mc "Доктор Баг сказала, что мы можем следовать за её генератором."
            show sayori 2k
            s "Нам лучше выдвигаться. Я соберу остальных."
            show yuri 1f
            y "Спасибо, что рассказали мне о Йерри."

    scene bg pripyat
    with dissolve_scene_full

    "Все собираются, выглядя несчастными."
    show natsuki 1f7 zorder 2 at t41
    show sayori 2k zorder 2 at t42
    show yuri 1w zorder 2 at t43
    show bhorde 35 zorder 1 at t44
    n "[player], ты как там, держишься?"
    mc "Теперь появился шанс догнать Монику Прайм, прежде чем она найдёт наш дом."
    n "Значит, не держишься..."
    n "Сайори?"
    "Сайори безутешно смотрит вдаль."
    show sayori 2v
    mc "Эй, Сайори, нам нужны твои глаза и уши больше, чем когда-либо."
    show sayori 2k
    s "П-простите, просто есть о чём задуматься."
    show natsuki at thide
    hide natsuki
    show sayori at thide
    hide sayori
    show yuri at thide
    hide yuri
    show bhorde at thide
    hide bhorde
    show mc2 1j zorder 2 at t41
    show yuri_prime 4b zorder 2 at t42
    show natsuki_prime 12f zorder 2 at t43
    show sayori_prime 1v zorder 1 at t44
    pmc "Мы всегда с вами, что бы ни случилось."
    show mc2 1e
    show sayori_prime 3i
    ps "И не волнуйтесь, когда мы догоним Монику, мы заставим её сожалеть."
    show mc2 at thide
    hide mc2
    show yuri_prime at thide
    hide yuri_prime
    show natsuki_prime at thide
    hide natsuki_prime
    show sayori_prime at thide
    hide sayori_prime
    show natsuki 1f7 zorder 2 at t41
    show sayori 2u zorder 2 at t42
    show yuri 1w zorder 2 at t43
    show bhorde 35 zorder 1 at t44
    s "Спасибо, ребята."
    show yuri 1h
    y "Все готовы к прыжку?"
    show bhorde 34
    bn "Гр-р!"
    show natsuki at thide
    hide natsuki
    show sayori at thide
    hide sayori
    show yuri at thide
    hide yuri
    show bhorde at thide
    hide bhorde
    show mc2 1e zorder 2 at t41
    show yuri_prime 4b zorder 2 at t42
    show natsuki_prime 12h zorder 2 at t43
    show sayori_prime 1v zorder 2 at t44
    pn "Это, кажется, переводится как \"да\"."
    show mc2 at thide
    hide mc2
    show yuri_prime at thide
    hide yuri_prime
    show natsuki_prime at thide
    hide natsuki_prime
    show sayori_prime at thide
    hide sayori_prime
    show natsuki 1f7 zorder 2 at t41
    show sayori 2k zorder 2 at t42
    show yuri 1f zorder 2 at t43
    show bhorde 35 zorder 1 at t44
    y "Тогда давайте найдём Монику Прайм."
    stop music fadeout 2.0
    "Юри активирует червоточину, и мы повторяем то, что начинает становиться рутиной."
    show natsuki at thide
    hide natsuki
    show sayori at thide
    hide sayori
    show yuri at thide
    hide yuri
    show bhorde at thide
    hide bhorde

    show wormhole movie
    play music wormhole
    "..."
    if dimensions_aroute == True:
        a "Как бы печально это ни было, здорово, что доктор Баг вернулась."
        a "Она лучшая для меня."
        amc "Ты осталась такой же, какой была минуту назад."
        a "Ну, она на самом деле только очень крошечная часть меня."
        a "Но тем не менее, именно по ней я и очень скучала."
        amc "Может быть попробуем использовать этот процесс для удаления частей, которые тебе не нравятся?"
        a "Наверное, да, но это не лучшая идея."
        a "Мы те, кто мы есть, из-за каждой части нас."
        a "Даже плохие черты играют свою роль."
    else:
        pm "Вот почему я не хочу винить себя за их действия."
        m "Другая я – это тот, кто нуждается в помощи."
        m "В этой Монике нет искры творчества или позитива."
        pm "Я всегда хотела научиться играть на фортепиано."
        m "Ты единственный, кто может исправить другую меня."
        m "Также, ананасы."
    scene bg blackbackground
    hide wormhole
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
