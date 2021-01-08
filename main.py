import pandas as pd
import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials

# Settings for display in editor
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 100)
pd.set_option('display.max_seq_items', None)
pd.set_option('display.expand_frame_repr', True)
pd.set_option('display.max_colwidth', None)


# Opening and reading all posts from spreadsheet
gc = gspread.service_account("fp-dashboard-284608-e1c4cb864ad0.json")
sh = gc.open("Social media History ")
worksheet = sh.worksheet("Social media posts")

# Storage, renaming of columns
df = pd.DataFrame(worksheet.get_all_records())
df.rename(columns={"social media": "social_media", "Engagements (likes + comments + shares)": "engagements", "post id":"post_id","post creation date":"post_creation_date"}, inplace=True)

# Dataframe with only needed columns.
df_short = df[['date','social_media', 'post_id', 'post_creation_date', 'engagements']]
df_short['engagements'] = pd.to_numeric(df_short.engagements) # Change all values to numerical values

# Instagram data
df_insta = df_short[(df_short['social_media'] == 'instagram') & (df_short['engagements'] >= 60)]
print(df_insta)

# LinkedIn data
df_linkedIn = df_short[(df_short['social_media'] == 'linkedIn') & (df_short['engagements'] >= 140)]
print(df_linkedIn)

#print(df_short.engagements.unique())



#should I extract only columns 
# do I need to extract all data, or should I extract only the las X rows. Research max size of dataframes.
# do we need only an automation, or do we also want to know how past posts did?
#limitations to google api data. limitations for dataframes


