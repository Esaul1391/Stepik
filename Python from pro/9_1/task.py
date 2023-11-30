def zip_longest(*args, fill=None):
    m = max(args, key=len)
    for i in args:
        while len(i)!=m:
            i.append(fill)
    return zip(args)

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))


# names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
# budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
# box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]
#
# profits = [box_offices - budgets for box_offices, budgets in zip(box_offices, budgets)]
#
# res = sorted(zip(names, profits))
#
# for film, prof in res:
#     print(f"{film}: {prof}$")


# def is_greater(data, number):
#     sp = []
#     for i in data:

#         sp.append(sum(i)>number)
#
#     return any(sp)
#
# data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]
#
# print(is_greater(data, 3))



# films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
#          'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
#          'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
#          'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
#          'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
#          'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
#          'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
#          'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
#          'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
#          'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
#          'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}
# sp = {}
# for i, k in films.items():
#
#     sp[i]= sum(k.values())/2
#
#
# print(min(sp.items(), key=lambda x: x[1])[0])