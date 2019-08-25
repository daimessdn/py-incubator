# Bubble Short

list = []

for i in range(0,25):
	x = float(input(""))
	list.append(x)

# swap the elements to arrange in order
# ascending
for iter_num in range(len(list)-1, 0, -1):
	for index in range(iter_num):
		if (list[index] > list[index+1]):
			temp = list[index]
			list[index] = list[index+1]
			list[index+1] = temp

# descending
# for iter_num in range(len(list)-1, 0, -1):
# 	for index in range(iter_num):
# 		if (list[index] > list[index+1]):
# 			temp = list[index]
# 			list[index] = list[index+1]
# 			list[index+1] = temp

# with subprogram
# def bubblesort(list):
# 	for iter_num in range(len(list)-1, 0, -1):
# 		for index in range(iter_num):
# 			if (list[index] > list[index+1]):
# 				temp = list[index]
# 				list[index] = list[index+1]
# 				list[index+1] = temp

# bubblesort(list)

print(list)