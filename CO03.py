import pandas as pd
def CO03(filelist) :
    
    BOM={}
    partMapping={}
    with open(filelist) as files :
        for filename in files : 
            filename=filename.replace("\n","").strip()
            lines=open(filename).readlines()
            ordernr=lines[0][-11:].replace("\n","").strip()
            if (ordernr!=filename) :
                print ("Not Mached",ordernr, filename)

            for line in lines[10:-1] :    
                spltline=line.split("|")    
                partnr=spltline[2].strip()
                description=spltline[3].strip()
                qty=int(float(spltline[4].strip()))
                BOM[partnr] = BOM.get(partnr, 0) + qty   
                partMapping[partnr] = partMapping.get(partnr,description)
    header=['partnr','qty']
    df=pd.DataFrame(data=[BOM.keys(), BOM.values()]).transpose()
    df.columns=header
    df['description']=df['partnr'].apply(lambda x : partMapping[x])    
    
    return df