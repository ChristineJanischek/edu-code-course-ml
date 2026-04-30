import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#Liest Daten aus der Datenquelle ein und bereitet sie für die Regression vor
df = pd.read_csv('../../notebooks/daten/haeuser.csv')
X = df[['groesse_m2']]
y = df['preis_euro']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Trainiert das lineare Regressionsmodell und bewertet es anhand von MSE und R2-Score
modell = LinearRegression()
modell.fit(X_train, y_train)
y_pred = modell.predict(X_test)
print('Koeffizient:', modell.coef_[0])
print('Intercept:', modell.intercept_)
print('MSE:', mean_squared_error(y_test, y_pred))
print('R2:', r2_score(y_test, y_pred))

#Visualisiert (Diagramm) die echten Werte und die Vorhersagen des Modells
plt.figure(figsize=(6,4))
plt.scatter(X_test, y_test, color='steelblue', label='Echte Werte')
plt.plot(X_test, y_pred, color='crimson', label='Regression')
plt.title('Lineare Regression: Groesse -> Preis')
plt.xlabel('Groesse (m2)')
plt.ylabel('Preis (Euro)')
plt.legend()
plt.tight_layout()
plt.savefig('regression_groesse_preis.png', dpi=150)
plt.show()

## Reflexion
#Was sagt der Koeffizient inhaltlich aus?
#Der Koeffizient ist die Steigung der Regressionsgeraden.Inhaltlich bedeutet er hier:
# Pro zusätzlichem 1 m² Wohnfläche ändert sich der 
# vorhergesagte Preis im Mittel um genau diesen Koeffizienten 
# (in Euro).Beispiel:Wenn der Koeffizient 3200 ist, dann sagt das Modell:+1 m² → etwa +3200 Euro erwarteter Preis.

#Wo liegen Grenzen des Modells?
# Kurz: Das Modell ist gut fuer einen 
# einfachen ersten Trend, aber zu simpel 
# fuer realistische, praezise Preisprognosen.