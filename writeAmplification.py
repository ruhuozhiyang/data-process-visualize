import matplotlib.pyplot as plt

x = [10, 48, 95, 143, 191]
y_default = [28, 83, 185, 380, 610]
y_sw_compaction = [13, 52, 103, 158, 206]
plt.plot(x, y_default, 's-', color='g', label="Default")
plt.plot(x, y_sw_compaction,'^-', color='r', label="SWCompaction")
plt.xlabel("Data Size (GB)")
plt.ylabel("Actual Disk Write I/O (GB)")
plt.legend(loc="best")
plt.show()