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
channel = {}
for i in channel_description:
    if len(i) >= 6: print(i)
    for k in channel_category:
        if len(k) >= 6: print(k)
        for g in channel_title:
            if len(g) >= 6: print(g)

    # print(key, end="")
