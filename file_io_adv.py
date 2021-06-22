#file read/write in python

# write operation
with open('month.txt' , mode='w') as month_file:
    month_file.write('January\n')
    month_file.write('February\n')
    month_file.write('March\n')
    month_file.write('April\n')
    month_file.write('May\n')
    month_file.write('June\n')
    month_file.write('July\n')
    month_file.write('August\n')
    month_file.write('September\n')

month_file.close()

# append in existing file
with open('month.txt' , mode='a') as append_month_file:
    append_month_file.write('October\n')
    append_month_file.write('November\n')
    append_month_file.write('December\n')
append_month_file.close()

# read from a file
with open('month.txt',mode='r') as read_month_file:
    print(read_month_file.read())
read_month_file.close()

print('---------------------------------------------------')
# read from a file line by line
with open('month.txt',mode='r') as read_month_file:
    month_list = read_month_file.readlines()
    print(month_list)
read_month_file.close()
