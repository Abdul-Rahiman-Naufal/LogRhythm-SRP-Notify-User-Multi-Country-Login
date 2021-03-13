# Devleoped by Abdul Rahiman Naufal
# abdulrahimannaufal@gmail.com

import sys
import xml.etree.ElementTree as ET
from pathlib import Path
'''arg1 = 
   arg2 =
   arg3 =
'''

def generateXML(file):

    root = ET.Element("data")

    item = ET.SubElement(root, "items")

    ET.SubElement(item, "item", name="from").text = ""

    ET.SubElement(item, "item", name="to").text = ""

    ET.SubElement(item, "item", name="SMTP").text = ""

    tree = ET.ElementTree(root)

    tree.write(file)


mail_From=sys.argv[1]
mail_To=sys.argv[2]
SMTP_Server=sys.argv[3]

config_file="C:/Program Files/LogRhythm/SmartResponse Plugins/MultiCountryLoginConfigFile.xml"


my_file = Path(config_file)


if (my_file.is_file()==False):    

    generateXML(config_file)


tree = ET.parse(config_file)

root = tree.getroot()

for elem in root.iter('item'):

    if(elem.attrib["name"] == "from"):

        elem.text=mail_From 

    elif(elem.attrib["name"] == "to"):

        elem.text=mail_To

    elif(elem.attrib["name"] == "SMTP"):

        elem.text=SMTP_Server

try:
    tree.write(config_file)
    print("Configuration saved.")
except:
    print("Error Occured.")