ticket = int(input('Введите количество билетов, которые желаете приобрести'))
price = 0
for i in range (ticket):
    i += 1
    while True:
        age = input(f'возраст посетителя №{i}?')
        age = int(age)
        if age < 18:
            price += 0
            print('проходит на конференцию бесплатно')
        elif 18 <= age <= 25:
            price += 990
            print('стоимость 990 руб.')
        else:
            price += 1390
            print('полная стоимость 1390 руб.')
        if type (age) == int:
            break
if ticket > 3:
    price = price - price * 0.10
    print('Сумма к оплате =', price, 'руб.')
else:
    print('Сумма к оплате = ', price, 'руб.')

