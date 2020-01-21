>>> n = symbols('n', integer=True)

Warning: this shell runs with SymPy 1.5.1 and so examples pulled from
other documentation may provide unexpected results.
Documentation can be found at http://docs.sympy.org/1.5.1.

>>> p = symbols('p')

>>> a1_a1 = 1 - p + p/(n+1)
>>> a1na1 = p - p/(n+1)
>>> a2_a2__a1_a1 = 1 - p + p/(n+1)
>>> a2_a2__a1na1 = p / (n+1)
>>> a2na2__a1_a1 = p - p/(n+1)
>>> a2na2__a1na1 = 1 - p/(n+1)
>>> simplify(a2_a2__a1_a1 + a2na2__a1_a1)
1

>>> simplify(a2_a2__a1na1 + a2na2__a1na1)
1

>>> simplify(a1_a1 + a1na1)
1

>>> a2_a2 = a2_a2__a1_a1 * a1_a1 + a2_a2__a1na1 * a1na1
>>> a2na2 = a2na2__a1_a1 * a1_a1 + a2na2__a1na1 * a1na1
>>> simplify(a2_a2 + a2na2)
1

>>> a2_a2.evalf(subs={p: 0.1, n: 4})
0.848

>>> a2_a2.evalf(subs={p: 0.3, n: 4})
0.592

>>> simplify(a2_a2)
np2−2np+n+1n+1
