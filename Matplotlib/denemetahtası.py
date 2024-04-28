import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,3) # 2ye 2 toplam 4 axs alanı oluştur?
fig.suptitle("grafik başlığı")

axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="blue")
axs[0,2].plot(x,x**3,color="green")
axs[1,0].plot(x,x**4,color="black")
axs[1,1].plot(x,x**5,color="yellow")
axs[1,2].plot(x,x**6,color="purple")


plt.show()