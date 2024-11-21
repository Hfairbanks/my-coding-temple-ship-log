likes_sweet = input("do you like your coffee sweet? (yes/no)")
likes_sweet = input("do you perfer milk in your coffee?(yes/no)")

if likes_sweet == 'yes' and ("likes_milk") == 'yes':
  print("how about a carmel latte?")
elif likes_sweet == 'no' and ("likes_milk") == 'yes':
  print("an americano with a dash of milk sounds good for you")
elif likes_sweet == 'yes' and ("likes_milk") == 'no':
  print("try a black coffee with two sugar cubes")
else:
  print("black coffee it is!")


  days_overdue = int (input("how many days is the book overdue?"))
  fine =0
if days_overdue <= 5:
    fine = days_overdue * 1
elif days_overdue <= 10:
 fine = days_overdue * 2
else:
 fine = days_overdue * 5
print(f"your fine is $ {fine}.")
