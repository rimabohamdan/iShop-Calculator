basket = []
cost = []
print("***Welcome to iShop calculator***")
items = int(input("\nHow many items are there in your basket today ?"))
if items > 0 :
   print("\nLet's get to counting them..")
   for i in range(0,items) :
      name = input(f"Please tell me the name of the item number {i+1} ")
      basket.append(name)
      price = float(input(f"What is the price of {name} : $"))
      cost.append(price)

   see_basket = input("Would you like to see your entire basket items ?").lower()
   if see_basket == "yes" :
      print(basket)
      see_cost = input("Would you like to see how much it'll cost ?").lower()
      if see_cost == "yes" :
         print("Buying these item will cost :$")
         print(sum(cost))
      else :
         print("Press enter to exit")
   else :
       print("Press enter to exite")
else: 
    print("Seems like you're not in the mood for shopping today")
