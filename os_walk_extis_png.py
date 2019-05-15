# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
tree=os.walk(r'd:\python data')
dir_list=[]
for full in tree: dir_list += [full[0]]
[ print(os.path.join(dirs,f)) for f in os.listdir(dirs) for dirs in dir_list  if f.endswith('png')]
