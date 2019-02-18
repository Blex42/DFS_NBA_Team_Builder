def DK_TeamBuildermod(dfr,dkteams,samplepercent):
    
    #Data
    import pandas as pd
    import numpy as np

    #Date
    import datetime as dt   

    #Stats
    from statistics import mean, median

    ###Optimizepackage
    import pulp

    from DFS_NBA_Team_Builder import DK_Optimization_Function

    ##Set some variables
    randstate =42
    rowlist =[]
    modellist = ["AvgPointsPerGame"]
    ###############
    ######Positions
    pglist= []
    sglist= []
    sflist= []
    pflist= []
    clist= []
    ##Ugly loop to create position columns
    for value in dfr["Position"]:
        #value ="PF/C"
        #print(value)
        if "PG" in value:
            pglist.append(1)
            #print(1)
        if "SG" in value:
            sglist.append(1)
            #print(2)
        if "SF" in value:
            sflist.append(1)
            #print(3)
        if "PF" in value:
            pflist.append(1)
            #print(4)
        if "C" in value:
            clist.append(1)
            #print(5)
        mlist= (pglist,sglist,sflist,pflist,clist)
        #print(len(max(mlist, key=len)))
        while True:
            if len(pglist)<len(max(mlist, key=len)):
                pglist.append(0)
                break
            else:
                break
        while True:
            if len(sglist)<len(max(mlist, key=len)):
                sglist.append(0)
                break
            else:
                break
        while True:
            if len(sflist)<len(max(mlist, key=len)):
                sflist.append(0)
                break
            else:
                break
        while True:
            if len(pflist)<len(max(mlist, key=len)):
                pflist.append(0)
                break
            else:
                break
        while True:
            if len(clist)<len(max(mlist, key=len)):
                clist.append(0)
                break
            else:
                break
    ###Send the lists to a dataframe
    dfr["PG"]=pglist
    dfr["SG"]=sglist
    dfr["SF"]=sflist
    dfr["PF"]=pflist
    dfr["C"]=clist
    ###Create a position total
    dfr["postotal"]=(dfr["PG"]+dfr["SG"]+dfr["SF"]+dfr["PF"]+dfr["C"])
    dfr["Guard_Class"]=np.where((dfr["PG"]+dfr["SG"])>=1,1,0)
    dfr["Forward_Class"]=np.where((dfr["SF"]+dfr["PF"])>=1,1,0)
    dfr["Center_Class"]=np.where((dfr["C"])>=1,1,0)
    dfr["Util_Class"]=np.where((dfr["PG"]+dfr["SG"]+dfr["SF"]+dfr["PF"]+dfr["C"])>=1,1,0)
    dfr["Dual_Class"]=(dfr["Guard_Class"]+dfr["Forward_Class"]+dfr["Center_Class"])
    dfr["Total"]=(dfr["postotal"]+dfr["Guard_Class"]+dfr["Forward_Class"]+dfr["Util_Class"])

    mstrdfr =pd.DataFrame(columns=['Position', 'Name + ID', 'Name', 'ID', 'Roster Position', 'Salary',
       'Game Info', 'TeamAbbrev', 'AvgPointsPerGame', 'PG', 'SG', 'SF', 'PF',
       'C', 'postotal', 'Guard_Class', 'Forward_Class', 'Center_Class',
       'Util_Class', 'Dual_Class', 'Total'])

    for name, repeat in zip(dfr["Name"],dfr["Total"]):
        #print(repeat)
        #print(name)
        pglist= []
        sglist= []
        sflist= []
        pflist= []
        clist= []
        glist=[]
        flist=[]
        ulist=[]
        holder=dfr[dfr["Name"]==name]
        newdf = pd.DataFrame(np.repeat(holder.values,(repeat),axis=0))
        newdf.columns=['Position', 'Name + ID', 'Name', 'ID', 'Roster Position', 'Salary',
        'Game Info', 'TeamAbbrev', 'AvgPointsPerGame', 'PG', 'SG', 'SF', 'PF',
        'C', 'postotal', 'Guard_Class', 'Forward_Class', 'Center_Class',
        'Util_Class', 'Dual_Class', 'Total']
        #break
        for pg,sg,sf,pf,c,Guard_Class,Forward_Class,Util_Class in zip(holder["PG"],holder["SG"],holder["SF"],holder["PF"],holder["C"],holder["Guard_Class"],holder["Forward_Class"],holder["Util_Class"]):
            if pg==1:
                pglist.append(1)
                sglist.append(0)
                sflist.append(0)
                pflist.append(0)
                clist.append(0)
                glist.append(0)
                flist.append(0)
                ulist.append(0)
            if sg ==1:
                pglist.append(0)
                sglist.append(1)
                sflist.append(0)
                pflist.append(0)
                clist.append(0)
                glist.append(0)
                flist.append(0)
                ulist.append(0)
            if sf ==1:
                pglist.append(0)
                sglist.append(0)
                sflist.append(1)
                pflist.append(0)
                clist.append(0)
                glist.append(0)
                flist.append(0)
                ulist.append(0)
            if pf ==1:
                pglist.append(0)
                sglist.append(0)
                sflist.append(0)
                pflist.append(1)
                clist.append(0)
                glist.append(0)
                flist.append(0)
                ulist.append(0)
            if c ==1:
                pglist.append(0)
                sglist.append(0)
                sflist.append(0)
                pflist.append(0)
                clist.append(1)
                glist.append(0)
                flist.append(0)
                ulist.append(0)
            if pg or sg ==1:
                pglist.append(0)
                sglist.append(0)
                sflist.append(0)
                pflist.append(0)
                clist.append(0)
                glist.append(1)
                flist.append(0)
                ulist.append(0)
            if sf or pf ==1:
                pglist.append(0)
                sglist.append(0)
                sflist.append(0)
                pflist.append(0)
                clist.append(0)
                glist.append(0)
                flist.append(1)
                ulist.append(0)
            if pg or sg or sf or pf or c ==1:
                pglist.append(0)
                sglist.append(0)
                sflist.append(0)
                pflist.append(0)
                clist.append(0)
                glist.append(0)
                flist.append(0)
                ulist.append(1)
            #print(len(pglist))
            #print(len(sglist))
            #print(len(sflist))
            #print(len(pflist))
            #print(len(clist))
            newdf["PG"]=pglist
            newdf["SG"]=sglist
            newdf["SF"]=sflist
            newdf["PF"]=pflist
            newdf["C"]=clist
            newdf["Guard_Class"]=glist
            newdf["Forward_Class"]=flist
            newdf["Util_Class"]=ulist
            mstrdfr=mstrdfr.append(newdf,ignore_index= True)
    #Function to add unique values to the dataframe
    namecounter =[]
    counter =1
    for mstid in mstrdfr['Name'].unique():
        counter =1
        for i in range(len(mstrdfr[mstrdfr['Name']==mstid])):
            namecounter.append(counter)
            counter = counter +1
    mstrdfr["Countercol"]= namecounter
    mstrdfr["Countercol"]=mstrdfr["Countercol"].astype(str)
    mstrdfr["Unq_Masterid"] = (mstrdfr['Name']+','+mstrdfr["Countercol"])
    ##Part 3
    ##delete dataframes if needed
    try:
        del sampoptdf
        del playerlist
        del mstrplayer
    except:
        pass
    
    mstrdfr=mstrdfr.set_index("Unq_Masterid")
    dkpoints =[]
    loopnum=[]
    playerlist=  pd.DataFrame()
    mstrplayer=  pd.DataFrame()
    finaldf =pd.DataFrame()

    ##Store the basic data
    rowlist.append(samplepercent)
    loopcounter = 1 ##Mastercounter#The tells the for function how many loops its done 
    mastercount =1
    ##Team building function
    for modeltype in modellist:
        print(modeltype)
    loopcounter = 1
    sampoptdf = mstrdfr.copy()
    playerlist=  pd.DataFrame()
    mstrplayer=  pd.DataFrame()
    ###Loop to generate teams
    while len(mstrplayer) < dkteams:
        if  loopcounter ==1:
            optdf= sampoptdf.copy()
            loopnum.append(loopcounter)
            stagedf, stagedf2=DK_Optimization_Function.teamoptmizer(optdf,loopcounter,modeltype)
        else:
            optdf= sampoptdf.groupby('Position').apply(lambda grp: grp.sample(frac =samplepercent))
            optdf= optdf.drop('Position',axis=1)
            optdf= optdf.reset_index()
            optdf=optdf.set_index("Unq_Masterid")
            #sampoptdf.sample(frac =samplepercent)
        loopnum.append(loopcounter)
        stagedf, stagedf2=DK_Optimization_Function.teamoptmizer(optdf,loopcounter,modeltype)
        if len(stagedf) != 8:
            print("Issue with Team Builder Team Omitted")
        else:
            loopcounter= loopcounter+1
            mstrdfr=mstrdfr.reset_index()
            team=stagedf.merge(mstrdfr,on="Unq_Masterid",how ='inner')
            mstrdfr=mstrdfr.set_index("Unq_Masterid")
            ##Save the data for the list
            dkpoints.append(team[modeltype].sum())
            playerlist=  pd.DataFrame()
            playerlist=playerlist.append(stagedf2,ignore_index=True)
            playerlist.columns = ["0","1","2","3","4","5","6","7","Team","modeltype"]
            if loopcounter ==2:
                mstrplayer = playerlist.copy()
            else:
                mstrplayer = mstrplayer.append(playerlist)
                mstrplayer=mstrplayer.drop_duplicates(subset=("0","1","2","3","4","5","6","7"),keep ='last')
    rowlist.append(modeltype)
    rowlist.append(len(mstrplayer))
    rowlist.append(max(dkpoints))
    rowlist.append(min(dkpoints))
    rowlist.append(mean(dkpoints))
    rowlist.append(median(dkpoints))
    ##Clear out the old stuff
    if len(finaldf)==0:
        finaldf = mstrplayer.copy()
    else:
        finaldf=finaldf.append(mstrplayer)
    del playerlist
    dkpoints =[]
    #TeamInfo
    dkupload =pd.DataFrame(columns=["PG","SG","SF","PF","C","G","F","UTIL"])
    for index,row in mstrplayer.iterrows():
        #print(row)
        ###Take the row and get the nessesary data to construct a DKteam to upload
        teamdf=pd.DataFrame(row)
        teamdf=teamdf.rename(columns={0:"Unq_Masterid"})
        gval=teamdf[8:9].iloc[0].values
        teamdf=teamdf[:8]
        teamdf=teamdf.set_index("Unq_Masterid")
        teamdf=teamdf.merge(mstrdfr,on="Unq_Masterid",how ='inner')
        teamdf=teamdf.sort_values(["Dual_Class","postotal"])
        ###Position counts
        ############################
        pgcount =0
        sgcount=0
        sfcount=0
        pfcount=0
        ccount=0
        gcount=0
        fcount=0
        ucount=0
        pglits =[]
        sglits=[]
        sflits=[]
        pflits=[]
        clits=[]
        glits=[]
        flits=[]
        ulits=[]
        roundcount=0
        loopcount=0
        groupcount=0
        ############################
        for idz,pg,sg,sf,pf,c,gclass,fclass in zip(teamdf["ID"],teamdf["PG"],
                                    teamdf["SG"],teamdf["SF"],teamdf["PF"],teamdf["C"],
                                    teamdf["Guard_Class"],teamdf["Forward_Class"]):
            #print(pg,sg,sf,pf,c,gclass,fclass)

            if pg >0:
                #print("In1")
                if pgcount==0:
                    #print("in2")
                    pglits.append(idz)
                    pgcount=pgcount+1
                    roundcount=roundcount+1
            if roundcount==0:
                if sg >0:
                    if sgcount==0:
                        sglits.append(idz)
                        sgcount=sgcount+1
                        roundcount=roundcount+1
            if roundcount==0:
                if sf >0:
                    if sfcount==0:
                        sflits.append(idz)
                        sfcount=sfcount+1
                        roundcount=roundcount+1
            if roundcount==0:
                if pf >0:
                    if pfcount==0:
                        pflits.append(idz)
                        pfcount=pfcount+1
                        roundcount=roundcount+1
            if roundcount==0:
                if c >0:
                    if ccount==0:
                        clits.append(idz)
                        ccount=ccount+1
                        roundcount=roundcount+1
            if roundcount==0:
                if gclass >0:
                    #print("In")
                    if gcount==0:
                        glits.append(idz)
                        gcount=gcount+1
                        roundcount=roundcount+1

            if roundcount==0:
                if fclass >0:
                    if fcount==0:
                        flits.append(idz)
                        fcount=fcount+1
                        roundcount=roundcount+1
            if roundcount==0:
                if ucount==0:
                    ulits.append(idz)
                    ucount=ucount+1
                    roundcount=roundcount+1

            roundcount=0
        try:
            if pgcount !=0 or sgcount!=0 or sfcount!=0 or pfcount!=0 or ccount!=0 or gcount!=0 or fcount!=0 or ucount!=0:
                miniupload =pd.DataFrame({"PG":pglits,"SG":sglits,"SF":sflits,"PF":pflits,"C":clits,"G":glits,"F":flits,"UTIL":ulits})
                dkupload=dkupload.append(miniupload)
                print("Created team"+str(gval))
            else:
                print("Failed in First Else Statement")
                print(gval)
        except:
            print("Ouch caught in Except Loop")
            print(gval)
            break
            ####Check the list of players that are going to  be on the teams
    stackframes=[dkupload["PG"],dkupload["SG"],dkupload["SF"],dkupload["PF"],dkupload["C"],dkupload["G"],dkupload["F"],dkupload["UTIL"]]
    stackeddkup=pd.concat(stackframes)
    stackeddkup=stackeddkup.to_frame()
    stackeddkup=stackeddkup.rename(columns={0:"ID"})
    stackeddkup["ID"]=stackeddkup["ID"].astype(int)
    stackeddkup=stackeddkup.merge(dfr,on="ID",how ='inner')
    stackeddkupgb=stackeddkup.groupby("Name").agg({"ID":"count","AvgPointsPerGame":"mean"}).sort_values("ID",ascending =0)
    return stackeddkupgb,dkupload