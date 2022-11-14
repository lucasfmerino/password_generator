import random


class Password:
    numbers = "1234567890"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    uppers = lowers.upper()
    symbols = "!@#$%&*<>/\?_."

    def __init__(self, number=True, lower=True, upper=True, symbol=True):
        self.number = number
        self.lower = lower
        self.upper = upper
        self.symbol = symbol

    def gen_pass(self, pass_len: int = 10):
        """
        The function is intended to validate the password character types and generate a random value.
        Args:
            pass_len: Indicates the number of characters in the password.
        Returns: The random value generated
        """
        password = ""
        if self.number:
            password += self.numbers
        if self.lower:
            password += self.lowers
        if self.upper:
            password += self.uppers
        if self.symbol:
            password += self.symbols
        password = "".join(random.sample(password, pass_len))
        return password


if __name__ == '__main__':

    password = Password()
    Valorant_pass = password.gen_pass()
    print(Valorant_pass)





