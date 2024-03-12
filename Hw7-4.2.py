def sub_add(x, y):
    z = x + y
    return z

def main():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    r = sub_add(a, b)
    s = sub_add(r, c)
    t = sub_add(sub_add(s,d), sub_add(5,6))
    u = sub_add(t+7, s+8)
    print("%d %d %d %d " %(r, s, t, u))

main()
#Supawit Sangrattanayon 64050694                                                