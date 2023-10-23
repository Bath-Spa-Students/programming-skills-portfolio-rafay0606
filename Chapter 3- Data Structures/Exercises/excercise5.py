## Exercise 5: Change Guest List :ballot_box_with_check:

# List of people to invite to dinner
guests = ["Muhammad Ali", "Steve Jobs", "Bob Marley", "Paul Walker", "Neil Armstrong"]

# Print invitations to each person
for guest in guests:
    print(f"Dear {guest},\nyou are cordially invited to dinner at my place. Please join us for a wonderful evening.\n\nSincerely, [Rafay]")

# Name of the guest who can't make it
guest_that_cant_make_it = "Neil Armstrong"
print(f"\nUnfortunately, {guest_that_cant_make_it} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new person
guests.remove(guest_that_cant_make_it)
new_guest = "Tom Cruise"
guests.append(new_guest)

# Print second set of invitation messages
for guest in guests:
    print(f"Dear {guest},\nYou are cordially invited to dinner at my place. I would be honored to have you as my guest.\n\nSincerely, [Rafay]")
