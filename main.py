from Question import *


if __name__ == "__main__":
    q = Question()
    print("请输入问题~")
    while 1:
        question = input("~~~~~~~~\n")
        result = q.solve(question)
        print(result)


