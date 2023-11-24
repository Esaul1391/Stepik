# from collections import Counter
#
# witcher_inventory = Counter(doppler_trophy=1, alcohest=10, mahakaman_spirit=10,
#                             siren_vocal_cords=3, ghouls_blood=4)
#
# losses = dict(ducat=10, alcohest=20, mahakaman_spirit=5, ghouls_blood=4)
#
# witcher_inventory.subtract(losses)
#
# print(witcher_inventory)
import csv
# from collections import Counter
#
# counter1 = Counter(a=2, b=3, c=6)
# counter2 = Counter(a=5, b=7, c=1)
#
# print(counter1&counter2)



# from collections import Counter
#
# sp = input().lower().split()
# l = Counter(sp)
# l = l.most_common(1)
# print(l[0][0])
# # sp = []
# # for i in range(len(l)):
# #     if l[i][1] == l[0][1]:
# #         sp.append(l[i][0])
# # # sp = sorted(sp)
# #
# # print(sp[0])


from collections import Counter

f = "name_log.csv"

with open(f, encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader)
    changes_count = Counter(row[1] for row in reader)

for email, count in sorted(changes_count.items()):
    print(f"{email}: {count}")
