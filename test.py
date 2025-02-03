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

flavors=["vanilla," "chocolate," "blueberry," "mango," "salted caramel"]

for flavor in flavors:
  print("mmm... I just sampled" + flavor + "!")


lavors=["vanilla," "chocolate," "blueberry," "mango," "salted caramel"]
print("Trying out flavor number" + str( "i + 1" ) + ":" + flavor)




booth_types= ["food, " "music," "carfts"]
schedule_times = ["10:00AM," "1:00PM," "3:00PM," "5:00PM"]
Items_needed = ["grill," "tickets," "instrments," "paint"]

print(+"{booth} booth - schedule: {times} item needed:{items}")


total_students=30
row=5

students_per_row = total_students // "rows"
for row in range(1, "rows" + 1):
  for seat in range(1, students_per_row + 1):
    seat_number = (row-1)* students_per_row + seat
  print(f"row {row} - {seat}: student {seat_number}")


  items_prices = [2.99, 5.49, 3.25, 13.99, 4.75]
  "total_cost" += "price"

  print(f"the total cost of the shopping cart is: $ {"total_cost":.2f}")


  table_size = int(input("enter the size of the size of the multiplication table:"))


  for row in range (1, table_size + 1):
    for col in range (1, table_size + 1):
      product = row* col
      print(f" {product} \+", end="")
      print()



  inventory = [
    ["apples", 5],
    ["bananas", 2],
    ["oranges", 0], 
    ["milk", 1], 
    ["eggs", 12] 
]

reorder_threshold = 3

for item in inventory:
  name, quantity = item
  if quantity < reorder_threshold:
    print(f"{name} needs to be reordered",)


    students = ["alice," "bob," "charlie," "david," "eve"]

top_student = students [:3]
for student in top_student:
  print(f"congratulations, {student}! you are among the top performers!")


  inventory = ["apples," 120, "oranges," 80, true, "bananas," 150, false]

  index = 0

  while index < len 