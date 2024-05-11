import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

print(scaledX)

# Predict CO2 values
regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]]) # Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms:

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)