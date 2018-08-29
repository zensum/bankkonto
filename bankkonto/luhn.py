"""
Luhn algorithm implementation

References:
https://sv.wikipedia.org/wiki/Luhn-algoritmen

Code adopted from here:
https://github.com/joke2k/faker/blob/master/faker/providers/ssn/sv_SE/__init__.py

"""


def _digits_of(number):
    return [int(i) for i in str(number)]


def _luhn_checksum(card_number):
    digits = _digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(_digits_of(2 * digit))
    return total % 10


def validate_luhn(card_number):
    return _luhn_checksum(card_number) == 0


def calculate_luhn(partial_card_number):
    # Append a zero check digit to the partial number and calculate checksum
    check_digit = _luhn_checksum(int(partial_card_number) * 10)
    # If the (sum mod 10) == 0, then the check digit is 0
    # Else, the check digit = 10 - (sum mod 10)
    return check_digit if check_digit == 0 else 10 - check_digit



