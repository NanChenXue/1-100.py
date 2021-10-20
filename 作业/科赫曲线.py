import turtle as  t
def kcho(n,size):
    if n==0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            kcho(n-1,size/3)
def main():
    t.setup(600,400)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.speed(10)
    level=4
    for i in range(3):
        kcho(level,300)
        t.right(120)
main()
