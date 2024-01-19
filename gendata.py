import re

def extract_content(markdown_text):
    # 正则表达式，匹配Markdown的标题和列表项
    pattern = re.compile(r'^(#{1,6})\s*(.*)|(^[\t ]*(-|\+|\*)\s+(.*))', re.MULTILINE)

    # 解析Markdown文本
    parsed_items = []
    for match in pattern.finditer(markdown_text):
        if match.group(1):  # 标题
            level = len(match.group(1))  # 标题级别由#的数量决定
            text = match.group(2).strip()
        else:  # 列表项
            # 列表项的层级由前导空格和制表符决定
            level = len(match.group(3)) - len(match.group(3).lstrip('\t ')) + 4
            text = match.group(5).strip()

        parsed_items.append((level, text))

    # 存储配对的内容
    paired_content = []

    # 遍历解析后的项，寻找相邻两级内容
    for i in range(len(parsed_items) - 1):
        current_level, current_text = parsed_items[i]
        next_items = []

        # 向下查找下一个级别的内容
        for j in range(i + 1, len(parsed_items)):
            next_level, next_text = parsed_items[j]
            if next_level == current_level + 1:
                next_items.append("<li>" + next_text + "</li>")
            elif next_level <= current_level:
                break

        if next_items:
            combined_next_items = "<ul>\n" + "\n".join(next_items) + "\n</ul>"
            paired_content.append((current_text, combined_next_items))

    return paired_content


