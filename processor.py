import re
from numpy import random

import argparse

parser = argparse.ArgumentParser(description="processortt",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--file", default='', type=str, help="specify file name")
parser.add_argument("-o", "--output", default='', type=str, help="specify output file name")


args = parser.parse_args()
config = vars(args)
print(config)

data = open(config["file"], 'r').read()
data = re.sub(r'(?<=([.]\d{3}))\d*','',data)
data = re.sub(r'G0','G0 Z6\nG0',data)
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,4):
            for l in range (1,4):
                data = re.sub(rf'(?<=(G0 X\d{{{i}}}.\d{{{k}}} Y\d{{{j}}}.\d{{{l}}}))\n','\nG0 Z5\n',data)
data = re.sub(r'G1','G0',data)
data = re.sub(r'F\d*','F5000',data)
data = re.sub(r'^([^\n]*\n){2}','G21\nG90\nG0 Z5 F1000\n',data)
data = re.sub(r'\nM2','G0 Z10',data)

#offset
data = re.sub(r'(?<=X)(\d*[.]\d*|(\d*))',lambda m : str(float(m.group(0))+40),data)
data = re.sub(r'(?<=Y)(\d*[.]\d*|(\d*))',lambda m : str(float(m.group(0))+17),data)
data = re.sub(r'(?<=([.]\d{3}))\d*','',data)


data = re.sub(r';.*',';svg',data)
# random shift
#print(indices)
indices = [(m.start(0), m.end(0)) for m in re.finditer(r'(?<=;svg)\nG0 Z6\nG0 X\d*[.]\d* Y\d*[.]\d*\nG0 Z5\n', data)]
for id,n in enumerate(indices[:-1]):
    print(id)
    off = random.normal(0,0.3)
    windices = [(m.start(0), m.end(0)) for m in re.finditer(r'(?<=;svg)\nG0 Z6\nG0 X\d*[.]\d* Y\d*[.]\d*\nG0 Z5\n', data)]
    st = windices[id][1]
    su = windices[id][0]
    en = windices[id+1][0]
    # data = re.sub(rf'^[\s\S]{{{st}}} (?<=Y)(\d*[.]\d*|(\d*)) [\s\S]{{{len(data)-en}}}$',lambda m : str(float(m.group(0))+off),data)
    # data = re.sub(rf'^[\s\S]{{{su}}} (?<=Y)(\d*[.]\d*|(\d*)) [\s\S]{{{len(data)-st}}}$',lambda m : str(float(m.group(0))+off),data)

    data = data[:st]+re.sub(r'(?<=Y)(\d*[.]\d*|(\d*))',lambda m : str(float(m.group(0))+off),data[st:en])+data[en:]
    data = data[:su]+re.sub(r'(?<=Y)(\d*[.]\d*|(\d*))',lambda m : str(float(m.group(0))+off),data[su:st])+data[st:]


#data = re.sub(r'(?<=Y)(\d*[.]\d*|(\d*))',lambda m : str(float(m.group(0))+random.normal(0,0.1)),data)

f = open(config["output"], "w")
f.write(data) 
