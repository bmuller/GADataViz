# Exercises
Here are two resources for online tools to visualize the data in this folder:
* [Google Fusion Tables](http://www.google.com/drive/apps.html#fusiontables)
* [Raw Density App](http://app.raw.densitydesign.org/#/)

As a good first step, use the example data on the Raw Density app to check out the movie data as a bubble chart.  Or a circlular dendogram of cocktail ingredients (or circle pack).

## Basic Sales
The *basic_sales.csv* file contains (fake) sales records with the following columns: category, subcategory, date purchased, and day of week.

This can be explored easily in Fusion Tables.  First, [download the raw file](https://raw2.github.com/bmuller/GADataViz/master/data/basic_sales.csv).  Then, [create a new Fusion table](http://www.google.com/drive/apps.html#fusiontables) and choose "Comma" as the seaparator character.  All of the other defaults in the setup are fine.

Add a chart by clicking on the red X.  Select the bar chart and then click "Summarize data" to see a summary of which category was purchased the most.

Then, select subcategory from the dropdown and filter by different categories (using the "Filter" dropdown).  Try the pie chart as well and select multiple categories.

Also - we can view this data with the [Raw Density App](http://app.raw.densitydesign.org/#/) to see an Alluvial Diagram showing the popularity of each category and subcategory.

## Basic Sales Summary
The *basic_sales_summary.csv* file contains (fake) sales summaries with the following columns: category, subcategory, total purchases, and refund rate.

The same process can be followed as with the basic sales file by first [download the raw file](https://raw2.github.com/bmuller/GADataViz/master/data/basic_sales_summary.csv).

Next, though, add a formula column (under "Edit" dropdown), and use a name of *refunds* with a formula of:

    'refund rate' * 'total purchases'

and a format of whole numbers (i.e., *1235*).

Then, add a chart, click on the bar chart option, select "subcategory" as the Category, and show the total purchases and refunds values.  Then, filter by category using the filter dropdown to select different categories.  This allows you to compare refund rates.

Also - we can view this data with the [Raw Density App](http://app.raw.densitydesign.org/#/) to see an Alluvial Diagram showing the popularity of each category and subcategory (different from before because now we must specify a link value).  We can also use circle packing to see the relative comparisons of refund rates by category/subcategory.

## Online Purchase Data
The *online_purchases.csv* file contains (fake) sales data from a website.  It has the following columns: category, subcategory, date purchased, date first viewed, price, and whether or not an email was received by the purchaser for the product.
