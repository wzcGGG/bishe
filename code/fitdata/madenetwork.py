import model_framework
import main_config

modelConfig = main_config.modelConfig
model = model_framework.AgentBasedModel()
model.addKeys(modelConfig)
model.loadBuilder(filename=r'Building.csv')
model.loadAgent("newAgent.csv")
model.createWorld()
model.visualizeBuildings()
