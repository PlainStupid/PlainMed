import urllib

from bs4 import BeautifulSoup
import re
from app import db
from app.mod_medication.models import Medicine

# http://www.lyfjabokin.is/Lyf/Abilify/

# This regex works in most cases
#
medicalRegex = "^(?P<Medicine>[^\(\/\d]*)"

req = urllib.request.Request("http://lyfjaver.is/lyfjaskra")
response = urllib.request.urlopen(req)
bsoup = BeautifulSoup(response)
medtable = bsoup.find("table", {"class": "medicine-table"})
allmeds = medtable.findAll("tr")[2:]

medicineList = {}

for x in allmeds:
    soup = BeautifulSoup(str(x))
    medPre = soup.find("td", {"class": "row1"}).string
    regMed = re.compile(medicalRegex, re.I | re.VERBOSE | re.M)
    medName = regMed.match(medPre).group("Medicine").strip()

    medChemical = soup.findAll("td")[3].string

    if medName not in medicineList:
        medicineList[medName] = {"type":"", "chemical":medChemical, "link":str(medName).replace(" ", "")}



for x in medicineList:
    newMed = Medicine(x, medicineList[x]["link"], medicineList[x]["chemical"], medicineList[x]["type"])
    db.session.add(newMed)

db.session.commit()
