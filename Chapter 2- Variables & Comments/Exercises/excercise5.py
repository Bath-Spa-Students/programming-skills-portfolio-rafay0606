## Exercise 5: USB Shopper :ballot_box_with_check:

# Price of each USB stick
usb_stick_price = 6

# Total budget in pounds
total_budget = 50

# Calculate how many USB sticks she can buy
usb_sticks_purchased = total_budget // usb_stick_price

# Calculate the remaining pounds after the purchase
remaining_pounds = total_budget % usb_stick_price

# Display the results
print("The girl can purchase", usb_sticks_purchased, "USB sticks.")
print("She would end up with ", remaining_pounds, "pounds left.")
