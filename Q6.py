def add_polynomials(p1, p2):
    result = {}
    for power in p1:
        result[power] = result.get(power, 0) + p1[power]
    for power in p2:
        result[power] = result.get(power, 0) + p2[power]
    return result

def print_polynomial(poly):
    terms = []
    for power in sorted(poly.keys(), reverse=True):
        coeff = poly[power]
        if coeff != 0:
            if power == 0:
                terms.append(f"{coeff}")
            elif power == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{power}")
    return " + ".join(terms) if terms else "0"

poly1 = {2: 3, 1: 2, 0: -4}
poly2 = {3: 1, 1: 4, 0: 5}
result = add_polynomials(poly1, poly2)
print("Polynomial 1:", print_polynomial(poly1))
print("Polynomial 2:", print_polynomial(poly2))
print("Sum:", print_polynomial(result))
