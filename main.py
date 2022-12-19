def gcd(a, b):
    print(f"gcd з параметром: {a, b}")

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    result = a + b
    print(f"gcd результат: {result}")
    return result


def gcdex(a, b):
    print(f"gcdex з параметром: {a, b}")

    d0, d1 = (a, b)
    x0, x1 = (1, 0)
    y0, y1 = (0, 1)

    q = 0
    while d1 != 0:
        q = d0 // d1
        d0, d1 = (d1, d0 - d1 * q)
        x0, x1 = (x1, x0 - x1 * q)
        y0, y1 = (y1, y0 - y1 * q)
    print(f"gcdex результат: {d0, x0, y0}")
    return d0, x0, y0


def inverse_element(a, n):
    print(f"inverse_element з параметром: {a, n}")
    print("==============")

    d, x, y = gcdex(a, n)
    if d == 1:
        result = x % n
        print(f"inverse_element результат: {result}")

        return result

    return 0


def phi(m):
    print(f"phi з параметром: {m}")

    result = m
    i = 2
    while i * i <= m:
        if m % i == 0:
            while m % i == 0:
                m //= i
            result -= result // i
        else:
            i += 1
    if m > 1:
        result -= result // m

    print(f"euler результат: {result}")

    return result


def inverse_element_2(a, p):
    print(f"euler з параметром: {a, p}")
    print("==============")

    phi_res = phi(p) - 1

    result = (a ** phi_res) % p
    print(f"euler результат: {result}")

    return result


if __name__ == '__main__':
    gcd(18, 30)
    print("==============")
    gcdex(612, 342)
    print("==============")
    inverse_element(5, 18)
    print("==============")
    phi(34)
    print("==============")
    inverse_element_2(3, 34)
    print("==============")
