#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Suat Berkant Gülen

people = {"Ahmet Özkoparan" : {"Memleket": "İstanbul",
								"Meslek" : "Öğretmen",
								"Yaş" : 34},
			"Mehmet Yağız" : {"Memleket": "Adana",
								"Meslek" : "Mühendis",
								"Yaş" : 40},
			"Seda Bayrak" : {"Memleket": "İskenderun",
								"Meslek" : "Doktor",
								"Yaş" : 30}}


print(people)


name = "Hakkında ayrıntılı bilgi edinmek \
istediğiniz kişinin adını girin: "

person = input(name)

detail = input("Memleket/Meslek/Yaş? ")

print(people[person][detail])

# Sözlük içerisindeki verilerin sıralama gibi bir kavramı yoktur.
# Sözlükteki öğeler açısından ‘sıra’ diye bir kavram yoktur.

# ! Not: Python3.7 ve sonrasında, sözlükler içerdikleri öğelerin eklenme sırasını korumaktadır. !

