# The Collatz Conjecture
# https://www.youtube.com/watch?v=094y1Z2wpJg
#
# Narendra Nag
# Aug 7, 2021

# for any input n
# while n != 1
#   if n is odd, then n = (n * 3) + 1
#   if n is even then n = n / 2
#   add n to the y-axis list
#   add the iterator to the x-axis list
# take the leading digit of n and create a histogram


import matplotlib.pyplot as plt

n = 0
counter = 0


n = int(input("Enter seed number to start with: "))

x_axis = [counter]
y_axis = [n]

while n != 1:

    print(n)

    if(n % 2 == 0):
        n = n / 2
    else:
        n = (n * 3) + 1
    
    counter = counter + 1
    
    x_axis.append(counter)
    y_axis.append(n)


    

# plot n on graph

plt.plot(x_axis, y_axis, color="blue", marker="o", linestyle="dashed", linewidth=1, markerfacecolor="green", markersize=10)
plt.xlabel("Iteration")
plt.ylabel("n")
plt.title("Collatz Conjecture Series for " + str(y_axis[0]))
plt.show()
