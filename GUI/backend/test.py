import joblib
# file names
labels = ["PH", "SUNLIGHT", "HUMIDITY",
          "TEMPERATURE", "SOIL MOISTURE", "WATER LEVEL"]

md = "vs"
name = labels[0] + md + labels[1]

phm1 = joblib.load("./ph/PHvsHUMIDITY.joblib")
phm2 = joblib.load("./ph/PHvsSOIL MOISTURE.joblib")
phm3 = joblib.load("./ph/PHvsSUNLIGHT.joblib")
phm4 = joblib.load("./ph/PHvsTEMPERATURE.joblib")
phm5 = joblib.load("./ph/PHvsWATER LEVEL.joblib")

print(phm1.predict([[7.5]]))
print(phm2.predict([[7.5]]))
print(phm3.predict([[7.5]]))
print(phm4.predict([[7.5]]))
print(phm5.predict([[7.5]]))
