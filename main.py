from readFile import *

file_name = "KakaoTalkChats.txt"

def main():
	lines = read_file(file_name)
	for line in lines:
		print(line)



if __name__ == "__main__":
	main()