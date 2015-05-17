from bs4 import BeautifulSoup
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import urllib
import re
from app import db
from app.mod_medication.models import Medicine


# http://www.lyfjabokin.is/Lyf/Abilify/

#This regex works in most cases
#
medicalRegex = "^(?P<Medicine>[^\(\/\d]*)"
def main():
    medicine = getMeds()

    newList = set()
    for med in medicine:
        regMed = re.compile(medicalRegex, re.I|re.VERBOSE|re.M)
        medName = regMed.match(med).group("Medicine")
        newList.add(medName.strip())

    sortedMeds = sorted(newList)
    for x in sortedMeds:
        newMed = Medicine(x, str(x).replace(" ", ""))
        db.session.add(newMed)

    db.session.commit()

	

def getMeds():
    req = urllib.request.Request('http://lyfjaver.is/lyfjaskra')
    response = urllib.request.urlopen(req)
    bsoup = BeautifulSoup(response)
    tables = bsoup.findAll('td', {'class': 'row1'})

    return [i.string for i in tables]

if __name__ == '__main__':
    main()