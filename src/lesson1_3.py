class lesson_1_3:
    @staticmethod
    def AND(num1, num2):
        """二进制按位“与”的操作

        :param num1:
        :param num2:
        :return:二进制按位“与”的结果
        """
        return num1 & num2

    @staticmethod
    def OR(num1, num2):
        """二进制按位“或”的操作

        :param num1:
        :param num2:
        :return:二进制按位“或”的结果
        """
        return num1 | num2

    @staticmethod
    def XOR(num1, num2):
        """二进制按位“异或”的操作

        :param num1:
        :param num2:
        :return:二进制按位“异或”的结果
        """
        return num1 ^ num2


if __name__ == '__main__':
    a = 53
    b = 35
    print("数字%d(%s)和数字%d(%s)的按位‘或’结果是%d(%s)" %
          (a, bin(a), b, bin(b), lesson_1_3.OR(a, b), bin(lesson_1_3.OR(a, b))))
    print("数字%d(%s)和数字%d(%s)的按位‘与’结果是%d(%s)" %
          (a, bin(a), b, bin(b), lesson_1_3.AND(a, b), bin(lesson_1_3.AND(a, b))))
    print("数字%d(%s)和数字%d(%s)的按位‘异或’结果是%d(%s)" %
          (a, bin(a), a, bin(a), lesson_1_3.XOR(a, a), bin(lesson_1_3.XOR(a, a))))
