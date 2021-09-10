from Question import Question

if __name__ == "__main__":
    q = Question()
    print("请输入问题~")
    result = q.solve("大连疫情如何了")   # 0
    result += q.solve("攀枝花有疫情吗") # 0
    result += q.solve("顺义如何")  # 0
    result += q.solve("目前有哪些地方是高风险地区")  # 3
    result += q.solve("上海的高风险地区")  # 6
    result += q.solve("朝阳确诊人数")  # 1
    result += q.solve("北京中风险")  # 7
    result += q.solve("贵阳低风险地区有哪些")  # 8
    result += q.solve("上海低风险")  # 8
    result += q.solve("葫芦岛的风险评级")  # 2
    result += q.solve("渭南风险")  # 2
    result += q.solve("高风险地区")  # 3
    result += q.solve("中风险")  # 4
    result += q.solve("低风险地区有哪些")  # 5
    result += q.solve("哪些地方中风险")  # 4
    print(result)
