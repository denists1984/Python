####Get value with DOM#####

import xml.dom.minidom as minidom
from xml.dom.minidom import parse

xml_file = raw_input("Please provide full path with File name from the list: ")
dom = parse(xml_file)
exp_value = raw_input("Please provide search creteria : ")
values = dom.getElementsByTagName(exp_value)

for i in values:
    print " ".join(t.nodeValue for t in i.childNodes if t.nodeType == t.TEXT_NODE)
