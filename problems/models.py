######
#   Collection of ODEs
######

def standard(s, t):
    """
    Simple x' = Ax ODE with A being a 2x2 matrix or differently written
    x' = ax+by
    y' + cx+dy
    :param s:
    :param t:
    :return:
    """
    a = -1
    b = -1
    c = -1
    d = -11
    x = s[0]
    y = s[1]
    dxdt = a * x + b * y
    dydt = c * x + d * y
    return [dxdt, dydt]


def planarsystems(s, t):
    """
    ODE from planarsystems exercise 1 (Dimensionless)
    :param s:
    :param t:
    :return:
    """
    l1 = 1
    l2 = 1.5
    x = s[0]
    y = s[1]
    dxdt = x * (1 - x) - l1 * x * y
    dydt = y * (1 - y) - l2 * x * y
    return [dxdt, dydt]


def planarsystems_extended(s, t):
    """
    ODE from planarsystems exercise 1 (Dimensionless)
    :param s:
    :param t:
    :return:
    """
    k1 = 1
    k2 = 1
    r = 2
    b1 = 1
    b2 = 1
    x = s[0]
    y = s[1]
    dxdt = r * x * (1 - x / k1) - b1 * x * y
    dydt = r * y * (1 - y / k2) - b2 * x * y
    return [dxdt, dydt]


def planarsystems2(s, t):
    k = 3
    l = 2
    x = s[0]
    y = s[1]
    dxdt = -k*x*y
    dydt = k*x*y - l*y
    return [dxdt, dydt]

def chemical_oscillations(s, t):
    a = 10
    b = 3*a/5-25/a+1
    x = s[0]
    y = s[1]
    dxdt = a-x - (4*x*y)/(1+x*x)
    dydt = b*x*(1-y/(1+x*x))
    return [dxdt, dydt]
