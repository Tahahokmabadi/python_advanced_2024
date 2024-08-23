try:
    age = int(input("Enter your age:\t"))
    if age <= 0:
        print("Are you sure about that?!")
    elif age >= 18:
        print("You can vote.")
    else:
        print("You can't vote.")
        
except ValueError:
    print("Non-numeric inputs are not accepted!")
    
except KeyboardInterrupt:
    print("Input interrupted!")
    
except BaseException as e:
    print(f"An error occurred:\n{e}")

finally:
  print("Anyway, support the country!!!")
