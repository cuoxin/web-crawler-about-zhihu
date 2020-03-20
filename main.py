import crawler
import terms
import word_cloud


def main():
    list_url = input(r"地址>").split("/")
    int_question_num = int(list_url[-1])

    crawler.F_run(int_question_num)
    dic_ = terms.F_run()
    word_cloud.F_run(dic_)


if __name__ == "__main__":
    main()