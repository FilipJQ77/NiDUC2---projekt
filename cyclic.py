# -*- coding: utf-8 -*-
import numpy as np
import math
dzielnik = [1,0,1,1]


def encode_cyclic(bits: list) -> list:
    bits_amount = len(bits)
    bits_temp = []
    
    for i in range(bits_amount):
        bits_temp.append(bits[i])
        
    for i in range(len(dzielnik)-1):
        bits_temp.append(0)

    
    
    for i in range(bits_amount):
        if bits_temp[i] == 1:
            for j in range(len(dzielnik)):
                bits_temp[i+j] = int(np.logical_xor(bits_temp[i+j], dzielnik[j]))
            
    for i in range(len(dzielnik)-1):
        bits.append(bits_temp[bits_amount+i])

    return bits




def decode_cyclic(bits:list ) -> list:
    bits_amoun = len(bits)
    
    bits_tem = []
    
    for i in range(bits_amoun):
        bits_tem.append(bits[i])
    
    for i in range(bits_amoun-len(dzielnik)+1):
        if bits_tem[i] == 1:
            for j in range(len(dzielnik)):
                bits_tem[i+j] = int(np.logical_xor(bits_tem[i+j], dzielnik[j]))
     
    suma=0
    for i in range(len(dzielnik)):
        suma+=bits_tem[bits_amoun -1 - i]

    for i in range(len(dzielnik)-1):
        del bits[len(bits)-1]
    
    if suma!=0:
        bits.append("R")         
        
  
    return bits