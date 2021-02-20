# -*- coding: utf-8 -*- 
from models.trade import *

def parsing(lines):
	for i, line in enumerate(lines):
		#print(line)
		if line.find("해외주식 체결집계 내역 안내") >= 0:
			trade = Trade(lines[i:i+10])

