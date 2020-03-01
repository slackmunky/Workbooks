import pandas as pd
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', None)

visits = pd.read_csv(r'..\Data Files\visits.csv', parse_dates=[1])
cart = pd.read_csv(r'..\Data Files\cart.csv', parse_dates=[1])
checkout = pd.read_csv(r'..\Data Files\checkout.csv', parse_dates=[1])
purchase = pd.read_csv(r'..\Data Files\purchase.csv', parse_dates=[1])

visit_to_cart = pd.merge(visits, cart, how="left")
visit_to_checkout = visit_to_cart.merge(checkout, how="left")
all_data = visit_to_checkout.merge(purchase, how="left")

print("Total visits: ", len(visits))
empty_cart = float(len(
        visit_to_cart[visit_to_cart.cart_time.isnull()])
                   / len(visit_to_cart))
print("Visit only: ", "%.2f" % empty_cart)

no_checkout = float(len(
        visit_to_checkout[visit_to_checkout.checkout_time.isnull()])
                    / len(visit_to_checkout))
print("To cart: ", "%.2f" % no_checkout)

no_purchase = float(len(
        all_data[all_data.purchase_time.isnull()])
                    / len(all_data))
print("No purchase: ", "%.2f" % no_purchase)

total_visits = len(all_data)
total_purchases = len(all_data.purchase_time)

purchased = (float(len(
        all_data) - len(all_data[all_data.purchase_time.isnull()]))
             / len(all_data))
print("Percent purchased: ", "%.2f" % purchased)

all_data["time_to_purchase"] = all_data.purchase_time - all_data.visit_time
print("Time to purchase: ", all_data.time_to_purchase.mean())
