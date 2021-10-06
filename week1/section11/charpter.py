class Decrypt():
    def __init__(self, code_wprd):
        self.code_wprd = code_wprd

    def decrypt(self):
        code_wprd = self.code_wprd.replace("0", 'O').replace("1", 'I').replace("2", 'Z').replace("3", 'E').replace("4",
                                                                                                                   'Y').replace(
            "5", 's').replace("6", 'G').replace("7", 'L').replace("8", 'B').replace("9", 'P')
        return code_wprd


class exchange():
    def ruble(self, currencys, money):
        if currencys == "RMB":
            print(str(money) + "RMB=" + str(money * 9.912) + "RUB")
            return str(money) + "RMB=" + str(money * 9.912) + "RUB"
        if currencys == "RUB":
            print(str(money) + "RUB=" + str(money * 0.1009) + "RMB")
            return str(money) + "RUB=" + str(money * 0.1009) + "RMB"


if __name__ == '__main__':
    Decrypt = Decrypt("1234567890")
    password = Decrypt.decrypt()
    print(password)

    exchange = exchange()
    exchange.ruble('RUB', 100)
