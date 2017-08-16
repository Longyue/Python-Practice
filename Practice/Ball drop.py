#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
#　　第10次落地时，共经过多少米？第10次反弹多高？
total_length = 0.0
height = 100.0
for i in range(10):
    height = height/2
    total_length += 3 * height
total_length = total_length - height

print("Total length = %f, the 10th height = %f" %(total_length, height))

Sn = 100.0
Hn = Sn / 2

for n in range(2,11):
    Sn += 2 * Hn
    Hn /= 2

print('Total of road is %f' % Sn)
print('The tenth is %f meter' % Hn)