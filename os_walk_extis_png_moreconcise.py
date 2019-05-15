# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import os
dir_list=[ fs[0] for fs in os.walk(r'd:\python data')]
[ print(os.path.join(dirs,f)) for f in os.listdir(dirs) for dirs in dir_list  if f.endswith('png')]
