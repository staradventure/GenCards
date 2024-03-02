import re

import gendata
from gencard import create_deck


def main(file_path,file_name,deck_name,deck_path):
    # 读取Markdown文件
    with open(f"{file_path}\\{file_name}.md", 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    # 提取内容
    card_data = gendata.extract_content(markdown_text)
    # 打印结果
    for pair in card_data:
        print(pair)
    create_deck(deck_path,deck_name, card_data)

