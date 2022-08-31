class lesson_1_1:
    @staticmethod
    def decimal_to_binary(decimal_source):
        """十进制转换成二进制

        :param decimal_source: int
        :return: str
        """
        return bin(decimal_source)

    @staticmethod
    def binary_to_decimal(binary_source):
        """二进制转换成十进制

        :param binary_source: str
        :return: int
        """
        return int(binary_source, 2)

    @staticmethod
    def binary_to_octonary(binary_source):
        """二进制转换成八进制

        :param binary_source: str
        :return: str
        """
        return oct(int(binary_source, 2))


if __name__ == '__main__':
    print(lesson_1_1.binary_to_octonary('0b1100100'))
    # hexadecimal to binary
    print(bin(int('0x64', 16)))
    # decimal to decimal
    print(int('100', 10))
    # decimal to octonary
    print(oct(int('100', 10)))
    # decimal to hexadecimal
    print(hex(int('100', 10)))

    print("{:b}".format(int('0o144', 8))) # octonary to binary
    print("{:o}".format(int('0o144', 8))) # octonary to ocatonay
    print("{:x}".format(int('0o144', 8))) # octonary to hexadecimal
