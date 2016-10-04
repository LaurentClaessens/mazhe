function y = somme(arg)
	taille = 10
	v = 0:taille
	w = sin(arg).^v	
		# L'astuce est de faire a.^v pour faire [a^i for i in v]
	y = sum(w)
end

somme(pi/5) %2.4189
