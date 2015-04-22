import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-6, 6, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.xlabel("t")
plt.ylabel("cos(t)")
plt.show()
image = np.random.rand(50, 50)
plt.imshow(image, cmap=plt.cm.gray)
plt.show()