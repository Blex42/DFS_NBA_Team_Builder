


def teamoptmizer(workingdf,Loopcount,datatype):
        #Data
    import pandas as pd
    import numpy as np

    #Date
    import datetime as dt   

    #Stats
    from statistics import mean, median

    ###Optimizepackage
    import pulp



    #######Optmization function
    optmodel= pulp.LpProblem("Points max problem", pulp.LpMaximize)
    playerstatus= pulp.LpVariable.dicts("playerstatus",
                                       ((Unq_Masterid) for Unq_Masterid in workingdf.index),
                                        cat='Binary')
    optmodel += pulp.lpSum([playerstatus[Unq_Masterid]*workingdf.loc[(Unq_Masterid), datatype] for Unq_Masterid in workingdf.index])
    ##################################################################
    ###Roster Constraints
    ##################################################################
    optmodel += pulp.lpSum([playerstatus[i] for i in playerstatus])==8
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"PG"]) for i in workingdf.index])<=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"PG"]) for i in workingdf.index])>=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"SG"]) for i in workingdf.index])<=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"SG"]) for i in workingdf.index])>=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"SF"]) for i in workingdf.index])<=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"SF"]) for i in workingdf.index])>=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"PF"]) for i in workingdf.index])<=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"PF"]) for i in workingdf.index])>=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"C"]) for i in workingdf.index])<=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"C"]) for i in workingdf.index])>=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"Guard_Class"]) for i in workingdf.index])<=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"Guard_Class"]) for i in workingdf.index])>=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"Forward_Class"]) for i in workingdf.index])<=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"Forward_Class"]) for i in workingdf.index])>=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"Util_Class"]) for i in workingdf.index])<=1
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"Util_Class"]) for i in workingdf.index])>=1

    for player in workingdf["Name"].unique():
        #print(player)
        sub_playeridx = workingdf[workingdf["Name"]==player].index
        optmodel += pulp.lpSum([playerstatus[i] for i in sub_playeridx])<= 1

    ##################################################################
    #Team Constraints
    ##################################################################
    #optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"TeamAbbrev "]=="DET") for i in workingdf.index])<=2
    ##################################################################
    ####Salary
    ##################################################################
    optmodel += pulp.lpSum([playerstatus[i]*(workingdf.loc[(i),"Salary"]) for i in workingdf.index])<=50000
    optmodel.solve()
    #print(pulp.LpStatus[optmodel.status])
    Idz=[]
    playerst=[]
    for val in playerstatus:
        
        Idz.append(val)
        playerst.append(playerstatus[val].varValue)
    stagedf=pd.DataFrame({"Unq_Masterid":Idz,"Status":playerst})
    stagedf=stagedf[stagedf["Status"]==1]
    stagedf2 = stagedf.sort_values("Unq_Masterid",ascending=1)
    stagedf.insert(1,"Grouping",Loopcount)
    
    #
    stagedf2 = stagedf2[["Unq_Masterid"]]
    stagedf2 = stagedf2.transpose()
    stagedf2["num"] = Loopcount 
    stagedf2["model"] = datatype
    stagedf2 =stagedf2.values.tolist()
    #stagedf2=stagedf2.append(Loopcount)
    ##
    return stagedf, stagedf2