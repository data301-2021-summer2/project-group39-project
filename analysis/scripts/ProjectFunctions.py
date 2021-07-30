#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def CoachData(n):
   
    df = (
        pd.read_csv(n)
       .groupby(['head_coach','team_id'])
       .sum()
       .reset_index()
       .drop(['game_id'], axis = 'columns')
        )
    return df

def TeamData(n):
        # Method chaining begins
    df = (
         pd.read_csv(n)
        )
    df2 = (
         df[(df['team_id']) <= 54 ]
         .drop(['game_id','HoA','settled_in','head_coach','faceOffWinPercentage','startRinkSide'], axis ='columns')
         .groupby('team_id').sum()
         .reset_index(drop=True)
    )
    return df2

def TeamList(n):
        # Method chaining begins
    df = (
         pd.read_csv(n)
        .drop(['franchiseId','abbreviation','link'],axis='columns')
        .sort_values(by='team_id',ascending=True)
        .reset_index(drop=True)
        )
    return df

def gameclean(n):
    df = (
         pd.read_csv(n)
        .drop(['season' , 'type', 'date_time_GMT' , 'away_team_id' , 'home_team_id' , 'outcome' , 'home_rink_side_start'], axis='columns')
        .drop(['venue_link','venue_time_zone_id','venue_time_zone_offset','venue_time_zone_tz'], axis='columns')
        
    )
    return df

def ShiftsCleaning(adress1):
        
    df = (
         pd.read_csv(adress1)
        .assign(shiftlength=lambda adress1:(adress1['shift_end']-adress1['shift_start']))
        )
    df2 = (
         df4[(df4['shiftlength']) > 0 ]
        .drop(['period','shift_start','shift_end'], axis='columns')
    )
    return df2
        
def GroupingPlayer(df):
    df1 = (
        df.groupby('ID').mean()
    )
    return df1
        
def StatsCleaning(adress2):
    df7 = (pd.read_csv(adress2)
          .drop(['faceoffTaken', 'takeaways', 'giveaways','hits','blocked','faceOffWins','evenTimeOnIce','penaltyMinutes','powerPlayTimeOnIce','shortHandedTimeOnIce'],axis='columns')
          .assign(Goals=lambda adress2:(adress2["goals"]+adress2["powerPlayGoals"]+adress2["shortHandedGoals"]))
          .assign(Assists=lambda adress2:(adress2["assists"]+adress2["powerPlayAssists"]+adress2["shortHandedAssists"]))
          .drop(['goals','assists','powerPlayGoals','powerPlayAssists','shortHandedGoals','shortHandedAssists','game_id','player_id'], axis='columns')
          )
    return df7

