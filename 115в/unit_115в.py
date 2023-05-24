def logic(n):
    s = 0
    for k in range(1, n+1):  # от 1 до n
        s += 1/((2*k+1)**2)
    return s
