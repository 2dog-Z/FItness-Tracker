这是一个使用递归函数创建的地牢探险程序，包含多种递归生成的元素和互动场景。程序通过递归函数实现了楼梯、正方形、菱形的打印，字符串反转以及随机故事生成等功能。

## 功能介绍

程序包含以下主要功能模块：

1. **楼梯生成** - 递归打印不同级别的楼梯
2. **正方形生成** - 递归打印空心正方形
3. **菱形生成** - 递归打印空心菱形
4. **字符串反转** - 递归反转输入的字符串
5. **随机句子生成** - 基于结构文件递归生成随机句子
6. **地牢探险故事** - 递归生成包含多次遭遇的地牢探险故事

## 函数说明

### `stairs(level: int)`

递归打印楼梯，每一行比上一行多一个台阶字符（▅）。

- 参数：`level` - 楼梯的级数

### `square(size: int, current = 0)`

递归打印空心正方形，使用◆字符作为边框。

- 参数：
  - `size` - 正方形的边长
  - `current` - 当前打印的行数（内部参数）

### `diamond(size: int, row = 0)`

递归打印空心菱形，使用 * 字符作为边框。

- 参数：
  - `size` - 菱形的大小（必须为正奇数）
  - `row` - 当前打印的行数（内部参数）

### `mirror(string: str)`

递归反转并打印输入的字符串。

- 参数：`string` - 需要反转的字符串

### `generate_structure(file_path: str) -> dict`

从文件中读取句子结构并转换为字典。

- 参数：`file_path` - 包含句子结构的文件路径
- 返回：包含结构信息的字典

### `generate_sentence(symbol, structure)`

基于结构字典递归生成随机句子。

- 参数：
  - `symbol` - 起始符号
  - `structure` - 句子结构字典

### `story(encounters: int)`

递归生成包含指定次数遭遇的地牢探险故事，每次遭遇会随机触发不同事件。

- 参数：`encounters` - 遭遇的次数

## 使用方法

1. 确保存在`stranger_structure.txt`文件用于该文件用于存储神秘陌生人的对话结构，格式为`键:值1|值2|值3`，例如：

```plaintext
<s>:<greeting>,<warning>
<greeting>:Hello there|Greetings traveler
<warning>:danger ahead|beware of monsters
```

1. 调用`story(n)`函数开始探险，其中`n`为想要的遭遇次数，例如：

```python
story(3)  # 生成包含3次遭遇的地牢探险故事
```

## 注意事项

- 所有递归函数都包含递归深度超限的错误处理
- 菱形生成仅接受正奇数作为大小参数
- 正方形和楼梯生成仅接受正整数作为大小参数
- 若`stranger_structure.txt`文件不存在，神秘陌生人的对话将无法正常生成

​	（USYD INFO1110课程项目，Readme由AI生成）
