import random as r
import datetime as dt
from datetime import date as d
from prettytable import PrettyTable as pt
from random import *

# table row count definition
row_count =  randint(1, 100) # can be fixed

# date restrictions 
r_end_date = d.today()
r_start_date = r_end_date - dt.timedelta(days = r.randrange(randint(1,100))) # can be fixed
delta_days = r_end_date - r_start_date # can be changed, and used abs() to calc difference if r_end_date is random
delta_days = delta_days.days # days between date range

# email category names
email_subject_group = ['Purchase','Spam','Friend']

# prettify fake data table
table = pt()
table.title = 'Fake Data'
table.field_names = ['ID', 'Email Subject', 'Email Date']

for i in range(row_count):
    random_date = r_start_date + dt.timedelta(days = r.randrange(delta_days)) # add random number of days to 1st of January
    random_date = random_date.isoformat() # format date to isformat which is %Y-%m-%d
# Email subject with random number in the end, number is in the range of 1 to delta_days
    random_email_subject = 'Email Subject' + ' ' + r.choice(email_subject_group) + ' ' + str(r.randrange(delta_days))
    table.add_row([i + 1,random_email_subject,random_date]) # adding new row with new values to the table

print(table)
