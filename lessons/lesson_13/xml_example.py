import xml.etree.ElementTree as ET

# Завантаження XML-файлу
tree = ET.parse('example.xml')
root = tree.getroot()

# Читання та виведення даних з елементів XML-документу
for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild.tag, subchild.text)

        if subchild.tag == 'timingExbytes':
            new_el = ET.SubElement(subchild, 'new_element')
            new_el.text = 'new el text'

ET.ElementTree(root).write('new_xml.xml')
            #
            # for c in subchild:
            #     if c.tag == 'micro':
            #         print(f'Micro text is {c.text}')