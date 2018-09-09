import os
from xml.etree import ElementTree

file = 'box2.xml'
file_path = os.path.abspath(os.path.join('data', file))
dom = ElementTree.parse(file_path)

details = dom.findall('issue')
CONFIG_PROPERTIES = {}
c = 0
for d in details:
    c = c+1
    name = d.find('name').text
    severity = d.find('severity').text
    confidence = d.find('confidence').text
    host = d.find('host').text
    request = d.find('path').text
    CONFIG_PROPERTIES = c, name, severity, confidence, host+request
    print(' {}, {}, {}, {}, {} '.format(
         c, name, severity, confidence, host+request
     ))


