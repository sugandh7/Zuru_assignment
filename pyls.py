import pandas as pd
import json
import sys
import argparse
from datetime import datetime


with open('structure.json') as f:
    data = json.load(f)
parser = argparse.ArgumentParser(description="Example script for command line arguments.")
df = pd.json_normalize(data)
list_of_arguments=sys.argv
length_of_arguments=len(sys.argv)
print(f"list_of_arguments: {length_of_arguments}")
print(f"length_of_arguments: {list_of_arguments}")


if length_of_arguments==1:
    arr=[]
    arr=df["contents"]
    list_of_names=[]

    for i, individual_dict in enumerate(arr[0]):
        if(individual_dict['name'][0]!='.'):
            list_of_names.append(individual_dict['name']) 
            
    str=""
    for l in list_of_names:
        str=str +"  "+ l
    print("{}".format(str))        
           
elif  length_of_arguments==2 and list_of_arguments[1]=='-A' :           
    arr=[]
    arr=df["contents"]
    list_of_names=[]

    for i, individual_dict in enumerate(arr[0]):
            list_of_names.append(individual_dict['name']) 
            
    str=""
    for l in list_of_names:
        str=str +"  "+ l
    print("{}".format(str))        
elif  length_of_arguments==2 and list_of_arguments[1]=='-l' :
    arr=[]
    arr=df["contents"]
    data = {
    "permissions":[],
    "size":[],
    "time_modified":[],
    "name":[]
    }
    for c in arr:
        for d in c:
            if d['name'][0]!='.':    
                str1=''
                data['permissions'].append(d['permissions'])
                data['size'].append(str(d['size']))
                data['time_modified']=pd.to_datetime(d['time_modified'], unit='s')
                data['name'].append(d['name'])   
    df = pd.DataFrame(data)
    
    print(df)           
elif  length_of_arguments==3 and list_of_arguments[1]=='-l' and list_of_arguments[2]=='-r' : 
    # *********
    arr=[]
    arr=df["contents"].iloc[::-1]
    data = {
    "permissions":[],
    "size":[],
    "time_modified":[],
    "name":[]
    }
    for c in arr:
        for d in c:
            if d['name'][0]!='.':    
                str1=''
                
                data['permissions'].append(d['permissions'])
                data['size'].append(str(d['size']))
                # data['time_modified']=pd.to_datetime(d['time_modified'], unit='s')
                data['time_modified'].append(pd.to_datetime(d['time_modified'], unit='s'))
                data['name'].append(d['name'])  
    df = pd.DataFrame(data)
    df = df.iloc[::-1].reset_index(drop=True)
    print(df)           
elif  length_of_arguments==4 and list_of_arguments[1]=='-l' and list_of_arguments[2]=='-r' and list_of_arguments[3]=='-t': 
    arr=[]
    arr=df["contents"].iloc[::-1]
    data = {
    "permissions":[],
    "size":[],
    "time_modified":[],
    "name":[]
    }
    for c in arr:
        for d in c:
            if d['name'][0]!='.':    
                str1=''
                
                data['permissions'].append(d['permissions'])
                data['size'].append(str(d['size']))
                data['time_modified'].append(pd.to_datetime(d['time_modified'], unit='s'))
                data['name'].append(d['name']) 
    df = pd.DataFrame(data)
    df = df.iloc[::-1].reset_index(drop=True)
    sorted_df = df.sort_values(by='time_modified', ascending=False)
    print(sorted_df)           

elif  length_of_arguments==5   and list_of_arguments[1]=='-l' and list_of_arguments[2]=='-r' and list_of_arguments[3]=='-t': 
    # *********
    parts = list_of_arguments[4].split('=')

    if len(parts) > 1:
        value = parts[1]
    else:
        value = '' 
    arr=[]
    arr=df["contents"].iloc[::-1]
    data = {
    "permissions":[],
    "size":[],
    "time_modified":[],
    "name":[]
    }
    if  value=='dir' or  value=='file': 
        for c in arr:
            for d in c:
                if d['name'][0]!='.' and value=='dir' and d['permissions'][0]=='d':    
                    data['permissions'].append(d['permissions'])
                    data['size'].append(str(d['size']))
                    data['time_modified'].append(pd.to_datetime(d['time_modified'], unit='s'))
                    data['name'].append(d['name'])           
                elif d['name'][0]!='.' and value=='file' and d['permissions'][0]=='-':    
                    data['permissions'].append(d['permissions'])
                    data['size'].append(str(d['size']))
                    data['time_modified'].append(pd.to_datetime(d['time_modified'], unit='s'))
                    data['name'].append(d['name'])
                            
        df = pd.DataFrame(data)
        df = df.iloc[::-1].reset_index(drop=True)
        sorted_df = df.sort_values(by='time_modified', ascending=False)
        print(sorted_df)           
    else:
        print('error: \'folder\' is not a valid filter criteria. Available filters are \'dir\' and \'file\'')
      
elif  length_of_arguments==2 and list_of_arguments[1]=='-h': 
    # *********
    arr=[]
    arr=df["contents"].iloc[::-1]
    data = {
    "permissions":[],
    "size":[],
    "time_modified":[],
    "name":[]
    }
    for c in arr:
        for d in c:
            if d['name'][0]!='.':    
                str1=''
                
                data['permissions'].append(d['permissions'])
                data['time_modified'].append(pd.to_datetime(d['time_modified'], unit='s'))
                data['name'].append(d['name'])    
                if d['size']<1024:
                    data['size'].append(str(d['size']/1024)+'K')
                elif d['size']>1024 and  d['size']<1024*1024:
                    data['size'].append(str(d['size']/1024)+'M')
                else:
                    data['size'].append(str(d['size']/1024*1024*1024)+'G')
            
    df = pd.DataFrame(data)
    df = df.iloc[::-1].reset_index(drop=True)
    sorted_df = df.sort_values(by='time_modified', ascending=False)
    print(sorted_df)           
    

else :
    pass
