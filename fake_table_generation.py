import random as r
import time as t
import datetime as dt
from datetime import date as d
from prettytable import PrettyTable as pt
from random import *


# table row count definition
row_count =  randint(1, 100)

# date limitations to make data more realistic
r_end_date = d.today()
r_start_date = r_end_date - dt.timedelta(days = r.randrange(randint(10,100)))

# function of random date 
def random_date(x,y):
    diff = abs((x - y).days)
    random = r.randrange(diff)
    return x + dt.timedelta(days = random+1)

# array for email subject 
email_subject_group = ['Purchase','Spam','Friend']

# prettytable definition
table = pt()
table.title = 'Fake Data'
table.field_names = ['ID', 'Email Subject', 'Email Date']

# loop to generate rows
for i in range(row_count):
    random_dates = random_date(r_start_date,r_end_date).isoformat()
    random_email_subject = 'Email Subject' + ' ' + r.choice(email_subject_group) + ' ' + str(r.randrange(randint(1,100)))
    table.add_row([i + 1,random_email_subject,random_dates])

print(table)
