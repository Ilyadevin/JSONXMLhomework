import json
from pprint import pprint

with open("newsafr.json", encoding="utf-8-sig") as file:
    json_data = file.read()
data = json.loads(json_data)
data_json = data["rss"]
# for key in data_json["channel"]:
#     if key == "description":
#         print(type(key))
channel_description = data_json["channel"]["description"].split(" ")
channel_category = data_json["channel"]["category"].split(" ")
channel_title = data_json["channel"]["title"].split(" ")
channel_item = data_json["channel"]["items"]
channel = {}
for ch_dis in channel_description:
    if len(ch_dis) >= 6: print(ch_dis)
    for ch_cat in channel_category:
        if len(ch_cat) >= 6: print(ch_cat)
        for ch_t in channel_title:
            if len(ch_t) >= 6: print(ch_t)
            for ch_item in channel_item:
                splited_ch_item_description = ch_item["description"].split(" ")
                for ch_item_split in splited_ch_item_description:
                    if len(ch_item_split) >= 6:
                        print(ch_item_split)
                for ch_item_ in channel_item:
                    splited_ch_item_title = ch_item_["title"].split(" ")
                    for splited_title in splited_ch_item_title:
                        if len(splited_title) >=6:
                            print(splited_title)