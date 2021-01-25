from flask import Flask,render_template,request
import json
#demmarer le  server
app = Flask(__name__)
app.config["DEBUG"] = True

global data
f = open("covid.json")
data = json.load(f)

@app.route('/', methods=['GET'])
def home():
    listCountries =getCountries()
    return render_template("index.html",listCountries=listCountries)

@app.route("/", methods=['POST'])
def result():
    country1 = request.form['country1']
    country2 = request.form['country2']
    country3 = request.form['country3']
    listCountries = getCountries()
    #Recuperation des derniers 10 jours
    listDates = getDates()
    #Recuperation des cases country 1 2 3
    listCountry1 = getCases(country1)
    listCountry2 = getCases(country2)
    listCountry3 = getCases(country3)

    return render_template("index.html",listCountries=listCountries,country1=country1,country2=country2,country3=country3,
                           listDates=listDates,listCountry1=listCountry1,listCountry2=listCountry2,
                           listCountry3=listCountry3)

def getDates():
    listDates =[]
    for item in data["records"]:
        if item["geoId"] == "AF":
            listDates.append(item["dateRep"])
    return(listDates[:10])

def getCases(country):
    listCases = []
    for item in data["records"]:
        if item["countryterritoryCode"] == country:
            listCases.append({"cases" : item["cases"],"deaths" : item["deaths"]})
    return (listCases[:10])

def getCountries():
    listCountries =[]
    previous = ""
    for item in data["records"]:
        if(previous != item["countryterritoryCode"]):
            listCountries.append({"code" : item["countryterritoryCode"],"abr" : item["countriesAndTerritories"]})
        previous = item["countryterritoryCode"]
    # print(listCountries)
    return  listCountries
app.run()