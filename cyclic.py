# -*- coding: utf-8 -*-
import numpy as np
import math
dzielnik = [1,0,0,1,0,1]
len_dzielnik = len(dzielnik)

def encode_cyclic(bits: list) -> list:
    bits_amount = len(bits)
    bits_temp = []
    
    for i in range(bits_amount):
        bits_temp.append(bits[i])
        
    for i in range(len_dzielnik-1):
        bits_temp.append(0)

    
    
    for i in range(bits_amount):
        if bits_temp[i] == 1:
            for j in range(len_dzielnik):
                bits_temp[i+j] = int(np.logical_xor(bits_temp[i+j], dzielnik[j]))
    
    
    for i in range(len_dzielnik-1):
        bits.append(bits_temp[bits_amount+i])

    return bits




def decode_cyclic(bits:list ) -> list:
    bits_amoun = len(bits)
    
    bits_tem = []
    
    for i in range(bits_amoun):
        bits_tem.append(bits[i])
    
    for i in range(bits_amoun-len_dzielnik+1):
        if bits_tem[i] == 1:
            for j in range(len_dzielnik):
                bits_tem[i+j] = int(np.logical_xor(bits_tem[i+j], dzielnik[j]))
     
    suma=0
    for i in range(len_dzielnik):
        suma+=bits_tem[bits_amoun -1 - i]
    
    print(bits_tem)
        
    
   # if suma!=0:
      #  bits.append("R")
    
    if suma == 0:
        for i in range(len_dzielnik-1):
            bits.pop(-1)
        return bits
    
    elif suma == 1:
        for i in range(len_dzielnik-1):
            bits.pop(-1)
        bits.append("F")
        return bits
    
    else:
        return repair_crc(bits)
        
    
    return bits

def repair_crc(broken:list)->list:
    
    broken_1 =[]
    broken_2=[]
    broken_len=len(broken)
    
    for i in range(broken_len):
        broken_1.append(broken[i])
        broken_2.append(broken[i])
    
    rotacje=0;
    
    while rotacje<broken_len-1:
        broken_1 = broken_1[1:]+broken_1[:1]
        rotacje+=1
        
        for i in range(broken_len-len_dzielnik+1):
            if broken_1[i] == 1:
                for j in range(len_dzielnik):
                    broken_2[i+j] = int(np.logical_xor(broken_1[i+j], dzielnik[j]))
        
        print(broken_2, rotacje)
        
        test=0
        for i in range(broken_len):
            test+=broken_2[i]
        
        
        if test==1:
            for i in range(broken_len):
                broken_1[i]+=broken_2[i]
            broken_1 = broken_1[-(rotacje):]+broken_1[:-(rotacje)]
            
            return broken_1
        
    return ["R"]
    
lista = [1,1,0,1,0,0,1,1,1,0,1,1,1,1]

#lista = lista[3:]+lista[:3] w lewo

#print(encode_cyclic(lista))

print (encode_cyclic([1,1,1,1,0,0,1,1,1,0,1,1,1,1]))

#print(decode_cyclic(encode_cyclic(lista)))

# [1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]

print (decode_cyclic([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]))
