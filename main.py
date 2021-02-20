# -*- coding: utf-8 -*- 
from readFile import *
from parsing import *

stock_text_file_name = "files/KakaoTalkChats.txt"
mystock_spreadsheel_url = "https://docs.google.com/spreadsheets/d/1mF0hjhNsDkfVe71jIcEx_UwHJUZJBkrc9C9_PYYiUJc/edit#gid=0"

def main():
	ticker_table = read_spreadsheet(mystock_spreadsheel_url)
	lines = read_stock_file(stock_text_file_name)
	print("parsing!!!")
	parsing(lines)



if __name__ == "__main__":
	main()


