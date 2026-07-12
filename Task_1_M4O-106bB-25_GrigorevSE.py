import os
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    A = 1.34941
    FuncPart1 = np.sin(x) * np.sin(A)
    FuncPart2 = np.abs(100 - np.sqrt(x**2 + A**2) / np.pi)
    FullFunc = -0.0001 * (np.abs(FuncPart1 * np.exp(FuncPart2)) + 1)**0.1
    return FullFunc

Start = -10
Stop = 10
Step = 0.01
values_X = np.arange(Start, Stop + Step, Step)
values_Y = f(values_X)
result = np.sum(values_Y)
total_points = len(values_X)

results_dir = "results"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)
xml_path = os.path.join(results_dir, "result.xml")

with open(xml_path, "w", encoding="utf-8") as xml_file:
    xml_file.write('<?xml version="1.1" encoding="UTF-8" ?>\n')
    xml_file.write('<data>\n')
    xml_file.write(' <xdata>\n')
    xml_file.write(f'{total_points}\n')
    for x_val in values_X:
        xml_file.write(f' <x>{x_val}</x>\n')
    xml_file.write(' </xdata>\n')
    xml_file.write(' <ydata>\n')
    for y_val in values_Y:
        xml_file.write(f' <y>{y_val}</y>\n')
    xml_file.write(' </ydata>\n')
    xml_file.write('</data>\n')

print(f"'result.xml'создан точек: {total_points}")
plt.figure()
plt.plot(values_X, values_Y)
plt.title("y = f(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()