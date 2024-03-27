# class Test:
#     __slots__ = ['name', 'owner']
#     def __init__(self) -> None:
#         pass
#
# test = Test()
# print(test.__slots__)


# from collections import OrderedDict
#
# class Queue:
#     def __init__(self, pairs=None):
#         if pairs is None:
#             self.queue = OrderedDict()
#         else:
#             if isinstance(pairs, dict):
#                 self.queue = OrderedDict(pairs)
#             else:
#                 self.queue = OrderedDict(pairs)
#
#     def add(self, pair):
#         key, value = pair
#         if key in self.queue:
#             del self.queue[key]
#         self.queue[key] = value
#
#     def pop(self):
#         if not self.queue:
#             raise KeyError('Очередь пуста')
#         return self.queue.popitem(last=False)

    # def __str__(self):
    #     return f"Queue({list(self.queue.items())})"
    #
    # def __len__(self):
    #     return len(self.queue)
    #
    #
    #



# import random
#
# class Card:
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank
#
#     def __str__(self):
#         return f'{self.suit}{self.rank}'
#
#
# class Deck:
#     def __init__(self):
#         self.cards = [Card(suit, rank) for suit in "♣♢♡♠" for rank in "23456789XJQKA"]     #    происходит композиция
#
#     def shuffle(self):
#         if len(self.cards) != 52:
#             raise ValueError("Перемешивать можно только полную колоду")
#         random.shuffle(self.cards)
#
#     def deal(self):
#         if not self.cards:
#             raise ValueError("Все карты разыграны")
#         return self.cards.pop()
#
#     def __str__(self):
#         return f"Карт в колоде: {len(self.cards)}"






# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f"{self.name}, {self.price}$"
#
#
# class ShoppingCart:
#     def __init__(self, items=None):
#         self.items = items if items else []
#
#     def add(self, item):
#         self.items.append(item)       # здесь проиходит композиция
#
#     def total(self):
#         return sum(item.price for item in self.items)
#
#     def remove(self, name):
#         self.items = [item for item in self.items if item.name != name]
#
#     def __str__(self):
#         return "\n".join(str(item) for item in self.items)