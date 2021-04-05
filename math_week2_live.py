test_list = ['one', 'two', 'three']
test_tuple = (1,2,3,4,5,6,7,8,9)

#for i in test_tuple:
#    print(i)

for i in range(2,8):
    if (i % 2 == 0):
        print(i)
        if(i==6):
            break
    print(i)

def sum_all(*args):
    sum = 0
    for i in args:
        sum = sum + i
        return sum
print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,5,6,7,8,9,10))
