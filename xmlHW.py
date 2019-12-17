import xml.etree.ElementTree as ET

try:
    tree = ET.ElementTree(file="newsafr.xml")
    root = tree.getroot()
    items = root.findall("channel/item")
    for item in items:
        item_split = (item.find("description").text.split(" "))
        for i in item_split:
            if len(i) >= 6:
                # print(i)
                listed_strings = {}
                counter_i = 0
                for key in i:
                    if i in i:
                        counter_i += 1
                        key = i
                        value = counter_i
                        listed_strings[key] = value
                        print(listed_strings)

finally:
    print("END")

print("--------------------------------------------------------------------------------------------")


def def_titles():
    tree = ET.ElementTree(file="newsafr.xml")
    root = tree.getroot()
    title = root.findall("channel/title")
    for titles in title:
        title_split = root.findall("channel/title")
        for k in title_split:
            if len(k) >= 6:
                listed_titles = {}
                counter_t = 0
                for key_t in k:
                    if k in k:
                        counter_t += 1
                        key_t = k
                        value1 = counter_t
                        listed_titles[key_t] = value1
                        print(listed_titles)
                    return

print("END 2")

def_titles()