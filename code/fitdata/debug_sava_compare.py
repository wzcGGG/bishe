import model_framework
import main_config

output_folder = "outputs/base"
modelConfig = main_config.modelConfig
model_framework.createFilledPlot(modelConfig, modelName="baseModel",simulationN=5, outputDir=output_folder)