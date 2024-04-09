# Imorting pandas and data set

import pandas as pd
import datetime
import numpy as np
from numpy import nan

df = pd.read_csv(r'c:\Users\Simona\Desktop\Personal_Portfolio\Apsilankymas\Apsilankymas.csv')
print(df)

# Checking for the column names to see which ones are not useful to drop

column_names = list(df.columns.values)
print(column_names)

df_dropped = df.drop(['_type', '_revision', 'vda_id', 'gimimo_metai_gr', 'vartojimo_budas'], axis = 1)

# Removing duplicates from the data set by pacient(pacientas)

df_wo_dup = df_dropped.drop_duplicates(['pacientas'])
print(df_wo_dup)

# Filling blanks 

df_wo_na = df_wo_dup.fillna('Not provided')

print('is nan', df_wo_na.isna().values.any()) 
print('is null', df_wo_na.isnull().values.any()) 

# Renaming columns from lithuanian to english

df_wo_na_rn = df_wo_na.rename(columns={'_revision' : 'revision_id' , 
                                      'pacientas' : 'patient', 
                                      'vizito_data' : 'visit_date', 
                                      'lytis' : 'sex', 
                                      'amzius_gr' : 'age_group', 
                                      'gyvenamoji_vieta' : 'residence', 
                                      'issilavinimas' : 'education', 
                                      'uzimtumas' : 'occupation', 
                                      'sveikatos_draudimas' : 'health_insurance', 
                                      'vizitas' : 'visit', 
                                      'vartojimo_stazas' : 'period_of_drug_abuse', 
                                      'epizodai': 'episodes', 
                                      'apsilankymai' : 'visits', 
                                      'diagnoze' : 'diagnosis'})

column_names_new = list(df_wo_na_rn.columns.values)
print(column_names_new)

# Renaming useful strings from lithuanian to english for future visualization

## Visit

df_wo_na_rn['visit'].unique()

df1 = df_wo_na_rn.replace({'visit' : { 'pirminis' : 'Primary', 'pakartotinis' : 'Repeated'}})

df1['visit'].unique()

## Occupation

df1['occupation'].unique()

df2 = df1.replace({'occupation' : { 'augina mažamečius vaikus' : 'Raising small children', 
                                    'dirba' : 'Working', 
                                    'mokosi' : 'Studying',
                                    'nedirba, bet draustas' : 'Not working but insured',
                                    'nedirbantis' : 'Not working',
                                    'pensininkas' : 'Retired',
                                    'draustas savo lėšom' : 'Self-insured', 
                                    'duomenų nepateikė' : 'Not provided',
                                    'neįgalus' : 'Disabled',
                                    'registruotas darbo biržoje' : 'Registered in Labor Service'}})

df2['occupation'].unique()

## Education

df2['education'].unique()

substring = '65'
filter = df2['education'].str.contains(substring)
filtered_df = df2[~filter]

df3 = filtered_df.replace({'education' : { 'spec. vidurinis (profesinis)' : 'Vocasional training', 
                                   'nenurodė' : 'Not provided', 
                                   'duomenų nepateikė' : 'Not provided',
                                   'vidurinis (12 kl.)' :'High school', 
                                   'pradinis (1-4 kl.)' : 'Primary school' ,
                                   'pagrindinis (9-10 kl.)' : 'Junior high school', 
                                   'aukštesnysis' : 'College', 
                                   'aukštasis' : 'University'}})

df3['education'].unique()

## Residence 

df3['residence'].unique()

df4 = df3.replace({'residence' : {'Vilniaus miestas' : 'Vilnius', 
                                  'Vilniaus apskritis': 'Vilnius', 
                                  'Alytaus apskritis' : 'Alytus',
                                  'Panevėžio apskritis' : 'Panevezys', 
                                  'Utenos apskritis' : 'Utena', 
                                  'Šiaulių apskritis' : 'Siauliai',
                                  'Kauno apskritis' : 'Kaunas', 
                                  'Marijampolės apskritis' : 'Marijampole', 
                                  'Klaipėdos apskritis' : 'Klaipeda',
                                  'Tauragės apskritis' : 'Taurage', 
                                  'Telšių apskritis' : 'Telsiai', 
                                  'Užsienis' : 'Abroad'}})

df4['residence'].unique()

## Sex

df4['sex'].unique()

df5 = df4.replace({'sex' : {'vyras' : 'Male', 'moteris': 'Female'}})

df5['sex'].unique()

## Period of drug abuse

df5['period_of_drug_abuse'].unique()

df6 = df5.replace({'period_of_drug_abuse' : { '100.0' : '0', 'Not provided' : '0'}})

df6['period_of_drug_abuse'] = df6['period_of_drug_abuse'].astype(int)

df6['period_of_drug_abuse'].unique()

# Getting only year from the date

df6['visit_date'].unique()

df6['date'] = pd.to_datetime(df5['visit_date'])
print(df6)

df6['date'] = pd.to_datetime(df6['date'])
df6['year'], df6['month'] = df6['date'].dt.year, df6['date'].dt.month
df6

# Age group

df6['age_group'].unique()

df7 = df6.replace({'age_group' : {'14-Oct' : 'Not provided'}})

df7['age_group'].unique()

# Checking the type of df5 before exporting 

type(df7)

