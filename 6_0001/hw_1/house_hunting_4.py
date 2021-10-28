#This version does not use recursion
#It is an iterative solution which doesn't use function definitions
import sys 
st_sal = float(input("what is your starting salary?"))
cost = 10**6
pct = .25
pmt = cost*pct
r = .04
rise = .07
tr = 36


#bisection search
#calculate initial values for amon and bmon, the number of months for max
#and min savings rates

a = 1
b = 10000
csav = 0
mon = 0
sal = st_sal
sav = a/10000
while csav < pmt-100:
  mon+=1
  csav = csav*(1+r/12)
  csav = csav+(sal/12)*sav
  if mon%6 == 0 and mon != 0:
    sal = sal*(1+rise)
amon = mon
csav = 0
mon = 0
sal = st_sal
sav = b/10000
while csav < pmt-100:
  mon+=1
  csav = csav*(1+r/12)
  csav = csav+(sal/12)*sav
  if mon%6 == 0 and mon != 0:
    sal = sal*(1+rise)
bmon = mon
if amon < 36:
  print("Optimal rate of savings: .01%")
  print("0 steps in bisection search.")
  sys.exit()
if bmon > 36:
  print("You cannot save enough for a down payment in 36 months.")
  print("0 steps in bisection search.")
  sys.exit()
#begin the outer while loop
cond = False
steps = 0
while cond == False:
  steps+=1
  c = (a+b)//2
  mon = 0
  sal = st_sal
  sav = c/10000
  csav = 0
  while csav < pmt-100:
    mon +=1
    csav = csav*(1+r/12)
    csav = csav+(sal/12)*sav
    if mon%6 == 0 and mon != 0:
      sal = sal*(1+rise)
  cmon = mon
  if cmon == 36:
    #process the c-string and print it
    #need two decimal places displayed, and leading zero
    #if it is less than 1
    str_rep = str(c)
    leng = len(str_rep)
    if leng >= 3:
      w = str_rep[:leng-2]
      d = str_rep[leng-2:]
      str_rep = w + "." + d + "%"
      print("Optimal savings rate: " + str_rep)
      print(str(steps) + " steps in bisection search.")
      sys.exit()
    else:
      str_out = "0."
      if leng == 1:
        str_out = str_out+"0"+str_rep
        print("Optimal savings rate: " + str_out)
        print(str(steps) + "steps in bisection search.")
        sys.exit()
      if leng == 2:
        str_out = str_out+str_rep
        print("Optimal savings rate: " + str_out)
        print(str(steps) + "steps in bisection search.")
        sys.exit()
    cond = True #this line is not supposed to be reached, it is here
    #to avoid stack overflow
  if cmon < 36:
    #c is too high
    if c <= 2:
      print("Optimal savings rate: 0.0" + str(c) + "%")
      print(str(steps) + " steps in bisection search.")
      sys.exit()
    b = c
  else:
    #c is too low
    if c >= 9999:
      print("You cannot save enough for a down payment.")
      print(steps + "steps in bisection search.")
      sys.exit()
    a = c 
    


