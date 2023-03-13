"""
Головний цикл гри "Блукачка по Львову"
"""

import game

kozelnytska = game.Street("Козельницька")
kozelnytska.set_description("Студмістечко.\nТут ви можете зустріти студентів\
 факультету прикладнх наук, які вмирають від дедлайнів і не мають сил \
з кимось боротися, окрім сну.\nЩоб піти далі Ви вказуєте напрямок, на зустрічі\
 з ворогом маєте можливість поговорити, боротися та взяти те, що знаходиться.")

stryiska = game.Street("Стрийська")
stryiska.set_description("Стрийська - найдовша львівська вулиця, але часто тут зустрінеш...")

naukova = game.Street("Наукова")
naukova.set_description("Наукова - отримала назву \
від науково-дослідних інститутів і ту можна побачити....")

vygovskoho = game.Street("Івана Виговського")
vygovskoho.set_description("Одна з найбільгих вулиць Залізничногго райнону і тут...")

horodotska = game.Street("Городоцька")
horodotska.set_description("Велика вулиця, яка бере початок у центрі, \
її протяжність 8,5 км, тут зустрінемоооо...")

kozelnytska.link_street(stryiska, "північ")
stryiska.link_street(naukova, "південь")
naukova.link_street(vygovskoho, "захід")
vygovskoho.link_street(horodotska, "схід")
horodotska.link_street(kozelnytska, 'північ')

lotr = game.Enemy("Лотр", "А це негідник, розбійник, грабіжник")
lotr.set_conversation("А куди це ми прямуємо, не поговоривши зі мною?")
lotr.set_weakness("прикраси та гроші")
stryiska.set_character(lotr)

batyar = game.Enemy("Батяр", "Гульвіса, п'яничка, брутальний чоловік")
batyar.set_conversation("Зупиняємось тут, перехожий!")
batyar.set_weakness("львівське пиво")
naukova.set_character(batyar)

zbuy = game.Enemy("Збуй", "Розбійник, грабіжник.")
zbuy.set_conversation("ОГО, хто це?!")
zbuy.set_weakness("дукати")
vygovskoho.set_character(zbuy)

laidak = game.Enemy("Лайдак", " Нероба, лінива людина.")
laidak.set_conversation("Стііііій?!")
laidak.set_weakness("булочка")
horodotska.set_character(laidak)

dukaty = game.Item("дукати")
dukaty.set_description("Нові грошики")
vygovskoho.set_item(dukaty)

roll = game.Item("булочка")
roll.set_description('Смачна булочка')
horodotska.set_item(roll)

accessories = game.Item("прикраси та гроші")
accessories.set_description("Дорогоцінні предмети, що приваблюють")
stryiska.set_item(accessories)

beer = game.Item("львівське пиво")
beer.set_description("Улюблене львівське пиво батярів")
naukova.set_item(beer)

current_room = kozelnytska
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["північ", "південь", "захід", "схід"]:
        current_room = current_room.move(command)
    elif command == "поговорити":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "боротися":
        if inhabitant is not None:
            print("Чим будете боротися?")
            fight_with = input()
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    print("Урааа, Ви виграли бійку!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Вітання, Ви перемогли ворога!")
                        dead = True
                else:
                    print("Не засмучуйтесь, Ви програли.")
                    print("Кінець гри")
                    dead = True
            else:
                print("Ви не маєте " + fight_with)
        else:
            print("Немає з ким битися")
    elif command == "взяти":
        if item is not None:
            print("Ви поклали " + item.get_name() + " у торбу")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("Нема що взяти!")
    else:
        print("Що робити з " + command + "?")
