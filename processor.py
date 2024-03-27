import re


data = open('gcode/lorem.gcode', 'r').read()
data = re.sub(r'(?<=([.]\d{3}))\d*','',data)
data = re.sub(r'G0','G0 Z6\nG0',data)
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,4):
            for l in range (1,4):
                data = re.sub(rf'(?<=(G0 X\d{{{i}}}.\d{{{k}}} Y\d{{{j}}}.\d{{{l}}}))\n','\nG0 Z5\n',data)
data = re.sub(r'G1','G0',data)
data = re.sub(r'F\d*','',data)
data = re.sub(r'^([^\n]*\n){2}','G21\nG90\nG0 Z5 F1000\n',data)
data = re.sub(r'\nM2','G0 Z10',data)

f = open("gcode/lorem2.gcode", "w")
f.write(data) 