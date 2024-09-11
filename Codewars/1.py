def get_sum(a,b):
    a, b = sorted([a, b])
    return sum(range(a, b + 1))

# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)




# def spin_words(sentence):
#     return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])
#
# print(spin_words('more is Kata more passed letter takes with the present reversed with and all all'))

# def domain_name(url):
#     return url.replace('http://', '').replace('www.', '').replace('https://', '').split('.')[0]
#
#
#
# print(domain_name('https://123'))
# from collections import Counter
#
#
# def duplicate_encode(word):
#     word = word.lower()
#     dict_word = Counter(word)
#     res = ['(' if dict_word[i] == 1 else ')' for i in word]
#     return ''.join(res)
#
# print(duplicate_encode("recede"))






# def make_readable(seconds):
#     min = seconds/(60 * 60)
#     sek = (seconds%(60 * 60)) * 100
#     return f'{min}--{sek} '
#
# print(make_readable(359999))