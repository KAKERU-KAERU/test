import pandas as pd

data_by_list=[
    ['spam',500,3],
    ['egg',168,8],
    ['beacon',1250,1]
]

df_by_lsit=pd.DataFrame(data_by_list)
print(df_by_lsit)

data_by_dict={
    'name':['spam','egg','beacon'],
    'unit price':[500,168,1250],
    'num':[3,8,1]
}

index=['one','two','three']
df_by_dict=pd.DataFrame(data_by_dict,index=index)
print(df_by_dict)