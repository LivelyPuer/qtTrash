import json

import requests
from lxml import etree

url = "https://buduguru.org"
dct = {}


def get_professions():
    for i in range(1, 44):
        if i in (13, 22, 31):
            continue
        cnt = requests.get(url + f"/profession/{i}").text
        htmlparser = etree.HTMLParser()
        tree = etree.fromstring(cnt, htmlparser)
        # print(tree.xpath('//h1/text()'))
        # print("\n".join(
        #     tree.xpath('//ul[@class="skills-item"]/h5[text() = "Личные качества"]/following-sibling::li/text()')))
        # print("\n".join(
        #     tree.xpath('//ul[@class="skills-item"]/h5[text() = "Основные навыки"]/following-sibling::li/text()')))
        dct[tree.xpath('//h1/text()')[0]] = {"url": url + f"/profession/{i}",
                                             "characteristic": "\n".join(map(lambda x: x.strip(),
                                                                             tree.xpath(
                                                                                 '//ul[@class="skills-item"]/h5[text() = "Личные качества"]/following-sibling::li/text()'))),
                                             "skills": "\n".join(map(lambda x: x.strip(), tree.xpath(
                                                 '//ul[@class="skills-item"]/h5[text() = "Основные навыки"]/following-sibling::li/text()')))}
        print(i, "/", 43)

    with open("sample.json", "w", encoding="utf-8") as outfile:
        json.dump(dct, outfile, ensure_ascii=False)


def get_dict() -> dict:
    with open('sample.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data
