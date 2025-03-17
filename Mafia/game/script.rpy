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
    image bg house_dar_inside = im.Scale("images/house_dar_inside.png", 1920, 1080)
    image bg house_dar_outside = im.Scale("images/house_dar_outside.png", 1920, 1080)

    

# Игра начинается здесь:
label start:
    
    jump begin_story #story/episode_0