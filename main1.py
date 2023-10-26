# Запрашиваем первоначальную цену товара
initial_price = int(input("Введите цену товара: "))

# Запрашиваем размер скидки в процентах
discount_percentage = int(input("Введите процент скидки: "))

# Рассчитываем стоимость товара с учетом скидки
discounted_price = initial_price - (initial_price * discount_percentage // 100)

# Выводим стоимость товара с учетом скидки
print(discounted_price)




# цену товара: 2200
#Введите процент скидки: 15
#1870