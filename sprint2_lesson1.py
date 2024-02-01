# Import modules
import requests
import json
import xml.etree.ElementTree as ET

# Request JSON
resp1 = requests.get('https://rest.ensembl.org/lookup/symbol/homo_sapiens/BRCA2?content-type=application/json;expand=1')
# Request XML
resp2 = requests.get('https://rest.ensembl.org/lookup/symbol/homo_sapiens/BRCA2?content-type=text/xml;expand=1')

# Collect the JSON as a Python dictionary (handled by requests)
resp1_dict = resp1.json()

# Collect and format the XML response and parse with ElementTree
# Collect
resp2_xml = resp2.content
# Format
resp2_xml = resp2_xml.decode("utf-8")
# Parse
resp2_tree = ET.ElementTree(ET.fromstring(resp2_xml))
# Get root
resp2_root = resp2_tree.getroot()

#Parse the JSON response
for key in resp1_dict.keys():
    print(key)