from unittest import result
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import json
import joblib
from numpy import float128

flask_app = Flask(__name__)
app = flask_app
app.config["DEBUG"] = True
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# parameters
parameters = {
    "ph": "ph",
    "humidity": "humidity",
    "temperature": "temperature",
    "sunlight": "sunlight",
    "waterlevel": "waterlevel",
    "humidity": "humidity",
    "soilmoisture": "soilmoisture"
}

# Ph model errors
model_errors = {
    "pe1": 1400.6801396681608,  # PH  VS  SUNLIGHT
    "pe2": 1283.4906160104363,  # PH  VS  HUMIDITY
    "pe3": 1497.0339198759996,  # PH  VS  TEMPERATURE
    "pe4": 1147.7690783499438,  # PH  VS  SOIL MOISTURE
    "pe5": 1594.5763039379087,  # PH  VS  WATER LEVEL
    "su1": 2.914971770893177,  # SUNLIGHT  VS  PH
    "su2": 21.990260124107035,  # SUNLIGHT  VS  HUMIDITY
    "su3": 1.6663726595838935,  # SUNLIGHT  VS  TEMPERATURE
    "su4": 5.76621465069425,  # SUNLIGHT  VS  SOIL MOISTURE
    "su5": 34355.4685188945,  # SUNLIGHT  VS  WATER LEVEL
    "hum1": 2.058147364447074,  # HUMIDITY  VS  PH
    "hum2": 1232.9017457689258,  # HUMIDITY  VS  SUNLIGHT
    "hum3": 2.301294291413467,  # HUMIDITY  VS  TEMPERATURE
    "hum4": 5.0597943179416935,  # HUMIDITY  VS  SOIL MOISTURE
    "hum5": 38287.992393352404,  # HUMIDITY  VS  WATER LEVEL
    "tem1": 1.5660927674867369,  # TEMPERATURE VS PH
    "tem2": 1033.2154030177874,  # TEMPERATURE  VS  SUNLIGHT
    "tem3": 14.906973341690247,  # TEMPERATURE  VS  HUMIDITY
    "tem4": 4.215324647784953,  # TEMPERATURE  VS  SOIL MOISTURE
    "tem5": 26125.363234854656,  # TEMPERATURE  VS  WATER LEVEL
    "sol1": 1.9809564110660427,  # SOIL MOISTURE  VS  PH
    "sol2": 1397.2128370043545,  # SOIL MOISTURE  VS  SUNLIGHT
    "sol3": 23.186468175740938,  # SOIL MOISTURE  VS  HUMIDITY
    "sol4": 2.8621531061798064,  # SOIL MOISTURE  VS  TEMPERATURE
    "sol5": 22109.241921149747,  # SOIL MOISTURE  VS  WATER LEVEL
    "wat1": 1.3300073382331121,  # WATER LEVEL  VS  PH
    "wat2": 1623.4099193353563,  # WATER LEVEL  VS  SUNLIGHT
    "wat3": 22.321268684583778,  # WATER LEVEL  VS  HUMIDITY
    "wat4": 3.3930703741951533,  # WATER LEVEL  VS  TEMPERATURE
    "wat5": 2.7279496213609526,  # WATER LEVEL  VS  SOIL MOISTURE
}

# file names
labels = ["PH", "SUNLIGHT", "HUMIDITY",
          "TEMPERATURE", "SOIL MOISTURE", "WATER LEVEL"]
# predict with PH with APIs
ph1 = "/"+parameters["ph"]+"/"+parameters["sunlight"]
ph2 = "/"+parameters["ph"]+"/"+parameters["humidity"]
ph3 = "/"+parameters["ph"]+"/"+parameters["temperature"]
ph4 = "/"+parameters["ph"]+"/"+parameters["soilmoisture"]
ph5 = "/"+parameters["ph"]+"/"+parameters["waterlevel"]


# predict with sunlight APIs
su1 = "/"+parameters["sunlight"]+"/"+parameters["ph"]
su2 = "/"+parameters["sunlight"]+"/"+parameters["humidity"]
su3 = "/"+parameters["sunlight"]+"/"+parameters["temperature"]
su4 = "/"+parameters["sunlight"]+"/"+parameters["soilmoisture"]
su5 = "/"+parameters["sunlight"]+"/"+parameters["waterlevel"]


# predict temperature with parameters APIs
tem1 = "/"+parameters["temperature"]+"/"+parameters["ph"]
tem2 = "/"+parameters["temperature"]+"/"+parameters["sunlight"]
tem3 = "/"+parameters["temperature"]+"/"+parameters["humidity"]
tem4 = "/"+parameters["temperature"]+"/"+parameters["soilmoisture"]
tem5 = "/"+parameters["temperature"]+"/"+parameters["waterlevel"]

# predict humidity with parameters APIs
hum1 = "/"+parameters["humidity"]+"/"+parameters["ph"]
hum2 = "/"+parameters["humidity"]+"/"+parameters["sunlight"]
hum3 = "/"+parameters["humidity"]+"/"+parameters["temperature"]
hum4 = "/"+parameters["humidity"]+"/"+parameters["soilmoisture"]
hum5 = "/"+parameters["humidity"]+"/"+parameters["waterlevel"]

# predict water level with parameters APIs
wat1 = "/"+parameters["waterlevel"]+"/"+parameters["ph"]
wat2 = "/"+parameters["waterlevel"]+"/"+parameters["sunlight"]
wat3 = "/"+parameters["waterlevel"]+"/"+parameters["humidity"]
wat4 = "/"+parameters["waterlevel"]+"/"+parameters["temperature"]
wat5 = "/"+parameters["waterlevel"]+"/"+parameters["soilmoisture"]

# predict soil moisture with parameters APIs
sol1 = "/"+parameters["soilmoisture"]+"/"+parameters["ph"]
sol2 = "/"+parameters["soilmoisture"]+"/"+parameters["sunlight"]
sol3 = "/"+parameters["soilmoisture"]+"/"+parameters["humidity"]
sol4 = "/"+parameters["soilmoisture"]+"/"+parameters["temperature"]
sol5 = "/"+parameters["soilmoisture"]+"/"+parameters["waterlevel"]


# result
result = {

}

# Load models
phm1 = joblib.load("./ph/PHvsSUNLIGHT.joblib")
phm2 = joblib.load("./ph/PHvsHUMIDITY.joblib")
phm3 = joblib.load("./ph/PHvsTEMPERATURE.joblib")
phm4 = joblib.load("./ph/PHvsSOIL MOISTURE.joblib")
phm5 = joblib.load("./ph/PHvsWATER LEVEL.joblib")

sum1 = joblib.load("./sunlight/SUNLIGHTvsPH.joblib")
sum2 = joblib.load("./sunlight/SUNLIGHTvsHUMIDITY.joblib")
sum3 = joblib.load("./sunlight/SUNLIGHTvsTEMPERATURE.joblib")
sum4 = joblib.load("./sunlight/SUNLIGHTvsSOIL MOISTURE.joblib")
sum5 = joblib.load("./sunlight/SUNLIGHTvsWATER LEVEL.joblib")

temm1 = joblib.load("./temperature/TEMPERATUREvsPH.joblib")
temm2 = joblib.load("./temperature/TEMPERATUREvsSUNLIGHT.joblib")
temm3 = joblib.load("./temperature/TEMPERATUREvsHUMIDITY.joblib")
temm4 = joblib.load("./temperature/TEMPERATUREvsSOIL MOISTURE.joblib")
temm5 = joblib.load("./temperature/TEMPERATUREvsWATER LEVEL.joblib")

humm1 = joblib.load("./humidity/HUMIDITYvsPH.joblib")
humm2 = joblib.load("./humidity/HUMIDITYvsSUNLIGHT.joblib")
humm3 = joblib.load("./humidity/HUMIDITYvsTEMPERATURE.joblib")
humm4 = joblib.load("./humidity/HUMIDITYvsSOIL MOISTURE.joblib")
humm5 = joblib.load("./humidity/HUMIDITYvsWATER LEVEL.joblib")

watm1 = joblib.load("./waterlevel/WATER LEVELvsPH.joblib")
watm2 = joblib.load("./waterlevel/WATER LEVELvsSUNLIGHT.joblib")
watm3 = joblib.load("./waterlevel/WATER LEVELvsHUMIDITY.joblib")
watm4 = joblib.load("./waterlevel/WATER LEVELvsTEMPERATURE.joblib")
watm5 = joblib.load("./waterlevel/WATER LEVELvsSOIL MOISTURE.joblib")

solm1 = joblib.load("./soilmoisture/SOIL MOISTUREvsPH.joblib")
solm2 = joblib.load("./soilmoisture/SOIL MOISTUREvsSUNLIGHT.joblib")
solm3 = joblib.load("./soilmoisture/SOIL MOISTUREvsHUMIDITY.joblib")
solm4 = joblib.load("./soilmoisture/SOIL MOISTUREvsTEMPERATURE.joblib")
solm5 = joblib.load("./soilmoisture/SOIL MOISTUREvsWATER LEVEL.joblib")


@cross_origin()
@app.route("/", methods=["GET"])
def index1():
    return "Predictive analysis of hydroponic using hydroponic system"


# predict with ph


@cross_origin()
@app.route(ph1, methods=["POST", "GET"])
def fun1():
    # predict humidity with ph
    form_data = json.loads(request.data)
    data = float(form_data["data"])
    result["val"] = phm1.predict([[data]])[0]
    result["MAE"] = model_errors["pe1"]
    print(phm1.predict([[data]]))
    return jsonify(result)


@app.route(ph2, methods=["POST", "GET"])
def fun2():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = phm2.predict([[data]])[0]
    result["MAE"] = model_errors["pe2"]
    return jsonify(result)


@app.route(ph3, methods=["POST", "GET"])
def fun3():
    form_data = json.loads(request.data)
    print(form_data)
    data = float128(form_data["data"])
    result["val"] = phm3.predict([[data]])[0]
    result["MAE"] = model_errors["pe3"]
    return jsonify(result)


@app.route(ph4, methods=["POST", "GET"])
def fun4():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = phm4.predict([[data]])[0]
    result["MAE"] = model_errors["pe4"]
    return jsonify(result)


@app.route(ph5, methods=["POST", "GET"])
def fun5():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = phm5.predict([[data]])[0]
    result["MAE"] = model_errors["pe5"]
    return jsonify(result)

# sunlight with parameters


@app.route(su1, methods=["POST", "GET"])
def fun6():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = sum1.predict([[data]])[0]
    result["MAE"] = model_errors["su1"]
    return jsonify(result)


@app.route(su2, methods=["POST", "GET"])
def fun7():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = sum2.predict([[data]])[0]
    result["MAE"] = model_errors["su2"]
    return jsonify(result)


@app.route(su3, methods=["POST", "GET"])
def fun8():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = sum3.predict([[data]])[0]
    result["MAE"] = model_errors["su3"]
    return jsonify(result)


@app.route(su4, methods=["POST", "GET"])
def fun9():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = sum4.predict([[data]])[0]
    result["MAE"] = model_errors["su4"]
    return jsonify(result)


@app.route(su5, methods=["POST", "GET"])
def fun10():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = sum5.predict([[data]])[0]
    result["MAE"] = model_errors["su5"]
    return jsonify(result)

# humidity with parameters


@app.route(hum1, methods=["POST", "GET"])
def fun11():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = humm1.predict([[data]])[0]
    result["MAE"] = model_errors["hum1"]
    return jsonify(result)


@app.route(hum2, methods=["POST", "GET"])
def fun12():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = humm2.predict([[data]])[0]
    result["MAE"] = model_errors["hum2"]
    return jsonify(result)


@app.route(hum3, methods=["POST", "GET"])
def fun13():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = humm3.predict([[data]])[0]
    result["MAE"] = model_errors["hum3"]
    return jsonify(result)


@app.route(hum4, methods=["POST", "GET"])
def fun14():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = humm4.predict([[data]])[0]
    result["MAE"] = model_errors["su4"]
    return jsonify(result)


@app.route(hum5, methods=["POST", "GET"])
def fun15():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = humm5.predict([[data]])[0]
    result["MAE"] = model_errors["hum5"]
    return jsonify(result)

# temperature with parameters


@app.route(tem1, methods=["POST", "GET"])
def fun16():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = temm1.predict([[data]])[0]
    result["MAE"] = model_errors["tem1"]
    return jsonify(result)


@app.route(tem2, methods=["POST", "GET"])
def fun17():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = temm2.predict([[data]])[0]
    result["MAE"] = model_errors["tem2"]
    return jsonify(result)


@app.route(tem3, methods=["POST", "GET"])
def fun18():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = temm3.predict([[data]])[0]
    result["MAE"] = model_errors["tem3"]
    return jsonify(result)


@app.route(tem4, methods=["POST", "GET"])
def fun19():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = temm4.predict([[data]])[0]
    result["MAE"] = model_errors["tem4"]
    return jsonify(result)


@app.route(tem5, methods=["POST", "GET"])
def fun20():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = temm5.predict([[data]])[0]
    result["MAE"] = model_errors["tem5"]
    return jsonify(result)


# waterlevel with parameters


@app.route(wat1, methods=["POST", "GET"])
def fun21():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = watm1.predict([[data]])[0]
    result["MAE"] = model_errors["wat1"]
    return jsonify(result)


@app.route(wat2, methods=["POST", "GET"])
def fun22():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = watm2.predict([[data]])[0]
    result["MAE"] = model_errors["wat2"]
    return jsonify(result)


@app.route(wat3, methods=["POST", "GET"])
def fun23():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = watm3.predict([[data]])[0]
    result["MAE"] = model_errors["wat3"]
    return jsonify(result)


@app.route(wat4, methods=["POST", "GET"])
def fun24():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = watm4.predict([[data]])[0]
    result["MAE"] = model_errors["wat4"]
    return jsonify(result)


@app.route(wat5, methods=["POST", "GET"])
def fun25():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = watm5.predict([[data]])[0]
    result["MAE"] = model_errors["wat5"]
    return jsonify(result)


# soil moisture with parameters


@app.route(sol1, methods=["POST", "GET"])
def fun26():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = solm1.predict([[data]])[0]
    result["MAE"] = model_errors["sol1"]
    return jsonify(result)


@app.route(sol2, methods=["POST", "GET"])
def fun27():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = solm2.predict([[data]])[0]
    result["MAE"] = model_errors["sol2"]
    return jsonify(result)


@app.route(sol3, methods=["POST", "GET"])
def fun28():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = solm3.predict([[data]])[0]
    result["MAE"] = model_errors["sol3"]
    return jsonify(result)


@app.route(sol4, methods=["POST", "GET"])
def fun29():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = solm4.predict([[data]])[0]
    result["MAE"] = model_errors["sol4"]
    return jsonify(result)


@app.route(sol5, methods=["POST", "GET"])
def fun30():
    form_data = json.loads(request.data)
    data = float128(form_data["data"])
    result["val"] = solm5.predict([[data]])[0]
    result["MAE"] = model_errors["sol5"]
    return jsonify(result)


# Run app
app.run()
