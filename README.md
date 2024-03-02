# 将markdown文件导出为Anki卡片的软件！
可将xmind思维导图转换为markdown文件后用此代码，每两个相邻级别的内容进行一个卡牌制作！

然而latex公式需要手动在markdown里面粘贴，这块xmind没做好。
粘贴前后需要在公式前后加上一对$$符号。加一对$是行内公式，加一对$$是块级公式。

# 注意：本程序设计的是只加一对$符号。

命令行版：

以Windows版为例，在api.exe所在的目录中打开cmd，输入：

`api.exe string1 string2 string3 string4`

其中string1~4是参数，分别是markdown文件所在文件夹、文件名、牌组名、牌组所要存储的目标文件夹。

输入参数版：

![image](https://github.com/staradventure/GenCards/assets/91239079/3a31765f-a870-46d5-b606-f4e371aabb45)
