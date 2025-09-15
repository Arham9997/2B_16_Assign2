def multiply_polynomials(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]
    return result
poly1 = [2, 0, 3]
poly2 = [1, 4]
result = multiply_polynomials(poly1, poly2)
print(result)
