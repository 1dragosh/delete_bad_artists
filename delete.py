# -*- coding: utf-8 -*-

# Author: 1dragosh

import os

bad = ['bruno mars']

dr = '/media/dragos/FAD1-8614/'

for x in os.listdir(dr):
    fl = dr + x
    if os.path.isdir(fl):
        for y in os.listdir(fl):
            npt = fl + "/" + y
            for _ in bad:
              if _ in y.lower():
                  print(npt)
                  os.remove(npt)
    else:
        for _ in bad:
              if _ in x.lower():
                print(fl)
                os.remove(fl)










