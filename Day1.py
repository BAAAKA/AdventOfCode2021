
with open('inputDay1.txt','r') as f:
    lines = f.readlines()

count = 0
pl = 0
for i, l in enumerate(lines):
    pl = int(lines[i-3])
    cl = int(lines[i])
    if int(cl)>int(pl):
        print('{} increased'.format(i))
        count+=1
    else:
        print('{} decreased'.format(i))
    print("pl {} and l {}".format(pl, cl))
print('Total is: {}'.format(count))