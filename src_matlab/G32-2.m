u=1:100;
v=2.^(cos(2*u));
sum(v)	% 111.89

function retour=s(N)
u=1:N;
v=2.^(cos(2*u));
retour=sum(v);
end

for i=100:200
s(i)
end
% Le dernier est 223.88

