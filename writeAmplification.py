import matplotlib.pyplot as plt

# SWCompaction
# x = [10, 48, 95, 143, 191]
# y_default = [38, 131, 280, 523, 801]
# y_sw_compaction = [23, 93, 198, 272, 397]
# plt.plot(x, y_default, 's-', color='g', label="Default")
# plt.plot(x, y_sw_compaction,'^-', color='r', label="SWCompaction")
# plt.xlabel("Data Size (GB)")
# plt.ylabel("Actual Disk Write I/O (GB)")
# plt.legend(loc="best")
# plt.show()

# DPStore
x = [10, 48, 95, 143, 191]
y_default = [38, 131, 280, 523, 701]
y_dp_compaction = [12, 84, 225, 403, 516]
plt.plot(x, y_default, 's-', color='g', label="Default")
plt.plot(x, y_dp_compaction,'^-', color='r', label="DPStore")
plt.xlabel("Data Size (GB)")
plt.ylabel("Actual Disk Write I/O (GB)")
plt.legend(loc="best")
plt.show()
