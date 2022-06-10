import pandas as pd
import random as r
from datetime import date as d


row_count = 1000
email_subject_group = ['Purchase','Spam','Friend']

# list of integers in consequtive order
id_list = list(range(1, row_count+1))
# list of dates in consequitve order from today + row_count-1 days(can be randomized number), and then randomized, can 
date_list = r.choices(pd.date_range(d.today(), periods=row_count, freq='D'),k = row_count)
# permutation of email subject group elements and id list elements, concatenated with email subject text, and then randomized
email_list = r.choices(['Email Subject ' + str(x) + ' ' + str(y) for x in email_subject_group for y in id_list],k = row_count) 
# data frame with 3 new lists
df = pd.DataFrame({ 'ID': id_list, 'Email Subject': email_list , 'Email Date': date_list })

print(df)