salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Функция для расчета необходимой финансовой подушки безопасности
def calculate_safety_capital(salary:int, spend:int, increase:float, months:int):
    current_spend = spend
    money_capital = 0  # Капитал

    for month in range(months):
        deficit = max(0, current_spend - salary)  # Нехватка средств после зарплаты
        money_capital += deficit  # Добавляем нехватку в общий дефицит
        current_spend *= (1 + increase)  # Увеличиваем расходы на следующий месяц

    return round(money_capital)

# Рассчитываем необходимую подушку безопасности
required_money_capital = calculate_safety_capital(salary, spend, increase, months)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_money_capital, end="\n")
