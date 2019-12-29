import pymorphy2


result = {}
morph = pymorphy2.MorphAnalyzer()
with open(file='text.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        for word in line.split():
            word = word.lower()
            if word == '—':
                continue
            word = ''.join(char for char in word if char.isalpha())
            p = morph.parse(word)[0]
            if word in result:
                result[word]['count'] += 1
            else:
                result[word] = {'count': 1, 'normal_form': p.normal_form}
tuple_res = list(result.items())
tuple_res.sort(key=lambda x: x[1]['count'], reverse=True)
for i in range(5):
    print(tuple_res[i])
print(len(result))
