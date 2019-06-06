function y = ma_fonction(arg)
	sq = sqrt(abs(arg))+1;
	a = sqrt(sq);
	b = sin( exp(arg.^3)+1 );
	numerateur = a*b;	% 1.3371
	c = atan(arg.^2);
	d = (log(sq)).^(3/2);
	denominateur = c+d;	% 1.6001
	y = numerateur/denominateur;	% 0.83566
end

reponse = ma_fonction(-1.2)
