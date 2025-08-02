from bdb import effective

money = int(input())
#Количество денег у игрока.
price_1 = int(input())
heal_1 = 5
# Цена первого зелья, которое восстанавливает 5 очков здоровья.
price_2 = int(input())
heal_2 = 10
# Цена второго зелья, которое восстанавливает 10 очков здоровья.
price_3 = int(input())
heal_3 = 15
#Цена третьего зелья, которое восстанавливает 15 очко   в здоровья.
sold_1, sold_2, sold_3 = heal_1/price_1, heal_2/price_2, heal_3/price_3
sold_1, sold_2, sold_3 = round(sold_1,2), round(sold_2,2), round(sold_3,2)
print(f'Вы можете купить {money//price_1} единиц первого зелья, {money//price_2} - второго зелья, {money//price_3} - третьего зелья.')
print(f'Эффективность первого зелья - {sold_1}, второго - {sold_2}, третьего - {sold_3}.')
print(f'Лучшая эффективность - {max(sold_1,sold_2,sold_3)}.')