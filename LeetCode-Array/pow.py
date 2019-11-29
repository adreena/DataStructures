


def pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    temp = pow(x, int(n/2))
    if n >0:
        if n%2 == 0:
            return temp*temp
        else:
            return temp*temp*x
    else:
        return temp*temp/x
