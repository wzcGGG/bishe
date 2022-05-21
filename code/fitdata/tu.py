import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import numpy as np
import scipy.stats as st

def realandI(days ):
    "真实与模拟数据"
    realdata = np.load('realdata.npy')
    realdata = realdata[0:days]
    x = np.linspace(0, days-1, days)
    plt.scatter(x, realdata, color='w', edgecolors='k')
    plt.plot(x, realdata, 'k')
    plt.legend()
    plt.title('realdata')
    plt.savefig("realdata.png")
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

realandI(90)
