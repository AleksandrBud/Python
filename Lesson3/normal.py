# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.
def write_file(inf):
    file = open('salary.txt', 'w')
    for key, value in inf.items():
        if value < 500000:
            file.write('{} - {}\n'.format(key, value))
    file.close()
    file = open('salary.txt', 'r')
    for line in file:
        t_name, t_zp = line.split(' - ')
        print('{} - {}'.format(str(t_name).upper(),round(int(t_zp)*0.87,2)))
    file.close()

names = ['Вася', 'Антон', 'Иван', 'Александр']
zp = [15645, 21457, 12587, 600567]

write_file(dict(zip(names, zp)))
#print(persons)
#      if map(lambda val: val < 500000, inf.values()):
#         print(inf.values())
# for val in inf.values():
#     print(val)