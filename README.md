# biliBV

## 来源

[算法来源](https://www.zhihu.com/question/381784377/answer/1099438784)

感谢原作者，知乎用户mcfx.

[开源链接](https://github.com/ShiSheng233/bili_BV)

## 怎样使用这个库

非常简单，只有两个函数.

- decode()
  - 将BV字符串转换为av编号，返回值是一个int类型的av编号.
  - 用法
    - 传入一个字符串，以"BV"开头.
    - 例子:BV1FE411A7Xd  -> decode("BV1FE411A7Xd")

- encode()
  - 将av编号转换为BV字符串，返回值一个str类型的BV字符串
  - 用法
    - 传入一个字符串，以"av"开头.
    - 例子:av97809031 -> encode("av97809031")