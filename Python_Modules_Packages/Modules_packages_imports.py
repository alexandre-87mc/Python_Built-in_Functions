#Modules, packages and imports
import math
#Not using math.xxx
sq5_1 = 5**0.5
sq5_2 = math.sqrt(5)
print(sq5_1)
print(sq5_2)
#Not using import but using math.xx
from math import sqrt
print(sqrt(5))

#In python we have the powerfull option to install a bunch of libraries
#To install a librarie use the "pip install" command.

#Matplotlib Pie Charts
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.bar(y,2,10)
plt.show() 
