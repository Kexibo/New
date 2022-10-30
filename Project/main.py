import analyzer
print('Введите Помощь, чтобы вам помогли')
wwod=input('Введите свои хотелки: ')
while wwod!='off':
    analyzer.main(wwod)
    wwod=input('Введите свои хотелки: ')