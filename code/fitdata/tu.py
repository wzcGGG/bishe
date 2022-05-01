import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import numpy as np
import scipy.stats as st

def realandI(days , mean_num_I, name):
    "真实与模拟数据"
    realdata = np.load('realdata.npy')
    realdata = realdata[0:days]
    x = np.linspace(0, days-1, days)
    plt.scatter(x, realdata, color='w', edgecolors='k')
    plt.plot(x, realdata, 'k')
    plt.plot(mean_num_I, label='I')
    plt.legend()
    plt.title('real and prenum_I')
    name = "./img/"+ "jiu"+str(name) + "resultREAL.png"
    plt.savefig(name)
    plt.show()
    pass
def plotSIR(days , mean_num_S, mean_num_I, mean_num_R):
    "模拟数据SIR的95%置信区间"
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(0, days - 1, days)
    ax.plot(x, mean_num_S, label='S')
    ax.plot(x, mean_num_I, label='I')
    ax.plot(x, mean_num_R, label='R')
    ax.set_title("numSIR")
    plt.savefig("resultSIR.png")
    plt.show()
    pass
#
# df = pd.read_excel(r'.\configuration\data.xlsx')
#
# Y = []
# x = df['day']
# x = np.array(x)[0:100]
# y = df['new']
# y = np.array(y)
# for i in range(0, 100):
#     if i < 14:
#         Y.append(np.sum(y[0:i]))
#     else:
#         Y.append(np.sum(y[i-14:i]))
# x = np.array(x)
# Y = np.array(Y)
#
# plt.scatter(x, Y, color='w', edgecolors='k')
# plt.plot(x, Y, 'k')
#
# # 95%置信区间
# # generate dataset
# b = np.load(file=r"temp.npy")
# # dataS = b[:, 0, :]
# dataI = b[:, 1, 0:90]
# # dataR = b[:, 2, :]
#
# # predicted expect and calculate confidence interval
# # dataS_mean = np.mean(dataS, 0)
# dataI_mean = np.mean(dataI, 0)
# # dataR_mean = np.mean(dataR, 0)
#
#
# # Slow_CI_bound, Shigh_CI_bound = st.t.interval(0.95, 100 - 1, loc=np.mean(dataS, 0),scale=st.sem(dataS))
# # Ilow_CI_bound, Ihigh_CI_bound = st.t.interval(0.95, 100 - 1, loc=np.mean(dataI, 0),scale=st.sem(dataI))
# # Rlow_CI_bound, Rhigh_CI_bound = st.t.interval(0.95, 100 - 1, loc=np.mean(dataR, 0),scale=st.sem(dataR))
#
# # plot confidence interval
# x = np.linspace(0, 100 - 1, num=100)
# # plt.plot(dataS_mean, linewidth=1, label='S')
# plt.plot(dataI_mean, linewidth=1, label='I')
# # plt.plot(dataR_mean, linewidth=1, label='R')
# # plt.fill_between(x, Slow_CI_bound, Shigh_CI_bound, alpha=0.5)
# # plt.fill_between(x, Ilow_CI_bound, Ihigh_CI_bound, alpha=0.5)
# # plt.fill_between(x, Rlow_CI_bound, Rhigh_CI_bound, alpha=0.5)
# plt.legend()
# # plt.title('num_I')
# plt.show()
#
# #
# # df = pd.read_excel(r'.\configuration\data.xlsx')
# #
# # Y = []
# # x = df['day']
# # x = np.array(x)
# # y = df['new']
# # y = np.array(y)
# # for i in range(0, 99):
# #     if i < 14:
# #         Y.append(np.sum(y[0:i]))
# #     else:
# #         Y.append(np.sum(y[i-14:i]))
# # fig, ax = plt.subplots()
# #
# # ax.scatter(x, Y, color='w', edgecolors='k')
# # ax.plot(x, Y, 'k')
# #
# # ax.set(xlim=(0, 100), xticks=np.arange(0, 100, 10),
# #        ylim=(0, 150), yticks=np.arange(0, 150, 50))
# #
# # plt.show()