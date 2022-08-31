class lesson_1_2:
    @staticmethod
    def left_shift(num, m):
        """向左移位

        :param num:等待移位的十进制数
        :param m:向左移的位数
        :return:移位后的十进制数
        """
        return num << m

    @staticmethod
    def right_shift(num, m):
        """向右移位

        :param num:等待移位的十进制数
        :param m:向右移的位数
        :return:移位后的十进制数
        """
        return num >> m


if __name__ == '__main__':
    num = 53
    m = 1
    print("数字{:d}的二进制向左移{:d}位是{:d}".format(num, m, lesson_1_2.left_shift(num, m)))
    print("数字{:d}的二进制向右移{:d}位是{:d}".format(num, m, lesson_1_2.right_shift(num, m)))

    n = 3
    print("数字{:d}的二进制向左移{:d}位是{:d}".format(num, n, lesson_1_2.left_shift(num, n)))
    print("数字{:d}的二进制向右移{:d}位是{:d}".format(num, n, lesson_1_2.right_shift(num, n)))
