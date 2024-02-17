import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

default_filename = "default-secs-ops-3"
better_filename = "better-secs-ops-3"
default_secs = []
default_opss = []
better_secs = []
better_opss = []

default_f = open(default_filename, encoding='utf-8')
default_line = default_f.readline()
while default_line:
    if "operations;" in default_line.split(" "):
        sec = default_line.split(" ")[2]
        default_secs.append(sec)
        ops = 0
        if sec != '0':
            ops = default_line.split(" ")[6]
        default_opss.append(float(ops))
    default_line = default_f.readline()
print(default_secs, default_opss, end='\n')
default_f.close()

better_f = open(better_filename, encoding='utf-8')
better_line = better_f.readline()
while better_line:
    if "operations;" in better_line.split(" "):
        sec = better_line.split(" ")[2]
        better_secs.append(sec)
        ops = 0
        if sec != '0':
            ops = better_line.split(" ")[6]
        better_opss.append(float(ops))
    better_line = better_f.readline()
print(better_secs, better_opss, end='\n')
better_f.close()

# 两个是配置代码，第一行表示，允许使用中文，第二个表示允许使用负数
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 这三个表示就跟名字一样，标识作用
# plt.title(default_filename + "&" + better_filename)
plt.xlabel("time(sec)")
plt.ylabel("operation per sec")

# print(default_secs[0], default_secs[len(default_secs) - 1])
# print(better_secs[0], better_secs[len(better_secs) - 1])
dsmax = int(default_secs[len(default_secs) - 1])
bsm = int(better_secs[len(better_secs) - 1])

# 这个前两参数表示横坐标的开始和结尾，第三个参数表示你要分成多少份
d_x = np.linspace(0, dsmax, dsmax)
b_x = np.linspace(0, bsm, bsm)
plt.axis([0, dsmax if dsmax > bsm else bsm,
          0, max(default_opss) if max(default_opss) > max(better_opss) else max(better_opss) + 10000]);

# 下面是节点个状态信息，一定要使用numpy自带的array，不然会出错
default_x = np.array(default_secs)
default_y = np.array(default_opss)
better_x = np.array(better_secs)
better_y = np.array(better_opss)

# 这个就是最重要的平滑操作了，要是不使用这个操作的话，画出来的就是点和点之间的直线
model_default = make_interp_spline(default_x, default_y)
ys_default = model_default(d_x)
model_better = make_interp_spline(better_x, better_y)
ys_better = model_better(b_x)

# 给每条线设定颜色，和添加label，linestyle表示你要使用曲线的样式，有多少种网上有
plt.plot(d_x, ys_default, color='blue', label='default', linestyle='-')
plt.plot(b_x, ys_better, color='red', label='sliding-window', linestyle='-')

# legend() 函数只有在你需要使用laber 这个参数的时候才会用到
plt.legend()
plt.show()
