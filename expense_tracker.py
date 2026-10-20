import json
import os
expenses = {}
username = input("Please Enter your name :")
filename = f"{username}_expenses.json"
print(filename)


if os.path.exists(filename):
    with open(filename, "r") as file:
        expenses = json.load(file)

else:
    expenses = {}

print("Your Saved Expenses :" , expenses)






while True :
 print("Personal Expense Menu\n1. Add Expense\n2. Search Expense\n3. Delete Expense\n4. Update Expense\n5. View All Expenses\n6. View Spending Summary\n7. Search Category\n8. Maximum Expense\n9. Minimum Expense\n10. Exit")
        
 try:  
        choice = int(input("Enter your choice: "))

 except ValueError:
        print("Please Enter numbers only!")
        continue 


   

 if choice == 1 :
    print("You selected Add Expense!")
    add_category = input("Enter the category for the expense: ")
    if add_category not in expenses:
                expenses[add_category] = {}
        
    
    while True:
     add_expense = input("Enter the new expense that you want to add: ")

     if add_expense in expenses[add_category]:
        print("Expense already exists in category!")
        continue

     break
        
      
          
          
    while True:
      try:
        add_amount = int(input("Amount for the added expense: "))

        if add_amount <= 0:
            print("Please enter a valid positive amount!")
            continue

        break

      except ValueError:
        print("Please enter numbers only!")

    expenses[add_category][add_expense] = add_amount
       
    print("All expenses with added expense:", expenses)
    
   
    
        
        
    
    
    
    

    
 elif choice == 2 :
    print("You Selected Search Expense!")
    search_name = input("Enter Expense name to search: ")
    found = False

    for category, items in expenses.items():
        if search_name in items:
         print(search_name, "costs Rs.", items[search_name])
         found = True
         break

    if not found:
          print("Expense not found!")

 elif choice == 3 :
    print("You Selected Delete Expense!")
    delete_expense = input("Enter the name of the expense that you want to be removed: ")
    found = False

    for category, items in list(expenses.items()):
       if delete_expense in items:
          del items[delete_expense]
          print("Expense Deleted Successfully!")
          found = True

          if not items:
            del expenses[category]
          break

    if not found:
       print("Expense not found!")

    print("Updated Expenses:", expenses)

 elif choice == 4 :
   print("You Selected Update Expense!")
   update_name = input("Enter the expense name you want to update: ")
   found = False

   for category, items in list(expenses.items()):
    if update_name in items:
        update_amount = int(input("Enter the new amount: "))
        update_category = input("Enter the new category for the updated expense: ")

        del items[update_name]

        if not items:
            del expenses[category]

        if update_category not in expenses:
            expenses[update_category] = {}

        expenses[update_category][update_name] = update_amount

        print("Expense Updated Successfully!")
        found = True
        break

   if not found:
      print("Expense not found!")

   print("Updated Expenses:", expenses)

 elif choice == 5 :
   print("You Selected View all expenses!")
   for category, items in expenses.items():
      print(category)
      for name, amount in items.items():

       
       print("Expense name :", name)
       print("Amount :", amount)

 elif choice == 6 :
   print("You selected View spending summary!")
   Total = 0
   for category, items in expenses.items():
    category_total = 0

    for amount in items.values():
        category_total = category_total + amount

    print(category, ": Rs.", category_total)
    Total = Total + category_total

   print("Total Spending: Rs.", Total)

 elif choice == 7:
    print("You Selected Search Category!")
    search_category = input("Enter the category that you want to search: ")

    if search_category in expenses:
     print("Expenses in", search_category, ":", expenses[search_category])
    else:
     print("Category not found!")

 elif choice == 8:
    print("You Selected Maximum Expense!")
    highest_amount = 0
      
    for category, items in expenses.items():
          for name, amount in items.items():
              if amount > highest_amount :
                  highest_amount = amount
                  expensive_name = name
                  expensive_category = category
      
    print("Most Expensive Expense:", expensive_name)
    print("Category:", expensive_category)
    print("Amount: Rs.", highest_amount)

 elif choice == 9:
    print("You Selected Minimum Expense!")
    cheapest_amount = float("inf")

    for category, items in expenses.items():
       for name, amount in items.items():
        if amount < cheapest_amount :
            cheapest_amount = amount
            cheapest_name = name
            cheapest_category = category

    print("Cheapest Expense:", cheapest_name)
    print("Category:", cheapest_category)
    print("Amount: Rs.", cheapest_amount)

 elif choice == 10:
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expenses saved successfully!")
    print("Thank you for using Personal Expense Tracker!")
    print("Exiting the program. Goodbye!")
    break


 else :
   print("Invalid! Please Select from 1 to 7")







            


    
