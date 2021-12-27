print("Now we will calculate marketing:\nPrices:"
      "\n-----------\nTomatoes=8.9 NIS\nCucumbers=6.9 NIS\nCola=10 NIS\nChicken=25 NIS")

tomato = int(input("Enter how many tomatoes : "))
cucumbers = int(input("Enter how many cucumbers : "))
cola = int(input("Enter how many cola : "))
chicken = int(input("Enter how many chicken : "))

print("Summary of your order:\n-------------\ntomatos : {0}\ncucumbers : {1}\nCola : {2}\nChicken : {3}"
      .format(tomato, cucumbers, cola, chicken))

summary = (tomato * 8.9) + (cucumbers * 6.9) + (cola * 10) + (chicken * 25)
print("\nYou have to pay :", str(summary), "NIS without tax")
print("\nYou have to pay :", str("%.1f" % (summary * 1.17)), "NIS with 17% tax")
