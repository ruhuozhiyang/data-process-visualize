import matplotlib.pyplot as plt
from numpy import long

default_m_filename = "default-compaction-record-4"
better_m_filename = "better-compaction-record-3"
default_num = []
default_filesizes = []
better_num = []
better_filesizes = []

default_f = open(default_m_filename, encoding='utf-8')
default_lines = default_f.read().splitlines()
i = 1
for ele in default_lines:
    filesizes = ele.split(" ")
    filesizes.pop(0)
    if filesizes:
        default_num.append(i)
        default_filesizes.append(filesizes)
        i = i + 1
# print(default_num, end='\n')
# print(default_filesizes, end='\n')
default_f.close()

j = 1
better_f = open(better_m_filename, encoding='utf-8')
better_lines = better_f.read().splitlines()
for ele in better_lines:
    filesizes = ele.split(" ")
    filesizes.pop(0)
    if filesizes:
        better_num.append(j)
        better_filesizes.append(filesizes)
        j = j + 1
# print(better_num, end='\n')
# print(better_filesizes, end='\n')
better_f.close()

x_max = len(default_num) if len(default_num) > len(better_num) else len(better_num)
y_max = 0

f2 = 0
for xe, ye in zip(default_num, default_filesizes):
    if ye:
        longYe = [long(x) for x in ye]
        maxy = max(longYe) / (1024 * 1024)
        miny = min(longYe) / (1024 * 1024)
        plt.scatter(xe, maxy, color='blue')
        plt.scatter(xe, miny, color='blue')
        if maxy > miny:
            if f2 == 0:
                plt.plot([xe, xe], [miny, maxy], color='blue', label='default', linestyle='dashdot')
            else:
                plt.plot([xe, xe], [miny, maxy], color='blue', linestyle='dashdot')
            f2 = f2 + 1
        else:
            print(max(ye), min(ye), maxy, miny)
        if maxy > y_max:
            y_max = maxy

f1 = 0
for xe, ye in zip(better_num, better_filesizes):
    if ye:
        longYe = [long(x) for x in ye]
        maxy = max(longYe) / (1024 * 1024)
        miny = min(longYe) / (1024 * 1024)
        plt.scatter(xe, maxy, color='red')
        plt.scatter(xe, miny, color='red')
        if maxy > miny:
            if f1 == 0:
                plt.plot([xe, xe], [miny, maxy], color='red', label='better', linestyle='dashdot')
            else:
                plt.plot([xe, xe], [miny, maxy], color='red', linestyle='dashdot')
            f1 = f1 + 1
        else:
            print(max(ye), min(ye), maxy, miny)
        if maxy > y_max:
            y_max = maxy

# plt.title(default_m_filename + "&" + better_m_filename)
# plt.axis([0, x_max + 500, 0, y_max + 1000])
plt.axis([0, x_max, 0, y_max + 100])
plt.xlabel("Number of compactions")
plt.ylabel("Compaction data volume(MB)")
plt.legend()
plt.show()
