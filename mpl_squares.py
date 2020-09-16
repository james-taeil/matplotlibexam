import matplotlib.pyplot as plt

squares = []

for i in range(101):
    j = i ** 2
    squares.append(j)


plt.plot(squares)

plt.show()