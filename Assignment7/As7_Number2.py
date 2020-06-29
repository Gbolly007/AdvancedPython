f = lambda x: (lambda y: (lambda z: x + y + z))
#Task1
fg=f(2)
gf=fg(3)
print(gf(4))
#Task2
g=lambda x,y,z: x + y + z
print(g(2,3,4))
