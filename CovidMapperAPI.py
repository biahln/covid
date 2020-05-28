

import requests

class CovidMapperAPI:

    def __init__(self):
        
        self.covidMapperUrlBaseUFs = "https://covid-api-brasil.herokuapp.com"
        self.covidMapperUrlBaseCountries = "https://covid19-brazil-api.now.sh/api/report/v1/countries"
        self.dataUFsList = []
        self.Countrys = [
            "Brazil",
            "China",
            "Italy",
            "US"
        ]

        self.covidMapperUFs = [
            "AC",
            "AL",
            "AP",
            "AM",
            "BA",
            "CE",
            "DF",
            "ES",
            "GO",
            "MA",
            "MT",
            "MS",
            "MG",
            "PA",
            "PB",
            "PR",
            "PE",
            "PI",
            "RJ",
            "RN",
            "RS",
            "RO",
            "RR",
            "SC",
            "SP",
            "SE",
            "TO"
        ]

    def covidMapperAllCases(self):

        urlAllCases = "/casos"

        return requests.get(self.covidMapperUrlBaseUFs + urlAllCases).json()

    def covidMapperCasesByData(self, data: str):

        urlCasesByData = "/casos/{}".format(data)

        return requests.get(self.covidMapperUrlBaseUFs + urlCasesByData).json()

    def covidMapperCasesByState(self, stateUF: str):

        urlCasesByState = "{}".format(stateUF)

        return requests.get(self.covidMapperUrlBaseUFs + urlCasesByState).json()

    def covidMapperCasesByDataAndState(self, data: str, stateUF: str):

        urlCasesByDAtaAndState = "/{}/{}".format(stateUF, data)

        return requests.get(self.covidMapperUrlBaseUFs + urlCasesByDAtaAndState).json()

    # Método que traz o total de casos de covid até a data de consulta
    def TotalCases(self):

        return self.covidMapperAllCases().get('totalCasos')

    # Método que traz o total de mortes de covid até a data de consulta
    def TotalDeaths(self):

        return self.covidMapperAllCases().get('totalMortes')

    def dataUFs(self):

        for UFs in self.covidMapperUFs:

            covidMapperRequest = requests.get(self.covidMapperUrlBaseUFs + '/{}'.format(UFs)).json()

        
            self.dataUFsList.append(covidMapperRequest.get('casos'))
            self.dataUFsList.append(covidMapperRequest.get('mortes'))


        self.covidMapperDataUFs = [
            ["AC", self.dataUFsList.__getitem__(0), self.dataUFsList.__getitem__(1)],
            ["AL", self.dataUFsList.__getitem__(2), self.dataUFsList.__getitem__(3)],
            ["AP", self.dataUFsList.__getitem__(4), self.dataUFsList.__getitem__(5)],
            ["AM", self.dataUFsList.__getitem__(6), self.dataUFsList.__getitem__(7)],
            ["BA", self.dataUFsList.__getitem__(8), self.dataUFsList.__getitem__(9)],
            ["CE", self.dataUFsList.__getitem__(10), self.dataUFsList.__getitem__(11)],
            ["DF", self.dataUFsList.__getitem__(12), self.dataUFsList.__getitem__(13)],
            ["ES", self.dataUFsList.__getitem__(14), self.dataUFsList.__getitem__(15)],
            ["GO", self.dataUFsList.__getitem__(16), self.dataUFsList.__getitem__(17)],
            ["MA", self.dataUFsList.__getitem__(18), self.dataUFsList.__getitem__(19)],
            ["MT", self.dataUFsList.__getitem__(20), self.dataUFsList.__getitem__(21)],
            ["MS", self.dataUFsList.__getitem__(22), self.dataUFsList.__getitem__(23)],
            ["MG", self.dataUFsList.__getitem__(24), self.dataUFsList.__getitem__(25)],
            ["PA", self.dataUFsList.__getitem__(26), self.dataUFsList.__getitem__(27)],
            ["PB", self.dataUFsList.__getitem__(28), self.dataUFsList.__getitem__(29)],
            ["PR", self.dataUFsList.__getitem__(30), self.dataUFsList.__getitem__(31)],
            ["PE", self.dataUFsList.__getitem__(32), self.dataUFsList.__getitem__(33)],
            ["PI", self.dataUFsList.__getitem__(34), self.dataUFsList.__getitem__(35)],
            ["RJ", self.dataUFsList.__getitem__(36), self.dataUFsList.__getitem__(37)],
            ["RN", self.dataUFsList.__getitem__(38), self.dataUFsList.__getitem__(39)],
            ["RS", self.dataUFsList.__getitem__(40), self.dataUFsList.__getitem__(41)],
            ["RO", self.dataUFsList.__getitem__(42), self.dataUFsList.__getitem__(43)],
            ["RR", self.dataUFsList.__getitem__(44), self.dataUFsList.__getitem__(45)],
            ["SC", self.dataUFsList.__getitem__(46), self.dataUFsList.__getitem__(47)],
            ["SP", self.dataUFsList.__getitem__(48), self.dataUFsList.__getitem__(49)],
            ["SE", self.dataUFsList.__getitem__(50), self.dataUFsList.__getitem__(51)],
            ["TO", self.dataUFsList.__getitem__(52), self.dataUFsList.__getitem__(53)]
        ]

       
        return self.covidMapperDataUFs


    def covidMapperCountrys(self):

        countriesRequest = requests.get(self.covidMapperUrlBaseCountries).json()

        recoveredList = {}

        for data in countriesRequest.get("data"):

            if data.get("country") == self.Countrys.__getitem__(0):

                recoveredList.__setitem__("Brazil",  data.get("recovered"))

            
            if data.get("country") == self.Countrys.__getitem__(1):

                recoveredList.__setitem__("China", [data.get("cases"), data.get("recovered"), data.get("deaths")])

            if data.get("country") == self.Countrys.__getitem__(2):

                recoveredList.__setitem__("Italy", [data.get("cases"), data.get("recovered"), data.get("deaths")])

            if data.get("country") == self.Countrys.__getitem__(3):

                recoveredList.__setitem__("US", [data.get("cases"), data.get("recovered"), data.get("deaths")])

        return recoveredList