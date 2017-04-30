┌────────────────────────────────────────────────────────────────────┐
│ SageMath version 7.3, Release Date: 2016-08-04                     │
│ Type "notebook()" for the browser-based notebook interface.        │
│ Type "help()" for help.                                            │
└────────────────────────────────────────────────────────────────────┘
sage: n(taylor(arctan(x),x,0,5)(1/sqrt(3)))*6
3.15618147156995
sage: n(taylor(arctan(x),x,0,10)(1/sqrt(3)))*6
3.14260474566308
sage: n(taylor(arctan(x),x,0,20)(1/sqrt(3))*6-pi)
-2.14265171338823e-6
sage: n(taylor(arctan(x),x,0,58)(1/sqrt(3))*6-pi)
8.88178419700125e-16
