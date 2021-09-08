# 根据问题分类器的结果对不同的问题进行答案检索
from getdata import *


class distribute:
    def __init__(self):
        self.dict = {
            0: self.get_location_condition,
            1: self.get_location_number,
            2: self.get_location_degree,  # 某地的风险评级
            3: self.get_high_location,  # 全国的高风险地区
            4: self.get_medium_location,   # 全国的中风险
            5: self.get_low_location,   # 全国的低风险地区
            6: self.get_location_highdegree,  # 某地的高风险地区
            7: self.get_location_mediumdegree,  # 某地的中风险地区
            8: self.get_location_lowdegree,     # 某地的低风险地区
        }

    def get_question_answer(self, question_type_num, location):
        # 刷新数据
        get_data()
        self.location = location
        answer = self.dict[question_type_num]()
        return answer

    # Question 0 - 整体情况
    """
    每一行中：
        0省份
        1城市
        2更新时间
        3目前确诊人数
        4累计确诊人数
        5疑似病例
        6死亡人数
        7死亡率
        9治愈人数
        10治愈率
        12风险评级
    """
    # 0
    def get_location_condition(self):
        location = self.location
        # print(location)
        nowconfirm = 0
        allconfirm = 0
        suspect = 0
        dead = 0
        heal = 0
        degree = list()
        location1 = list()
        a = 0
        with open('/Users/mac/Desktop/自然语言处理PJ/数据获取/data.csv', 'r', encoding='utf-8') as f:
            text = f.read().splitlines()
            for i in range(len(text)):
                line = text[i].split(',')
                if location == line[1]:
                    nowconfirm = line[3]
                    allconfirm = line[4]
                    suspect = line[5]
                    dead = line[6]
                    heal = line[9]
                    degree = line[12]
                    break
                if location == line[0]:
                    nowconfirm += int(line[3])
                    allconfirm += int(line[4])
                    suspect += int(line[5])
                    dead += int(line[6])
                    heal += int(line[9])
                    if line[12] != '':
                        location1.append(line[1])
                        degree.append(line[12])
                        a = a + 1

        # 生成回答
        res = location + "目前确诊" + str(nowconfirm) + "人" + ",累计确诊" + str(allconfirm) + "人，疑似病例" + str(suspect) + "个，死亡人数"
        res = res + str(dead) + "人，治愈人数" + str(heal) + "人。"
        if a == 0:
            res = res + "目前" + str(location) + "无任何风险地区。"
        else:
            res = res + "其中"
            for i in range(len(location1)):
                res = res + location1[i] + "为" + degree[i] + ","
        res = res + "还是要坚持做好防护工作哦！"
        return res

    # 1
    def get_location_number(self):
        location = self.location
        nowconfirm = 0
        allconfirm = 0
        a = 0
        with open('/Users/mac/Desktop/自然语言处理PJ/数据获取/data.csv', 'r', encoding='utf-8') as f:
            text = f.read().splitlines()
            for i in range(len(text)):
                line = text[i].split(',')
                if location == line[1]:
                    nowconfirm = line[3]
                    allconfirm = line[4]
                    break
                if location == line[0]:
                    nowconfirm += int(line[3])
                    allconfirm += int(line[4])

        # 生成回答
        res = location + "目前确诊" + str(nowconfirm) + "人" + ",累计确诊" + str(allconfirm)
        return res

    # 2
    def get_location_degree(self):
        location = self.location
        degree = list()
        location1 = list()
        a = 0
        with open('/Users/mac/Desktop/自然语言处理PJ/数据获取/data.csv', 'r', encoding='utf-8') as f:
            text = f.read().splitlines()
            for i in range(len(text)):
                line = text[i].split(',')
                if location == line[1]:
                    degree = line[12]
                    break
                if location == line[0] and line[12] != '':
                    location1.append(line[1])
                    degree.append(line[12])
                    a = a + 1

        # 生成回答
        if a == 0:
            res = "目前" + str(location) + "无任何风险地区。"
        else:
            res = str(location) + "的"
            for i in range(len(location1)):
                res = res + location1[i] + "为" + degree[i]
                if i != len(location1)-1:
                    res = res + ','
        return res

    # 3
    def get_high_location(self):
        degree = list()
        location1 = list()
        a = 0
        with open('/Users/mac/Desktop/自然语言处理PJ/数据获取/data.csv', 'r', encoding='utf-8') as f:
            text = f.read().splitlines()
            for i in range(len(text)):
                line = text[i].split(',')
                if line[12] != '':
                    if '高' in line[12]:
                        location1.append(line[1])
                        degree.append(line[12])
                        a = a + 1

        # 生成回答
        if a == 0:
            res = "目前无任何高风险地区。"
        else:
            res = '目前全国有' + str(a) + "个高风险地区："
            for i in range(len(location1)):
                res = res + location1[i] + "为" + degree[i]
                if i != len(location1)-1:
                    res = res + ','
        return res

    # 4
    def get_medium_location(self):
        degree = list()
        location1 = list()
        a = 0
        with open('/Users/mac/Desktop/自然语言处理PJ/数据获取/data.csv', 'r', encoding='utf-8') as f:
            text = f.read().splitlines()
            for i in range(len(text)):
                line = text[i].split(',')
                if line[12] != '':
                    if '中' in line[12]:
                        location1.append(line[1])
                        degree.append(line[12])
                        a = a + 1

        # 生成回答
        if a == 0:
            res = "目前无任何中风险地区。"
        else:
            res = '目前全国有' + str(a) + "个中风险地区："
            for i in range(len(location1)):
                res = res + location1[i] + "为" + degree[i]
                if i != len(location1) - 1:
                    res = res + ','
        return res

    # 5
    def get_low_location(self):
        degree = list()
        location1 = list()
        a = 0
        with open('/Users/mac/Desktop/自然语言处理PJ/数据获取/data.csv', 'r', encoding='utf-8') as f:
            text = f.read().splitlines()
            for i in range(len(text)):
                line = text[i].split(',')
                if line[12] != '':
                    if '低' in line[12]:
                        location1.append(line[1])
                        degree.append(line[12])
                        a = a + 1

        # 生成回答
        if a == 0:
            res = "目前无任何低风险地区。"
        else:
            res = '目前全国有' + str(a) + "个低风险地区："
            for i in range(len(location1)):
                res = res + location1[i] + "为" + degree[i]
                if i != len(location1) - 1:
                    res = res + ','
        return res

    # 6
    def get_location_highdegree(self):
        location = self.location
        degree = list()
        location1 = list()
        a = 0
        with open('/Users/mac/Desktop/自然语言处理PJ/数据获取/data.csv', 'r', encoding='utf-8') as f:
            text = f.read().splitlines()
            for i in range(len(text)):
                line = text[i].split(',')
                if location == line[1]:
                    degree = line[12]
                    break
                if location == line[0] and line[12] != '' and '高' in line[12]:
                    location1.append(line[1])
                    degree.append(line[12])
                    a = a + 1

        # 生成回答
        if a == 0:
            res = "目前" + str(location) + "无任何高风险地区。"
        else:
            res = str(location) + "的"
            for i in range(len(location1)):
                res = res + location1[i] + "为" + degree[i]
                if i != len(location1)-1:
                    res = res + ','
        return res

    # 7
    def get_location_mediumdegree(self):
        location = self.location
        degree = list()
        location1 = list()
        a = 0
        with open('/Users/mac/Desktop/自然语言处理PJ/数据获取/data.csv', 'r', encoding='utf-8') as f:
            text = f.read().splitlines()
            for i in range(len(text)):
                line = text[i].split(',')
                if location == line[1]:
                    degree = line[12]
                    break
                if location == line[0] and line[12] != '' and '中' in line[12]:
                    location1.append(line[1])
                    degree.append(line[12])
                    a = a + 1

        # 生成回答
        if a == 0:
            res = "目前" + str(location) + "无任何中风险地区。"
        else:
            res = str(location) + "的"
            for i in range(len(location1)):
                res = res + location1[i] + "为" + degree[i]
                if i != len(location1) - 1:
                    res = res + ','
        return res

    # 8
    def get_location_lowdegree(self):
        location = self.location
        degree = list()
        location1 = list()
        a = 0
        with open('/Users/mac/Desktop/自然语言处理PJ/数据获取/data.csv', 'r', encoding='utf-8') as f:
            text = f.read().splitlines()
            for i in range(len(text)):
                line = text[i].split(',')
                if location == line[1]:
                    degree = line[12]
                    break
                if location == line[0] and line[12] != '' and '低' in line[12]:
                    location1.append(line[1])
                    degree.append(line[12])
                    a = a + 1

        # 生成回答
        if a == 0:
            res = "目前" + str(location) + "无任何低风险地区。"
        else:
            res = str(location) + "的"
            for i in range(len(location1)):
                res = res + location1[i] + "为" + degree[i]
                if i != len(location1) - 1:
                    res = res + ','
        return res