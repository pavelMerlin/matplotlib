import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import *

# # =========== РАБОТА С plot и стилями к нему
# # x = np.array([1, 3, 5, 1])
# # y = np.array([3, -1, 3, 3])
#
# y = np.arange(5)
# x = np.array([a*a for a in y])
# plt.plot(x+2, y, color="g", marker="s", markerfacecolor="w")
#
# # ["EVEN" if n % 2 == 0 else "ODD" for n in numbers]
# y1 = np.arange(4)
# x1 = np.array([a+5 if a % 2 == 0 else a+1 for a in y1])
#
# lines = plt.plot(x, y, ":b*", x1, y1, ".-r")
# plt.setp(lines[1], linestyle=":", marker="*", markerfacecolor="w", lw=4)
# plt.fill_between(x1, y1, where=(x1 > 2))
#
# plt.grid()
# plt.show()

# # =========== РАБОТА С add_subplot и figure
# fig = plt.figure(figsize=(7, 4))
# ax1 = fig.add_subplot(1, 3, 1)
# ax1.plot(np.arange(0, 5, 0.1))
#
# f, ax = plt.subplots(2, 2)
#
# f.set_size_inches(7, 4)
# f.set_facecolor("#eee")
#
# ax[0, 0].plot(np.arange(0, 10, 0.1))
# ax[0, 1].plot(np.random.randn(10))
# plt.show()

# # =========== РАБОТА С GridSpec и размещением графиков
# ws = [1, 2, 5]
# hs = [2, 0.5]
#
# fig = plt.figure(figsize=(7, 4))
# gs = GridSpec(ncols=3, nrows=2, figure=fig, width_ratios=ws, height_ratios=hs)
#
# ax1 = plt.subplot(gs[0, 0])
# ax2 = plt.subplot(gs[1, 0:2])
# ax3 = fig.add_subplot(gs[:, 2])
# ax1.plot(np.random.random(10))
# ax2.plot(np.random.random(10))
# ax3.plot(np.random.random(10))
# plt.show()

fig = plt.figure(figsize=(10, 10))
ax = plt.subplot()
ax.plot(np.array([1, 2, 5, 3]))

# устанавливаем лимиты
ax.set(xlim=(0, 10), ylim=(0, 10))

lc = NullLocator()

ax.grid()
ax.xaxis.set_major_locator(lc)
# ax.yaxis.set_major_locator(NullLocator())

# шаг
ax.xaxis.set_major_locator(MultipleLocator(base=1))
ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0.2))
ax.xaxis.set_major_locator(FixedLocator([1, 3, 0.2]))

plt.show()
