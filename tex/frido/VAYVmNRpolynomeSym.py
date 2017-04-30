sage: P(x)=x**3+2*x**2+3*x+4
sage: S=solve(  P(x)==0,x  )   
sage: sols=[ s.rhs() for s in S  ]
sage: Q=[  s**2 for s in sols ] 
sage: s=sum(Q)
sage: s.simplify_full()
-2
