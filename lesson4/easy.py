# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
main_list = [random.randint(-100, 100)**2 for k in range(random.randrange(10))]
print(main_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
list_1 = ['Яблоко', 'апельсин', 'банан', 'киви']
list_2 = ['Яблоко', 'гурша', 'апельсин']
list_3 = [fruit for fruit in list_1 if fruit in list_2]
print(list_3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
main_list = [random.randint(-100, 100) for k in range(random.randrange(20))]
result_list = [val for val in main_list if (val % 3 == 0) & (val > 0) & (val % 4 != 0)]
print(main_list)
print(result_list)
