import numpy as np

def solve_Xk(i):
    xk_odd_val = None
    xk_even_val = None
    k_odd = 2 * i - 1
    k_even = 2*i

    if k_odd % 2 == 1:
        xk_odd_val = i
    if k_even % 2 == 0:
        xk_even_val = -i

    return k_odd, xk_odd_val, k_even, xk_even_val

def solve_Yk(a, b, c, Xk):
    yK = (a * Xk ** 2) + (b * Xk) + c
    return yK


def create_table(a, b, c, s):
    xk_0 = 0
    yk_0 = solve_Yk(a, b, c, xk_0)
    table = [{xk_0: (xk_0, yk_0)}]

    for i in range(1, s):
        k_odd, xk_odd,k_even, xk_even = solve_Xk(i)
        yk_odd = solve_Yk(a, b, c, xk_odd)
        yk_even = solve_Yk(a, b, c, xk_even)
        table.append({k_odd : (xk_odd, yk_odd)})
        if len(table) == (s+1): break
        table.append({k_even : (xk_even, yk_even)})
        if len(table) == (s+1): break

    return table

def Solve_Sys_Equ(p0, p1, p2, table):
    x0 = table[p0][p0][0]
    y0 = table[p0][p0][1]


    x1 = table[p1][p1][0]
    y1 = table[p1][p1][1]

    x2 = table[p2][p2][0]
    y2 = table[p2][p2][1]

    print("P:",table[p0])
    print("P:", table[p1])
    print("P", table[p2])
    print(str(x0) +"^2*p +" +str(x0)  + "h +" + "d" + "=" + str(y0))
    print(str(x1) + "^2*p +" + str(x1) + "h +" + "d" + "=" + str(y1))
    print(str(x2) + "^2*p +" + str(x2) + "h +" + "d" + "=" + str(y2))

    A = np.array([[x0**2, x0, 1], [x1**2, x1, 1], [x2**2, x2, 1]])
    B = np.array([y0, y1, y2])

    sol_set = np.linalg.inv(A).dot(B)

    p = round(sol_set[0])
    h = round(sol_set[1])
    d = round(sol_set[2])
    return p,h,d


print("The Secret Sharing Schemes")

print("y = ax^2 + bx + c")

a = int(input("Enter value for a: ").strip())
b = int(input("Enter value for b: ").strip())
c = int(input("Enter value for c: ").strip())

n = int(input("Enter total N number of VPs: ").strip())
m = int(input("Enter total M number of Mangers: ").strip())

# a = 1
# b = 2
# c = 5
# n = 3
# m = 4


s = n + m
print("n+m = S:", s)
print("There are", s+1, "points including zero")

table_set = create_table(a, b, c, s)
print(table_set)

print("\nAssign {P(1); P(2); P(3)} to the President")
print("Assign {P(1); P(2); P(3)} to the CEO")
print("Assign {P(0); P(k)} to k-th VP")
print("Assign {P(n+i)} to i-th Manager\n")

print("Make a selection of the P values. Remember lists start from zero!")
p_val0 = int(input("Select first P value: ").strip())
p_val1 = int(input("Select second P value: ").strip())
p_val2 = int(input("Select third P value: ").strip())


p, h , d = Solve_Sys_Equ(p_val0, p_val1, p_val2, table_set)

print("p =", p ," a =",a)
print("h =", h ," b =",b)
print("d =", d ," c =",c)

if p == a and h == b and d == c:
    print("Success!! we have a matching set!")

