
for i in range(1, 104):
    if i < 10:
        a = '0000{}'.format(i)
    if 10 <= i < 100:
        a = '000{}'.format(i)
    if 100 <= i < 1000:
        a = '00{}'.format(i)
    #else:
        #a = '0{}'.format(i)
    print(a)

