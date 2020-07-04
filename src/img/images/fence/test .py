import os
import shutil
import re

p=re.compile('20[0-1]\d+\d.jpg')


for a,b,c in os.walk('./'):
    for i in c:
        print(i)
        if i[-3:]=='jpg':
            os.rename(i,p.findall(i)[0])

