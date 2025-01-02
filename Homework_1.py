import pulp

# Створюємо модель
prob = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Змінні
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

water = 100
sugar = 50
lemon_juice = 30
fruit_puree = 40

# Обмеження ресурсів
prob += 2 * lemonade + 1 * fruit_juice <= water, "Water Constraint"
prob += 1 * lemonade <= sugar, "Sugar Constraint"
prob += 1 * lemonade <= lemon_juice, "Lemon Juice Constraint"
prob += 2 * fruit_juice <= fruit_puree, "Fruit Puree Constraint"

prob += lemonade + fruit_juice, "Total Production"

# Розв'язання моделі
prob.solve()

# Результати
print("Статус:", pulp.LpStatus[prob.status])
print("Кількість вироблених Лимонадів:", pulp.value(lemonade))
print("Кількість вироблених Фруктових соків:", pulp.value(fruit_juice))

