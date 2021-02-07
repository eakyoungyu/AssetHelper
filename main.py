# -*- coding: utf-8 -*- 
from readFile import *
from parsing import *

file_name = "KakaoTalkChats.txt"

def main():
	lines = read_stock_file(file_name)
	print("parsing!!!")
	parsing(lines)



if __name__ == "__main__":
	main()