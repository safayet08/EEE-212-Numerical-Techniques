import numpy as np
import numpy.linalg as LA
import numpy.random
import matplotlib.pyplot as plt


def error(a,b):
    return abs((a-b) / (a)) * 100

def ln(x, iterations):
    sign = 1
    idx = 1
    result = 0
    tmp = x/idx
    while idx <= iterations:
        result = result + tmp * sign
        idx += 1
        tmp = (x * tmp) / idx
        sign *= -1
    
    return result

x_val = 0.2  # x_val = value of x
no_of_iteration = 1000 # Number of iterations

# 1 (a)
print(ln(float(x_val),int(no_of_iteration)))


plt.style.use('fivethirtyeight') 
fig = plt.figure(figsize=(10,20)) 
plt1 = fig.add_subplot(221) 
plt2 = fig.add_subplot(222) 
plt3 = fig.add_subplot(223) 

# 1 (c)

x = np.arange(-1, 1, 0.1)
y = np.log(1 + x)
plt1.plot(x, y, label = "ln(1+x)" , linewidth = 1, marker = 'o', markerfacecolor = 'black', markersize = '5')

# 1 (c)

iteration = [1, 3, 5, 20, 50]
results = []
z = []
for n in iteration:
    for i in x:
        results.append(ln(i, n))
    z.append(np.array(results))
    del results[:]     

plt2.plot(x, y,label="Main Function" , linewidth=1, marker = 'o', markerfacecolor = 'black', markersize = '5')

plt2.plot(x,z[0],linewidth = 1, label="Iteartion 1",marker = 'o', markerfacecolor = 'black', markersize = '5')
plt2.plot(x,z[1],linewidth = 1, label="Iteartion 3",marker = 'o', markerfacecolor = 'black', markersize = '5')
plt2.plot(x,z[2],linewidth = 1, label="Iteartion 5",marker = 'o', markerfacecolor = 'black', markersize = '5')
plt2.plot(x,z[3],linewidth = 1, label="Iteartion 20",marker = 'o', markerfacecolor = 'black', markersize = '5')
plt2.plot(x,z[4],linewidth = 1, label="Iteartion 50",marker = 'o', markerfacecolor = 'black', markersize = '5')


# 1 (d)

n = 2
x = np.arange(2,51)
y = []
while n <= 50:
    curr = calculate_ln(0.5,n)
    old = calculate_ln(0.5,n-1)
    err = error(curr,old)
    y.append(err)
    n += 1

plt3.plot(x,y,linewidth = 1,label="Error vs Iteration",marker = 'o', markerfacecolor = 'black', markersize = '5')
fig.subplots_adjust(hspace=.5,wspace=0.5) 

plt1.legend()
plt2.legend()
plt3.legend()
plt.show()