┌────────────────────────────────────────────────────────────────────┐
│ SageMath Version 7.0, Release Date: 2016-01-19                     │
│ Type "notebook()" for the browser-based notebook interface.        │
│ Type "help()" for help.                                            │
└────────────────────────────────────────────────────────────────────┘
sage: f(x)=10**(-3)*x**2+0.8*x-1.2*10**(-5)
sage: solve(f(x)==0,x)
[x == -1/50*sqrt(400000030) - 400, x == 1/50*sqrt(400000030) - 400]
sage: numerical_approx(-1/50*sqrt(400000030))
-400.000015000000
sage: numerical_approx( 1/50*sqrt(400000030) - 400  )
0.0000149999996779115
