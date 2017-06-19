import xml.etree.ElementTree as etree    #1
tree = etree.parse('files/feed.xml')  #2
root = tree.getroot()                    #3
print(root)   
print(root.tag)                        #1
## '{http://www.w3.org/2005/Atom}feed'
print(len(root))                       #2
## 8
for child in root:                     #3
        print(child)                   #4

print(root.attrib)                           #1
## {'{http://www.w3.org/XML/1998/namespace}lang': 'en'}
print(root[4])                               #2
## <Element {http://www.w3.org/2005/Atom}link at e181b0>
print(root[4].attrib)                        #3
## {'href': 'http://diveintomark.org/',
## 'type': 'text/html',
## 'rel': 'alternate'}
print(root[3])                               #4
## <Element {http://www.w3.org/2005/Atom}updated at e2b4e0>
print(root[3].attrib)                        #5
## {}        