import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

default_m_filename = "opslogs-default-1region-150GB-metrics-1"
better_m_filename = "opslogs-better-1region-150GB-metrics-1.1"
default_secs = [0]
default_c = [0]
better_secs = [0]
better_c = [0]

default_f = open(default_m_filename, encoding='utf-8')
default_lines = default_f.read().splitlines()
i = 1
for ele in default_lines:
    if "CompactionInputSize_mean:" in ele.split(" "):
        default_secs.append(10 * i)
        default_c.append(ele.split(" ")[1])
    i = i+1
print(default_secs, default_c, end='\n')
default_f.close()

j=1
better_f = open(better_m_filename, encoding='utf-8')
better_lines = better_f.read().splitlines()
for ele in better_lines:
    if "CompactionInputSize_mean:" in ele.split(" "):
        better_secs.append(10 * j)
        better_c.append(ele.split(" ")[1])
    j=j+1
print(better_secs, better_c, end='\n')
better_f.close()

# 两个是配置代码，第一行表示，允许使用中文，第二个表示允许使用负数
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 这三个表示就跟名字一样，标识作用
plt.title(default_m_filename + better_m_filename)
plt.xlabel("time(sec)")
plt.ylabel("compactionSize")

print(default_secs[0], default_secs[len(default_secs) - 1])
print(better_secs[0], better_secs[len(better_secs) - 1])
dsmax = int(default_secs[len(default_secs) - 1])
bsm = int(better_secs[len(better_secs) - 1])
# 这个前两参数表示横坐标的开始和结尾，第三个参数表示你要分成多少份
d_x = np.linspace(0, dsmax, dsmax)
b_x = np.linspace(0, bsm, bsm)

# 下面是节点个状态信息，一定要使用numpy自带的array，不然会出错
default_x = np.array(default_secs)
default_y = np.array(default_c)
better_x = np.array(better_secs)
better_y = np.array(better_c)

# 这个就是最重要的平滑操作了，要是不使用这个操作的话，画出来的就是点和点之间的直线
model_default = make_interp_spline(default_x, default_y)
ys_default = model_default(d_x)
model_better = make_interp_spline(better_x, better_y)
ys_better = model_better(b_x)

# 给每条线设定颜色，和添加label，linestyle表示你要使用曲线的样式，有多少种网上有
plt.plot(d_x, ys_default, color='red', label='default', linestyle='-')
plt.plot(b_x, ys_better, color='blue', label='better', linestyle='-')

# legend() 函数只有在你需要使用laber 这个参数的时候才会用到
plt.legend()
plt.show()
