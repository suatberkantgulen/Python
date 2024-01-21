#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Suat Berkant Gülen

# Tıpkı listeler gibi, sözlükler de büyüyüp küçülebilen bir veri tipidir. 

people = {}

print(people)

#  sözlük[anahtar] = değer
people["Ahmet"] = "Adana"

print(people)
print(people["Ahmet"])

notes = {}

notes["Ahmet"] = 45
notes["Mehmet"] = 77
notes["Seda"] = 98
notes["Deniz"] = 95
notes["Ege"] = 95
notes["Zeynep"] = 100

print(notes)

# Bir sözlüğe değer olarak bütün veri tiplerini verebiliriz.

different_values = {}

different_values["a"] = 1
different_values["b"] = "2"
different_values["c"] = [3, 4, 5]
different_values["d"] = 'alti'
different_values["e"] = (7, 8, 9)

print(type(different_values["a"]))
print(type(different_values["b"]))
print(type(different_values["c"]))
print(type(different_values["d"]))
print(type(different_values["e"]))

# Sözlükler değer olarak her türlü veri tipini kabul etmektedir. 
# Ama durum sözlük anahtarları açısından böyle değildir. 
# Yani sözlüklere anahtar olarak her veri tipini atayamayız !

# !!! Bir değerin ‘anahtar’ olabilmesi için, 
# o öğenin değiştirilemeyen (immutable) bir veri tipi olması gerekir.
# Değiştirilemeyen veri tipleri : Demetler, Sayılar, Karakter Dizileri
# Değiştirilebilen veri tipleri : Listeler, Sözlükler

different_keys = {}

different_values[(1, 2, 3)] = "key tuple" # anahtar olarak demet ekleme
print(different_values[(1, 2, 3)])

# Liste anahtar olarak atanamaz! Alt satır hata verecektir.
# different_values[[4, 5]] = "key list" # anahtar olarak liste ekleme
