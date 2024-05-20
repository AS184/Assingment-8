loop = (input("Y if you would like to loop, N if you would like to exit:  "))
while loop == "Y":
  p = float(input("Enter principle amount:  "))
  r = float(input("Enter the interest rate:  "))
  total_t = 0
  print("\n Year ", "Beginning Balance", "Ending Balance")
  for y in range(1,6,1):
   t = p * r
   eb = t + p
   print("\n Year ", y, "{:2F}".format(p),"{:2F}".format(eb))
   p = eb
   total_t = total_t + t
  print("\n Total intrest earned: ", "{:2F}".format(total_t))
  loop = (input("Y if you would like to loop, N if you would like to exit:  "))