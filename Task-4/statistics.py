import func

numbers=[12, 18, 7, 10, 16, 14, 11, 8, 12, 15]
print(f"\n1- minmum numper : {func.find_min(numbers)}\n\n"
      f"2- maxmum numper : {func.find_max(numbers)}\n\n"
      f"3- the mean : {func.find_mean(numbers)}\n\n"
      f"4- the mode : {func.find_mode(numbers)}\n\n"
      f"5- median : {func.find_median(numbers)}\n\n"
      f"6- range : {func.find_range(numbers)}\n\n"
      f"7- variance : {func.find_variance(numbers)}\n\n"
      f"8- standard deviasion : {func.find_STD(numbers)}\n\n"
      f"9- quartiles : {func.find_Quariles(numbers)}\n\n"
      f"10- interquartil range : {func.find_IQR(numbers)}\n\n")



'''
choose_num_of_list=int(input("enter num of numper in list : "))
numbers=func.get_numbers(choose_num_of_list)

print("\n1- minmum numper \n"
      "2- maxmum numper \n"
      "3- the mean \n "
      "4- mode \n"
      "5- median \n"
      "6- range \n"
      "7- variance \n"
      "8- standard deviasion \n"
      "9- quartiles \n"
      "10- interquartil range \n")
operation_chooes=int(input("============ choose operation from (1:10) ================ : "))

chooese_operation = {
        1: func.find_min,
        2: func.find_max,
        3: func.find_mean,
        4: func.find_mode,
        5: func.find_median,
        6: func.find_range,
        7: func.find_variance,
        8: func.find_STD,
        9: func.find_Quariles,
        10: func.find_IQR,
        11: exit
    }
print(chooese_operation[operation_chooes](numbers))

'''