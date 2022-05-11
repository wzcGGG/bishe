state2IdDict :	字典	key: state --> value: list of agentIds

dateDescriptor :	日期描述	can be "E": even, "O": odd, or "W": weelend

building_df, room_df:	建筑和房屋的dataframe

agent_df:	代理的dataframe

adjacencyDict： 房间的"connected_to"id + 行进时间

buildings，rooms：由building_df和room_df实例化的类

buildingNameId，roomNameId：name与id的对应表

room_cap_log：room	log