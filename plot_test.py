import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
x_points = xrange(0,9)
y_points = xrange(0,9)
p = ax.plot(x_points, y_points, 'b')
ax.set_xlabel('x-points')
ax.set_ylabel('y-points')
ax.set_title('Simple XY point plot')
fig.show()
plt.show()


