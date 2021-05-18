#!/bin/python3

import math
import os
import random
import re
import sys

num = int(input())

if((num % 2 == 1)):
    print('Weird')
elif((num>1) and (num<6)):
    print('Not Weird')
elif((num>5) and (num<21)):
    print('Weird')
else:
    print('Not Weird')