import pandas as pd
import numpy as np

# import data from xlsx
xls = pd.ExcelFile('eBook.xlsx')
sheet_num = '001'
dict_df = {}
for i in range(246):
    value = pd.read_excel(xls, sheet_num)
    dict_df[sheet_num] = value
    unpadded = int(sheet_num) + 1
    sheet_num = '0' * (3 - len(str(unpadded))) + str(unpadded)

# Create 9 Dataframes to store new infos
out_df = {}
out_df['chapter_1'] = pd.DataFrame({'Question': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12']})
out_df['chapter_2'] = pd.DataFrame({'Question': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12']})
out_df['chapter_3'] = pd.DataFrame({'Question': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12']})
out_df['chapter_4'] = pd.DataFrame({'Question': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12']})
out_df['chapter_5'] = pd.DataFrame({'Question': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12']})
out_df['chapter_6'] = pd.DataFrame({'Question': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12']})
out_df['chapter_7'] = pd.DataFrame({'Question': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12']})
out_df['chapter_14'] = pd.DataFrame({'Question': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12']})
out_df['chapter_15'] = pd.DataFrame({'Question': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12']})

# Create a separate sheet that stores all participants infos
info = pd.DataFrame({'id': ['Gender', 'Grade', 'Age']})

# avoid performance warning
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

# import data
sheet_num = '001'
for i in range(246):
    for chapter in range(7):
        question = 1
        score_list = []
        for question in range(12):
            col_value = dict_df[sheet_num].iloc[6+question]['Unnamed: ' + str(2 + chapter)]
            if np.isnan(col_value):
                score_list.append("N/A")
            else:
                score_list.append(col_value)
        key = 'chapter_' + str(chapter + 1)
        out_df[key][sheet_num] = score_list
    # if last column is chapter 14
    if dict_df[sheet_num].iloc[4]['Unnamed: 9'] == 'Chapter 14':
        question = 1
        score_list = []
        for question in range(12):
            score_list.append(dict_df[sheet_num].iloc[6+question]['Unnamed: 9'])
        out_df['chapter_14'][sheet_num] = score_list
        
        spacer = [np.nan] * 12
        out_df['chapter_15'][sheet_num] = spacer


    # if last column is chapter 15
    elif dict_df[sheet_num].iloc[4]['Unnamed: 9'] == 'Chapter 15':
        question = 1
        score_list = []
        for question in range(12):
            score_list.append(dict_df[sheet_num].iloc[6+question]['Unnamed: 9'])
        out_df['chapter_15'][sheet_num] = score_list
        
        spacer = [np.nan] * 12
        out_df['chapter_14'][sheet_num] = spacer

    # add participants info to the dataset
    gender = dict_df[sheet_num].iloc[0]['Unnamed: 2']
    grade = dict_df[sheet_num].iloc[1]['Unnamed: 2']
    age = dict_df[sheet_num].iloc[2]['Unnamed: 2']
    
    info[sheet_num] = [gender, grade, age]
    
    # increase sheet_num for loop to continue
    unpadded = int(sheet_num) + 1
    sheet_num = '0' * (3 - len(str(unpadded))) + str(unpadded)

# export dataframes to one xlsx file
with pd.ExcelWriter("output.xlsx") as writer:
    out_df['chapter_1'].to_excel(writer, sheet_name="Chapter 1")  
    out_df['chapter_2'].to_excel(writer, sheet_name="Chapter 2")  
    out_df['chapter_3'].to_excel(writer, sheet_name="Chapter 3")  
    out_df['chapter_4'].to_excel(writer, sheet_name="Chapter 4")  
    out_df['chapter_5'].to_excel(writer, sheet_name="Chapter 5")  
    out_df['chapter_6'].to_excel(writer, sheet_name="Chapter 6")  
    out_df['chapter_7'].to_excel(writer, sheet_name="Chapter 7")   
    out_df['chapter_14'].to_excel(writer, sheet_name="Chapter 14")  
    out_df['chapter_15'].to_excel(writer, sheet_name="Chapter 15")
    info.to_excel(writer, sheet_name="Participants")