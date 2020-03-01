import pandas as pd
import numpy as np

# Prints whole big DataFrame. SUPER DUPER AMAZING USEFUL!!!!!!!!!!!!!!!
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
        visit_to_cart[visit_to_cart.cart_time.isnull()])) \
             / float(len(visit_to_cart))
print("Visit only: ", empty_cart)

no_checkout = float(len(
        visit_to_checkout[visit_to_checkout.checkout_time.isnull()])) \
              / float(len(visit_to_checkout))
print("To cart: ", no_checkout)

no_purchase = float(len(
        all_data[all_data.purchase_time.isnull()])) \
              / float(len(all_data))
print("No purchase: ", no_purchase)
