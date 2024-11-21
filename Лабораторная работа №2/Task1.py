money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 1.05  # Ежемесячный рост цен
month = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital > (spend-salary): # пока хватает капитала с учетом зп
    money_capital += salary # зп
    money_capital -= spend # расходы
    spend *= increase # ежемесячный рост цен
    month += 1 # счетчик месяцев
print("Количество месяцев, которое можно протянуть без долгов:", month, end="\n")

