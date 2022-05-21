import model_framework
import main_config

output_folder = "outputs/base"
modelConfig = main_config.modelConfig
model_framework.simpleCheck(modelConfig)
# data = dict()
# for key in data:
#     if key == 'onCampus':
#         for i in range(len(data[key])):
#             data[key][i] = (sorted(data[key][i])[-101:-1])[::-1]
#     else:
#         for i in range(len(data[key])):
#             data[key][i] = (sorted(data[key][i])[-100:])[::-1]
# #
# def plotp(data):
#     import seaborn as sns
#     import statfile as stat
#     import numpy as np
#     import matplotlib.pyplot as plt
#     for key in data:
#         num = len(data[key][0])
#         maxVals = []
#         minVals = []
#         mean = []
#         fig, ax = plt.subplots(figsize=(10, 5))
#         x = [i for i in range(num)]
#         for i in range(num):
#             instanceList = [d[i] for d in data[key]]
#             instanceData = stat.analyzeData(instanceList)
#             mean.append(instanceData[0])
#         ax.plot(x, mean, label=key,color='k', alpha=0.5,linewidth = 1.2)
#         ax.legend()
#         plt.xlabel("num of people")
#         plt.ylabel("value")
#         plt.title(key)
#         plt.show()
