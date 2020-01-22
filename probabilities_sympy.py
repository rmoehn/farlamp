# -*- encoding: utf-8 -*-

from sympy import symbols, simplify

n = symbols('n', integer=True)
p = symbols('p')

a1_a1 = 1 - p + p/(n+1)
a1na1 = p - p/(n+1)
a2_a2__a1_a1 = 1 - p + p/(n+1)
a2_a2__a1na1 = p / (n+1)
a2na2__a1_a1 = p - p/(n+1)
a2na2__a1na1 = 1 - p/(n+1)
simplify(a2_a2__a1_a1 + a2na2__a1_a1)
# 1

simplify(a2_a2__a1na1 + a2na2__a1na1)
# 1

simplify(a1_a1 + a1na1)
# 1

a2_a2 = a2_a2__a1_a1 * a1_a1 + a2_a2__a1na1 * a1na1
a2na2 = a2na2__a1_a1 * a1_a1 + a2na2__a1na1 * a1na1
simplify(a2_a2 + a2na2)
# 1

a2_a2.evalf(subs={p: 0.1, n: 4})
# 0.848

a2_a2.evalf(subs={p: 0.3, n: 4})
# 0.592

# >>> simplify(a2_a2)
# np2−2np+n+1n+1

for pval in [0.01, 0.1, 0.3]:
    print("{} & {:.3f} & & {:.3f} & \\\\".format(pval, a1_a1.evalf(subs={p: pval, n: 4}),
                              a2_a2.evalf(subs={p: pval, n: 4}),))
