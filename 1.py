#coding: utf-8

def happy():
    print("Happy Birthday to you!")

def sing(P):
    happy()
    happy()
    print("Happy Birthday dear " + P + "!")
    happy()

# main
import turtle
f = open("aa.txt", "w", encoding="utf-8")
f.write("你好")
f.close()
turtle.up(100)

sing("李明")
print("hello")
