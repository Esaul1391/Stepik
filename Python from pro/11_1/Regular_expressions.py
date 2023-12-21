pattern_7 = r'7-\d{3}-\d{3}-\d{2}-\{d2}'
pattern_8 = r'8-\d{3}-\d{4}-\d{4}'
import re
def find_num(text):
    print(re.findall(pattern_8 | pattern_7, text))
    print(re.findall(pattern_7, text))
find_num('Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911')
