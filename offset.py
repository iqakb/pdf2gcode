import re
from numpy import random

import argparse

parser = argparse.ArgumentParser(description="processortt",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--file", default='', type=str, help="specify file name")
parser.add_argument("-o", "--output", default='', type=str, help="specify output file name")
parser.add_argument("-x", "--xoff", default='', type=float, help="specify x offset (to the right)")
parser.add_argument("-y", "--yoff", default='', type=float, help="specify y offset (up)")


args = parser.parse_args()
config = vars(args)
print(config)

data = open(config["file"], 'r').read()
#offset
data = re.sub(r'(?<=X)(\d*[.]\d*|(\d*))',lambda m : str(float(m.group(0))+config["xoff"]),data)
data = re.sub(r'(?<=Y)(\d*[.]\d*|(\d*))',lambda m : str(float(m.group(0))+config["yoff"]),data)
data = re.sub(r'(?<=([.]\d{3}))\d*','',data)

f = open(config["output"], "w")
f.write(data) 
