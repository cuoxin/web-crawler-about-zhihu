""" 运行爬虫，将内容保存在 data.csv 中 """

import requests
import json
import csv
import time
import os
from Retuen_User_Agent import *

def F_getHtml(headers, num, question_num):
    ''' 输出网页 '''

    str_url_1 = "https://www.zhihu.com/api/v4/questions/"

    str_url_2 = "/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset="

    str_url_3 = "&platform=desktop&sort_by=default"

    str_url = str_url_1 + str(question_num) + str_url_2 + str(num) + str_url_3

    try:
        html = requests.get(str_url, headers = headers)
        html.raise_for_status()
        html.encoding = 'utf-8'
    
    except:
        print("crawler.F_getHtml 运行失败")
        input("Please press KeyEnter to continue...")
        os._exit(0)
    
    return html.text


def F_saveCsv(str_data):
    ''' 保存数据 '''
    with open("./data.csv", "a", encoding="utf-8-sig", newline='') as f:
        f_csv_write = csv.writer(f)
        f_csv_write.writerow([str_data])


def F_run(int_question_num):
    headers = {}
    headers["user-agent"] = F_returnUserAgent()

    num = 0
    while True:

        str_html = F_getHtml(headers, num, int_question_num)
        dic_html = json.loads(str_html)

        for i in range(0, 5):
            try:
                str_need_data = dic_html["data"][i]["content"]
                F_saveCsv(str_need_data)
            except:
                pass

        os.system("cls")
        print("正在读取{}-{}的回答".format(num, num + 5))

        if dic_html["paging"]["is_end"]:
            os.system("cls")
            print("读取完毕")
            break

        num += 5
        time.sleep(0.01)