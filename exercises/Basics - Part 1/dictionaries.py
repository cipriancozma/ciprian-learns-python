# Dictionary
dictionary = {
    'a': 1,
    'b': 2
}

print(dictionary['a'])

dictionary_1 = {
    'weapons': [1, 2, 3],
    'greeting': 'hello',
    'is_Magic': True
}

print(type(dictionary_1))

print(dictionary_1.get('greeting', 'hi'))

print('weapons' in dictionary_1)

print('is_Magic' in dictionary_1.keys())

print(dictionary_1.popitem())

print(dictionary_1.update({'is_Magic': False}))

print(dictionary_1)
