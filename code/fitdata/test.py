import model_framework
import platform
import statfile
import copy
import fileRelated
import pandas as pd
import experiment as experiment
import main_config
from pathlib import Path
import numpy as np
import time
import tu

def main():
    # 初始model，输出感染图像，并且画出置信区间
    start = time.perf_counter()
    modelName = 'test'
    modelConfig = main_config.modelConfig
    R0_controls = {
        "World": [
            ("DynamicCapacity", False),
        ],
        "HybridClass": [
            ("ChangedSeedNumber", 10),
        ],
    }
    output_folder = "test"
    days = 90
    R0Count, multiCounts = 100, 300

    # # select base_p
    realdata = np.load('realdata.npy')
    realdata = realdata[0:days]
    # for i in np.arange(0.8, 0.9, 0.02):
    #     modelConfig["Infection"]["baseP"] = i
    #     mean_num_I = model_framework.multiSimulation(multiCounts, modelConfig, days, debug=False, modelName=modelName,
    #                                                  outputDir=output_folder)
    #     abs_error = np.sum(np.abs(realdata - mean_num_I))
    #     fang_error = sum((realdata - mean_num_I) ** 2)
    #     cun = "baseP=" + str(i) + "对应的绝、方误差" + str(abs_error) + "*****" + str(fang_error) + '\n'
    #     file = open('result.txt', 'a')
    #     file.write(cun)
    #     file.close()
    # end = time.perf_counter()
    # min = round((end - start) / 60)
    # s = 'Running time: ' + str(min) + ' mins'
    # file = open('result.txt', 'a')
    # file.write(s)
    # file.close()
    modelConfig["Infection"]["baseP"] = 0.9
    meanI, abs_error = model_framework.multiSimulationP(multiCounts, modelConfig, days, debug=False, modelName=modelName,realdata = realdata,outputDir=output_folder)
    file = open('result.txt', 'a')
    cun = "baseP=" + str(0.9) + "最优对应的绝对误差" + str(abs_error) + '\n'
    file.write(cun)
    file.close()

if __name__ == "__main__":
    main()
