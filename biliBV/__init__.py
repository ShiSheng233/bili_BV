# -*- coding: UTF-8 -*-
key = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
dic = {}
for a in range(58):
	dic[key[a]]=a
s=[11,10,3,8,4,6]
xor=177451812
add=8728348608

def decode(BV):
	r=0
	for a in range(6):
		r+=dic[BV[s[a]]]*58**a
	return (r-add)^xor

def encode(av):
	av=(int(str(av).lstrip('av'))^xor)+add
	r=list('BV1  4 1 7  ')
	for a in range(6):
		r[s[a]]=key[av//58**a%58]
	return ''.join(r)
