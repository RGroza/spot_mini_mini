import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

f = "logs/log3.csv"
data = pd.read_csv(f)

t = data["stepCount"][50:]
velX = data["velX"]
velY = data["velY"]
velZ = data["velZ"]
posX = data["posX"]
posY = data["posY"]
posZ = data["posZ"][50:]

# plt.plot(t, velX, label="x")
# plt.plot(t, velY, label="y")
# plt.plot(t, velZ, label="z")
# plt.legend(loc="upper left")

# plt.grid()

# plt.title('Velocities')
# plt.xlabel('Step Count')
# plt.ylabel('m/s')

# plt.show()
# plt.savefig("velXYZ.png")

# plt.plot(t, posX, label="x")
# plt.plot(t, posY, label="y")
plt.plot(t, posZ, label="z")
plt.legend(loc="upper left")

plt.grid()

plt.title('Positions')
plt.xlabel('Step Count')
plt.ylabel('m')

plt.show()
plt.savefig("posXYZ.png")

# numJoints = 12
# for j in range(numJoints):
#     plt.plot(data["q" + str(j)], label="q" + str(j))
#     plt.plot(data["u" + str(j)], label="u" + str(j))

# plt.legend(loc="upper left")

# plt.grid()

# plt.title('Joint Data')
# plt.xlabel('Step Count')
# plt.ylabel('')

# plt.show()
# plt.savefig("joints.png")
