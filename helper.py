import numpy
def medal(df):
    Country=df['NOC'].unique().tolist()
    Country.sort()
    #Country.insert(0,"Select")
    return Country
def medals(df,country):
    
    df_d=df[df['NOC']==country].drop_duplicates().reset_index()
    if country=='Select':
        temp_df= df_d
    else:
        temp_df=df_d[ df_d['NOC']==country]
    return temp_df

def medals_graph(df):
    Top_10_Gold=df[['NOC','Total','Rank by Total']]
    Top_10_Gold=Top_10_Gold.sort_values('Total',ascending=False).reset_index().head(10)
    return Top_10_Gold

def athelets(df):
    Top_athelets=df.groupby('NOC').size()
    num_ath=Top_athelets.to_frame('Total_Atheles')
    num_ath1=num_ath.sort_values('Total_Atheles',ascending=False).reset_index().head(10)
    return num_ath1
def athelets_c(df):
    Country=df['NOC'].unique().tolist()
    Country.sort()
    return Country
def Atheletes_list(df,country):
    #Top_athelets=df.groupby('NOC').size()
    #num_ath=Top_athelets.to_frame('Total_Atheles')
    temp_df=df[df['NOC']==country].drop_duplicates().reset_index()
    if country=='Select':
        temp1_df= temp_df
    else:
        temp1_df=df[df['NOC']==country]
    return temp1_df
    #temp_df= num_ath.query('NOC=="country"')
    #return temp_df
    
