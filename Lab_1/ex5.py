"""
Задание 5.1
Условие:
В задании создан словарь, с информацией о разных устройствах.
Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1). 
И вывести информацию о соответствующем устройстве на стандартный поток вывода (информация будет в виде словаря).
Ограничение: нельзя изменять словарь london_co.
Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без использования условия if.
"""
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
device_name = input('Введите название устройства о котором необходимо вывести информацию (r1, r2, sw1)')
print(london_co.get(device_name, 'Указанное имя не верное, проверьте правильность введённой информации'))


"""
Задание 5.1a
Условие:
Переделать скрипт из задания 5.1 таким образом, чтобы, кроме имени устройства, запрашивался также параметр устройства, который нужно отобразить.
Вывести информацию о соответствующем параметре, указанного устройства.
"""
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
device_name = input('Введите название устройства о котором необходимо вывести информацию (r1, r2, sw1)')
device_atrib = input('Укажите параметр устройства, который хотите получить в отображении')
print(london_co[device_name][device_atrib])


"""
Задание 5.1b
Условие:
Переделать скрипт из задания 5.1a таким образом, чтобы, при запросе параметра, отображался список возможных параметров. Список параметров надо получить из словаря, 
а не прописывать вручную.
Вывести информацию о соответствующем параметре, указанного устройства.
"""
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
device_name = input('Введите название устройства о котором необходимо вывести информацию (r1, r2, sw1)')
device_atrib = input(london_co[device_name].keys())
print(london_co[device_name][device_atrib])


"""
Задание 5.1c
Условие:
Переделать скрипт из задания 5.1b таким образом, чтобы, при запросе параметра, которого нет в словаре устройства, отображалось сообщение „Такого параметра нет“.
Если выбран существующий параметр, вывести информацию о соответствующем параметре, указанного устройства.
""""
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
device_name = input('Введите название устройства о котором необходимо вывести информацию (r1, r2, sw1)')
device_atrib = input(london_co[device_name].keys())
print(london_co[device_name].get(device_atrib, 'Такого параметра нет'))

"""
Задание 5.1d
Условие:
Переделать скрипт из задания 5.1c таким образом, чтобы, при запросе параметра, пользователь мог вводить название параметра в любом регистре.
"""
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
device_name = input('Введите название устройства о котором необходимо вывести информацию (r1, r2, sw1)')
device_atrib = input(london_co[device_name].keys())
print(london_co[device_name].get(device_atrib.lower(), 'Такого параметра нет'))

"""
Задание 5.2
Условие:
Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
Затем вывести информацию о сети и маске в таком формате:
Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
"""
ip = input('Введите IP-сеть в форматие х.х.х.х/mask')
ip = ip.split('/')
network = ip[0].split('.')
mask = int(ip[1])
mask_str = str('1'*mask + (32-mask)*'0')

ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(int(network[0]), int(network[1]), int(network[2]), int(network[3])))

ip_template1 = '''
Mask:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template1.format(int(mask_str[:8], 2), int(mask_str[8:16], 2), int(mask_str[16:24], 2), int(mask_str[24:32], 2)))

"""
Задание 5.2a
Условие:
Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети, надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.
Пример адреса сети (все биты хостовой части равны нулю):
10.0.1.0/24
190.1.0.0/16
Пример адреса хоста:
10.0.1.1/24 - хост из сети 10.0.1.0/24
10.0.5.1/30 - хост из сети 10.0.5.0/30
"""
ip = input('Введите IP-сеть в форматие х.х.х.х/mask')
ip = ip.split('/')
network = ip[0].split('.')
mask = int(ip[1])
mask_str = str('1'*mask + (32-mask)*'0')

ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(int(network[0]), int(network[1]), int(network[2]), 0))

ip_template1 = '''
Mask:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template1.format(int(mask_str[:8], 2), int(mask_str[8:16], 2), int(mask_str[16:24], 2), int(mask_str[24:32], 2)))

#5.2b немного не понятно, получается что есть список из которого я беру элементы, а не прошу их инпутом. не вижу смысла делать тогда эту задачу.
# так как разница в коде минимальная, просто вместо переменной инпута буду запрашивать элемент из массива аргументов. 
"""
Задание 5.3
Условие:
Скрипт должен запрашивать у пользователя: информацию о режиме интерфейса (access/trunk)
номере интерфейса (тип и номер, вида Gi0/3)
номер VLANа (для режима trunk будет вводиться список VLANов)
В зависимости от выбранного режима, на стандартный поток вывода, должна возвращаться соответствующая конфигурация access или trunk 
(шаблоны команд находятся в списках access_template и trunk_template).
При этом, сначала должна идти строка interface и подставлен номер интерфейса, а затем соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).
"""
access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
work_mode = input('Введите режим работы интерфейса (access/trunk ):')
interface = input('Введите тип и номер интерфейса:')
vlans = input ('Введите vlans(s):')

config = [
['switchport mode access',
 'switchport access vlan {}',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable'],
['switchport trunk encapsulation dot1q',
 'switchport mode trunk',
 'switchport trunk allowed vlan {}']
]
work_mode = work_mode.count('trunk')
print('\n' * 2)
print('interface {}'.format(interface))
print('\n'.join(config[work_mode]).format(vlans))

#До этого я пытался полученный текст склеивать с строкой template и получать в итоге (текст пользователя)_template, а дальше к этой переменной обращаться через текст формат, 
#но возникли ошибки и не получилось так сделать, а через этот костыль получится что при любом неверном введенном параметре, он будет форматировать 0 элемент массива config
#тут или проверки прикрутить или ту идею с именем переменной разобрать.

"""
Задание 5.3a
Условие:
Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима, задавались разные вопросы в запросе о номере VLANа или списка VLANов:
для access: „Введите номер VLAN:“
для trunk: „Введите разрешенные VLANы:“
"""
access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
work_mode = input('Введите режим работы интерфейса (access/trunk ):')
interface = input('Введите тип и номер интерфейса:')
work_mode = work_mode.count('trunk')
modes = [
['Введите VLAN:'],
['Введите VLANs:']
]

vlans = input (' '.join(modes[mode]))

config = [
['switchport mode access',
 'switchport access vlan {}',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable'],
['switchport trunk encapsulation dot1q',
 'switchport mode trunk',
 'switchport trunk allowed vlan {}']
]

print('\n' * 2)
print('interface {}'.format(interface))
print('\n'.join(config[work_mode]).format(vlans))