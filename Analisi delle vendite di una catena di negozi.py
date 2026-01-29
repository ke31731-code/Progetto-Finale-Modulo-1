import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Creazione di un dataframe attraverso l'utilizzo di un dizionario
dati = [
    {"Data": "2023-09-01", "Negozio": "Milano",   "Prodotto": "Smartphone", "Quantita": 5,  "Prezzo_unitario": 499.99},
    {"Data": "2023-09-01", "Negozio": "Roma",     "Prodotto": "Laptop",     "Quantita": 3,  "Prezzo_unitario": 899.00},
    {"Data": "2023-09-01", "Negozio": "Napoli",   "Prodotto": "TV",         "Quantita": 4,  "Prezzo_unitario": 649.90},
    {"Data": "2023-09-02", "Negozio": "Torino",   "Prodotto": "Tablet",     "Quantita": 6,  "Prezzo_unitario": 329.99},
    {"Data": "2023-09-02", "Negozio": "Firenze",  "Prodotto": "Cuffie",     "Quantita": 11, "Prezzo_unitario": 89.90},
    {"Data": "2023-09-02", "Negozio": "Milano",   "Prodotto": "Smartphone", "Quantita": 8,  "Prezzo_unitario": 489.50},
    {"Data": "2023-09-03", "Negozio": "Roma",     "Prodotto": "Laptop",     "Quantita": 2,  "Prezzo_unitario": 950.00},
    {"Data": "2023-09-03", "Negozio": "Napoli",   "Prodotto": "TV",         "Quantita": 5,  "Prezzo_unitario": 599.00},
    {"Data": "2023-09-03", "Negozio": "Torino",   "Prodotto": "Tablet",     "Quantita": 3,  "Prezzo_unitario": 339.90},
    {"Data": "2023-09-04", "Negozio": "Milano",   "Prodotto": "Smartphone", "Quantita": 7,  "Prezzo_unitario": 510.00},
    {"Data": "2023-09-04", "Negozio": "Firenze",  "Prodotto": "Cuffie",     "Quantita": 14, "Prezzo_unitario": 79.99},
    {"Data": "2023-09-05", "Negozio": "Roma",     "Prodotto": "Laptop",     "Quantita": 4,  "Prezzo_unitario": 920.00},
    {"Data": "2023-09-05", "Negozio": "Napoli",   "Prodotto": "TV",         "Quantita": 3,  "Prezzo_unitario": 620.00},
    {"Data": "2023-09-06", "Negozio": "Milano",   "Prodotto": "Smartphone", "Quantita": 9,  "Prezzo_unitario": 495.00},
    {"Data": "2023-09-06", "Negozio": "Torino",   "Prodotto": "Tablet",     "Quantita": 5,  "Prezzo_unitario": 349.00},
    {"Data": "2023-09-06", "Negozio": "Firenze",  "Prodotto": "Cuffie",     "Quantita": 10, "Prezzo_unitario": 94.50},
    {"Data": "2023-09-07", "Negozio": "Roma",     "Prodotto": "Laptop",     "Quantita": 1,  "Prezzo_unitario": 880.00},
    {"Data": "2023-09-07", "Negozio": "Napoli",   "Prodotto": "TV",         "Quantita": 6,  "Prezzo_unitario": 580.00},
    {"Data": "2023-09-08", "Negozio": "Milano",   "Prodotto": "Smartphone", "Quantita": 6,  "Prezzo_unitario": 505.00},
    {"Data": "2023-09-08", "Negozio": "Torino",   "Prodotto": "Tablet",     "Quantita": 7,  "Prezzo_unitario": 319.99},
    {"Data": "2023-09-08", "Negozio": "Firenze",  "Prodotto": "Cuffie",     "Quantita": 9,  "Prezzo_unitario": 85.00},
    {"Data": "2023-09-09", "Negozio": "Roma",     "Prodotto": "Laptop",     "Quantita": 3,  "Prezzo_unitario": 940.00},
    {"Data": "2023-09-09", "Negozio": "Napoli",   "Prodotto": "TV",         "Quantita": 4,  "Prezzo_unitario": 610.00},
    {"Data": "2023-09-10", "Negozio": "Milano",   "Prodotto": "Smartphone", "Quantita": 5,  "Prezzo_unitario": 520.00},
    {"Data": "2023-09-10", "Negozio": "Torino",   "Prodotto": "Tablet",     "Quantita": 8,  "Prezzo_unitario": 329.00},
    {"Data": "2023-09-10", "Negozio": "Firenze",  "Prodotto": "Cuffie",     "Quantita": 12, "Prezzo_unitario": 92.00},
    {"Data": "2023-09-11", "Negozio": "Milano",   "Prodotto": "Smartphone", "Quantita": 4,  "Prezzo_unitario": 485.00},
    {"Data": "2023-09-11", "Negozio": "Roma",     "Prodotto": "Laptop",     "Quantita": 5,  "Prezzo_unitario": 910.00},
    {"Data": "2023-09-12", "Negozio": "Napoli",   "Prodotto": "TV",         "Quantita": 3,  "Prezzo_unitario": 590.00},
    {"Data": "2023-09-12", "Negozio": "Torino",   "Prodotto": "Tablet",     "Quantita": 6,  "Prezzo_unitario": 345.00},
]
#Creazione del dataframe e successivo salvataggio del file in formato csv
df = pd.DataFrame(dati)

df.to_csv("Vendite.csv")

#------------------------------------------------------ELABORARE I DATI CON PANDAS---------------------------------------------------------

print(f"\n Prime 5 righe del Dataframe: {df.head(5)}") #df.head(5) stampa le prime 5 righe del Df

#Stampa il numero totale di righe e colonne del Df con df.shape
print(f"\n Numero di righe e colonne presenti:\n", df.shape) 

#Stampa le informazioni generali del dataframe con df.info()
df.info()


df["Incasso"] = df["Quantita"] * df["Prezzo_unitario"] #Crea una nuova colonna ["Incasso"] per il DataFrame 

#Totale degli incassi della catena di negozi
incasso_totale = df["Incasso"].sum()
print(f"\n Incasso totale:\n {incasso_totale.round(2):.2f} €")

#Media degli incassi medi per negozio
incasso_negozio = df.groupby("Negozio")["Incasso"].mean()
print(f"\n Incasso medio in € per\n {incasso_negozio.round(2)}")

#Stampa solo i 3 prodotti più venduti
vendite_prodotto = df.groupby("Prodotto")["Quantita"].sum().nlargest(3)
print(f"\n I 3 prodotti più venduti", vendite_prodotto)

#Utilizzo groupby per raggruppare i dati delle colonne ["Negozio",Prodotto], per poi ricavare la medie degli incassi oer ognuna
incasso_medio = df.groupby(["Negozio", "Prodotto"])["Incasso"].mean()
print(f"\n Incasso medio per prodotto:\n", incasso_medio.round(2))

#-----------------------------------------ELABORARE I DATI CON NUMPY CON ARRAY BIDIMENSIONALI--------------------------------------

#Estraggo la colonna["Quantita"] per calcolarne la media con NumPy
q= df["Quantita"].to_numpy()
media = np.mean(q)


max= np.max(q)    #valore più alto presente nella colonna quantità (np.max)
min = np.min(q)   #valore più basso (np.min)
percentuale = (q > q.mean()).mean() * 100   #Formula per calcolare la percentuale media delle vendite
dev = np.std(q)

print(f"\n------:DATI STATISTICI DELLE VENDITE:---------") #Stampa dei valori statistici calcolati con annesso arrotondamento delle cifre 
print(f"\n Media delle quantità vendute: {media.round(2)} unità\n")#attraverso .round(2) per una lettura più comoda dei dati
print(f"Valore max delle quantità vendute: {max.round(2)} unità\n")
print(f"Valore min delle quantità vendute: {min.round(2)} unità\n")
print(f"Deviazione Standard: {dev.round(2)}\n")
print(f"Percentuale di vendite sopra la media: {percentuale.round(2)}%")

#Trasforma le colonne del df in un array 2D NumPy

arr = df.loc[:, ["Quantita", "Prezzo_unitario"]].to_numpy()#Usa df.loc per lavorare solo sulle colonne["Quantità", "Prezzo_unitario"]

print(f"\nArray NumPy 2D: Quantità|Prezzo unitario:\n", arr)

#Confronto di un array sugli incassi con la stessa colonna del DataFrame
incasso_num = arr[:,0] * arr[:,1] 
print(f"\n Incassi calcolati in array NumPy:\n {incasso_num}\n")
print(f"\n Incassi registrati nel Dataframe:\n{df["Incasso"].to_numpy()}")#Ho usato .to_numpy per una migliore visibilità di entrambi gli array


#-----------------------------------------ELABORARE GRAFICAMENTE I DATI CON MATPLOTLIB--------------------------------------------------


#Grafico a barre degli incassi per negozio
plt.figure(figsize=(10,6))
plt.bar(df["Negozio"], df["Incasso"], color= "skyblue", label= "Incasso")
plt.title("Incasso totale per negozio (in €)", color= "Black", fontsize= 10)
plt.ylabel("Incasso")
plt.xlabel("Negozio")
plt.grid(True, axis="y", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

#Grafico a torta delle percentuali di incasso per prodotti
plt.figure(figsize=(8,8))
incasso_prodotto = df.groupby("Prodotto")["Incasso"].sum()
plt.pie(incasso_prodotto, labels=incasso_prodotto.index, autopct="%1.1f%%")
plt.title("Percentuale di incasso per prodotto")
plt.tight_layout()
plt.show()

#Grafico a linee per andamento degli incassi della catena
plt.figure(figsize=(12,7)) 
incassi_daily = df.groupby("Data")["Incasso"].sum()
plt.plot(incassi_daily.index, incassi_daily.values, marker = "o", color="orange",linewidth= 2, label="Incasso")
plt.title("Andamento giornaliero degli incassi (in €)")
plt.grid(True, linestyle="--", alpha= 0.7)
plt.tight_layout()
plt.legend()
plt.show()


#-------------------------------------------------------ANALISI AVANZATA DEI DATI----------------------------------------

#Crea la nuova colonna "Categoria" che suddivide i prodottiattraverso l'uso di un dizionario
categorie={'Smartphone': 'Informatica',
    'Laptop':     'Informatica',
    'Tablet':     'Informatica',
    'TV':         'Elettrodomestici',
    'Cuffie':     'Elettrodomestici',}

df["Categoria"] = df["Prodotto"].map(categorie)

#Statistiche per categorie
incasso_categorie = df.groupby("Categoria")["Incasso"].sum().round(2) #Incasso totale per categorie(sum)
print(f"\n Incasso totale per", incasso_categorie)

vendita_media = df.groupby("Categoria")["Quantita"].mean().round(2)
print(f"\n Quantità media (in unità) venduta per {vendita_media}") #Vendite medie per categorie (mean)

print(df)
df.to_csv("vendite_analizzate.csv", index=False, encoding="utf-8") #utf-8 per formato scrittura più leggibile
print("Analisi salvata in formato CSV")


#------------------------------------------------------------ESTENSIONI----------------------------------------------------------------

#Utilizzo subplots() per creare un garfico combinato

fig,ax1= plt.subplots(figsize=(9,6)) #Dimensioni della figura

#Grafico a barre degli incassi medi per categoria
ax1.bar(incasso_categorie.index, incasso_categorie.values, width=0.50, color = "green", edgecolor="black", label="Incasso medio")
ax1.set_xlabel("Categoria")
ax1.set_ylabel("Incasso medio")
ax1.grid(axis="y", alpha=0.4) 


ax2= ax1.twinx() #twinx() mi serve per portare il grafico a linee verso l'asse Y

#Grafico a linea delle quantità medie vendute per categoria
ax2.plot (vendita_media.index, vendita_media.values , color="darkred", marker="o", markersize=6, linestyle="--", label = "Quantità media")
ax2.set_ylabel("Quantità media venduta", color="darkred")
plt.tight_layout()
plt.show()

#Funzione che riproduce una classifica dei migliori prodotti venduti per incasso(ho usato una top 3 come esempio)
def top_n_prodotti(n):
    return df.groupby("Prodotto")["Incasso"].sum().sort_values(ascending=False).head(n)

print(f"\n Top prodotti più venduti per incasso(in €):\n {top_n_prodotti(3).round(2)}")


    


































