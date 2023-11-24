class LengthError():
    pass


class LetterError():
    pass


class DigitError():
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError('LenghtError')

    lowc = any(c.islower() for c in string)
    upc = any(c.isupper() for c in string)

    if not (lowc and upc):
        raise LengthError("LetterError")

    if not any(c.isdigit() for c in string):
        raise DigitError('DigitError')

    return True

while True:
    password = input()
    try:
        is_good_password(password)
        print("Success!")
        break
    except LengthError:
        print("LengthError")
    except LetterError:
        print("LetterError")
    except DigitError:
        print("DigitError")

# def is_good_password(passwd):
#     if len(passwd) >= 9 and any(c.isupper() for c in passwd) and any(c.islower() for c in passwd):
#         return True
#
#     return False
#
# print(is_good_password('МойПарольСамыйЛучший111'))
