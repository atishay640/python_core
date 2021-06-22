#file read/write in python

# write operation
days_file = open('days.txt',mode='w+')
days_file.write('Sunday\n')
days_file.write('Monday\n')
days_file.write('Tuesday\n')
days_file.write('Wednesday\n')
days_file.write('Thursday\n')
days_file.close()

# append in existing file
append_d_file = open('days.txt' , mode='a')
append_d_file.write('Friday\n')
append_d_file.write('Saturday\n')
append_d_file.close()

# read from a file
read_d_file = open('days.txt' , mode='r')
text = read_d_file.read()
print(text)
