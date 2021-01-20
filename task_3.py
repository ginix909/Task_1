import sympy
from sympy import Symbol, Mul, expand, degree, simplify

x = Symbol('x')                   # явно задали объект типа 'Symbol'.

def checking_limits(polynomial_1,polynomial_2):
    degree_of_polynomial_1 = degree(polynomial_1, x)
    degree_of_polynomial_2 = degree(polynomial_2, x)

    if degree_of_polynomial_1 > 20 or degree_of_polynomial_2 > 20:
        print(f'Степень одного из многочленов превышает 20: {degree_of_polynomial_1,degree_of_polynomial_2}')
    else:
        result_with_brackets = Mul(polynomial_1, polynomial_2)
        result_without_brackets = expand(result_with_brackets)
        simplify_result = simplify(result_without_brackets)
        print(simplify_result)

checking_limits(x+2,x**3-x**2+1)




