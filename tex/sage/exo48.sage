# -*- coding: utf8 -*-
import outilsMAT1151

var('x')
fa(x) = cos(x)
fb(x) = sqrt(x+1)-sqrt(x)
fc(x) = (1+x)**(1/6)-1
print outilsMAT1151.ConditionnementRelatif(fa,pi/2)
print outilsMAT1151.ConditionnementRelatif(fb,oo)
print outilsMAT1151.ConditionnementRelatif(fc,0)
