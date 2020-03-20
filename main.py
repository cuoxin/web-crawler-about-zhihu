import crawler
import terms
import word_cloud


def main():
    crawler.F_run()
    dic_ = terms.F_run()
    word_cloud.F_run(dic_)


if __name__ == "__main__":
    main()