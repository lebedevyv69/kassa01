bilet = int(input("Количество человек: "))
price = []
for i in range(1, bilet+1):
    age=(int(input (f"Возраст участника номер {i}?")))
    if age < 18:
        price.append(0)
    elif 18 <= age <= 25:
        price.append(990)
    else:
        price.append(1390)
if bilet>3:
    a=int(sum(price)*0.9)
else:
    a=sum(price)
print('Сумма покупки =', a)
