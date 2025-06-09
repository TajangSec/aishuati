# 此脚本是针对pdf复制题目有断行的情况的，一般用不到这个脚本
# 从pdf文件复制题目文本时，经常出现换行，然后转json会把后半段题干变成选项
# 此脚本是规范题目的，也就是去除换行


import re

def clean_question_text(text):
    # 按行分割并去除每行首尾空白
    lines = [line.strip() for line in text.splitlines()]
    cleaned = []
    current = []
    in_options = False

    for line in lines:
        if not line:  # 空行跳过
            continue
        
        # 检测是否进入选项部分（A：、B：等）
        if re.match(r'^[A-Z][：.:]', line):
            in_options = True
            if current:  # 将当前累积的题干内容合并
                cleaned.append(''.join(current))
                current = []
            cleaned.append(line)  # 添加选项行
        
        elif in_options:  # 选项部分的续行
            cleaned[-1] += line  # 直接拼接到最后一个选项
        
        else:  # 题干部分
            # 行尾是标点或括号则直接拼接，否则视为单词需要连接
            if current and (current[-1][-1] in '，。、；：）》'"'" or line[0] in '（《'):
                current.append(line)
            else:
                current.append(' ' + line)  # 添加空格防止词语粘连

    # 处理最后剩余的题干内容
    if current:
        cleaned.insert(0, ''.join(current).strip())
    
    return '\n'.join(cleaned)

# 测试数据
input_text = """
1.空字符串的布尔值是 False( 1 分 )
A. 对
B. 错
答案：A
2.条件表达式不能取代一般 if 的语句( 1 分 )
A. 对
B. 错
答案：B
3.在 Switch 语句中,每一个 case 常量表达式的值可以相同( 1 分 )
A. 对
B. 错
答案：B
4.关于 python 类, 类的实例方法必须创建对象后才可以调用( 1 分 )
A. 对
B. 错
答案：A
5.Python 字符串方法 replace()对字符串进行原地修改( 1 分 )
A. 对
B. 错
答案：B
6.index() 方法检测字符串中是否包含子字符串 str， 如果 str 不在 返回-1( 1 分 )
A. 对
B. 错
答案：B
7.在 python 内存管理，变量无须先创建和赋值而直接使用( 1 分 )
A. 对
B. 错
答案：B
8.find() 方法检测字符串中是否包含子字符串 str 如果包含子字符串返回开始的
索引值，否则会报一个异常( 1 分 )
A. 对
B. 错
答案：B
9.在 c 语言中,任何表达式语句都是表达式加分号组成的( 1 分 )
A. 对
B. 错
答案：A
10.在 python 内存管理，变量不必事先声明( 1 分 )
A. 对
B. 错
答案：A
11.count() 方法用于统计字符串里某个字符出现的次数( 1 分 )
A. 对
B. 错
答案：A
12.C 语言函数返回类型默认定义类型是 void( 1 分 )
A. 对
B. 错
答案：B
13.空列表对象的布尔值是 False( 1 分 )
A. 对
B. 错
答案：A
14.栈和队列的都具有先入后出的特点( 1 分 )
A. 对
B. 错
答案：B
15.除字典类型外，所有标准对象均可以用于布尔测试( 1 分 )
A. 对
B. 错
答案：B
16.关于 python 类,类的实例方法必须创建对象前才可以调用( 1 分 )
A. 对
B. 错
答案：B
17.在 c 语言中,在对数组全部元素赋初值时,不可省略行数,可以省略列数( 1 分 )
A. 对
B. 错
答案：B
18.在 python 内存管理，可以使用 del 释放资源( 1 分 )
A. 对
B. 错
答案：A
19.值为 0 的任何数字对象的布尔值是 False( 1 分 )
A. 对
B. 错
答案：A
20.在 c 语言中,浮点型常量的指数表示中, e 是可以省略的( 1 分 )
A. 对
B. 错
答案：B
21.表达式 ‘a’+1 的值为’b’( 1 分 )
A. 对
B. 错
答案：B
22.在 c 语言中,continue 不是结束本次循环,而是终止整个循环( 1 分 )
A. 对
B. 错
答案：B
23.Python 支持使用字典的“键”作为下标来访问字典中的值( 1 分 )
A. 对
B. 错
答案：A
24.在 try...except...else 结构中，如果 try 块的语句引发了异常则会执行 else 块中的
代码( 1 分 )
A. 对
B. 错
答案：B
25.变量的两个值:本身值和地址值都是可以改变的( 1 分 )
A. 对
B. 错
答案：B
26.定义 Python 函数时，如果函数中没有 return 语句，则默认返回空值 None( 1 分 )
A. 对
B. 错
答案：A
27.在 c 语言中,逗号既可以作为运算符,也可作为分隔符( 1 分 )
A. 对
B. 错
答案：A
28.函数形参的存储单元是动态分配的( 1 分 )
A. 对
B. 错
答案：A
29.Python 中一切内容都可以称为对象( 1 分 )
A. 对
B. 错
答案：A
30.对于数字 n，如果表达式 0 not in [n%d for d in range(2, n)] 的值为 True 则说明
n 是素数( 1 分 )
A. 对
B. 错
答案：A
"""

# 清洗文本
cleaned_text = clean_question_text(input_text)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)
print(cleaned_text)