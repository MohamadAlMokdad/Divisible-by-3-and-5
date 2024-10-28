x = int(input("Enter number: "))

if x >= 15:
  for i in range(1, x+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
else:
     print("Please enter a number greater than or equal to 15, as there are no numbers less than 15 that are divisible by both 3 and 5")
  
  
    
