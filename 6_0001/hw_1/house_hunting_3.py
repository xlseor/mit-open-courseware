import sys
rise = .07
r = .04
pct_dn = .25
cost = 1000000
sal = float(input("please enter your starting salary:  "))
tr = 36
pmt = pct_dn*cost


def mon_to_pmt(sal, rise, r, sav, pmt): #take in the savings rate and return months to
  #save enough for down payment
  mon = 0
  csav = 0
  while csav < pmt:
    csav = csav+csav*r/12
    csav = csav+sal*sav/12
    if mon % 6 == 0 and mon != 0:
      sal = sal*(1+rise)
    mon+=1
  return mon

def bsc_sch(sal, rise, r, pmt, tr, a, b, n): #a and b are integers 1 to 10000
  #n is a counter for the number of bisections performed
  #it is passed in at the beginning of each new recursion. 
  fa = mon_to_pmt(sal, rise, r, sav=a/10000, pmt=pmt)
  fb = mon_to_pmt(sal, rise, r, sav=b/10000, pmt=pmt)
  if fb > tr:
    print("You cannot save enough for a down payment in three years.")
    print(str(n) + " steps in bisection search.")
    return sys.exit()
  if fb == tr:
    return (b,n)    
  if fa == tr:
    return (a,n)
  c = a + abs(b-a)//2
  fc = mon_to_pmt(sal, rise, r, sav=c/10000, pmt=pmt)
  if fc == tr:
    return (c,n)
  if fc < tr:
    n+=1
    return bsc_sch(sal, rise, r, pmt, tr, a, c, n) 
  if fc > tr:
    n+=1
    return bsc_sch(sal, rise, r, pmt, tr, c, b, n)


tup = bsc_sch(sal, rise, r, pmt, tr, 1, 10000, 0)
ans = tup[0]
steps = tup[1]
ans = str(ans)
pad = 5-len(ans)
for i in range(0,pad):
  ans = "0" + ans
l_ans = ans[:3]
t_ans = ans[3:]
ans = l_ans + "." + t_ans + " %"
ans = ans[pad:]

print("Your optimal savings rate to make")
print("a down payment in 3 years: " + ans)
print(str(steps) + " steps in bisection search.")

