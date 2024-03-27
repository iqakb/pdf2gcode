import re


data = open('gcode/becus.gcode', 'r').read()
data = re.sub(r'(?<=([.]\d{3}))\d*','',data)
data = re.sub(r'G0','G0 Z6\nG0',data)
for i in range(1,5):
    for j in range(1,5):
        data = re.sub(rf'(?<=(G0 X\d{{{i}}}.\d{{3}} Y\d{{{j}}}.\d{{3}}))\n','\nG0 Z5\n',data)
data = re.sub(r'G1','G0',data)
data = re.sub(r'F\d*','',data)
data = re.sub(r'^([^\n]*\n){2}','G21\nG90\nG0 Z5 F1000\n',data)
data = re.sub(r'\nM2','G0 Z10',data)

f = open("gcode/becus2.gcode", "w")
f.write(data) 