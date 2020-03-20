""" 从 data.csv 中读取数据，输出带有频率的字典 """
import jieba
import re
import string


def F_operate(S,re_ed_tag, re_ed_img):
    list_find = re_ed_tag.findall(S)
    str_find = "".join(list_find)
    S = S.translate(str.maketrans('','', str_find))

    list_find = re_ed_img.findall(S)
    str_find = "".join(list_find)
    S = S.translate(str.maketrans('','', str_find))

    S = S.translate(str.maketrans('','',string.punctuation))

    return S


def F_add(S, dic_):
    Ge_result = jieba.cut(S)

    for terms in Ge_result:
        try:
            dic_[terms] += 1
        except:
            dic_[terms] = 1


def F_run():

    dic_termsFrequently = {}

    str_re = r"<.*?>"
    re_ed_tag = re.compile(str_re)
    str_re = r"<figure>.+</figure>"
    re_ed_img = re.compile(str_re)
    with open("./data.csv", "r", encoding="utf-8-sig") as f:
        while True:
            str_readline = f.readline()
            if str_readline:
                str_washed = F_operate(str_readline, re_ed_tag, re_ed_img)
                F_add(str_washed, dic_termsFrequently)
            else:
                break
    
    text = r"，。/《》？！；’：”‘“【】{}、（）的地了吗啊"
    for char in text:
        try:
            dic_termsFrequently.pop(char)
        except:
            pass
    
    return dic_termsFrequently

if __name__ == "__main__":
    F_run()