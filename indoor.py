#第一个练习
wenhou = input("写入HELLO ").lower()
print(wenhou)
#第二个练习和第三个练习都是同样的练的用只是用的值不一样，次数也不一样
two = input("写入一段话 ")
print(two.replace(":)","🙂").replace(":(","🙁"))
#第四个练习
m=int(input("输入质量："))
c=300000000
E = m * c**2
print(E)
#第五个练习
bill = float(input("Bill: ").replace("$", ""))
percent = float(input("Percent: ").replace("%", ""))
tip = bill * (percent / 100)
print(f"${tip:.2f}")