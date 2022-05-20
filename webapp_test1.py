import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
import plotly.express as px

df= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\crime1.csv')
st.markdown("<h1 style='text-align:left; color:red;'><u><b>Gender Discrimination and Inequality analysis</b></u></h1>",unsafe_allow_html=True)
#st.title("Gender Discrimination and Inequality analysis")
st.sidebar.title("FIELDS")
select1 = st.sidebar.selectbox('Domains',options=['Choose a field','Education','Workforce','Crime'])
if select1!="Crime":
    st.sidebar.title("Visualisation")
    select2=st.sidebar.selectbox('Domains',options=['Choose the type of visualisation you want to see','Bar style','Line style','Scatter style'])
else:
    data_url=('C:\\Users\\hp\Desktop\\stremlitut\\crime_processed_data.csv')
    data=pd.read_csv(data_url)
    st.sidebar.title("Visualisation")
    select3=st.sidebar.selectbox('Domains',options=['Choose the type of visualisation you want to see','Bar style','Map style'])
    #if select3=='Map style':
        #st.sidebar.title("Choose the state")
        #select2=st.sidebar.selectbox('State',options=df["STATE/UT"])

class education:
    @staticmethod
    def literacy_rate(vis):
        data= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\literacy rate 15 years and above.csv')
        df = data.loc[data['Country Name'] =='India']
        df.dropna(axis=1,inplace=True)
        dat = df.iloc[0, 4:]
        daf = pd.DataFrame(dat).reset_index()
        daf.columns = ['years', 'literacy_rate_of_15years_ above']
        fig1 = px.scatter(daf, x="years", y="literacy_rate_of_15years_ above", color="years")
        fig2 = px.line(daf, x="years", y="literacy_rate_of_15years_ above")
        fig3 = px.bar(daf, x="years", y="literacy_rate_of_15years_ above",color="years")
        st.title("LITERACY RATE")
        if vis=="Bar style":
            st.plotly_chart(fig3)
        elif vis=="Line style":
            st.plotly_chart(fig2)
        else:
            st.plotly_chart(fig1)

    @staticmethod
    def high_schooledu(vis):
        data= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\Progression to high school female.csv')
        df = data.loc[data['Country '] =='India']
        df.dropna(axis=1,inplace=True)
        dat = df.iloc[0, 4:]
        daf = pd.DataFrame(dat).reset_index()
        daf.columns = ['years', 'count']
        fig1 = px.bar(daf, x="years", y="count",color="years")
        fig2 = px.line(daf, x="years", y="count")
        fig3 = px.scatter(daf, x="years", y="count", color="years")
        st.title("High School Education")
        if vis=="Bar style":
            st.plotly_chart(fig1)
        elif vis=="Line style":
            st.plotly_chart(fig2)
        else:
            st.plotly_chart(fig3)
    @staticmethod
    def primary_edu(vis):
        data= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\Primary education female.csv')
        df = data.loc[data['Country Name'] == 'India']
        df.dropna(axis=1,inplace=True)
        dat = df.iloc[0, 4:]
        daf = pd.DataFrame(dat).reset_index()
        daf.columns = ['years', 'count']
        fig1 = px.bar(daf, x="years", y="count",color="years")
        fig2 = px.line(daf, x="years", y="count")
        fig3 = px.scatter(daf, x="years", y="count", color="years")
        st.title("Primary Education")
        if vis=="Bar style":
            st.plotly_chart(fig1)
        elif vis=="Line style":
            st.plotly_chart(fig2)
        else:
            st.plotly_chart(fig3)
    @staticmethod
    def GPI_primary(vis):
        data= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\Parity Index (primary).csv')
        main=data[data["Country Name"]=="India"]
        main.dropna(axis=1,inplace=True)
        main.drop(["Indicator Code"],axis=1)
        main.iloc[[0]]
        temp = main.iloc[0, 4:]
        final= pd.DataFrame(temp).reset_index()
        final.columns = ['Years', 'Gender Parity Index']
        fig1 = px.scatter(final, x="Years", y="Gender Parity Index", color="Years")
        fig2 = px.line(final, x="Years", y="Gender Parity Index")
        fig3 = px.bar(final, x="Years", y="Gender Parity Index",color="Years")
        st.title("Gender parity Index primary education")
        if vis=="Bar style":
            st.plotly_chart(fig3)
        elif vis=="Line style":
            st.plotly_chart(fig2)
        else:
            st.plotly_chart(fig1)
    @staticmethod
    def GPI_secondary(vis):
        data= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\Final year project\\Gender Parity Index(primary and secondary).csv')
        main=data[data["Country Name"]=="India"]
        main.dropna(axis=1,inplace=True)
        main.drop(["Indicator Code"],axis=1)
        main.iloc[[0]]
        temp = main.iloc[0, 4:]
        final= pd.DataFrame(temp).reset_index()
        final.columns = ['Years', 'Gender Parity Index']
        fig1 = px.scatter(final, x="Years", y="Gender Parity Index", color="Years")
        fig2 = px.line(final, x="Years", y="Gender Parity Index")
        fig3 = px.bar(final, x="Years", y="Gender Parity Index",color="Years")
        st.title("Gender parity Index secondary education")
        if vis=="Bar style":
            st.plotly_chart(fig3)
        elif vis=="Line style":
            st.plotly_chart(fig2)
        else:
            st.plotly_chart(fig1)

class Workforce:
    @staticmethod
    def wagensalaries(vis):
        data1= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\Wage and salaried workers, female.csv') 
        data2= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\Wage and salaried workers, male.csv') 
        main1=data1[data1["Country Name"]=="India"]
        main2=data2[data2["Country Name"]=="India"]
        main1.dropna(axis=1,inplace=True)
        main2.dropna(axis=1,inplace=True)
        temp1 = main1.iloc[0, 4:]
        temp2 = main2.iloc[0, 4:]
        final1= pd.DataFrame(temp1).reset_index()
        final1.columns = ['Years', 'Wage and salaried workers(female)']  
        final2= pd.DataFrame(temp2).reset_index()
        final2.columns = ['Years', 'Wage and salaried workers(male)']
        merged_inner = pd.merge(left=final1, right=final2, left_on='Years', right_on='Years')
        fig1 = px.line(merged_inner,x="Years", y=["Wage and salaried workers(female)","Wage and salaried workers(male)"])
        fig2 = px.scatter(merged_inner,x="Years", y=["Wage and salaried workers(female)","Wage and salaried workers(male)"])
        fig3 = px.bar(final1, x="Years", y="Wage and salaried workers(female)",color="Years")
        fig4 = fig = go.Figure(data=[
        go.Bar(name='Wage and salaried workers(female)', x=merged_inner["Years"], y=merged_inner["Wage and salaried workers(female)"]),
        go.Bar(name='Wage and salaried workers(male)', x=merged_inner["Years"], y=merged_inner["Wage and salaried workers(male)"])
        ])
        # Change the bar mode
        fig.update_layout(barmode='group')  
        st.title("Wage and salaried workers")
        if vis=="Bar style":
            st.plotly_chart(fig3)
            st.plotly_chart(fig4)
        elif vis=="Line style":
            st.plotly_chart(fig1)
        else:
            st.plotly_chart(fig2)
    @staticmethod
    def ratio_labourforce(vis):
        data= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\Ratio of female to male labor force participation rate.csv')
        main=data[data["Country Name"]=="India"]
        main.dropna(axis=1,inplace=True)
        temp = main.iloc[0, 4:]
        final= pd.DataFrame(temp).reset_index()
        final.columns = ['Years', 'Ratio of female to male labor force participation rate']
        fig1 = px.scatter(final, x="Years", y="Ratio of female to male labor force participation rate", color="Years")
        fig2 = px.line(final, x="Years", y="Ratio of female to male labor force participation rate")
        fig3 = px.bar(final, x="Years", y="Ratio of female to male labor force participation rate",color="Years")
        st.title("Female to male labour force participation")
        if vis=="Bar style":
            st.plotly_chart(fig3)
        elif vis=="Line style":
            st.plotly_chart(fig2)
        else:
            st.plotly_chart(fig1)
    @staticmethod
    def labourforce(vis):
        data1= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\labour male.csv')
        data2= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\labour female.csv')
        main1=data1[data1["Country Name"]=="India"]
        main2=data2[data2["Country Name"]=="India"]
        main1.dropna(axis=1,inplace=True)
        main2.dropna(axis=1,inplace=True)
        temp1 = main1.iloc[0, 4:]
        temp2 = main2.iloc[0, 4:]
        final1= pd.DataFrame(temp1).reset_index()
        final1.columns = ['Years', 'labour participation(female)']
        final2= pd.DataFrame(temp2).reset_index()
        final2.columns = ['Years', 'labour participation (male)']
        merged_inner = pd.merge(left=final1, right=final2, left_on='Years', right_on='Years')
        fig1 = px.line(merged_inner,x="Years", y=["labour participation(female)","labour participation (male)"])
        fig2 = px.scatter(merged_inner,x="Years", y=["labour participation(female)","labour participation (male)"])
        fig3 = px.bar(final1, x="Years", y="labour participation(female)",color="Years")
        fig4 = go.Figure(data=[
        go.Bar(name='LABOUR PARTICIPATION (FEMALE)', x=merged_inner["Years"], y=merged_inner["labour participation(female)"]),
        go.Bar(name='LABOUR PARTICIPATION (MALE))', x=merged_inner["Years"], y=merged_inner["labour participation (male)"])
        ])
        # Change the bar mode
        fig4.update_layout(barmode='group')
        st.title("Labour force participation")
        if vis=="Bar style":
            st.plotly_chart(fig3)
            st.plotly_chart(fig4)
        elif vis=="Line style":
            st.plotly_chart(fig1)
        else:
            st.plotly_chart(fig2)

class crime:
    @staticmethod
    def search_group(select,data):
        if select=='NONE':
            return
        else:
            for i in range(len(data["STATE/UT"])):
                if select==data["STATE/UT"].iloc[i]:
                    return data.iloc[[i]].reset_index()
    @staticmethod               
    def Crime_map():
        data= pd.read_csv('C:\\Users\\hp\Desktop\\stremlitut\\crime1.csv')
        st.sidebar.title("Choose the state")
        select=st.sidebar.selectbox('State',options=df["STATE/UT"])
        obj=crime.search_group(select,data)
        obj.drop(['Unnamed: 0','index'], axis = 1,inplace=True)
        obj['avg'] = pd.to_numeric(obj[["Rape","Kidnapping and Abduction","Dowry Deaths","Assault on women with intent to outrage her modesty","Insult to modesty of Women","Cruelty by Husband or his Relatives","Importation of Girls"]].mean(axis=1))
        st.write(obj)
        
        
        #if int(obj.iloc[0]['avg'])>0 and int(obj.iloc[0]['avg'])<2000:
            #folium.Marker(location=loc,popup='MODERATELY UNSAFE ZONE'+' WITH '+str(value)+' CRIMES PER YEAR',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='blue',icon='none')).add_to(m)
        #elif int(obj.iloc[0]>4000) and int(obj.iloc[0])<10000:
            #folium.Marker(location=loc,popup='SAFE'+' WITH '+str(value)+' CRIMES PER YEAR',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='green',icon='none')).add_to(m)
        #else:
            #folium.Marker(location=loc,popup='DANGEROUS ZONE'+' WITH '+str(value)+' CRIMES PER YEAR',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='red',icon='none')).add_to(m)
       
    @staticmethod
    def Crime_bar():
        data= pd.read_csv('crimes_against_women_2001-2014 (2).csv')
        data.drop(['Unnamed: 0','DISTRICT'], axis = 1,inplace=True)
        data.dropna(axis=1,inplace=True)
        data["STATE/UT"]=data["STATE/UT"].apply(lambda x: x.upper())
        group=data.groupby('STATE/UT',as_index=False)["Rape","Kidnapping and Abduction","Dowry Deaths","Assault on women with intent to outrage her modesty","Insult to modesty of Women","Cruelty by Husband or his Relatives","Importation of Girls"].mean()
        st.title("Number of rape cases per year")
        fig1 = px.bar(group, x="STATE/UT", y="Rape",color="STATE/UT")
        st.plotly_chart(fig1)    
        st.title("Kidnapping and Abduction cases per year")
        fig2 = px.bar(group, x="STATE/UT", y="Kidnapping and Abduction",color="STATE/UT")
        st.plotly_chart(fig2)
        st.title("Dowry deaths per year")
        fig3 = px.bar(group, x="STATE/UT", y="Dowry Deaths",color="STATE/UT")
        st.plotly_chart(fig3)
        st.title("Assault on women with intent to outrage her modesty per year")
        fig4 = px.bar(group, x="STATE/UT", y="Assault on women with intent to outrage her modesty",color="STATE/UT")
        st.plotly_chart(fig4)
        st.title("Cruelty by Husband or his Relatives per year")
        fig5 = px.bar(group, x="STATE/UT", y="Cruelty by Husband or his Relatives",color="STATE/UT")
        st.plotly_chart(fig5)




if select1=="Education" and select2!="Choose the type of visualisation you want to see":
    obj=education()
    obj.literacy_rate(select2)
    obj.high_schooledu(select2)
    obj.primary_edu(select2)
    obj.GPI_primary(select2)
    obj.GPI_secondary(select2)
elif select1=="Workforce" and select2!="Choose the type of visualisation you want to see":
    obj=Workforce()
    obj.wagensalaries(select2)
    obj.ratio_labourforce(select2)
    obj.labourforce(select2)
elif select1=="Crime" and select3!="Choose the type of visualisation you want to see":
    obj=crime()
    if select3=="Map style":
        obj.Crime_map()
    else:
        obj.Crime_bar()



