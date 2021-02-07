# -*- coding: utf-8 -*- 
def read_stock_file(file_name):
	file = open(file_name, "r")
	lines = file.readlines()
	file.close()
	return lines


def read_spread_sheet(file_name):
	return ticker_table, stock_table