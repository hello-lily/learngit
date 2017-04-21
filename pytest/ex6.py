# -*- coding:utf-8 -*-
# 在变量中加入变化 %d  % 后引用源
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# 引用两个变量， 字符串的形式也可以
y = "Those who know %s and those who %s."% (binary, do_not)

#目的，简化打印，可以面向化处理
print (x)
print (y)

#说实话我对%r的格式很陌生，c里不记得有这个
print("I said: %r." % x)
print("I also said: %s." % y)

#布尔型变量
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# 打印拼接布尔变量
print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e= "a string with a right side."

print (w + e)
