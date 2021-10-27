# tomato-worker
> 终端构建番茄 🍅 时钟 ⏰

## Feature
- 终端实时输出🍅⏰
- [ ] 🍅 ⏰ 完成通知
- [ ] 休息时间完成通知

## Usage
> python main.py -t {minutes} -r {minutes}

- t: 番茄钟设置的时间，默认为 25 mins（可选参数）
- r: 休息时间，默认为 5mins（可选参数）

#### Package
**argparse**
> argparse 模块可以让让轻松编写用户友好的命令行接口。程序定义它需要的参数，然后 argparse 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息

**ArgumentParser 对象**
> 创建一个新的 ArgumentParser 对象。所有的参数都作为关键字参数传入，参数描叙如下（🌟 表示常用参数）：

ArgumentParser -h 命令行展示格式：
usage
description
option arguments
epilog

- prog: 程序名称（默认：sys.argv[0]），默认情况下 Argument 对象使用 sys.argv[0] 来确定如何在帮助消息中显示程序名称
- usage: 描叙程序用于的字符串（默认值：从添加到解析器的参数生成, 一般不做修改）
```python
# prog & usage 联用
prog = 'parse'
parser = argparse.ArgumentParser(
    prog='parse', usage='{} [options]'.format(prog),
    description="test argparse"
)
output => usage: parse [options]
```
- 🌟 description: 在帮助文档之前（默认值：无），这个参数简要描叙这个程序做模式以及怎么做。在帮助消息中这个描叙会显示在命令行用法字符串和各种参数的帮助消息之间
- epilog: 在参数帮助文档之后显示的文本（默认值：无）
- parents: 一个 ArgumentParser 对象的列表
formatter_class: 用于自定义帮助文档输出格式的类
prefix_chars: 可选参数的前缀字符集合（默认值：'-'）
fromfile_prefix_chars: 当需要从文件中读取其他参数时，用于标识文件名称的前缀字符集合（默认值：None）
argument_default: 参数的全局默认值（默认值：None）
conflict_handle: 解决冲突选项的策略（通常是不必要的）
add_help: 为解析器添加一个 -h/--help 选项（默认值：True）
allow_abbrev: 如果缩写是无歧义的，则允许缩写长选项（默认：True）
exit_on_error: 决定当错误发生时，是否让 ArgumentParse 附带信息退出（默认值：True）

**add_argument() 方法**
> 定义单个命令行参数应当如何解析

- 🌟 name or flags: 一个命名或者一个选项字符串列表（- 指定的短参数，-- 指定长参数，-&-- 相当于关键字参数，如果使用 - or -- 则添加的参数为默认）
```python
   # 如果值使用 - 则 parse.parse_args() 通过 - 后面的参数获取, 如果使用 - 且使用 -- 则parse.parse_args() 通过 -- 后面指定的参数获取，如果没有使用 - or -- 则parse.parse_args() 通过 name 获取
    # eg:
    parser.add_argument('-n', type=int, help='input a int')
    parser.add_argument('-s', '--string', metavar='S', type=int, help='input a str')
    parser.add_argument('-t', '--test', metavar='T', type=int, help='input a test')
    parser.add_argument('age')
    args = parser.parse_args()

    # input => python3 args.py -n 123 123
    # output => Namespace(n=123, string=None, test=None, age='123')
```

- action: 当参数在命令行中出现时使用的动作基本类型
- nargs: 命令行参数应当消耗的数目
- const: 被一些 action 和 args 选择所需求的常数
- default: 当参数未在命令行中出现并且也不存在于命名空间对象时产生的值
- 🌟 type: 命令行参数应当被转换成的类型
- choices: 可用的参数容器
- required: 此命令行选项时可以省略
- 🌟 help: 一个此选项作用的简单描叙
- metavar: 在使用方法消息中使用参数值示例
- dest: 被添加到 parse_args() 所返回对象上的属性名

**parse_args() 方法**
> 将参数字符串转换为对象并将其设置为命名空间的属性，返回带有成员的命名空间

- args: 要解析的字符串列表。默认值是从 sys.argv 获取
- namespace: 用于获取属性的对象。默认值是一个空 Namespace 对象

**注意⚠️：**在解析命令参数时 parse_args() 会监测多种错误，包括有歧义的选项、无效类型、无效选项、错误位置参数等等。当出现错误时，它将退出并打印出错误文本同时附带用法消息
