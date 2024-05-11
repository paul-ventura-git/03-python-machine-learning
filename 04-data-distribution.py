import numpy
# pip install matplotlib
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 50.0, 260)

plt.hist(x, 10)
plt.show()