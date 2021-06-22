#
def cal_average(*args):
    sum = 0
    for num in args:
        sum+=num
    print(sum/len(args))
