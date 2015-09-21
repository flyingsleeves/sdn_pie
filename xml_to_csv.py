import xml.etree.ElementTree as ET
tree = ET.parse('sdn.xml')
root = tree.getroot()

countryCount = {}

for country in root.iter('country'):
	if country.text in countryCount:
		countryCount[country.text] += 1
	else:
		countryCount[country.text] = 1

f = open('data.csv', 'w')


print >> f, 'label,count'
for key in countryCount.keys():
	print >> f, '\"%s\",%d' % (key, countryCount[key])