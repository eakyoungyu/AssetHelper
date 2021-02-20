# -*- coding: utf-8 -*- 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from models.ticker_table import *

def read_stock_file(file_name):
	file = open(file_name, "r")
	lines = file.readlines()
	file.close()
	return lines

def read_spreadsheet(spreadsheet_url):
	scope = [
		'https://spreadsheets.google.com/feeds',
		'https://www.googleapis.com/auth/drive',
	]
	json_file_name = 'key/imagetotext-230713-e4fdfbc1968e.json'
	credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
	gc = gspread.authorize(credentials)
	doc = gc.open_by_url(spreadsheet_url)
	# 시트 선택하기
	worksheet = doc.worksheet('Ticker')
	tickers = worksheet.col_values(1)[1:]
	symbols = worksheet.col_values(2)[1:]
	ticker_table = TickerTable(tickers, symbols)
	print(ticker_table)
	return ticker_table