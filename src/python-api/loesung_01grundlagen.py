import pandas as pd
import matplotlib.pyplot as plt

#Aufgabe a)
df = pd.read_csv("../../notebooks/daten/haeuser.csv")
print(df.head())

#Lösung
#$ python loesung_01grundlagen.py 
#groesse_m2  zimmer  baujahr  preis_euro
#0          65       2     1990      180000
#1          80       3     2005      240000
#2         120       4     2010      380000
#3          45       1     1975      130000
#4          95       3     2015      310000

#Aufgabe b)
print("Form:",df.shape)
#Lösung: Form: (20, 4)

print("Spalten:",df.columns.tolist() )
df.info()
#Lösung
# Spalten: ['groesse_m2', 'zimmer', 'baujahr', 'preis_euro']
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 20 entries, 0 to 19
#Data columns (total 4 columns):
 #   Column      Non-Null Count  Dtype
#---  ------      --------------  -----
 #0   groesse_m2  20 non-null     int64
# 1   zimmer      20 non-null     int64
# 2   baujahr     20 non-null     int64
# 3   preis_euro  20 non-null     int64

#Aufgabe c)
#Durchschnittspreis
durchschnittspreis = df["preis_euro"].mean()
print("Durchschnittspreis:", durchschnittspreis)
#Lösung:Durchschnittspreis: 276400.0

#Teuerster Preis
teuerster_preis = df["preis_euro"].max()
print("Teuerster Preis:", teuerster_preis)
#Lösung: Teuerster Preis: 450000

#Günstigster Preis
guenstigster_preis = df["preis_euro"].min()
print("Günstigster Preis:", guenstigster_preis)
#Lösung: Günstigster Preis: 130000

#Aufgabe d)
#Histogramm der Hauspreise
plt.hist(df["preis_euro"], bins=20,color="steelblue", edgecolor="black")
plt.show()