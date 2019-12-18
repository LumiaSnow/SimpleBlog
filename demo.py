#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

for dirpath, dirnames, filenames in os.walk("./articles"):
    print(dirpath.split('/')[-1].split('\\')[-1])
