from multiprocessing.pool import ThreadPool


def fib_for(n):
  a,b = 0,1
  for i in range(n):
    a,b = b, a + b
  return a


output = ThreadPool().map(fib_for, [10**5]*150)
