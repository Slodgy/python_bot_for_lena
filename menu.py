import  datetime

def count_days_from_meeting():
    first_day = datetime.datetime(2017, 6, 2, 17)
    today = datetime.datetime.now()
    delta = today - first_day
    return(delta.days)


def count_days_from_offer():
    first_day = datetime.datetime(2017, 6, 25, 17)
    today = datetime.datetime.now()
    delta = today - first_day
    return(delta.days)

reasons = (
    "ты самая красивая!",
    "ты самая понимающая!",
    "ты самая храбрая!",
    "без тебя я просто не могу!",
    "ты моя вторая половинка!",
    "когда ты рядом, любые невзгоды нам нипочём!",
    "список твоих достоинств можно продолжать бесконечно!",
    "рядом с тобой я чувствую себя настоящим мужчиной!",
    "твой милоте нет предела!",
    "ты невероятно коммуникабельная милашка!",
    "мы созданы друг для друга!",
    "ты девушка моей мечты!",
    "ты самая сильная!",
    "вместе мы сможем всё, что только захотим!",
    "я хочу окружить тебя любовью и заботой!",
    "ты даёшь мне столько сил!",
    "рядом с тобой я забываю о всех невзгодах!",
    "с тобой я по-настоящему счастлив!"
)


names = (
    "котёнок",
    "зайка",
    "крошка",
    "ляпка",
    "лапуля",
    "золотце",
    "котик",
    "сладенькая моя",
    "мой котёночек",
    "моя родная",
    "принцесса",
    "пинцесса",
    "моя девочка",
    "золотце",
    "заенька",
    "зайчонок"
)

numbers = {
     1:"день",
     2:"дня",
     3:"дня",
     4:"дня",
     0:"дней",
     5:"дней",
     6:"дней",
     7:"дней",
     8:"дней",
     9:"дней"
 }
