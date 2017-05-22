from urllib.request import urlopen
import html5lib
from lxml import html
import lxml.etree as etree
from lxml.cssselect import CSSSelector

def parseModel(url):
    with urlopen(url) as f:
        parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("lxml"))
        document = parser.parse(f, transport_encoding=f.info().get_content_charset())
        find_btn = etree.XPath("//html:div[@class='span4 selector single-card product-selector first-card']", namespaces={"html": "http://www.w3.org/1999/xhtml"})
        print(len(find_btn(document)))
        for item in find_btn(document):
            url = "http://www.cat.com" + item[0].attrib['href']
            text = item[0][0][0][1].text
            print(url)
            print(text)

with urlopen("http://www.cat.com/ru_RU/products/new/equipment.html") as f:
    parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("lxml"))
    document = parser.parse(f, transport_encoding=f.info().get_content_charset())
    find_btn = etree.XPath("//html:div[@class='span3 selector class-selector']", namespaces={"html": "http://www.w3.org/1999/xhtml"})
    for item in find_btn(document):
        url = "http://www.cat.com" + item[0].attrib['href']
        text = item[0][0][0][1].text
        print(url)
        print(text)
        parseModel(url)
