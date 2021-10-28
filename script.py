
a=int(input('Введите количество билетов:'))
L=input('Введите возраст')
age = L.split()
age_numbers = list(map(int, age))
print (age_numbers)
M=[]
for i in age_numbers:
    if i < 10:
        M.append(0)
    if 18 <= i < 25:
        M.append(990)
    else:
        M.append(1390)
print (M)
S=sum(M)
print ("Сумма заказа:", S)
