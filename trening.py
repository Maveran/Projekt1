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