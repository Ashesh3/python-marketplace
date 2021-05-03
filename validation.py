import re


class Validation:
    @classmethod
    def is_valid_email(cls, email):
        return re.search(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email)

    @classmethod
    def is_valid_phone(cls, phone):
        return len(str(phone)) == 10 and bool(
            all(char.isdigit() for char in str(phone))
        )

    @classmethod
    def is_valid_pass(cls, password):
        return len(password) > 6 and bool(any(char.isdigit() for char in password))

    @classmethod
    def get_int_input(cls, inp, max_inp, allow_zero=False):
        while True:
            if str.isdigit(inp):
                inp = int(inp)
                if inp > (-1 if allow_zero else 0) and inp <= max_inp:
                    return inp
            print("Invalid Input, Enter a Choice: ")
            inp = input()
