class RoundedInt(int):
    def __new__(cls, num, even=True):
        if even:
            num = (num + 1) // 2 * 2
        else:
            num = (num + 1) // 2 * 2 - 1
        return super().__new__(cls, num)



# class LowerString(str):
#     def __new__(cls, obj):
#         isintace = super().__new__(cls, obj)
#         isintace.obj = obj.lower()
#         return isintace
# s1 = LowerString('BEEGEEK')
# s2 = LowerString('BeeGeek')
#
# print(s1)
# print(s2)
# print(s1 == s2)
# print(issubclass(LowerString, str))


# class UpperPrintString(str):
#     def __str__(self):
#         return f'{super().__str__().upper()}'
#
#
#
# s1 = UpperPrintString('beegeek')
# s2 = UpperPrintString('BeeGeek')
#
# print(s1)
# print(s2)