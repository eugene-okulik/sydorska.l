my_dict = {
    'tuple': (1, 'one', 2, 'two', False),
    'list': ['Life', 37, 'happy', 3.14, 5],
    'dict': {
        'name': 'Ton',
        'last_name': 'Cruz',
        'age': '47',
        'contry': 'USA',
        'status': 'active'
    },
    'set': {6, 7, None, 'text', False}
}
print(my_dict['tuple'][-1])
my_dict['list'].append('add new item to the end')
my_dict['list'].pop(1)
my_dict['dict'].update({('i am a tuple',): ('blabla')})
my_dict['dict'].pop('status')
my_dict['set'].add('hello')
my_dict['set'].remove(None)
print(my_dict)
