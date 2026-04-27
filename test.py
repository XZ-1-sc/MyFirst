x=input("请输入长度小于4的字符串: ")

y=chr(ord(x[0])-32)+chr(ord(x[1])-32)+chr(ord(x[2])-32)+chr(ord(x[3])-32)

print(f"转换成大写的字符串是:{y}")
