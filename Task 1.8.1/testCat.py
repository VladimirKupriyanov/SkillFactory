from cat import Cat

cat1 = Cat("Барон", "мальчик", 2)
cat2 = Cat("Сэм", "мальчик", 2)

print(f"Имя: {cat1.get_name()}, Пол: {cat1.get_gender()}, Возраст: {cat1.get_age()}")
print(f"Имя: {cat2.get_name()}, Пол: {cat2.get_gender()}, Возраст: {cat2.get_age()}")
