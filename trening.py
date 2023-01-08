# list2 = ["apple", "orange"]
# tuple2 = ("kiwi", "orange")
# list2.extend(tuple2)
# print(list2)

# for i in list2:
#     print(i)

inputlist = []

i=0
while i < 4:

    a = int(input(str("please input your number ")))
    print("your number is: " + str(a))

    inputlist.append(a)

    print("inputs", inputlist)
    i += 1;

print("testowanie")

rounding
listofinputsrounded = []
i = 0
while i < 2:
    a = float(input("input a number to round "))
    b = int(input("What place do you want the number to be rounded to?"))
    x = lambda a : round(a, b)
    print("rounded number ", x(a))
    print("input number ", a)
    listofinputsrounded.append(x(a))
    i += 1
    if i == 2:
        break
print(listofinputsrounded)
sum = 0
for i in range(0,len(listofinputsrounded)):
    sum = sum + listofinputsrounded[i]

n = len(listofinputsrounded)    
print("your input average is: ", (sum/n))

inputlist = []
i = 0
