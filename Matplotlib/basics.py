import matplotlib.pyplot as plt
import numpy as np


# x = [1,2,3,4]
# y=[1,4,9,16]

# plt.plot(x,y,"o--b") # Tablo oluşturuyor. Linewidth kalınlık belirtir.
#                                  # -g ,-b gibi renk belirtebiliriz yada direk color="red" gibi de yapabiliriz.
#                                  # -- çizgiyi tireli hale getirir. başka özellikler için sitesine bakabilirsin.
#                                  # marker,çizgi tipi,renk


# plt.axis([0,6,0,20]) # x değerleri 0'dan 6'ya , y değerleri 0'dan 20'ye gider şekilde ayarlar

# plt.title("Grafik Başlığı") # Grafiğe başlık
# plt.xlabel("X Label") # yataya(x) başlık
# plt.ylabel("Y Label") # dikeye(y) başlık

# plt.show() # oluşan tabloyu açıyor. print gibi

#-------------------------------#


# x = np.linspace(0,2,100) # 0-2 arası 100 eşit parçaya böl

# plt.plot(x,x,label="linear",color="blue")
# plt.plot(x,x**2,label="quadratic",color="green")        # Çokomelli
# plt.plot(x,x**3,label="cubic",color="red")

# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.title("Simple Plot")

# plt.legend() # Çizgilerin labellarını? belirtir(sol yukarı)  # Buda çokomelli


# plt.show()

#-----------------------------#

# x =np.linspace(0,2,100)

# fig,axs = plt.subplots(3) # 3 axs alanı oluştur?        # Çokomel

# axs[0].plot(x,x,color="red")
# axs[0].set_title("linear")

# axs[1].plot(x,x**2,color="green")
# axs[1].set_title("quadratic")

# axs[2].plot(x,x**3,color="black")
# axs[2].set_title("cubic")

# plt.tight_layout() # başlıkların grafiklere girmesini fln engelliyor        # Çokomel

# plt.show()

#----------------------------#

# x =np.linspace(0,2,100)
# fig,axs = plt.subplots(2,2) # 2ye 2 toplam 4 axs alanı oluştur?
# fig.suptitle("grafik başlığı")

# axs[0,0].plot(x,x,color="red")
# axs[0,1].plot(x,x**2,color="blue")
# axs[1,0].plot(x,x**3,color="green")
# axs[1,1].plot(x,x**4,color="black")


# plt.show()

#----------------------------#

# import pandas as pd

# df =pd.read_csv("C:/Users/Melih/Desktop/hersey/VisualStudioCode/Pandas/nba/all_seasons.csv")

# df=df.drop(["player_name"],axis=1).groupby("team_abbreviationteam_abbreviation").mean()

# df.plot(subplots=True)
# plt.legend()
# plt.show()

#----------------------------#
import pandas as pd

# Veriyi oku
df = pd.read_csv("C:/Users/Melih/Desktop/hersey/VisualStudioCode/Pandas/nba/all_seasons.csv")

# Sayısal olmayan sütunları düşür
df_numeric = df.drop(["player_name"], axis=1)

# Sayısal sütunlarda eksik değerleri doldur (opsiyonel)
df_numeric.fillna(df_numeric.mean(), inplace=True)

# Takım bazında ortalama değerleri hesapla
df_mean = df_numeric.groupby("team_abbreviation").mean()

# Grafikleri çizdir
df_mean.plot(subplots=True, legend=True)
plt.show()
