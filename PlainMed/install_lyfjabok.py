
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import sys

from app import db
from app.mod_medication.models import Medicine

try:
	driver = webdriver.Firefox()
except:
	print("Works currently for Firefox")
	sys.exit(1)

print("Start collecting medicine")
# Start running up lyfjabokin.is
driver.get("http://www.lyfjabokin.is")

# get the page's source code
html = driver.page_source
soup = BeautifulSoup(html)

# Medicine list - One medicine 
medicineList = {}
# medicineList = [MedicineName, medicineType, MedicineChemical, MedicineLink]

# For each found link which goes to the next page we run our scraper
while soup.find("a", {"class":"next"}):

	# Find the medicine list
	tables = soup.find("div", {"class": "medicines list"}).find("tbody").findAll("tr")
	# If it has the list we continue
	if tables:
		for medicine in tables:
			currMedicine = medicine.find("td", {"class": "name"})
			try:
				getType = medicine.find("td", {"class": "type"}).string
			except:
				getType = ""
			
			try:
				getChemical = medicine.find("td", {"class": "chemicals"}).string
			except:
				getChemical = ""

			try:
				getMedName = currMedicine.find("a")
				getMedLink = re.match("^.+\/(?P<MedLink>.+)\/", getMedName["href"]).group("MedLink")
				if getMedName.string not in medicineList:
					medicineList[getMedName.string] = {"type":getType, "chemical":getChemical, "link":getMedLink}
				#medicineList.add([getMedName.string, getType, getChemical, getMedLink])
			except:
				try:
					getMedName = currMedicine.find("span", {"class":"n"})
					if getMedName.string not in medicineList:
						medicineList[getMedName.string] = {"type":getType, "chemical":getChemical, "link": ""}
					#medicineList.add([getMedName.string, getType, getChemical, ""])
				except:
					pass

	# Try clicking the next button if it does exist,
	# else we quit the loop
	try:
		driver.find_element_by_class_name("next").click()
	except:
		break

	html = driver.page_source
	soup = BeautifulSoup(driver.page_source)

# Quit Firefox
driver.quit()

# Install to database
print("Adding to database")
for x in medicineList:
	newMedicine = Medicine(x, medicineList[x]["link"], medicineList[x]["chemical"], medicineList[x]["type"])
	db.session.add(newMedicine)

# We are done adding new medicine to the session
# so lets commit
db.session.commit()

print("Done")