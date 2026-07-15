import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('--style', choices=['solid', 'dashed', 'dotted'], default='solid')
args = parser.parse_args()

import matplotlib.pyplot as plt

def Read_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    x_data_point = root.find('xdata')
    y_data_point = root.find('ydata')
    x_values = []
    y_values = []
    for x_element in x_data_point.findall('x'):
        x_values.append(float(x_element.text))
    for y_element in y_data_point.findall('y'):
        y_values.append(float(y_element.text))
    return x_values, y_values


line_styles = {
    'solid': '-',
    'dashed': '--',
    'dotted': ':'
}
matplotlib_style = line_styles[args.style]
x_values, y_values = Read_file(args.input_file)

plt.plot(x_values, y_values, linestyle=matplotlib_style)
plt.title('гр. функции y=f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
