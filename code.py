import matplotlib.pyplot as plt

x = [2, 4, 5]
y = [2, 3, 6]

plt.plot(x, y, color="green", linestyle="dashed", linewidth=3, marker="o", markerfacecolor="yellow", markersize=12)

plt.ylim(1, 8)
plt.xlim(1, 8)

plt.xlabel("X, Axis")

plt.ylabel("Y, Axis")

plt.title("Demo Graph - Customization")

plt.show()
