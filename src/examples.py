# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:23:52 2017

@author: sylhare

"""

import pyprime as p
import unit_test as ut

#Demo of Grphical Prime functions
p.sacksPlot()
p.ulamPlot()

#Demo of the Primarity testing functions
print(p.isPrime(7))
print(p.fermat(7))
print(p.millerRabin(7))

#Demo of the Prime generating functions
print(p.genPrimes(7))
print(p.findPrimes(2, 7, p.fermat))

#Demo of the unit_test functions
print(ut.carmiTest(p.isPrime))
print(ut.ppTest(p.isPrime))