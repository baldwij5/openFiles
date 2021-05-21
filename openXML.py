from xml.dom import minidom

tag_name = 'from'

xml_name = r'C:\\Users\\jackb\\Desktop\\FileOpen\\note.xml'
mydoc = minidom.parse(xml_name)

print(mydoc.nodeName)
print(mydoc.firstChild.tagName)
