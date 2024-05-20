
def bilangan_terbesar(my_list):


	max = my_list[0]

	for x in my_list:
		if x > max:
			max = x
	return max



my_list = [10,20,5,30,15]
print(bilangan_terbesar(my_list))

