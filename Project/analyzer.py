import random
import webbrowser
def main(reg):
    if reg.find('писан')>=0:
        schedual()
    elif reg.find('ена')>=0:
        price()
    elif reg.find('онтак')>=0:
        contact()
    elif reg.find('дар')>=0:
        gift()
    elif reg.find('абот')>=0:
        job()
    elif reg.find('щь')>=0:
        Alarmhelp()
    else:
        print('Попробуйте ввести запрос более корректно')

def schedual():
    print(f'Понедельник - {random.randint(1,10000)} часов питона')
    print(f'Вторник - ')
    print(f'Среда - ')
    print(f'Четверг - ')
    print(f'Пятница - ')
    print(f'Суббота - ')
    print(f'Воскресенье - ')


def price():
    print("Что бы вы хотели купить из цветов, конфет и кукурузы")
    x=input('Какой товар: ')
    if x.find('еты'):
        print('Цена на цветы 2000 рублей')
    elif x.find('нфет'):
        print('Цена на конфеты 150 рублей')
    elif x.find('укуруз'):
        print('Цена за кукурузу 170 рублей/килограмм')

def contact():
    print('Наши контакты:')
    print('Телефон: +79603578833')
    print('Telegrem: @Susanna33')


def gift():
    if random.randint(-1,1) > 0:
        print('Держи котика!')
        print('╭━╮┈╭━╮┈┈┈┈┈╭━╮\n ┃╭╯┈┃┊┗━━━━━┛┊┃\n┃╰┳┳┫┏━▅╮┊╭━▅┓┃\n┃┫┫┫┫┃┊▉┃┊┃┊▉┃┃\n┃┫┫┫╋╰━━┛▅┗━━╯╋\n┃┫┫┫╋┊┊┊┣┻┫┊┊┊╋\n┃┊┊┊╰┈┈┈┈┈┈┈┳━╯\n┃┣┳┳━━┫┣━━┳╭╯')
    elif random.randint(-1,1) > 0:
        print('Держи собачку!')
        print('┈┈╱▔▔▔╲┈┈┈┈┈\n▇▔┈▍▍┃┈┃╭━╮┈\n╲━╯┈┈┃┈┃╰╮┃┈\n┈▔▔┃┈╰━╯╲┃┃┈\n┈┈┈┃┃┃┈┈▕┃┃┈\n┈┈┈┃┃┃╭┛▕╯┃┈\n┈┈┈┗┻┛┗━╯━╯┈')
    elif random.randint(-1,1) == 0:
        print('Держи ЛЕГЕНДАРНОГО ДРАКОНА!!!')
        webbrowser.open(r'pic.jpg')
    else: print('Прости сегодня без подарка(')

def job():
    X=input('Кем бы вы хотите работать: ')
    if random.randint(1,3)==1:
        print('Uhodi')
    elif random.randint(1,3)==2:
        print('Будешь работать уборщиком')
    elif random.randint(1,3)==3:
        print('Ну, будешь фермером')


def Alarmhelp():
    print('Расписание - посмотреть расписание')
    print('Цена - узнать цену товара')
    print('Контакты - наши контакты')
    print('Подарки - получить милый подарочек')
    print('Работа - найти работу')
    print('Помощь - тем кому очень сложно')
