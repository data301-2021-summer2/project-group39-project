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