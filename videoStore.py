"""
Program: videoStore.py
Author: George 10/27/2021

Program that accepts the number of video rentals in various pricing categories and outputs the total price.

"""
# Variables and constants
NEW_VIDEO = 3.00
OLD_VIDEO = 2.00

# Input phase
print("**Welcome to Five Star Retro Video**")
newRental = int(input("How many NEW videos are being rented? >>"))
oldRental = int(input("How many OLD videos are being rented? >>"))

# Calculation phase
totalCost = NEW_VIDEO * newRental + OLD_VIDEO * oldRental
# output phase
print("The customer is renting", newRental, "new video(s). And", oldRental, "old video(s).")
print("The total charge is: $", totalCost)