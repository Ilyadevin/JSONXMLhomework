import xml.etree.ElementTree as ET


def sd():
    global listed_strings, element
    tree = ET.ElementTree(file="newsafr.xml")
    root = tree.getroot()
    items = root.findall("channel/item")
    for item in items:
        item_discr = (item.find("description").text.split(" "))
        item_title = (item.find("title").text.split(" "))
        listed_strings = []
        for element in item_discr, item_title:
            listed_strings.append(element)
    counter_1 = 0
    counter_2 = 0
    for list_in_list in listed_strings:
        for i in list_in_list:
            if len(i) >= 6:
                if i == i:
                    counter_1 += 1
                    print(i, counter_1, counter_2)
            else:
                pass


sd()
