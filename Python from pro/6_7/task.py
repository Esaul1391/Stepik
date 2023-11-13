# data = 'mississippi'
# counter = {}
#
# for letter in data:
#      if letter not in counter:
#          counter[letter] = 0
#      counter[letter] += 1
#
# print(counter)
# from collections import Counter
#
# Counter('Sandy Cheeks')
# Counter('Sandy Cheeks'.split())
# Counter(Sandy=1.5, Cheeks=-3)
# Counter()
# Counter({'S': 1, 'a': 5, 'n': 3, 'd': 9, 'y': 7})
# Counter(Sandy='2', Cheeks='4')
# Counter({'S': '1', 'a': '5', 'n': '3', 'd': '9', 'y': '7'})
# Counter.fromkeys('Sandy', 1)


# from collections import Counter
#
# counter = Counter.fromkeys('abcd', 1)
#
# print(*counter.keys(), sum(counter.values()))

# from collections import Counter
#
# counter = Counter({1: 11, 2: 22, 3: 33})
#
# print(max(counter.keys()) + min(counter.values()))

# from collections import Counter
#
# pets = Counter(cat=3, dog=3, fox=2, hamster=1)
#
# print(pets['elephant'])
# print(*pets)


# from collections import Counter
#
# letters = Counter(set('Beautiful is better than ugly'))
#
# print(set('Beautiful is better than ugly'))

#
# from collections import Counter
#
# vegetables = Counter({'cabbage': 10, 'pepper': 7, 'pumpkin': 4})
#
# vegetables.update(['pepper', 'pepper', 'pepper'])
#
# print(vegetables['pepper'])


# from collections import Counter
#
# vegetables1 = Counter({'cabbage': 'ten', 'pepper': 'seven', 'pumpkin': 'four'})
# vegetables2 = Counter({'cabbage': 3, 'pepper': 2})
#
# vegetables1.update(vegetables2)
#
# print(vegetables1['pepper'])


# from collections import Counter
#
# vegetables = Counter({'cabbage': 10, 'pepper': 'seven', 'pumpkin': 'four'})
#
# vegetables.update({'cabbage': 5, 'pepper': 'two'})
#
# print(vegetables['pepper'])
# print(vegetables['cabbage'])

# from collections import Counter
#
# clothes = Counter([('shirt', 3), ('dress', 1), ('shirt', 3)])
#
# print(clothes[('shirt', 3)])


# from collections import Counter
#
# files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
#          'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
#          'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
#          'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
#          'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
#          'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
#          'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
#          'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
#          'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
#          'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
#          'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
#          'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
#          'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
# new_files = []
# for i in files:
#     i = i.split('.')
#     new_files.append(i[1])
# data = Counter(new_files)
# for i in sorted(data):
#     print(f"{i}: {data[i]}")

# from collections import Counter
# def count_occurences(word, words):
#     words = words.lower().split(' ')
#     data = Counter(words)
#     if word.lower() in words:
#         return data[word.lower()]
#     else:
#         return 0
#
#
#
# word = 'Java'
# words = 'Python C++ C# JavaScript Go Assembler'
#
# print(count_occurences(word, words))


# from collections import Counter
#
# produckt = Counter(input().split(','))
# produckt = sorted(produckt.items())
# print(type(produckt))
# print(produckt)
# for i in produckt:
#     print(f'{i[0]}: {i[1]}')




from collections import defaultdict

def calculate_cost(products):
    product_counts = defaultdict(int)
    product_prices = {}

    # Считаем количество каждого товара
    for product in products:
        product_counts[product] += 1

    # Заполняем цены для каждого товара (сумма Unicode кодов)
    for product in sorted(product_counts.keys()):
        unicode_sum = sum(ord(char) for char in product)
        product_prices[product] = unicode_sum
    sort_pr = dict(sorted(product_counts.items(), key=lambda item: item[1]))
    # Выводим результат
    for product, count in sort_pr.items():
        cost_per_unit = product_prices[product]
        total_cost = cost_per_unit * count
        print(f"{product}: {cost_per_unit} UC x {count} = {total_cost} UC")

# Считываем входные данные и вызываем функцию
input_products = input().split(',')
calculate_cost(input_products)