import xml.etree.ElementTree as ET


def sd():
        tree = ET.ElementTree(file="newsafr.xml")
        root = tree.getroot()
        items = root.findall("channel/item")
        for item in items:
            item_split = (item.find("description").text.split(" "))
            counter_i = 0
            listed_strings = []
            for element in item_split:
                if len(element) >= 6:
                    counter_i += 1
                    sorted(element)
                    listed_strings.append(element)
                    if element == element:
                        values = []
                        c = {element: listed_strings.count(element)}
                        print(c)
                else:
                    pass

sd()
print("--------------------------------------------------------------------------------------------")


# def def_titles():
#     tree = ET.ElementTree(file="newsafr.xml")
#     root = tree.getroot()
#     title = root.findall("channel/title")
#     for titles in title:
#         print(titles)
#         break
#         title_split = root.findall("channel/title")
        # for k in title_split:
        #     if len(k) >= 6:
        #         listed_titles = {}
        #         counter_t = 0
        #         for key_t in k:
        #             if k in k:
        #                 counter_t += 1
        #                 key_t = k
        #                 value1 = counter_t
        #                 listed_titles[key_t] = value1
        #                 print(listed_titles)return


# print("END 2")
#
# def_titles()