""" 得到带有词语频率的 dic ，输出 词云图 """
from wordcloud import WordCloud

def F_run(dic_frequent,int_question_num):

    wc = WordCloud(background_color="white", font_path="C:\\Windows\\Fonts\\simsun.ttc",scale=32)
    wc.generate_from_frequencies(dic_frequent)

    image = wc.to_image()
    image.show()
    path = "./{}result\\result.png".format(int_question_num)
    wc.to_file(path)