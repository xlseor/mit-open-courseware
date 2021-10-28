foo = 'zoo'
boo = 'cru'
bar = 'noo'

def my_func(foo=foo, boo=boo, bar=bar):
  print(foo)
  print(boo)
  print(bar)
  return [foo, boo, bar]

print(my_func())
