# Importando depedências
from flask import Flask, render_template
from flask_cors import CORS
from View import CovidMapperAPI
import json


# Instanciando o app
app = Flask(__name__)

# Configurações de permissão do acesso ao app
cors = CORS(app, resources = {r"/api/*": {"origins": "*"}})


# End Point

@app.route('/covidmapper', methods = ['GET', 'POST'])
def CallCovidMapper():

    covidData = CovidMapperAPI().covidMapperAllCases()
    covidDataUFs = CovidMapperAPI().dataUFs()
    covidCountries = CovidMapperAPI().covidMapperCountrys()

    templateData = {

        "dataChina": [covidCountries.get("China")[0], covidCountries.get("China")[1], covidCountries.get("China")[2]],
        "dataUS": [covidCountries.get("US")[0], covidCountries.get("US")[1], covidCountries.get("US")[2]],
        "dataItaly": [covidCountries.get("Italy")[0], covidCountries.get("Italy")[1], covidCountries.get("Italy")[2]],
        "dataBrasil" : [covidData.get('totalCasos'), covidCountries.get("Brazil"), covidData.get('totalMortes')],
        "AC": [covidDataUFs.__getitem__(0)[1], 0, covidDataUFs.__getitem__(0)[2]],
        "AL": [covidDataUFs.__getitem__(1)[1], 0, covidDataUFs.__getitem__(1)[2]],
        "AP": [covidDataUFs.__getitem__(2)[1], 0, covidDataUFs.__getitem__(2)[2]],
        "AM": [covidDataUFs.__getitem__(3)[1], 0, covidDataUFs.__getitem__(3)[2]],
        "BA": [covidDataUFs.__getitem__(4)[1], 0, covidDataUFs.__getitem__(4)[2]],
        "CE": [covidDataUFs.__getitem__(5)[1], 0, covidDataUFs.__getitem__(5)[2]],
        "DF": [covidDataUFs.__getitem__(6)[1], 0, covidDataUFs.__getitem__(6)[2]],
        "ES": [covidDataUFs.__getitem__(7)[1], 0, covidDataUFs.__getitem__(7)[2]],
        "GO": [covidDataUFs.__getitem__(8)[1], 0, covidDataUFs.__getitem__(8)[2]],
        "MA": [covidDataUFs.__getitem__(9)[1], 0, covidDataUFs.__getitem__(9)[2]],
        "MT": [covidDataUFs.__getitem__(10)[1], 0, covidDataUFs.__getitem__(10)[2]],
        "MS": [covidDataUFs.__getitem__(11)[1], 0, covidDataUFs.__getitem__(11)[2]],
        "MG": [covidDataUFs.__getitem__(12)[1], 0, covidDataUFs.__getitem__(12)[2]],
        "PA": [covidDataUFs.__getitem__(13)[1], 0, covidDataUFs.__getitem__(13)[2]],
        "PB": [covidDataUFs.__getitem__(14)[1], 0, covidDataUFs.__getitem__(14)[2]],
        "PR": [covidDataUFs.__getitem__(15)[1], 0, covidDataUFs.__getitem__(15)[2]],
        "PE": [covidDataUFs.__getitem__(16)[1], 0, covidDataUFs.__getitem__(16)[2]],
        "PI": [covidDataUFs.__getitem__(17)[1], 0, covidDataUFs.__getitem__(17)[2]],
        "RJ": [covidDataUFs.__getitem__(18)[1], 0, covidDataUFs.__getitem__(18)[2]],
        "RN": [covidDataUFs.__getitem__(19)[1], 0, covidDataUFs.__getitem__(19)[2]],
        "RS": [covidDataUFs.__getitem__(20)[1], 0, covidDataUFs.__getitem__(20)[2]],
        "RO": [covidDataUFs.__getitem__(21)[1], 0, covidDataUFs.__getitem__(21)[2]],
        "RR": [covidDataUFs.__getitem__(22)[1], 0, covidDataUFs.__getitem__(22)[2]],
        "SC": [covidDataUFs.__getitem__(23)[1], 0, covidDataUFs.__getitem__(23)[2]],
        "SP": [covidDataUFs.__getitem__(24)[1], 0, covidDataUFs.__getitem__(24)[2]],
        "SE": [covidDataUFs.__getitem__(25)[1], 0, covidDataUFs.__getitem__(25)[2]],
        "TO": [covidDataUFs.__getitem__(26)[1], 0, covidDataUFs.__getitem__(26)[2]],
    }
    data = (json.dumps(templateData)
    .replace(u'<', u'\\u003c')
    .replace(u'>', u'\\u003e')
    .replace(u'&', u'\\u0026')
    .replace(u"'", u'\\u0027'))

    return render_template('Menu.html', data=data)


if __name__ == "__main__":

    app.run(debug=True)
