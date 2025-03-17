# Определение персонажей игры.
define dar = Character('Дарио', color="#c8ffc8")  # Бывший Кирилл
define luc = Character('Люциан', color="#c8fac8")  # Бывший Сергей
define cas = Character('Кассий', color="#c8e8c8")  # Бывший Дима
define elias = Character('Элиас', color="#c8d8c8")   # Бывший Андрей
define ser = Character('Серафима', color="#c8c8ff")  # Бывшая Юля
define air = Character('Айрин', color="#c8c8fa")    # Бывшая Вика Е
define lucin = Character('Люцинда', color="#c8c8e8")  # Бывшая Вика Г
define tae = Character('Таэлия', color="#c8c8d8")   # Бывшая Маша И
define elinor = Character('Элинор', color="#c8c8c8")   # Бывшая Маша Т
define dra = Character('Дракон', color="#ffc8c8")   # Бывший Рома
define orl = Character('Орландо', color="#fac8c8")  # Бывший Влад
define mir = Character('Миранда', color="#e8c8c8")  # Бывшая Таня
define lea = Character('Леандр', color="#d8c8c8")   # Бывший Саша

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init:
    # logo_episodes
    image bg LS_episode0 = im.Scale("images/logo_scenes/01_prolog.jpg", 1920, 1080)
    image bg LS_episode1 = im.Scale("images/logo_scenes/02_episode_1.jpg", 1920, 1080)
    
    # legend
    image bg l_black_town = im.Scale("images/legend/black_town.png", 1920, 1080)
    image bg l_orden_on_table = im.Scale("/images/legend/orden_on_table.jpg", 1920, 1080)
    image bg l_people_and_cards = im.Scale("images/legend/people_and_cards.jpg", 1920, 1080)
    image bg l_cards_and_roles = im.Scale("images/legend/cards_and_roles.jpg", 1920, 1080)
    image bg l_old_house = im.Scale("images/legend/old_house.jpg", 1920, 1080)
    image bg l_empty_city = im.Scale("images/legend/empty_city.jpg", 1920, 1080)
    image bg l_cards_in_hands = im.Scale("/images/episode_01/cards.png", 1920, 1080)
    image bg l_empty_streets_dusk = im.Scale("/images/legend/empty_streets_dusk.jpg", 1920, 1080)
    image bg l_final_scene = im.Scale("/images/legend/final_scene.jpg", 1920, 1080)
    image bg l_final_cards = im.Scale("/images/legend/final_card.jpg", 1920, 1080)

    # episode 1
    image bg house_dar_inside = im.Scale("images/house_dar_inside.png", 1920, 1080)
    image bg house_dar_outside = im.Scale("images/house_dar_outside.png", 1920, 1080)
    image bg workout_park = im.Scale("images/workout_park.png", 1920, 1080)
    image bg gym_1 = im.Scale("images/gym_1.jpg", 1920, 1080)
    image bg gym_2 = im.Scale("images/gym_2.jpg", 1920, 1080)
    image black = Solid("#000000")

# Игра начинается здесь:
label start:
    
    jump start_ep_0

# переходы между эпизодами

label start_ep_0:
    stop music fadeout 1

    "Разработчик Kikuzawa"

    play music "splash_episode.mp3"

    scene bg LS_episode0 with dissolve
    
    pause 5.0

    stop music fadeout 5.0

    scene black with dissolve
    
    pause 1.5

    jump legend_prologue


label ep0_ep1:

    play music "splash_episode.mp3"

    scene bg LS_episode1 with dissolve
    
    pause 5.0

    stop music fadeout 5.0

    scene black with dissolve

    pause 1.5

    jump episode_1_scene_1