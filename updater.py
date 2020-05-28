import schedule
import time
from View import CovidMapperAPI

def update_data():
    covidData = CovidMapperAPI().covidMapperAllCases()


    templateData = {

        "dataBrasil" : [covidData.get('totalCasos'), 0, covidData.get('totalMortes')]
    }
    return templateData

schedule.every().day.at("09:00").do(update_data)

while True:
    schedule.run_pending()
    time.sleep(30)