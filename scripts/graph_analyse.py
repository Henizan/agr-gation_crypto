#import des librairies
import pandas as pd
import matplotlib.pyplot as plt

#chargement des données
df_fg = pd.read_csv("C:/ece_B3/projet_agr_crypto/data/exports/btc_fear_greed.csv") 
df_vol = pd.read_csv("C:/ece_B3/projet_agr_crypto/data/exports/volume_crypto.csv")
df_fg['date'] = pd.to_datetime(df_fg['date'])


#volume
fig, ax = plt.subplots(figsize=(7,4)) # Création d'une figure et d'un axe pour le graphique

ax.barh(df_vol['crypto'], df_vol['volume_moyen'], color=['orange', 'purple', 'deepskyblue']) # Création d'un graphique à barres horizontales
ax.set_xlabel("Volume moyen (USD)") # Étiquette de l'axe des x
ax.set_title("Volume moyen par crypto (BTC / ETH / XRP)") # Titre du graphique
ax.invert_yaxis() # Inverser l'axe des y pour que la plus grande barre soit en haut


for i, v in enumerate(df_vol['volume_moyen']): # Ajouter des étiquettes de valeur à chaque barre
    ax.text(v + v*0.02, i, f"{v:,.0f}", va='center', fontsize=9) # Positionner le texte légèrement à droite de chaque barre

plt.show() # Afficher le graphique


#fear_greed_btc
fig, ax1 = plt.subplots(figsize=(10,5)) # Création d'une figure et d'un axe pour le graphique

ax1.bar(df_fg['date'], df_fg['fear_greed_value'], color='lightgreen', alpha=0.6, label='Fear & Greed Index') # Création d'un graphique à barres pour l'indice Fear & Greed
ax1.set_ylabel("Fear & Greed Index", color='green') # Étiquette de l'axe des y pour l'indice
ax1.tick_params(axis='y', labelcolor='green') # Couleur des étiquettes de l'axe des y

ax2 = ax1.twinx() # Création d'un second axe y partageant le même axe x
ax2.plot(df_fg['date'], df_fg['close'], color='blue', linewidth=2, label='BTC Close') # Création d'un graphique en ligne pour le prix de clôture du BTC
ax2.set_ylabel("BTC Price (USD)", color='blue') # Étiquette de l'axe des y pour le prix du BTC
ax2.tick_params(axis='y', labelcolor='blue') # Couleur des étiquettes de l'axe des y

plt.title("Évolution du Bitcoin et du sentiment du marché", fontsize=13) # Titre du graphique
plt.show() # Afficher le graphique


#fear_greed_btc covid
covid = df_fg[(df_fg['date'] >= '2020-03-01') & (df_fg['date'] <= '2021-12-31')] # Filtrer les données pour la période COVID

fig, ax1 = plt.subplots(figsize=(10, 5)) # Création d'une figure et d'un axe pour le graphique

ax1.fill_between(covid_period['date'], covid['fear_greed_value'], color='limegreen', alpha=0.3) # Remplir la zone sous la courbe de l'indice Fear & Greed
ax1.set_ylabel("Fear & Greed Index", color='green') # Étiquette de l'axe des y pour l'indice
ax1.tick_params(axis='y', labelcolor='green') # Couleur des étiquettes de l'axe des y

ax2 = ax1.twinx() # Création d'un second axe y partageant le même axe x
ax2.plot(covid_period['date'], covid['close'], color='darkblue', linewidth=2) # Création d'un graphique en ligne pour le prix de clôture du BTC
ax2.set_ylabel("BTC Price (USD)", color='darkblue') # Étiquette de l'axe des y pour le prix du BTC
ax2.tick_params(axis='y', labelcolor='darkblue') # Couleur des étiquettes de l'axe des y

plt.title("Bitcoin & Sentiment du Marché pendant la période COVID (2020–2021)", fontsize=13, weight='bold') # Titre du graphique
plt.show() # Afficher le graphique