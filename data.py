import json
with open('data/quiz_data.json', 'r', encoding='utf-8') as file:
    quiz_data = json.load(file)
"""quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {
        'question': 'Чем завершается оператор if',
        'options': ['for', 'while', 'elif', 'else'],
        'correct_option': 3
    },
    {
        'question': 'Какой знак используется для возведения в степень?',
        'options': ['+', '-', '*', '**'],
        'correct_option': 3
    },
    {
        'question': 'Сколько основных циклов в языке Python?',
        'options': ['1', '2', '3', '4'],
        'correct_option': 1
    },
    {
        'question': 'Как называется оператор функции?',
        'options': ['set', 'a', 'def', 'str'],
        'correct_option': 2
    },
    {
        'question': 'Какой тип данных имеет следующие скобки []',
        'options': ['dict', 'list', 'str', 'set'],
        'correct_option': 1
    },
    {
        'question': 'Что такое NumPy',
        'options': ['функция', 'библиотека', 'переменная', 'константа'],
        'correct_option': 1
    },
        {
        'question': 'каким методом можно добавить значение переменной в кавычки не закрывая их?',
        'options': ['f', 'q', 'w', 'z'],
        'correct_option': 0
    },
        {
        'question': 'какое значение переменной будет в  z = 3**2',
        'options': ['27', '0', '9', '6'],
        'correct_option': 2
    }
]
"""