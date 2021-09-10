# 主函数：调用其他的类来完成整个流程
import jieba
import jieba.posseg
import re
from Classifier import Classifier
from answer import *


class Question:
    def __init__(self):
        self.classify = Classifier()  # 问题分类
        self.answer = Answer()  # 问题类型匹配分流到对应模版回答
        self.location = ''
        self.question_word = []
        self.question_flag = []

    def solve(self, question):
        self.pos_question = self.question_posseg(question)
        question_type_num = self.get_question_type()
        answer = self.answer.get_question_answer(question_type_num, self.location)
        return answer

    def question_posseg(self, question):
        clean_question = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "",
                                str(question).strip())
        # 导入自定义词典并分词标注
        jieba.load_userdict('/Users/mac/Desktop/自然语言处理PJ/数据获取/ld.txt')
        question = jieba.posseg.cut(str(clean_question))

        # question_word为分词后列表
        # question_flag为对应词性标注
        # result为返回值  如 ['攀枝花/ld', '疫情/n']
        question_word, question_flag = [], []
        result = []
        for w in question:
            temp_word = f"{w.word}/{w.flag}"
            result.append(temp_word)
            word, flag = w.word, w.flag
            question_word.append(str(word).strip())
            question_flag.append(str(flag).strip())
        self.question_word = question_word
        self.question_flag = question_flag
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
        question_template_num = self.classify.predict(question)
        return question_template_num
