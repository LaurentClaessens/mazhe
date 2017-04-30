x = [0.0005,0.001,0.005,0.01,0.02,0.05]
y = [422.74,421.36,415.80,412.00,407.24,399.09]

p = polyfit(sqrt(x),y,1) %-118.00   424.64
polyout(p,"x")

abcisses = 0.0005:0.0001:0.05
ordonnees = p(1)*sqrt(abcisses)+p(2)

plot(abcisses,ordonnees,':',x,y,'o')
print -dps exo34.ps
  

