import numpy as np
import matplotlib.pyplot as plt


def f(x1,x2):
    FunkPart1 = np.sqrt(abs(x2-0.01*(x2**2)))
    FunkPart2 = np.abs(x1+10)
    Fullfunk = 100 * FunkPart1 + 0.01 * FunkPart2
    return Fullfunk

x10, x20 = -10.0, 1.0
y0 = f(x10, x20)
x1 = np.linspace(-15.0, -5.0, 1000)
x2 = np.linspace(-3.0, 3.0, 1000)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

fig = plt.figure(figsize=(12, 9))
ax1 = fig.add_subplot(2,2,1, projection='3d')
ax1.plot_surface(X1, X2, Y, cmap ='viridis')
ax1.set_xlabel('X1')
ax1.set_ylabel('X2')
ax1.set_zlabel('y=f(x1,x2)')
ax1.set_title('изометрическом виде')

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.plot_surface(X1, X2, Y, cmap='viridis')
ax2.view_init(elev=90, azim=-90)
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_zlabel('y=f(x1, x2)')
ax2.set_title('Вид сверху')

ax3 = fig.add_subplot(2, 2, 3)
x1_line = np.linspace(-15.0, -5.0, 200)
y_line = f(x1_line, x20)
ax3.plot(x1_line, y_line)
ax3.set_xlabel('x1')
ax3.set_ylabel('y=f(x1, x2)')
ax3.set_title(f'y=f(x1) при x2={x20}')

ax4 = fig.add_subplot(2, 2, 4)
x2_line = np.linspace(-3.0, 3.0, 200)
y_line2 = f(x10, x2_line)
ax4.plot(x2_line, y_line2)
ax4.set_xlabel('x2')
ax4.set_ylabel('y=f(x1, x2)')
ax4.set_title(f'y=f(x2) при x1={x10}')

fig.suptitle(f'x10={x10}, x20={x20}, f(x10,x20)={y0}')
plt.tight_layout()
plt.show()
