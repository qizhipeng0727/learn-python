#-*- coding:utf-8 -*-
#姓名：戚志鹏
#1403050115
#通风一班
'''
求物理公式
'''

import math
k,p,T=1.38e-23,1.013e5,300.15
n=p/(k*T)
print 'n=',n
M,NA=32e-3,6.022e23
n=M/NA
print 'n=',n
n,m=2.45e25,5.31e-26
rho=n*m
print 'rho=',rho
R=8.31
v=math.sqrt(3*R*T/M)
print 'math.sqrt(v**2)=',math.sqrt(v**2)
epsilonk=3/2*k*T
print 'epsilonk=',epsilonk
epsilon=m/M*5/2*R*T
print 'epsilon=',epsilon