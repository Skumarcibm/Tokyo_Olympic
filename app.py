import streamlit as st
import pandas as pd
import helper
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
image = Image.open('E:\OJT_DataAnalysis\World-Triathlon.jpeg')
medals_21=pd.read_csv('E:\Dataset\Medals.csv')
athelete_21=pd.read_csv('E:\Dataset\Athletes.csv')

Gender_21=pd.read_csv('E:\Dataset\Genders.csv')
teams_21=pd.read_csv('E:\Dataset\Teams.csv')
coaches_21=pd.read_csv('E:\Dataset\Coaches.csv')

st.sidebar.title("Perfromance Analysis in Tokyo 2020")
st.sidebar.image(image)
user=st.sidebar.radio(
    'Select an Option',
    ('Overall Analysis','Medal Tally','India vs America',"Atheletes"))

if user=='Medal Tally':
    st.sidebar.header("Medal Tally")
    st.title("Performance of each country over Medals and their Rank")
    st.dataframe(medals_21)
    
    nation_over_medal=helper.medals_graph(medals_21)
    plt.figure(figsize=(12,5))
    plt.title("Top 10  Medalist Countries")
    sns.barplot(x=nation_over_medal['NOC'],y=nation_over_medal['Total'])
    plt.xlabel('Team')
    plt.ylabel('Number of Gold Medals')
    plt.xticks(rotation=75)
    st.pyplot(plt.gcf())
    
    country=helper.medal(medals_21)
    select_country=st.sidebar.selectbox("Select Country",country)
    abc=helper.medals(medals_21,select_country)
    
    if  select_country!="Select":
        st.title("Total medals Medals won by "+select_country )
    st.table(abc)

   
    #countries=helper.countrty_wise(medals_21,select_country)
    total=abc[['Gold','Silver','Bronze']].drop_duplicates().sum()
   
    length=len(total)

    plt.figure(figsize=(10,5))
    plt.title("Status of"+" "+select_country+" "+"Medals")
    x_axis=np.arange(length)
    plt.bar(x_axis,  abc['Gold'].drop_duplicates().sum(),label='Gold')
    plt.bar(x_axis, abc['Silver'].drop_duplicates().sum(),label='Silver')
    plt.bar(x_axis, abc['Bronze'].drop_duplicates().sum(),label='Bronze')
    sns.barplot(y=total,x=total.index)
    plt.xlabel("Medals")
    plt.ylabel("Medals Number")
    plt.xticks(x_axis,total,rotation='vertical')
    plt.legend()
    st.pyplot(plt.gcf())
    
if user=="Overall Analysis":
    st.title("Statics")
    event=athelete_21['Discipline'].unique().shape[0]
    country=athelete_21['NOC'].unique().shape[0]
    Atheletes=athelete_21['Name'].unique().shape[0]
    col1,col2,col3=st.columns(3)
   
    with col1:
        st.header("Sports")
        st.title(event)
    with col2:
        st.header("Nations")
        st.title(country)
    with col3:
        st.header("Atheletes")
        st.title(Atheletes)
    st.header("Coaches of each Contry")
    abc1=coaches_21.groupby('NOC').size()
    abc2=abc1.to_frame('Total_Coach')
    Top_10_Countries_Coaches=abc2.sort_values('Total_Coach',ascending=False).reset_index()
    st.dataframe(Top_10_Countries_Coaches)

    plt.figure(figsize=(12,9))
    sns.barplot(x=Top_10_Countries_Coaches['NOC'],y=Top_10_Countries_Coaches['Total_Coach'])
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf())

if user=="Atheletes":
    st.header("Country according their Atheletes")
    abc2=helper.athelets(athelete_21)
    st.dataframe(abc2)

    plt.figure(figsize=(12,5))
    plt.title("Top_10 Countries")
    sns.barplot(x=abc2['NOC'],y=abc2['Total_Atheles'])
    plt.xlabel('Team')
    plt.ylabel("Number of Medals")
    plt.xticks(rotation=75)
    st.pyplot(plt.gcf())
    
    country=helper.athelets_c(athelete_21)
    select_country=st.sidebar.selectbox("Select Country",country)
    abc3=helper.Atheletes_list(athelete_21,select_country)
    st.table(abc3)
    
    M=sum(Gender_21['Male'])
    F=sum(Gender_21['Female'])
    dataset=[M,F]
    colors=["r","g"]
    names=['Male','Female']
    plt.figure(figsize=(10,7))
    plt.pie(dataset,labels=names,autopct='%1.1f%',textprops={'fontsize':15},colors=colors)
    st.pyplot(plt.gcf())
    
if user=="India vs America":
    st.header("India`s Status")
    abc1=coaches_21.groupby('NOC').size()
    abc2=abc1.to_frame('Total_Coach')
    Top_10_Countries_Coaches=abc2.sort_values('Total_Coach',ascending=False).reset_index()
    st.dataframe(abc2.query('NOC=="India"').reset_index())

    


    e=athelete_21.query('NOC=="India"').drop_duplicates()
    st.dataframe(e)
    st.header("Total Discipline played by India") 
    st.title(e['Discipline'].drop_duplicates().count())

    c=e.groupby('Discipline').size()
    g=c.to_frame('Total')
    f=g.sort_values('Total',ascending=False).reset_index()
    st.table(f)
    st.header("Number of Atheletes of Country India")
    st.title(f['Total'].sum())
    
    st.title("Graphical Representation of India`s Discipline")
    plt.figure(figsize=(12,5))
    plt.title("Status of India`s Discipline")
    sns.barplot(x=f['Discipline'],y=f['Total'])
    plt.xlabel('Name of Discipline')
    plt.ylabel("Number of Discipline")
    plt.xticks(rotation=75)
    st.pyplot(plt.gcf())
    India_Stats=medals_21[medals_21['NOC']=="India"]
    st.dataframe(India_Stats)

    total=India_Stats[['Gold','Silver','Bronze']].drop_duplicates().sum()
    sum=0
    length=len(total)
    for i in range(0,length):
        sum=sum+total[i]
    print("Total Medals won by India in Tokyo Olympic={}".format(sum))  
    total

    plt.figure(figsize=(10,5))
    plt.title("Status of India Medals")
    x_axis=np.arange(length)
    plt.bar(x_axis,India_Stats['Gold'].drop_duplicates().sum(),label='Gold')
    plt.bar(x_axis,India_Stats['Silver'].drop_duplicates().sum(),label='Silver')
    plt.bar(x_axis,India_Stats['Bronze'].drop_duplicates().sum(),label='Bronze')
    sns.barplot(y=total,x=total.index)
    plt.xlabel("Medals")
    plt.ylabel("Medals Number")
    plt.xticks(x_axis,total,rotation='vertical')
    plt.legend()
    st.pyplot(plt.gcf())
    # America details
    st.header("United States of America `s Status")
    st.dataframe(abc2.query('NOC=="United States of America"').reset_index())
    e=athelete_21.query('NOC=="United States of America"').drop_duplicates()
    st.dataframe(e)
    st.header("Total Discipline played by America") 
    st.title(e['Discipline'].drop_duplicates().count())

    c=e.groupby('Discipline').size()
    g=c.to_frame('Total')
    f=g.sort_values('Total',ascending=False).reset_index()
    st.table(f)
    st.header("Number of Atheletes of Country America")
    st.title(f['Total'].sum())
    
    st.title("Graphical Representation of America`s Discipline")
    plt.figure(figsize=(12,5))
    plt.title("Status of United States of America`s Discipline")
    sns.barplot(x=f['Discipline'],y=f['Total'])
    plt.xlabel('Name of Discipline')
    plt.ylabel("Number of Discipline")
    plt.xticks(rotation=75)
    st.pyplot(plt.gcf())
    America_Stats=medals_21[medals_21['NOC']=="United States of America"]
    st.dataframe(America_Stats)

    total=America_Stats[['Gold','Silver','Bronze']].drop_duplicates().sum()
    sum=0
    length=len(total)
    for i in range(0,length):
        sum=sum+total[i]
    print("Total Medals won by America in Tokyo Olympic={}".format(sum))  
    total

    plt.figure(figsize=(10,5))
    plt.title("Status of America Medals")
    x_axis=np.arange(length)
    plt.bar(x_axis,America_Stats['Gold'].drop_duplicates().sum(),label='Gold')
    plt.bar(x_axis,America_Stats['Silver'].drop_duplicates().sum(),label='Silver')
    plt.bar(x_axis,America_Stats['Bronze'].drop_duplicates().sum(),label='Bronze')
    sns.barplot(y=total,x=total.index)
    plt.xlabel("Medals")
    plt.ylabel("Medals Number")
    plt.xticks(x_axis,total,rotation='vertical')
    plt.legend()
    st.pyplot(plt.gcf())

   
