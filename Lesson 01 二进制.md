# Lesson 01 二进制
# 1、什么是二进制？
十进制计数使用10作为基数，二进制使用2作为基数，二进制的数位就是2^n的形式。

# 2、计算机为什么使用二进制？
二进制的数据表达具有抗干扰能力强、可靠性高的优点；

二进制非常适合逻辑运算。

# 3、二进制的位操作
## 移位操作：
二进制左移一位，就是将数字翻倍。

二进制右移一位，就是将数字除以2并求整数商。

右移分为逻辑右移和算术右移：

* 逻辑右移 1 位，左边补 0 即可
* 算术右移是将各位依次右移指定位数，然后在左侧用原符号位补齐。

## 逻辑操作：
“或”：参与操作的位中只要有一个是1，最终结果就是1.

“与”：参与操作的位中必须全都是1，最终结果才是1，否则就为0。

“异或”：参与操作的位相同，最终结果就为0，否则为 1。

两个数值按位“异或”结果为 0，是这两个数值相等的必要充分条件，可以作为判断两个变量是否相等的条件

# 4、思考题
如果不使用 Java 语言自带的 BigInteger 类，我们还有什么方法来实现十进制到二进制的转换呢？（提示：可以使用二进制的移位和按位逻辑操作来实现。）

```python
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
```


