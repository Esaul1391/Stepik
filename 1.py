from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    if from_left:
        chainmap = chainmap.maps
    else:
        chainmap = reversed(chainmap.maps)
    res = None
    for search_map in chainmap:
        if key in search_map:
            res = search_map[key]
            break
    return res

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'na'))



# # from collections import ChainMap
# #
# #
# # def deep_update(chainmap, key, value):
# #     flag = True
# #     for i in chainmap.maps:
# #         if key in i:
# #             flag = False
# #             break
# #     for mapp in chainmap.maps:
# #         if key not in mapp and flag == True:
# #             mapp[key] = value
# #             flag = False
# #         if key in mapp:
# #             mapp[key] = value
#
#
# chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
# deep_update(chainmap, 'name', 'Dima')
#
# print(chainmap)

# from collections import ChainMap
#
#
# def get_all_values(cahainmap, key):
#     res_set = set()
#     for search in cahainmap.maps:
#         if key in search:
#             res_set.add(search[key])
#     return res_set
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# result = get_all_values(chainmap, 'age')
#
# print(result)
