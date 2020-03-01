import pandas as pd
import numpy as np

# Prints whole big DataFrame
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 20)

home_inventory = r"..\Data Files\inventory.csv"
inventory = pd.read_csv(home_inventory)

# print(inventory.head(10))
# print("\n\n")

staten_island = inventory[:10]
product_request = staten_island["product_description"]
seed_request = inventory[(inventory.location == "Brooklyn") & (
        inventory.product_type == "seeds")]

inventory["in_stock"] = inventory.quantity.apply(lambda num:
                                                 True
                                                 if num > 0
                                                 else False
                                                 )

inventory["total_value"] = inventory.price * inventory.quantity

inventory["full_description"] = inventory.apply(lambda row:
                                                "{} - {}".format(
                                                        row.product_type,
                                                        row.product_description
                                                ), axis=1)
print(inventory)
