
import lxml.etree as ET
from xml.etree import ElementTree

from bs4 import BeautifulSoup
barcodedata =r"""<?xml version="1.0" encoding="UTF-8"?>
<PrintLetterBarcodeData uid="432272190635" name="Niteen" gender="M" yob="1993" co="S/O: Shripal Singh Teotia" house="9/103, AKASH-3, F-2" street="SECTOR -3" loc="RAJENDER NAGAR" vtc="Sahibabad" po="Sahibabad" dist="Ghaziabad" subdist="Ghaziabad" state="Uttar Pradesh" pc="201005" dob="26/07/1993"/>"""

#with open("newxml.xml") as fp:
soup = BeautifulSoup(barcodedata, 'xml')
data = soup.find('PrintLetterBarcodeData')

print(data['dob'])
Userinformation = ['uid','name','gender','yob','co','lm','loc','vtc','po','dist','state','pc',]


# for info in data:
#     userinfo = info
#     userinfo = str(userinfo)
#
# print(userinfo)
# uid = userinfo.split(r' ')
# anotherdata = []
# for data in uid:
#     anotherdata.append(data.split(r'='))
# readdata = []
# finaldata = []
# for list in anotherdata:
#     readdata.append(list)
#     for element in list:
#         finaldata.append(element)
# print(finaldata)

# for i in range(len(1,finaldata)):
#     Userinformation[i] = finaldata[i+1]



# parser = ElementTree.XMLParser(encoding="utf-8")
# decode = ElementTree.fromstring(userinfo,parser=parser)




# file = r'/Users/rakeshredhu/Downloads/Tkinter-UI-master/newxml.xml'
# data = ElementTree.parse(file)

#
# userdata = data.findall('PrintLetterBarcodeData')
#
# for c in userdata:
#     Userinformation[0] = c.find('uid').text
#     Userinformation[1] =  c.find('name').text
#
# print(Userinformation[0],Userinformation[1])