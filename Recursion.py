def foo(n):
<<<<<<< HEAD
  if n == 0:
    print("Done!")
  else:
    print("Hello!")
    n -= 1
    foo(n)
=======
    if n == 0:
        print("Done!")
    else:
        print("Hello!")
        n -= 1
        foo(n)

>>>>>>> b433577a70a0b68085b6f45069faf4ae26df269a
foo(10)
