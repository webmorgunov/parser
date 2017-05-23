from urllib.request import urlopen
import html5lib
from lxml import html
import lxml.etree as etree
from lxml.cssselect import CSSSelector
import json

def parseModel(url):
    with urlopen(url) as f:
        parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("lxml"))
        document = parser.parse(f, transport_encoding=f.info().get_content_charset())
        specs = etree.XPath("//html:div[@class='productDetailSpec specifications']", namespaces={"html": "http://www.w3.org/1999/xhtml"})
        #print(len(find_btn(document)))
        cuttedList = specs(document)[0][1:-1]
        #print(cuttedList)
        for item in cuttedList:
            text = item[0][0][0][0].text
            table = item[0][1][0]
            for row in table:
                print(row[0].text + " : " + row[1][1].text)

def parseModelList(url):
    print()
    with urlopen(url) as f:
        string = f.read().decode('utf-8')
        json_obj = json.loads(string)
        for model in json_obj['models']:
            model_url = 'http://www.cat.com/' + model['detail_url']
            print(model['model_name'])
            parseModel(model_url)

with urlopen("http://www.cat.com/en_GB/products/new/equipment.html") as f:
    parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("lxml"))
    document = parser.parse(f, transport_encoding=f.info().get_content_charset())
    find_btn = etree.XPath("//html:div[@class='span3 selector class-selector']", namespaces={"html": "http://www.w3.org/1999/xhtml"})
    for item in find_btn(document):
        url = "http://www.cat.com" + item[0].attrib['href']
        text = item[0][0][0][1].text
        #print(url)
        print(text)
        url_arr = str.split(url, '/')
        name = str.split(url_arr[-1], '.')[0]
        model_url = 'http://www.cat.com/en_GB/products/new/equipment/' + name + '/_jcr_content.feed.json'
        #print(name)
        parseModelList(model_url)
