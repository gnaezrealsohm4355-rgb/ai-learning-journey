



def main():
#询问用户姓名,去除字符串两端的空白字符，将字符串的首字母大写
    name = input("What's yout name?").strip().title()
    hello(name)
#将字符串拆分成多个单词
#first,last=name.split(" ")
#向用户问好
#print(name)
#明天看str的其他用法
def hello(to="world"):
    print("hello,",to)


main()