"""
Задание №4.1
Условие: Обработать строку NAT таким образом, чтобы в имени интерфеса вместо FastEthernet было GigabitEthernet
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
"""
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(NAT)
newNAT = NAT.replace('Fast','Gigabit')
print(newNAT)

"""
Задание №4.2
Уловие: Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX:XXXX:XXXX:XXXX:XXXX:XXXX
mac = 'AAAA:BBBB:CCCC'
P.S Знаю, что костыльно, просто первое что пришло в голову, даже нет идей как это сдалть по нормальному
"""
mac = 'AAAA:BBBB:CCCC'
new_mac = str(int(mac[:2], 16)) + '.' + str(int(mac[2:4], 16)) + '.' + str(int(mac[5:7], 16)) + '.' + str(int(mac[7:9], 16))+ '.' + str(int(mac[10:12], 16)) + '.' + str(int(mac[12:], 16))
print(new_mac)
"""
Задание 4.3
Условие: Получить из строки config список VLANов вида:[''1', '3', '10', '20', '30', '100']
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
"""
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
config_list = config.split()
vlans = config_list[-1].split(',')
print(vlans)

"""
Задание 4.4
Условие: Список vlans это список VLANов, собранных со всех устройств сети, поэтому в списке есть повторяющиеся номера VLAN.
Из списка нужно получить уникальный список VLANов, отсортированный по возрастанию номеров.
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
"""
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
new_vlans = list(set(vlans))
new_vlans.sort()
print(new_vlans)

"""
Задание 4.5
Условие: 
Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']
command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
"""
command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
vlan1 = command1.split()
vlan2 = command2.split()
vlan1 = vlan1[-1].split(',')
vlan2 = vlan2[-1].split(',')
vlan1 = set(vlan1)
vlan2 = set(vlan2)
vlan = vlan1 & vlan2
print(sorted(vlan))

"""
Задание 4.6
Условие: Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:               OSPF
Prefix:                 10.0.24.0/24
AD/Metric:              110/41
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0
"""
ospf_route = 'OSPF 10.0.24.0/24 [110/41] via 10.0.13.3 3d18h FastEthernet0/0'

# Тут форматирование через F строки подойдет, я понял как подставлять значения, а вот как их вывести таблицей что-то не получилось, доделаю позже как разберусь

"""
Задание 4.7
Условие: 
Преобразовать MAC-адрес mac в двоичную строку такого вида:
101010101010101010111011101110111100110011001100

mac = 'AAAA:BBBB:CCCC'
"""
mac = 'AAAA:BBBB:CCCC'
mac = mac.replace(':', "")
a = bin(int(mac, 16))
print (a[2:])

"""
Задание 4.8
Условие: 
Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
первой строкой должны идти десятичные значения байтов
второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:

столбцами
ширина столбца 10 символов
Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001
"""
# Опять эти F строки, ладно сделаю

ip = '192.168.3.1'
ip = ip.split('.')

ip_template = '''
IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))
