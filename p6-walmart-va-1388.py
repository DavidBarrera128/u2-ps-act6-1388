import matplotlib.pyplot as plt
import numpy as np
# David Barrera NC = 1388
cant_productos = [10,150,200,300,500]
precio = [4000, 7000, 9000, 12000, 18000]

plt.plot(cant_productos,precio)
plt.show()

# perosnalizar grafica
plt.plot(cant_productos,precio,color="blue",marker="o",linestyle="dashed",linewidth=2,markersize=12)
plt.title("Ventas de walmart")
plt.xlabel(" cant_productos")
plt.ylabel("precios")
plt.show()
