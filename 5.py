# 5. Сейчас нам нужно вывести наименование продукта только, если количество букв в
# нем четное.
# Пройдитесь циклом по списку и выведи название каждого такого продукта.

spisok_prod = ["apples", "bananas", "milk", "tea", "bread", "coffee"]
count = 0

for i in spisok_prod:
    if len(i) % 2 == 0:
        print(i)
        count += 1


print(f'У тебя {count} продуктов, где {count} — значение переменной count')