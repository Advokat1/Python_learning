"""
Задание 7.1
Условие:
Аналогично заданию 4.6 обработать строки из файла ospf.txt и вывести информацию по каждой в таком виде:
"""
with open('ospf.txt', 'r') as text:
    file = text.readlines()
    for lines in file:
        lines = lines.strip().split()
        protocol = lines[0].replace('O', 'OSPF')
        prefix = lines[1]
        ad = lines[2].strip('[]')
        hop = lines[4].strip(',')
        update = lines[5].strip(',')
        interface = lines[6]
        ospf_route = """
        Protocol:             {0:10}
        Prefix:               {1:10}
        AD/Metric:            {2:10}
        Next-Hop:             {3:10}
        Last update:          {4:10}
        Outbound Interface:   {5:10}
        """
        print(ospf_route.format(protocol,prefix,ad,hop,update,interface))

"""
Задание 7.2
Условие:
Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
имя файла передается как аргумент скрипту.
Скрипт должен возвращать на стандартный поток вывода команды из переданного конфигурационного файла, исключая строки, которые начинаются с !.
Между строками не должно быть дополнительного символа перевода строки.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from sys import argv
name = argv[1:]
name = ''.join(name)
with open(name, 'r') as file:
    for lines in file:
        #проверка на наличие в строке ! для её игнорирования
        if lines.count('!') < 1:
            print(lines.strip('\n'))
"""
Задание 7.2a
Условие:
Сделать копию скрипта задания 7.2.
Дополнить скрипт: Скрипт не должен выводить команды, в которых содержатся слова, которые указаны в списке ignore.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ignore = ['!','duplex', 'alias', 'Current configuration']
with open('config_sw1.txt', 'r') as file:
    for lines in file:
        if lines.find(ignore[0]) == -1 and lines.find(ignore[1]) == -1 and lines.find(ignore[2]) == -1 and lines.find(ignore[3]) == -1:
            print(lines.strip('\n'))

"""
Задание 7.2b
Условие:
Дополнить скрипт из задания 7.2a: вместо вывода на стандартный поток вывода, скрипт должен записать полученные строки в файл config_sw1_cleared.txt
При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore. Строки, которые начинаются на ! отфильтровывать не нужно.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ignore = ['!','duplex', 'alias', 'Current configuration']
with open('config_sw1.txt', 'r') as file, open('config_sw1_cleared.txt', 'w') as text:
    for lines in file:
        if lines.find(ignore[1]) == -1 and lines.find(ignore[2]) == -1 and lines.find(ignore[3]) == -1:
            text.write(lines)

"""
Задание 7.2c
Условие:
Переделать скрипт из задания 7.2b: передавать как аргументы скрипту:
1)имя исходного файла конфигурации
2)имя итогового файла конфигурации
Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации, в которых содержатся слова из списка ignore. И записать остальные строки в итоговый файл.
Проверить работу скрипта на примере файла config_sw1.txt.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from sys import argv
names = argv[1:]
name_first = names[0]
name_second = names[1]
ignore = ['!','duplex', 'alias', 'Current configuration']
with open(name_first, 'r') as file, open(name_second, 'w') as text:
    for lines in file:
        if lines.find(ignore[1]) == -1 and lines.find(ignore[2]) == -1 and lines.find(ignore[3]) == -1:
            text.write(lines)

"""
Задание 7.3
Условие:
Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка, где есть MAC-адрес, должна быть обработана 
таким образом, чтобы на стандартный поток вывода была выведена таблица вида (показаны не все строки из файла):
"""
with open('CAM_table.txt', 'r') as file:
    for line in file:
        if line.count('.') == 2:
            str = line.strip('\n').split()
            print (str[0] + '@@@' + str[1] + '@@@' + str[3])

"""
Задание 7.3a
Условие:
Сделать копию скрипта задания 7.3.
Дополнить скрипт: Отсортировать вывод по номеру VLAN.
В результате должен получиться такой вывод:
"""
arr = []
with open('CAM_table.txt', 'r') as file:
    for line in file:
        if line.count('.') == 2:
            str = line.strip('\n').split()
            arr.append(str)
    arr.sort()
    for item in arr:
        print (item)

"""
Задание 7.3b
Условие:
Сделать копию скрипта задания 7.3a.
Дополнить скрипт:
Запросить у пользователя ввод номера VLAN.
Выводить информацию только по указанному VLAN.
"""
arr = []
vlan = input('Введите искомый Vlan')
with open('CAM_table.txt', 'r') as file:
    for line in file:
        if line.count('.') == 2:
            str = line.strip('\n').split()
            arr.append(str)
    arr.sort()
    for item in arr:
        if item[0] == vlan:
            print (item)
