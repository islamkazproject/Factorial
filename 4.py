# 4. Теперь нужно поочередно вывести каждое наименование продукта.
# Пройдитесь циклом по списку и выведи название каждого продукта.

spisok_prod = ["apples", "bananas", "milk", "tea", "bread"]
count = 0

for i in spisok_prod:
    print(i)
    count += 1

print(f"У тебя {count} продуктов, где {count} — значение переменной count")
