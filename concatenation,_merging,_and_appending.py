# -*- coding: utf-8 -*-
"""Concatenation, Merging, and Appending - Skeleton.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D2IeROYD5ySDWYqfy4YxwXdZ9EWGzpUT

# 1. DATAFRAME CONCATENATION
"""

# Import Pandas

import pandas as pd

# Creating a dataframe from a dictionary
# Let's define a dataframe with a list of bank clients with IDs = 1, 2, 3, 4, 5 
# Check this out: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html


bank_info = {'Bank Client ID': ['1', '2', '3', '4', '5'],
            'First Name': ['Nancy', 'Alex', 'Shep', 'Max', 'Allen'],
            'Last Name': ['Rob', 'Ali', 'George', 'Mitch', 'Steve']}

bank1_df = pd.DataFrame(bank_info, columns=['Bank Client ID', 'First Name', 'Last Name'])
bank1_df

# Let's define another dataframe for a separate list of clients (IDs = 6, 7, 8, 9, 10)

bank_info_2 = {'Bank Client ID': ['6', '7', '8', '9', '10'],
            'First Name': ['Bill', 'Dina', 'Sarah', 'Heather', 'Holy'],
            'Last Name': ['Christian', 'Mo', 'Steve', 'Bob', 'Michelle']}

bank2_df = pd.DataFrame(bank_info_2, columns=['Bank Client ID', 'First Name', 'Last Name'])
bank2_df

# Let's concatenate both dataframes #1 and #2
# Note that we now have client IDs from 1 to 10
# Note that by default ignore_index has been set to False meaning indexes from both dataframes are kept unchanged

bank_all_df = pd.concat([bank1_df, bank2_df])
bank_all_df

# Let's concatenate both dataframes #1 and #2
# Note that by setting ignore_index = True, the index has been automatically set to numeric and now ranges from 1 to 9

bank_all_df = pd.concat([bank1_df, bank2_df], ignore_index = True)

bank_all_df

# You can also use the append method to perform similar task
# Note that order matters!

bank_all_df = bank2_df.append(bank1_df, ignore_index = True)
bank_all_df

# You can also use the append method to perform similar task 

bank_all_df = bank1_df.append(bank2_df, ignore_index = True)
bank_all_df

"""**MINI CHALLENGE #1:**
- **Assume that you and your significant other become a new client at the bank and would like to add your first names, last names and unique client IDs. Define a new DataFrame and add it to the master list "bank_all_df"** 
"""

bank_info_3 = {'Bank Client ID': ['11', '12'],
            'First Name': ['Shrishti', 'Justin'],
            'Last Name': ['Tiwari', 'Bieber']}

bank3_df = pd.DataFrame(bank_info_3, columns = ['Bank Client ID', 'First Name', 'Last Name'])
bank3_df

bank_all_df = bank_all_df.append(bank3_df, ignore_index = True)
bank_all_df

"""# 2. DATAFRAME CONCATENATION WITH MULTI-INDEXING"""

# We can perform concatenation and also use multi-indexing dataframe as follows:

bank1_df

bank2_df

# You can access elements using multi-indexing as follows

bank_all_df = pd.concat([bank1_df, bank2_df], keys = ['Customer Group 1', 'Customer Group 2'])
bank_all_df

# You can access elements using multi-indexing as follows

bank_all_df.loc[('Customer Group 1'), :]

bank_all_df.loc[('Customer Group 1'), 0]

# You can access elements using multi-indexing as follows

bank_all_df.loc[('Customer Group 2'), 'First Name']

bank_all_df.loc[('Customer Group 2'), ['First Name', 'Last Name']]

"""**MINI CHALLENGE #2:**
- **Assume that you and your significant other belong to Customers Group #3. Use multindexing to add both names to the master list. Write a line of code to access Group #3 only.**
"""

bank3_df

bank_all_df = pd.concat([bank1_df, bank2_df, bank3_df], keys = ['Customer Group 1', 'Customer Group 2', 'Customer Group 3'])
bank_all_df

bank_all_df.loc[('Customer Group 3'),:]

bank_all_df.loc[('Customer Group 3'), 1]

"""# 3. DATA MERGING"""

# Let's concatenate both dataframes #1 and #2
# Note that we now have client IDs from 1 to 10
# Note that by default ignore_index has been set to False meaning indexes from both dataframes are kept unchanged

bank_all_df = pd.concat([bank1_df, bank2_df], ignore_index = True)
bank_all_df

# Let's assume we obtained additional information (Annual Salary) about our bank customers 
# Note that data obtained is for all clients with IDs 1 to 10

raw_data = {'Bank Client ID': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            'Annual Salary ($/Year)': [25000, 34000, 22000, 43000, 27000, 56000, 36000, 21000, 47000, 53000]}

bank_annual_salary = pd.DataFrame(raw_data)
bank_annual_salary

# Let's merge all data on 'Bank Client ID'

bank_all_df = pd.merge(bank_all_df, bank_annual_salary, on = 'Bank Client ID')
bank_all_df



"""**MINI CHALLENGE #3:**
- **Let's assume that you were able to obtain two new pieces of information about the bank clients such as: (1) credit card debt, (2) age**
- **Define a new DataFrame that contains this new information**
- **Merge this new information to the DataFrame "bank_all_df".** 
"""

bank_all_df = pd.concat([bank1_df, bank2_df], ignore_index = True)
bank_all_df

raw2_data = {'Bank Client ID': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
             'Credit Card Dept': [350, 270, 400, 340, 200, 480, 500, 420, 220, 380],
             'Age': [29, 22, 35, 28, 21, 38, 41, 39, 23, 37]}

bank_more_info = pd.DataFrame(raw2_data)
bank_more_info

bank_all_df = pd.merge(bank_all_df, bank_more_info, on = 'Bank Client ID')
bank_all_df

"""# MINI CHALLENGES SOLUTIONS

**MINI CHALLENGE #1 SOLUTION:**
- **Assume that you and your significant other become a new client at the bank and would like to add your first names, last names and unique client IDs. Define a new DataFrame and add it to the master list "bank_all_df"**
"""

new_data = {'Bank Client ID': ['11', '12'],
            'First Name': ['Justin', 'Sophie'], 
            'Last Name': ['Trudeau', 'Trudeau']}

bank3_df = pd.DataFrame(new_data, columns = ['Bank Client ID', 'First Name', 'Last Name'])
bank3_df

# Let's concatenate both dataframes #1 and #2
# Note that by setting ignore_index = True, the index has been automatically set to numeric and now ranges from 1 to 9
bank_all_df = pd.concat([bank_all_df, bank3_df], ignore_index = True)
bank_all_df





"""**MINI CHALLENGE #2 SOLUTION:**
- **Assume that you and your significant other belong to Customers Group #3. Use multindexing to add both names to the master list. Write a line of code to access Group #3 only.**
"""

bank1_df

bank2_df

new_data = {'Bank Client ID': ['11', '12'],
            'First Name': ['Justin', 'Sophie'], 
            'Last Name': ['Trudeau', 'Trudeau']}

bank3_df = pd.DataFrame(new_data, columns = ['Bank Client ID', 'First Name', 'Last Name'])
bank3_df

# We can perform concatenation and also use multi-indexing dataframe as follows:
bank_all_df = pd.concat([bank1_df, bank2_df, bank3_df], keys = ["Customers Group 1", "Customers Group 2",  "Customers Group 3"])
bank_all_df

# You can access elements using multi-indexing as follows
bank_all_df.loc[("Customers Group 3"), :]



"""**MINI CHALLENGE #3 SOLUTION:**
- **Let's assume that you were able to obtain two new pieces of information about the bank clients such as: (1) credit card debt, (2) age**
- **Define a new DataFrame that contains this new information**
- **Merge this new information to the DataFrame "bank_all_df".** 
"""

# Let's assume we obtained additional information (Annual Salary) about our bank customers 
# Note that data obtained is for all clients with IDs 1 to 10
 
raw_data = {
        'Bank Client ID': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'Credit Card Debt': [1000, 100, 500, 600, 0, 20, 360, 127, 3000, 2200],
        'Age': [44, 35, 67, 19, 22, 45, 48, 33, 34, 36]}
bank_credit_age_df = pd.DataFrame(raw_data, columns = ['Bank Client ID','Credit Card Debt', 'Age'])
bank_credit_age_df

# Let's merge all data on 'Bank Client ID'
bank_all_df = pd.merge(bank_all_df, bank_credit_age_df, on = 'Bank Client ID')
bank_all_df