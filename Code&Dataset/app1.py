import pandas as pd
import numpy as np
import pickle as pkl
import streamlit as st

ds=pd.read_csv("new_cleaned_ipl.csv")
model=pkl.load(open("IplM.pkl","rb+"))

st.title("IPL Winner Prediction")

team_encoder={'Chennai Super Kings':0,'Delhi Capitals':1,'Gujarat Titans':2,'Kolkata Knight Riders':3,'Lucknow Super Giants':4,
              'Mumbai Indians':5,'Punjab Kings':6,'Royal Challengers Bengaluru':7,'Rajasthan Royals':8,'Sunrisers Hyderabad':9}
toss_encoder={'bat':0,'field':1}
city_encoder={'Bangalore':2, 'Ahmedabad':1, 'Mohali':23, 'Jaipur':17, 'Chennai':7, 'Mumbai':24,
       'Kolkata':21,'Delhi':9, 'Hyderabad':15, 'Pune':27, 'Lucknow':22,
       'Cape Town':4, 'Abu Dhabi':0, 'Chandigarh':6, 'Guwahati':14, 'Navi Mumbai':25,
       'Sharjah':31, 'Dharamsala':10, 'Indore':16, 'Rajkot':29, 'Dubai':11,
       'Port Elizabeth':26, 'Kanpur':19, 'Ranchi':30, 'Cuttack':8, 'Visakhapatnam':32,
       'Centurion':5, 'Raipur':28, 'Durban':12, 'Johannesburg':18, 'Bloemfontein':3,
       'Kimberley':20, 'East London':13}

team1=sorted(ds['team1'].unique())
team2=sorted(ds['team2'].unique())
toss_decision=sorted(ds['toss_decision'].unique())
city=sorted(ds['city'].unique())

team1_input=st.selectbox("Enter The First Team",team1)
Team1=team_encoder.get(team1_input,-1)
team2_input=st.selectbox("Enter The Second Team",team2)
Team2=team_encoder.get(team2_input,-1)
if (team1_input) == (team2_input):
    st.write("Please Select 2 Diffrent Team")
else:
    toss_winner=[team1_input,team2_input]
    toss_input=st.selectbox("Enter the Toss Winning Team",toss_winner)
    Toss_Winner=team_encoder.get(toss_input,-1)
    toss_decision_input=st.selectbox("Enter The Toss Decision",toss_decision)
    Toss_Decision=toss_encoder.get(toss_decision_input,-1)
    city1=sorted(ds[ds['team1']==team1_input]['city'].unique())
    city_input=st.selectbox("Enter The City/Venue",city1)
    City=city_encoder.get(city_input,-1)

if st.button("Predict Winner"):
    win_team_encoder={0:'Chennai Super Kings',1:'Delhi Capitals',2:'Gujarat Titans',3:'Kolkata Knight Riders',4:'Lucknow Super Giants',
                      5:'Mumbai Indians',6:'Punjab Kings',7:'Royal Challengers Bengaluru',8:'Rajasthan Royals',9:'Sunrisers Hyderabad'}

    
    columns=['team1','team2','toss_winner','toss_decision','city']
    myinput=pd.DataFrame([[Team1,Team2,Toss_Winner,Toss_Decision,City]],columns=columns)
    winner_team=model.predict(myinput)[0]
    Winner=win_team_encoder.get(winner_team,-1)
    st.write("The Winning Team is:",Winner)