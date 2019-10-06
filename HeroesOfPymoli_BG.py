#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[51]:


# Dependencies and Setup
import pandas as pd
import numpy as np
# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data


# ## Player Count

# * Display the total number of players
# 

# In[2]:


total_player=pd.DataFrame({"Total Players":[purchase_data["SN"].nunique()]})
total_player


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


unique_items = purchase_data.groupby("Item ID")["Item ID"].nunique().count()
avg_price = purchase_data["Price"].mean()
num_purchase=purchase_data["Purchase ID"].count()
revenue=purchase_data["Price"].sum()

pd.DataFrame({"Number of Unique Items":[unique_items],
             "Average Price":["${:.2f}".format(avg_price)],
             "Number of Purchases":[num_purchase],
             "Total Revenue":["${:.2f}".format(revenue)]})


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[4]:


Demo_data=purchase_data.groupby("Gender")["SN"].nunique()
df=pd.DataFrame({'':Demo_data.index, 'Total Count':Demo_data.values})
sum_player=df["Total Count"].sum()
df["Percentage of Players"] = df["Total Count"] *100 / sum_player
df["Percentage of Players"]=df["Percentage of Players"].map("{:.2f}%".format)
new_demo=df.set_index('').sort_values("Total Count",ascending=False)
new_demo


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[5]:


purchase_count=purchase_data.groupby("Gender")["Purchase ID"].count()
avg_price=purchase_data.groupby("Gender")["Price"].mean()
total_value=purchase_data.groupby("Gender")["Price"].sum()
count=purchase_data.groupby("Gender").nunique()["SN"].unique()
avg_person=total_value/count


# In[6]:


purchasing_analysis=pd.DataFrame({"Purchase Count":purchase_count,
                                 "Average Purchase Price":avg_price,
                                 "Total Purchase Value":total_value,
                                 "Avg Total Purchase per Person":avg_person})
purchasing_analysis["Average Purchase Price"]=purchasing_analysis["Average Purchase Price"].map("${:.2f}".format)
purchasing_analysis["Total Purchase Value"]=purchasing_analysis["Total Purchase Value"].map("${:.2f}".format)
purchasing_analysis["Avg Total Purchase per Person"]=purchasing_analysis["Avg Total Purchase per Person"].map("${:.2f}".format)
purchasing_analysis


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[7]:


age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Age Group"] = pd.cut(purchase_data["Age"],age_bins, labels=group_names)

age_grouped = purchase_data.groupby("Age Group")
total_count_age = age_grouped["SN"].nunique()
percentage_by_age = (total_count_age/[purchase_data["SN"].nunique()]) * 100

age_demo = pd.DataFrame({"Total Count": total_count_age,"Percentage of Players": percentage_by_age})
age_demo.index.name = None
age_demo.style.format({"Percentage of Players":"{:,.2f}%"})


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[32]:


age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Age Group"] = pd.cut(purchase_data["Age"],age_bins, labels=group_names)
person_purchase=purchase_data.groupby("Age Group")
purchase_count=person_purchase["Purchase ID"].count()
avg_purchase_price=person_purchase["Price"].mean()
total_purchase=person_purchase["Price"].sum()
player_count=person_purchase["SN"].nunique()
avg_total_purchase=total_purchase/player_count

##DataFrame
Purchasing=pd.DataFrame({"Purchase Count":purchase_count,
                        "Average Purchase Price":avg_purchase_price.map("${:.2f}".format),
                        "Total Purchase Value":total_purchase.map("${:.2f}".format),
                        "Avg Total Purchase per Person":avg_total_purchase.map("${:.2f}".format)})
Purchasing


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[74]:


player_purchase=purchase_data.groupby("SN")
player_count=player_purchase["Item ID"].count()
player_price=player_purchase["Price"].mean()
player_totalvalue=player_purchase["Price"].sum()



Spender=pd.DataFrame({"Purchase Count":player_count,
                     "Average Purchase Price":player_price,
                     "Total Purchase Value":player_totalvalue})
Sort_Spender=Spender.sort_values("Total Purchase Value",ascending=False)
Sort_Spender["Average Purchase Price"]=Sort_Spender["Average Purchase Price"].map("${:.2f}".format)
Sort_Spender["Total Purchase Value"]=Sort_Spender["Total Purchase Value"].map("${:.2f}".format)
Sort_Spender.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[118]:


item_data=purchase_data.groupby(["Item ID","Item Name", "Price"])[ "Price"].agg(['count','sum'])
item_data.columns = ["Purchase Count", "Total Purchase Value"]

item_data.reset_index(inplace=True)
item_data.set_index(["Item ID","Item Name"] ,inplace=True)
item_data=item_data[["Purchase Count", "Price", "Total Purchase Value"]]
item_popular=item_data.sort_values("Purchase Count", ascending=False)
item_popular=item_popular.rename(columns={"Price":"Item Price"})

item_popular["Item Price"]=item_popular["Item Price"].map("${:.2f}".format)
item_popular["Total Purchase Value"]=item_popular["Total Purchase Value"].map("${:.2f}".format)
item_popular.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[121]:


profit_items=item_data.sort_values("Total Purchase Value", ascending=False)
profit_items=profit_items.rename(columns={"Price":"Item Price"})
profit_items["Item Price"]=profit_items["Item Price"].map("${:.2f}".format)
profit_items["Total Purchase Value"]=profit_items["Total Purchase Value"].map("${:.2f}".format)
profit_items.head()

