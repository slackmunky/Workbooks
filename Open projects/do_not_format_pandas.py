import pandas as pd
import numpy as np
from numpy.core.defchararray import lower

# Prints whole big DataFrame. SUPER DUPER AMAZING USEFUL!!!!!!!!!!!!!!!
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 20)

# Make sure you have the correct filepath or read_csv won't work. Use the
# "r" character in front of the filepath to make a raw string so the escape
# characters don't work. No escape!

bookshelf = r"Closed Projects\bookshelf.csv"
df_book = pd.read_csv(bookshelf)

employees = r"Closed Projects\employees.csv"
df_emp = pd.read_csv(employees)

inventory = r"Closed Projects\inventory.csv"
df_inv = pd.read_csv(inventory)

orders = r"Closed Projects\orders.csv"
df_orders = pd.read_csv(orders)

print(df_book)
print("\n\n")
#  df1 = pd.to_csv(bookshelf) will write to/as a csv file if your filepath
#  isn't garbage.

# Key: Value DataFrame layout. Keys are column headers, values are column data.
df0 = pd.DataFrame({
    "Product ID": [1, 2, 3, 4],
    "Product Name": ["t-shirt", "t-shirt", "skirt", "skirt"],
    "Color": ["blue", "green", "red", "black"]
})

# Row entry DataFrame layout. Rows of data as lists, with column headers
# named at the end of the file.
df = pd.DataFrame([
    ['January', 100, 100, 23, 100],
    ['February', 51, 45, 145, 45],
    ['March', 81, 96, 65, 96],
    ['April', 80, 80, 54, 180],
    ['May', 51, 54, 54, 154],
    ['June', 112, 109, 79, 129]],
        columns=['month', 'clinic_east',
                 'clinic_north', 'clinic_south',
                 'clinic_west'])

# Get data-type info about df
# print(df.info())

# One way to select a column == dataframe_name.column_to_select
clinic_north = df.clinic_north

# Select multiple columns. Make sure to use double brackets [[]]!
clinic_north_south = df[["clinic_north", "clinic_south"]]

# Selecting a row using ".iloc" index location:
march = df.iloc[2]
# Also works with index slicing:
april_may_june = df.iloc[-3:]

# Looking up a row using comparison operators:
# df[df.MyColumnName (== or < or > or !=) desired_column_value]
january = df[df.month == "January"]

# Row lookup arguments can be combined by separating them with & or | which
# are the "and" and "or" operators for the combination. First example is
# March OR April, second is March AND April
march_or_april = df[(df.month == "March") | (df.month == "April")]
march_and_april = df[(df.month == "March") & (df.clinic_north > 90)]
print(march_or_april)
print("\n")
print(march_and_april)

# Row specific lookup using the .isin method to specify data. Mind the
# syntax enclosures.
january_february_march = df[df.month.isin(["January", "February", "March"])]

# Creating a new DataFrame by looking things up keeps the old indices for
# the rows. Reset the indices using .reset_index().
# Select multiple row indices with ".loc" instead of ".iloc".
df2 = df.loc[[1, 3, 5]]  # New DataFrame
# "inplace" will/won't create a new df, and "drop" will/won't remove old
# indices.
df2.reset_index(inplace=True, drop=True)

# Add a column in the same way you would a new dict entry. When using this
# particular method, make sure to add as many values as there are columns.
df["clinic_central"] = [78, 89, 63, 92, 108, 95]
# You can also use a single value to enter all the way down.
df["is_operational"] = "Yes"
# You can also perform operations
df["total_visits"] = df.clinic_north + df.clinic_east + \
                     df.clinic_south + df.clinic_west + df.clinic_central
print(df)

df_names = pd.DataFrame([
    ['JOHN SMITH', 'john.smith@gmail.com'],
    ['Jane Doe', 'jdoe@yahoo.com'],
    ['joe schmo', 'joeschmo@hotmail.com']
],
        columns=['Name', 'Email'])

# The ".apply" method can be used to transform current data, in this case,
# adding the transformed data as a new column.
df_names["Lowercase Name"] = df_names.Name.apply(lower)

# Creating a lambda function
# The following returns the first and last letters of a string, or just the
# string if it's less than 2 characters in length. Note the lack of commas,
# periods, or semicolons in the body of the function!
mylambda = lambda string: string[0] + string[-1] if len(string) > 2 else string

# Splits on the space between names and returns the last value (last name).
# get_last_name = lambda name: name.split()[-1]
# Creates a "last_name" column by applying the lambda to "name"
# df["last_name"] = df.name.apply(get_last_name)

df_orders["shoe_source"] = df_orders.shoe_material.apply(lambda material: "animal" if material == "leather" else "vegan")
print(df_orders)
# Renaming column headers one at a time uses dict syntax.
df_emp.rename(columns={"id": "Employee ID", "name": "Full Name"}, inplace=True)
# If you don't use "inplace=True" new columns will be created. Change them
# back.
df_emp.rename(columns={"Employee ID": "id", "Full Name": "name"}, inplace=True)

# Renaming all the columns at once:
df_emp.columns = ["Employee ID", "Full Name", "Hourly Rate", "Hours Worked"]
# Gotta change 'em back for the functions to work. I'm not rewriting that.
df_emp.columns = ["id", "name", "hourly_wage", "hours_worked"]

df_emp["overtime_worked"] = df_emp.hours_worked.apply(
        lambda hours: "Yes" if hours > 40 else "No")

# When writing a function where the row by row output is dependant on row by
# row information, you need to use the following syntax. Don't forget
# "axis=1" at the end!
df_emp["total_earned"] = df_emp.apply(lambda row:
                                      (row["hours_worked"] - 40)
                                      * (row["hourly_wage"] * 1.5)
                                      + (40 * row["hourly_wage"])
                                      if row["hours_worked"] > 40
                                      else row["hours_worked"] * row[
                                          "hourly_wage"],
                                      axis=1
                                      )


# Pulling data from a DataFrame
print(df_orders.head(10))
# Syntax is "DataFrame_name.column_name.function()". Should be able to just look up some functions. A couple are below.
most_expensive = df_orders.price.max()
num_colors = df_orders.shoe_color.nunique()
print(most_expensive, num_colors)
# Like items can be grouped together using ".groupby"
# Syntax is "df_name.groupby("column_to_group").target_column.function()"
pricey_shoes = df_orders.groupby("shoe_type").price.max()
print(pricey_shoes)
# Usually, you want a new DataFrame, so use ".reset_index()" for that.
pricey_shoes_2 = df_orders.groupby("shoe_type").price.max().reset_index()
print(pricey_shoes_2)
# The function appied to a column can be a lambda function using ".apply"
# In this case, the "np.percentile(x, y)" function was used.
# x = the input array
# y = percentile to find
cheap_shoes = df_orders.groupby("shoe_color").price.apply(lambda x: np.percentile(x, 25)).reset_index()
print(cheap_shoes)
# You can also check against variables in multiple columns.
# "shoe_type" and "shoe_color" are columns indexed, and "id" is the column the function is performed upon.
shoe_counts = df_orders.groupby(["shoe_type", "shoe_color"]).id.count().reset_index()
print(shoe_counts)
# You can also create pivot tables using the syntax below.
shoe_counts_pivot = shoe_counts.pivot(
    columns="shoe_color",
    index="shoe_type",
    values="id").reset_index()