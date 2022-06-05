# predict humidity with
humidity1 = "/"+parameters["humidity"]+"/"+parameters["ph"]
humidity2 = "/"+parameters["humidity"]+"/"+parameters["sunlight"]
humidity3 = "/"+parameters["humidity"]+"/"+parameters["temperature"]
humidity4 = "/"+parameters["humidity"]+"/"+parameters["waterlevel"]
humidity5 = "/"+parameters["humidity"]+"/"+parameters["soilmoisture"]

# predict sunlight with
sunlight1 = "/"+parameters["sunlight"]+"/"+parameters["humidity"]
sunlight2 = "/"+parameters["sunlight"]+"/"+parameters["ph"]
sunlight3 = "/"+parameters["sunlight"]+"/"+parameters["temperature"]
sunlight4 = "/"+parameters["sunlight"]+"/"+parameters["waterlevel"]
sunlight5 = "/"+parameters["sunlight"]+"/"+parameters["soilmoisture"]

# predict temperature with
temperature1 = "/"+parameters["temperature"]+"/"+parameters["humidity"]
temperature2 = "/"+parameters["temperature"]+"/"+parameters["sunlight"]
temperature3 = "/"+parameters["temperature"]+"/"+parameters["ph"]
temperature4 = "/"+parameters["temperature"]+"/"+parameters["waterlevel"]
temperature5 = "/"+parameters["temperature"]+"/"+parameters["soilmoisture"]

# predict soilmoisture with
soilmoisture1 = "/"+parameters["soilmoisture"]+"/"+parameters["humidity"]
soilmoisture2 = "/"+parameters["soilmoisture"]+"/"+parameters["sunlight"]
soilmoisture3 = "/"+parameters["soilmoisture"]+"/"+parameters["temperature"]
soilmoisture4 = "/"+parameters["soilmoisture"]+"/"+parameters["waterlevel"]
soilmoisture5 = "/"+parameters["soilmoisture"]+"/"+parameters["ph"]

# predict waterlevel with
waterlevel1 = "/"+parameters["waterlevel"]+"/"+parameters["humidity"]
waterlevel2 = "/"+parameters["waterlevel"]+"/"+parameters["sunlight"]
waterlevel3 = "/"+parameters["waterlevel"]+"/"+parameters["temperature"]
waterlevel4 = "/"+parameters["waterlevel"]+"/"+parameters["ph"]
waterlevel5 = "/"+parameters["waterlevel"]+"/"+parameters["soilmoisture"]


# Predicting humidity with

@app.route(humidity1, methods=["POST", "GET"])
def fun6():
    return "Predict humidity with ph"


@app.route(humidity2, methods=["POST", "GET"])
def fun7():
    return "Predict humidity with sunlight"


@app.route(humidity3, methods=["POST", "GET"])
def fun8():
    return "Predict humidity with temperature"


@app.route(humidity4, methods=["POST", "GET"])
def fun9():
    return "Predict humidity with waterlevel"


@app.route(humidity5, methods=["POST", "GET"])
def fun10():
    return "Predict humidity with soilmoisture"

# Predicting temperature with


@app.route(temperature1, methods=["POST", "GET"])
def fun11():
    return "Predict temperature with humidity"


@app.route(temperature2, methods=["POST", "GET"])
def fun12():
    return "Predict temperature with sunlight"


@app.route(temperature3, methods=["POST", "GET"])
def fun13():
    return "Predict temperature with ph"


@app.route(temperature4, methods=["POST", "GET"])
def fun14():
    return "Predict temperature with waterlevel"


@app.route(temperature5, methods=["POST", "GET"])
def fun15():
    return "Predict temperature with soilmoisture"

# Predicting sunlight with


@app.route(sunlight1, methods=["POST", "GET"])
def fun16():
    return "Predict sunlight with humidity"


@app.route(sunlight2, methods=["POST", "GET"])
def fun17():
    return "Predict sunlight with ph"


@app.route(sunlight3, methods=["POST", "GET"])
def fun18():
    return "Predict sunlight with temperature"


@app.route(sunlight4, methods=["POST", "GET"])
def fun19():
    return "Predict sunlight with waterlevel"


@app.route(sunlight5, methods=["POST", "GET"])
def fun20():
    return "Predict sunlight with soilmoisture"

# Predicting soil moisture with


@app.route(soilmoisture1, methods=["POST", "GET"])
def fun21():
    return "Predict soilmoisture with humidity"


@app.route(soilmoisture2, methods=["POST", "GET"])
def fun22():
    return "Predict soilmoisture with sunlight"


@app.route(soilmoisture3, methods=["POST", "GET"])
def fun23():
    return "Predict soilmoisture with temperature"


@app.route(soilmoisture4, methods=["POST", "GET"])
def fun24():
    return "Predict soilmoisture with waterlevel"


@app.route(soilmoisture5, methods=["POST", "GET"])
def fun25():
    return "Predict soilmoisture with ph"

# Predicting water level with


@app.route(waterlevel1, methods=["POST", "GET"])
def fun26():
    return "Predict waterlevel with humidity"


@app.route(waterlevel2, methods=["POST", "GET"])
def fun27():
    return "Predict waterlevel with sunlight"


@app.route(waterlevel3, methods=["POST", "GET"])
def fun28():
    return "Predict waterlevel with temperature"


@app.route(waterlevel4, methods=["POST", "GET"])
def fun29():
    return "Predict waterlevel with ph"


@app.route(waterlevel5, methods=["POST", "GET"])
def fun30():
    return "Predict waterlevel with soilmoisture"
