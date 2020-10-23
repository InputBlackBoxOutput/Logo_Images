import os

def count():
	return len(os.listdir("Logo Images"))

def create_list():
	if "logo_list.txt" in os.listdir():
		os.remove("logo_list.txt")

	for each in os.listdir("Logo Images"):
		print(each)
		with open("logo_list.txt", 'a') as outfile:
			outfile.write(each + "\n")

if __name__ == '__main__':
	create_list()
	print(f"Count: {count()}")