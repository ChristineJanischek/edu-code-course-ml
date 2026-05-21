import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#Liest Daten aus der Datenquelle ein und bereitet sie für die Regression vor
df = pd.read_csv('../../notebooks/daten/studierende_noten.csv')
print(df.head)

#Kennzahlen
mean_note =df["note"].mean()
min_note = df["note"].min()
max_note = df["note"].min()
print("Durchschnitt: ",mean_note)
print("Minimum:",min_note )
print("Maximum:", max_note)

X = df[["lern_stunden","anwesenheit_prozent","uebungen_bearbeitet"]]
y = df['note']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Trainiert das lineare Regressionsmodell und bewertet es anhand von MSE und R2-Score
modell = LinearRegression()
modell.fit(X_train, y_train)
y_pred = modell.predict(X_test)
print('Koeffizient:', modell.coef_[0])
print('Intercept:', modell.intercept_)
print('MSE:', mean_squared_error(y_test, y_pred))
print('R2:', r2_score(y_test, y_pred))

