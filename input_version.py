import main
# 读取字符串参数
string1 = input("Please input file_path: ")
string2 = input("Please input file_name: ")
string3 = input("Please input deck_name: ")
string4 = input("Please input deck_path: ")

# 连接字符串
main.main(string1,string2,string3,string4)

# 打印结果
print("运行成功！")

# 防止程序立即退出
input("Press any key to exit.")