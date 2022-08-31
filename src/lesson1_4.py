class lesson_1_4:
    @staticmethod
    def decimal_to_binary(decimal_source):
        """十进制转换成二进制

        :param decimal_source: int
        :return: str
        """
        if decimal_source == 0:
            return "0b0"
        sign = '0b'
        if decimal_source < 0:
            sign = '-' + sign
            decimal_source *= -1

        nubmer_list = []
        while decimal_source != 0:
            nubmer_list.append(str(decimal_source & 1))
            decimal_source >>= 1
        return sign + ''.join(nubmer_list[-1::-1])


if __name__ == '__main__':
    print(lesson_1_4.decimal_to_binary(0))
