┌────────────────────────────────────────────────────────────────────┐
│ SageMath version 7.3, Release Date: 2016-08-04                     │
│ Type "notebook()" for the browser-based notebook interface.        │
│ Type "help()" for help.                                            │
└────────────────────────────────────────────────────────────────────┘
sage: var('a,b,k')
(a, b, k)
sage: f(x)=exp(-k*x)
sage: f.integrate(x,a,b)
e^(-a*k)/k - e^(-b*k)/k
