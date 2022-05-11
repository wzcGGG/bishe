modelConfig = {
        "Agents" : {
            "PossibleStates":{
                "neutral" : ["susceptible", "exposed"],
                "infected" : ["infected Asymptomatic", "infected Asymptomatic Fixed", "infected Symptomatic Mild", "infected Symptomatic Severe"],
                "recovered" : ["quarantined", "recovered"],
                "debugAndGraphingPurpose": ["falsePositive"],
                },
            "ExtraParameters":[
                        "agentId","path", "destination", "currLocation",
                        "statePersistance","lastUpdate", "personality",
                        "arrivalTime", "schedule",  "gathering", "contacts",
                        # "travelTime", "officeAttendee",
                ], # travelTime and officeAttendee will be commented out
            "ExtraZipParameters": [("motion", "stationary"), ("infected", False), ("compliance", False)],
            "booleanAssignment":[ ("gathering", 0.5)], # ("officeAttendee", 0),
            "immunity": 0,
            "vaccine": False,
            "vaccineEffectiveness": 0.9,
            "vaccinatedPopulation":0.3,
        },
        "Rooms" : {
            "ExtraParameters": ["roomId","agentsInside","oddCap", "evenCap", "classname", "infectedNumber", "hubCount"],
        },
        "Buildings" : {
            "ExtraParameters": ["buildingId","roomsInside"],
        },
        "Infection" : {
            # 修改传染
            "baseP" : 1.25,  # summer was 1.25
            "SeedNumber" : 15,
            "offCampusInfectionMultiplyer":  1,
            "offCampusInfectionP": 0.125,
            "SeedState" : "exposed",
            "Contribution" : {
                "infected Asymptomatic":0.5,
                "infected Asymptomatic Fixed":0.5,
                "infected Symptomatic Mild":1,
                "infected Symptomatic Severe":1,
            },
            # INFECTION STATE
            "TransitionTime" : {
                "susceptible" : -1, # never, unless acted on
                "exposed" : 3*24, # 3 days
                "infected Asymptomatic" : 3*24, # 2 days
                "infected Asymptomatic Fixed" : 14*24, # 14 days
                "infected Symptomatic Mild" : 11*24,# 11 Days
                "infected Symptomatic Severe" : 11*24, # 11 days
                "recovered" : -1, # never
                "quarantined" : 14*24, # 14 days
            },
            # INFECTION TRANSITION PROBABILITY
            "TransitionProbability" : {
                "susceptible" : [("exposed", 1)],
                "exposed" : [("infected Asymptomatic", 0.4), ("infected Asymptomatic Fixed", 1)],
                "infected Asymptomatic Fixed": [("recovered", 1)],
                "infected Asymptomatic": [("infected Symptomatic Mild", 0.5), ("infected Symptomatic Severe", 1)],
                "infected Symptomatic Mild": [("recovered", 1)],
                "infected Symptomatic Severe": [("recovered", 1)],
                "quarantined":[("susceptible", 1)],
                "recovered":[("susceptible", 0.5), ("recovered", 1)],
            },
        },
        "World" : {
            "UnitTime" : "Hours",
            # by having the supposed days to be simulated,
            # we can allocate the required space beforehand to speedup data storing
            "InferedSimulatedDays":100,
            # put the name(s) of intervention(s) to be turned on
            "TurnedOnInterventions":["Quarantine"],# ["HybridClasses", "ClosingBuildings", "Quarantine", "Screening", "FaceMasks"],

            "transitName": "transit_space_hub",
            "offCampusStudentCount":2500,
            "massInfectionRatio":0.10,
            "complianceRatio": 0,
            "stateCounterInterval": 24,
            "socialInteraction": 0.15,
            "LazySunday": True,
            "LargeGathering": True,
            "DynamicCapacity": False,
        },

        # interventions
        "FaceMasks" : {
            "MaskInfectivity" : 0.5,
            "MaskBlock":0.75,
            "use_compliance":True,
            "Facemask_mode": 0,
            "NonCompliantLeaf": ["dorm", "dining", "faculty_dining_hall", "faculty_dining_room"],
            "CompliantHub" : ["dorm", "dining"],
            "NonCompliantBuilding" : ["largeGathering"],
        },
        "Quarantine" : {
            # this dictates if we randomly sample the population or cycle through Batches
            "RandomSampling": False,
            "RandomSampleSize": 100,

            # for random sampling from the agent population
            "SamplingProbability" : 0,
            "ResultLatency":2*24,
            "WalkIn":True,
            "walkinProbability" : {
                "infected Symptomatic Mild": 0.7,
                "infected Symptomatic Severe": 0.95,
                },
            # 修改传染
            "BatchSize" : 1500,
            "TestFromVaccinated":False,
            "ShowingUpForScreening": 1,
            "offset": 8, # start at 8AM
            "checkupFrequency": 24*7,  # this is the interval between checkups, 24 = daily and 24*7 = weekly checkup
            "falsePositive":0.001,
            "falseNegative":0.03,
            "OnlySampleUnvaccinated": False,
        },
        "ClosingBuildings": {
            "ClosedBuildingOpenHub" : [],
            # close buildings in the list(remove them from the schedule), and go home or go to social spaces
            "ClosedBuilding_ByType" : ["gym", "library"],
            "GoingHomeP": 0.5,
            # the building in the list will be removed with probability and replaced with going home, otherwise it stays
            "Exception_SemiClosedBuilding": [],
            "Exception_GoingHomeP":0.5,

        },
        "HybridClass":{
            "RemoteStudentCount": 900,
            "RemoteFacultyCount": 200,
            "RemovedDoubleCount": 0,
            "OffCampusCount": 300,
            "TurnOffLargeGathering": True,
            "ChangedSeedNumber": 12,
        },
        "LessSocializing":{
            "StayingHome":0.75
        },
        "Exposure":{
            "CollectData":False,
            "OnCampusData": 2,
            "OffCampusData":2,
            "facultyData":0,
        }
    }