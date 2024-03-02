import sys
import main

# 检查参数数量
if len(sys.argv) != 5:
    print("Usage: python api.py <string1> <string2> <string3> <string4>")
    sys.exit(1)

# 读取字符串参数
string1 = sys.argv[1]
string2 = sys.argv[2]
string3 = sys.argv[3]
string4 = sys.argv[4]

# 连接字符串
main.main(string1,string2,string3,string4)

# 打印结果
print("运行成功！")
