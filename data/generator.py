import random
import time
import datetime
from math import exp

subcategories = {
    'Shirts': ['Short-sleeve', 'Long-sleeve', 'T-shirt'],
    'Pants': ['Long', 'Short'],
    'Shoes': ['Dress', 'Sneakers', 'Boat']
    }

def weightedSelection(options):
    totalprob = 0
    rand = random.random()
    for option, prob in options.items():
        totalprob += prob
        if rand <= totalprob:
            return option

## Basic Sales
f = open('basic_sales.csv', 'w')
f.write("category,subcategory,date purchased,day of week\n")
for _ in xrange(1000):
    category = weightedSelection({'Shirts': 0.2, 'Pants': 0.2, 'Shoes': 0.6})
    subcategory = random.choice(subcategories[category])
    timestamp = time.time() + (random.randint(0, 14) * 86400)
    date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    dayOfWeek = datetime.datetime.fromtimestamp(timestamp).strftime('%w')
    f.write(",".join([category, subcategory, date, dayOfWeek]) + "\n")
f.close()

## Basic Sales Summary
f = open('basic_sales_summary.csv', 'w')
f.write("category,subcategory,total purchases,refund rate\n")
for category, subs in subcategories.items():
    for sub in subs:
        purchases = str(random.randint(5, 500))
        refundRate = str(random.random())
        f.write(",".join([category, sub, purchases, refundRate]) + "\n")
f.close()

## Online Purchase Data
f = open('online_purchases.csv', 'w')
f.write("category,subcategory,date purchased,date first viewed,price,email received\n")
for _ in xrange(10000):
    category = weightedSelection({'Shirts': 0.2, 'Pants': 0.3, 'Shoes': 0.5})
    subcategory = random.choice(subcategories[category])
    timestamp = time.time() + (random.randint(0, 14) * 86400)
    datePurchased = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    dateViewed = datetime.datetime.fromtimestamp(timestamp - (exp(random.randint(0, 5)) * 864000)).strftime('%Y-%m-%d')
    price = str(round(random.randint(20,40) + exp(random.randint(0, 4)), 2))
    email = '1' if random.random() <= 0.8 else '0'
    f.write(",".join([category,subcategory,datePurchased,dateViewed,price,email]) + "\n")
f.close()
