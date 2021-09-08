# 主函数：调用其他的类来完成整个流程
import jieba
import jieba.posseg
import re
from Classifier import Question_classify
from distribute import *


class Question:
    def __init__(self):
        #         self.classify = Question_classify()  # 问题分类
        #         self.distribute = distribute()       # 问题类型匹配分流到对应模版回答
        #         self.location = ''
        #
        #     def Solve(self, question):
        #         # 对问题进行词性标注
        #         self.pos_question = self.question_posseg(question)  # 进行词性标注
        #         # 测试词性标注结果
        #         # print(self.pos_question)   # ['攀枝花/ld', '疫情/n']
        #
        #         # 将问题中实体替换为标注词性，然后分类，得到分类结果question_type_num
        question_type_num = self.get_question_type()
        # 测试分类结果
        # print(question_type_num)

        # 根据：
        # 词性标注得到的实体
        # 分类得到的问题类型
        # 来回答问题
        answer = self.distribute.get_question_answer(question_type_num, self.location)

        # answer = "抱歉，暂未统计相关信息"
        return answer

    # 通过词性标注来得到实体
    def question_posseg(self, question):
        # question为输入的问题
        # 去除问题可能出现的无关字符得到clean_question
        clean_question = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "",
                                     str(question).strip())
        # 导入自定义词典并分词标注
        # 自定义词典
        # ld 地名
        jieba.load_userdict('/Users/mac/Desktop/自然语言处理PJ/数据获取/ld.txt')
        question = jieba.posseg.cut(str(clean_question))

        # question_word为分词后列表
        # question_flag为对应词性标注
        # result为返回值  ['攀枝花/ld', '疫情/n']
        question_word, question_flag = [], []
        result = []
        for w in question:
            temp_word = f"{w.word}/{w.flag}"
            result.append(temp_word)

            word, flag = w.word, w.flag
            question_word.append(str(word).strip())
            question_flag.append(str(flag).strip())
        self.question_word = question_word
        # print(self.question_word) ['攀枝花', '疫情']
        self.question_flag = question_flag
        # print(question_flag)      ['ld', 'n']
        # print(result)
        return result

    def get_question_type(self):
        # 根据标注的问题词性来提取实体，得到实体对应位置
        if 'ld' in self.question_flag:
            index = self.question_flag.index('ld')
            self.location = self.question_word[index]
            self.question_word[index] = 'ld'
        for item in ['lr', 'mr', 'hr']:
            if item in self.question_flag:
                index = self.question_flag.index(item)
                self.question_word[index] = item


        question = "".join(self.question_word)
        # print("将问题转化为", question)  # ld疫情
        question_template_num = self.classify.predict(question)
        # print("使用模版编号： ", question_template_num)  0
        return question_template_num



# if __name__ == "__main__":
#     result = q.Solve("大连疫情如何了")   # 0
#     result = q.Solve("攀枝花有疫情吗")  # 0
#     result = q.Solve("顺义如何")  # 0
#     result = q.Solve("目前有哪些地方是高风险地区")  # 3
#     result = q.Solve("上海的高风险地区")  # 6
#     result = q.Solve("朝阳确诊人数")  # 1
#     result = q.Solve("北京中风险")  # 7
#     result = q.Solve("贵阳低风险地区有哪些")  # 8
#     result = q.Solve("上海低风险")  # 8
#     result = q.Solve("葫芦岛的风险评级")  # 2
#     result = q.Solve("渭南风险")  # 2
#     result = q.Solve("高风险地区")  # 3
#     result = q.Solve("中风险")  # 4
#     result = q.Solve("低风险地区有哪些")  # 5
#     result = q.Solve("哪些地方中风险")  # 4
