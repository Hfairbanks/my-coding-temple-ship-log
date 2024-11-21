full_name = "john Doe"
print (full_name)

myname = "John"
myname = "Doe"
print(myname)
print(myname)
fav_color = "Blue"
print (fav_color)

fruit1, fruit2, fruit3 = "apple", "banana", "cherry"
print(fruit1)
print(fruit2)
print(fruit3)

integer_var = 42
float_var = 3.14
string_var = "Hello world"

print(integer_var,type (integer_var))
print(float_var,type (float_var))
print(string_var,type (string_var))

mystery_variable = "1234"
variable_type = (mystery_variable)
print(variable_type)

dynamicvar =10
print(dynamicvar, type (dynamicvar))

dynamicvar = "python is great"
print(dynamicvar, type(dynamicvar))


flour_per_cake = 250 
total_flour = 2.5 * 1000
number_of_cakes = total_flour // flour_per_cake
print(number_of_cakes)

kingdom = "pythonland"
print(kingdom)

shirt1 =45
shirt2 =50

result = shirt1 < shirt2
print(result)

rain = True
heavy_rain = False
take_umbrela = rain or heavy_rain
print(take_umbrela)

result = 3 + 5 * 2 - 8
print(result)


pastries = 10
friends = 3
pastries_each = pastries // friends
left_over = pastries % friends
print(pastries_each, left_over)

kingdom = "pythonland"
kingdom += " is  wonderful" # kingdom + "is wonderful!"
print(kingdom)

knight1 = 45
kinght2 = 50
result = (knight1 == kinght2)
print(result)

eggs = True
flour = False
make_pancakes = eggs and flour
print(make_pancakes)

castle_height = 100
moat_width = 50
castle_height = 2 # castle_height = 200
moat_width /= 2 # moat_width = moat-width / 2
print(castle_height, moat_width)


torch_lit = True

if torch_lit == True:
    print("venture forth into the cave!")

    is_student = False
    is_student = True

    if is_student:
     print("you get a 50% student!")
    elif "is_senior":
        print("seniors enjoy a 40% discount!")
    else:
       print("regular entry fee applies!")


    is_friendly = False
    has_quest = True

    if not is_friendly:
       print("Be cautious! This character night not be helpful !")
    elif has_quest: 
       print("This character has a quest for you!")
    else:
       print("Just a regular village passing by.")


    
        
    want_veggie = True
    likes_spice = False

    if want_veggie and likes_spice:
          print("How about a spicy veggie wrap?")
    elif want_veggie:
        print("try our classic veggie burger!")
    else:
          print("check out our grill menu!")


         
         
    age= int(input("enter your age:"))
rating= input ("enter movie rating (g, pg, pg-13, r)")

if rating == "g":
   print("you can watch the movie!")
elif rating == "pg" and age >= 7:
   print("you can watch the movie!")
elif rating == "pg-13 and age >= 13":
   print("you can watch the movie!")
elif rating == "r" and age >= 17:
   print("you can watch the movie!")
else:
   print("you are not allowed to watch this movie")


temperature = float(input("enter today's temperature in fahrenheit"))
if temperature <20:
   print("wear a heavy coat and scarf!")
elif 20<= temperature <50:
   print("it is a little chilly. make sure to wear a light coat")
elif 50<= temperature <= 70:
   print("it might be good to wear a t-shirt and long pants")
else:
   

   grade = float(input)("enter your grade")("0-100:")

   if grade >=90:
      print("your letter grade is a.")
   elif grade >=80:
      print("your letter grade is b.")
   elif grade >=70:
      print("your letter grade is c.")
   elif grade >=60:
      print("your letter grade is d.")
   else:
      print("your letter grade is f.")


      exercise_minutes = int(input)("how many minutes do you exercise daily?")
      if exercise_minutes <30:
         print("you should consider exercising more for better health!")
      elif 30 <= exercise_minutes <=60:
         print("great job staying active!")
      else:
         print("you're an exercise superstar!")


