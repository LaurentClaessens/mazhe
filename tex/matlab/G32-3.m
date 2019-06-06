num = [1,2,4,5,7]
tailles = [130,120,123,114,131]

P=polyfit(num,tailles,3)
% P =   1.1404e-01  -2.5063e-02  -5.9937e+00   1.3451e+02

polyval(P,3)	% 119.39
polyval(P,6)	% 122.28
