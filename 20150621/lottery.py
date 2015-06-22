# coding: UTF-8

def solve(n, m, k):
  for k1 in k:
    for k2 in k:
      for k3 in k:
        for k4 in k:
          sum = k1 + k2 + k3 + k4
          if sum == m:
            return "Yes"           
  return "No"

#result = solve(3,10,[1,3,5])
#result = solve(3,9,[1,3,5])
result = solve(3,8,[1,3,5])
print result
