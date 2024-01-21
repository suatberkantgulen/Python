#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Suat Berkant Gülen


# Liste üreteçlerini kullanarak tek satırda ve hızlı bir şekilde listeler oluşturabiliyorduk. 
# Aynı şey sözlükler için de geçerlidir. 


alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'


# Amacımız bu harflerin her birine bir numara vermek.
comprehensions = {}
	
for i in alphabet:
	comprehensions[i] = alphabet.index(i)

print(comprehensions)

for i in range(len(alphabet)):
	comprehensions[alphabet[i]] = i

print(comprehensions)

comprehensions = {i: alphabet.index(i) for i in alphabet}

print(comprehensions)

# Sözlükler, her biri birbirinden : işareti ile ayrılan birtakım 
# anahtar-değer çiftlerinden oluşmaktadır. 

# Sözlük üreteci yapısında : işaretinin sol tarafına alphabet adlı listedeki her bir öğeyi; 
# sağ tarafına da bu öğelerin uzunluklarını ekleyebiliriz.

names = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]

lengthOfNames = {name : len(name) for name in names}

print(lengthOfNames)
