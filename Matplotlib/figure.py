import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20) # -10 la 9 arasını 20 eşit parçaya ayırır
y = x**3
z = x**2


#--------------------#
# figure = plt.figure()

# axes_cube = figure.add_axes([0.1,0.1,0.8,0.8]) # figure üzerine eklenecek axes alanın konumu
# axes_cube.plot(x,y,'b')
# axes_cube.set_xlabel("X Axis")
# axes_cube.set_ylabel("Y Axis")
# axes_cube.set_title("Cube")

# axes_square = figure.add_axes([0.15,0.6,0.25,0.25]) # soldan alttan genişlik yükseklik?
# axes_square.plot(x,y,'r')
# axes_square.set_xlabel("X Axis")
# axes_square.set_ylabel("Y Axis")
# axes_square.set_title("Square")

#--------------------#

# figure = plt.figure()

# axes = figure.add_axes([0,0,1,1]) # 0,0,1,1 bütün ekranı kaplar

# axes.plot(x,y,label="Square")
# axes.plot(x,z,label="Cube")
# axes.legend(loc=1) # loc ile legendın grafikte nereye geleceğini ayarlarız

#-------------------3

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(4,4)) # 2 satır 1 kolon. figsize grafik açıldığındaki boyutu belirler

axes[0].plot(x,y)
axes[0].set_title("Square")
axes[1].plot(x,z)
axes[1].set_title("Cube")

plt.tight_layout()
# fig.savefig("figure1.png") # grafiği figure1.png adıyla yukarıda figsize'a verdiğimiz değerlere göre bir png oluşturur
fig.savefig("figure1.pdf") # grafiği figure1.pdf adıyla yukarıda figsize'a verdiğimiz değerlere göre bir pdf oluşturur

plt.show()