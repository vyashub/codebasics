# List Excercise
month_list = [2200,2350,2600,2130,2190]

#month_dict = {'January':2200,'February':2350,'March':2600,'April':2130,'May':2190}

feb_exp = month_list[1]
jan_exp = month_list[0]


extra_spent = feb_exp - jan_exp
print('Feb extra Spent: ',extra_spent)


print('Quarter Expense: ',month_list[0] + month_list[1]  + month_list[2] )

print('2000$ spent ?',2000 in month_list)
        
month_list.append(1980)      
print(month_list)  


month_list[3] = month_list[3]-200
print(month_list)