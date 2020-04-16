"""
Задание 6.1
Условие:
Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX. Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.
Создать скрипт, который преобразует MAC-адреса в формат cisco и добавляет их в новый список mac_cisco
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
macs = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
new_macs = []
for mac in macs:
    new_macs.append(mac.replace(':','.'))
print(new_macs)

"""
Задание 6.2
Условие:
1)Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2)Определить тип IP-адреса.
3)В зависимости от типа адреса, вывести на стандартный поток вывода:
„unicast“ - если первый байт в диапазоне 1-223
„multicast“ - если первый байт в диапазоне 224-239
„local broadcast“ - если IP-адрес равен 255.255.255.255
„unassigned“ - если IP-адрес равен 0.0.0.0
„unused“ - во всех остальных случаях
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите ip адресс в формате x.x.x.x')
ip_arr = ip.split('.')
unicast = list(range(1, 224))
multicast = list(range(224, 240))
broadcast = '255.255.255.255'
unassigned = '0.0.0.0'
if  ip == broadcast:
    print("local broadcast")
elif ip == unassigned:
    print("unassigned")
elif int(ip_arr[0]) in unicast:
    print("unicast")
elif int(ip_arr[0]) in multicast:
    print("multicast")
else:
    print("unused")

"""
Задание 6.2a
Условие:
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
состоит из 4 чисел разделенных точкой,
каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение: „Неправильный IP-адрес“
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
count = 0
help_list = list(range(0, 256))
ip = input('Введите ip адресс в формате x.x.x.x')
ip_arr = ip.split('.')
if len(ip_arr) == 4:
    for item in ip_arr:
        if int(item) in help_list:
            count+=1
            print(count)
elif count == 4:
    unicast = list(range(1, 224))
    multicast = list(range(224, 240))
    broadcast = '255.255.255.255'
    unassigned = '0.0.0.0'
    if  ip == broadcast:
        print("local broadcast")
    elif ip == unassigned:
        print("unassigned")
    elif int(ip_arr[0]) in unicast:
        print("unicast")
    elif int(ip_arr[0]) in multicast:
        print("multicast")
    else:
        print("unused")
else:
    print("Не верно введенный ip")

"""
Задание 6.2a
Условие:
Сделать копию скрипта задания 6.2a.
Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
flag = 1
while bool(flag):
    count = 0
    help_list = list(range(0, 256))
    ip = input('Введите ip адресс в формате x.x.x.x')
    ip_arr = ip.split('.')
    if len(ip_arr) == 4:
        for item in ip_arr:
            if int(item) in help_list:
                count+=1
                print(count)
    if count == 4:
        flag-=1 
        unicast = list(range(1, 224))
        multicast = list(range(224, 240))
        broadcast = '255.255.255.255'
        unassigned = '0.0.0.0'
        if  ip == broadcast:
            print("local broadcast")
        elif ip == unassigned:
            print("unassigned")
        elif int(ip_arr[0]) in unicast:
            print("unicast")
        elif int(ip_arr[0]) in multicast:
            print("multicast")
        else:
            print("unused")
        continue
    else:
        print("Не верно введенный ip")

"""
Задание 6.3
Условие:
В скрипте сделан генератор конфигурации для access-портов.
Сделать аналогичный генератор конфигурации для портов trunk.
В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать, что с ним делать.
Поэтому в соответствии каждому порту стоит список и первый (нулевой) элемент списка указывает как воспринимать номера VLAN, которые идут дальше:
add - VLANы надо будет добавить (команда switchport trunk allowed vlan add 10,20)
del - VLANы надо удалить из списка разрешенных (команда switchport trunk allowed vlan remove 17)
only - на интерфейсе должны остаться разрешенными только указанные VLANы (команда switchport trunk allowed vlan 11,30)
Задача для портов 0/1, 0/2, 0/4:
сгенерировать конфигурацию на основе шаблона trunk_template
с учетом ключевых слов add, del, only
Код не должен привязываться к конкретным номерам портов. То есть, если в словаре trunk будут другие номера интерфейсов, код должен работать.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

access_template = ['switchport mode access',
'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }

for intf, vlan in fast_int['trunk'].items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if vlan[0] is 'add':
                print(' {} add {}'.format(command, ','.join(vlan[1:])))
            elif vlan[0] is 'only':
                print(' {} {}'.format(command, ','.join(vlan[1:])))
            elif vlan[0] is 'del':
                print(' {} remove {}'.format(command, ','.join(vlan[1:])))
        else:
            print(' {}'.format(command))