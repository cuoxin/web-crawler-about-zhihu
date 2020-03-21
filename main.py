import crawler
import terms
import word_cloud
import os


def main():
    list_url = input(r"地址>").split("/")
    int_question_num = int(list_url[-1])

    try:
        path = "./{}result".format(int_question_num)
        os.makedirs(path)
    except:
        pass

    crawler.F_run(int_question_num)
    dic_ = terms.F_run(int_question_num)
    word_cloud.F_run(dic_,int_question_num)


if __name__ == "__main__":
    main()