import os
import glob
path = 'C:/Users/IDREESIA/Documents/STSV-GitTraining/'
for entry in os.listdir(path):
    if  os.path.isfile(os.path.join(path, entry)):
        print(entry)

from os.path import join, splitext
from glob import glob
from collections import Counter

path = r'C:/Users/IDREESIA/Documents/STSV-GitTraining/'

c = Counter([splitext(i)[1][1:] for i in glob(join(path, '*'))])
for ext, count in c.most_common():
    print (ext, count)

print("Flashers","Solid State Relays","Pulse Relays","Time Relays","Toggle Relays","Speial Relays", "Voltage Monitors","Frequency Monitors","Standard Relays")