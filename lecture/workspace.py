import numpy as np
import matplotlib.pyplot as plt

l1 = 10
l2 = 10
def fk(theta_1, theta_2, length1, length2):
    theta_1 = np.deg2rad(theta_1)
    theta_2 = np.deg2rad(theta_2)
    x = length1*np.cos(theta_1) + length2 * np.cos(theta_1 + theta_2)
    y = length1*np.sin(theta_1) + length2 * np.sin(theta_1 + theta_2)
    return x,y

def mainp(theta_1, theta_2, length1, length2):
    theta_1 = np.deg2rad(theta_1)
    theta_2 = np.deg2rad(theta_2)

    x_1 = length1*np.cos(theta_1)  
    y_1 = length1 * np.cos(theta_1)

    x_2, y_2 = fk(theta_1, theta_2, length1, length2)
    return [[0,0], [x_1, y_1], [x_2, y_2]]

x_p = []
y_p = []

for i in range(0, 365, 5):
    for j in range(-90, 95, 5):
        xx, yy = fk(i, j, l1, l2)
        x_p.append(xx)
        y_p.append(yy)

theta1 = 0
theta2 = 10

#plot_list = mainp(theta1, theta2, l1, l2)
#plt.plot([plot_list[0][0], plot_list[1][0]], [plot_list[0][1], plot_list[1][1]], 'k-', lw=2)
#plt.plot([plot_list[1][0], plot_list[2][0]], [plot_list[1][1], plot_list[2][1]], 'k-', lw=2)

plt.scatter(x_p, y_p)
plt.show()
