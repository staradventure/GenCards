import random

import genanki

def create_deck(deck_path,deck_name, card_data):
    # 创建一个新的牌组
    my_deck = genanki.Deck(
      deck_id = random.randint(0, 99999),
      name=deck_name)

    # 定义卡片的样式
    my_note_model = genanki.Model(
      model_id=1,
      name='Basic Model',
      fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
      ],
      templates=[
        {
          'name': 'Card 1',
          'qfmt': '{{Question}}',  # 正面显示问题
          'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',  # 背面显示答案
        },
      ])

    # 添加卡片
    for question, answer in card_data:
        my_note = genanki.Note(
          model=my_note_model,
          fields=[question, answer])
        my_deck.add_note(my_note)

    # 生成牌组文件
    genanki.Package(my_deck).write_to_file(f'{deck_path}\\{deck_name}.apkg')

