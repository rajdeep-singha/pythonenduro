names=['rajdeep','eshita','beauty','tarun']
# names=list()
print(names)
print(names[0])
print(f'size of list {len(names)}')


for i in range(0,4):
   # print(names[i])

   """  for n in names:
        print(n) """

names.append("rajdeep")
        #print(names)

names.insert(1,'SRM')
print (names)

"""    names.pop()

        print(names) """




print(f"Rajdeep appeared{names.count('rajdeep')} times")


names.sort(reverse=True)
print (names)

