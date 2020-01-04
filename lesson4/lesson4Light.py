from random import choices


def choice_name(names, len_list):
    return choices(names, k=len_list)


def most_frequent(names):
        word = {}
        for name in names:
            word[name] = word.get(name, 0) + 1
        word = list(word.items())
        word.sort(key=lambda x: x[1], reverse=True)
        return word[0][0]


def less_letters(names):
    """
    Раз у меня имена начинаются на одну букву, находит самую редкую букву в списке
    :param names: список имен
    :return: символ реже всего встречающийся в списке
    """
    letters = {}
    for name in names:
        for char in name:
            letters[char] = letters.get(char, 0) + 1
    letters = sorted(list(letters.items()), key=lambda x: x[1])
    return letters[0][0]


source = choice_name(['Абрам', 'Аваз', 'Аввакум', 'Август', 'Августин', 'Авдей', 'Авраам', 'Автандил',
                      'Агап', 'Агафон', 'Аггей', 'Адам', 'Адис', 'Адольф', 'Адриан'], len_list=100)
print(source)
print(most_frequent(source))
print(less_letters(source))
