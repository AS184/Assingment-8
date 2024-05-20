f = open("Harperstudents.txt", "r")
name = f.readline().rstrip('\n')
total_tuition = 0
count = 0
while name != "":
  dcode = str(f.readline().rstrip('\n'))
  if dcode == "I":
    costpercredit = 250
  else:
    costpercredit = 500
  credit = int(f.readline())
  tuition = credit * costpercredit
  print(name, "has taken", credit, "credits and owes $", tuition)
  count = count + 1
  total_tuition = total_tuition + tuition
  name = f.readline().rstrip('\n')
print("The total tuition is $", total_tuition , "for", count, "students")
  