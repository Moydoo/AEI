# -*- coding: utf-8 -*-

clp_part_of_speech = {
		'A': u'rzeczownik', 
		'B': u'czasownik', 
		'C': u'przymotnik', 
		'D': u'liczebnik', 
		'E': u'zaimek', 
		'F': u'przysłówek', 
		'G': u'nieodmienna część mowy'
	}
		
clp_description = {
	'A': { #rzeczownik
			 1: u'Mianownik, liczba pojedyncza',
			 2: u'Dopełniacz, liczba pojedyncza',
			 3: u'Celownik, liczba pojedyncza',
			 4: u'Biernik, liczba pojedyncza',
			 5: u'Narzędnik, liczba pojedyncza',
			 6: u'Miejscownik, liczba pojedyncza',
			 7: u'Wołacz, liczba pojedyncza',
			 8: u'Mianownik, liczba mnoga',
			 9: u'Dopełniacz, liczba mnoga',
			10: u'Celownik, liczba mnoga',
			11: u'Biernik, liczba mnoga',
			12: u'Narzędnik, liczba mnoga',
			13: u'Miejscownik, liczba mnoga',
			14: u'Wołacz, liczba mnoga'
		},
	'B': { #czasownik
			 1: u'Bezokolicznik',
			 2: u'Osoba 1, liczba pojedyncza, czas teraźniejszy',
			 3: u'Osoba 2, liczba pojedyncza, czas teraźniejszy',
			 4: u'Osoba 3, liczba pojedyncza, czas teraźniejszy',
			 5: u'Osoba 1, liczba mnoga, czas teraźniejszy',
			 6: u'Osoba 2, liczba mnoga, czas teraźniejszy',
			 7: u'Osoba 3, liczba mnoga, czas teraźniejszy',
			 8: u'Osoba 2, liczba pojedyncza, tryb rozkazujący',
			 9: u'Osoba 3, liczba pojedyncza, tryb rozkazujący',
			10: u'Osoba 1, liczba mnoga, tryb rozkazujący',
			11: u'Osoba 2, liczba mnoga, tryb rozkazujący',
			12: u'Osoba 3, liczba mnoga, tryb rozkazujący',
			13: u'Imiesłów współczesny',
			14: u'Imiesłów czynny',
			15: u'Osoba 1, liczba pojedyncza, rodzaj męski, czas przeszły',
			16: u'Osoba 2, liczba pojedyncza, rodzaj męski, czas przeszły',
			17: u'Osoba 3, liczba pojedyncza, rodzaj męski, czas przeszły',
			18: u'Osoba 1, liczba pojedyncza, rodzaj żeński, czas przeszły',
			19: u'Osoba 2, liczba pojedyncza, rodzaj żeński, czas przeszły',
			20: u'Osoba 3, liczba pojedyncza, rodzaj żeński, czas przeszły',
			21: u'Osoba 1, liczba pojedyncza, rodzaj nijaki, czas przeszły',
			22: u'Osoba 2, liczba pojedyncza, rodzaj nijaki, czas przeszły',
			23: u'Osoba 3, liczba pojedyncza, rodzaj nijaki, czas przeszły',
			24: u'Osoba 1, liczba mnoga, rodzaj męskoosobowy, czas przeszły',
			25: u'Osoba 2, liczba mnoga, rodzaj męskoosobowy, czas przeszły',
			26: u'Osoba 3, liczba mnoga, rodzaj męskoosobowy, czas przeszły',
			27: u'Osoba 1, liczba mnoga, rodzaj niemęskoosobowy, czas przeszły',
			28: u'Osoba 2, liczba mnoga, rodzaj niemęskoosobowy, czas przeszły',
			29: u'Osoba 3, liczba mnoga, rodzaj niemęskoosobowy, czas przeszły',
			30: u'Osoba 1, liczba pojedyncza, rodzaj męski, tryb przypuszczający',
			31: u'Osoba 2, liczba pojedyncza, rodzaj męski, tryb przypuszczający',
			32: u'Osoba 3, liczba pojedyncza, rodzaj męski, tryb przypuszczający',
			33: u'Osoba 1, liczba pojedyncza, rodzaj żeński, tryb przypuszczający',
			34: u'Osoba 2, liczba pojedyncza, rodzaj żeński, tryb przypuszczający',
			35: u'Osoba 3, liczba pojedyncza, rodzaj żeński, tryb przypuszczający',
			36: u'Osoba 1, liczba pojedyncza, rodzaj nijaki, tryb przypuszczający',
			37: u'Osoba 2, liczba pojedyncza, rodzaj nijaki, tryb przypuszczający',
			38: u'Osoba 3, liczba pojedyncza, rodzaj nijaki, tryb przypuszczający',
			39: u'Osoba 1, liczba mnoga, rodzaj męskoosobowy, tryb przypuszczający',
			40: u'Osoba 2, liczba mnoga, rodzaj męskoosobowy, tryb przypuszczający',
			41: u'Osoba 3, liczba mnoga, rodzaj męskoosobowy, tryb przypuszczający',
			42: u'Osoba 1, liczba mnoga, rodzaj niemęskoosobowy, tryb przypuszczający',
			43: u'Osoba 2, liczba mnoga, rodzaj niemęskoosobowy, tryb przypuszczający',
			44: u'Osoba 3, liczba mnoga, rodzaj niemęskoosobowy, tryb przypuszczający',
			45: u'Forma nieosobowa',
			46: u'Imiesłów bierny',
			47: u'Imiesłów uprzedni',
		},
	'C': { #przymiotnik
			 1: u'Mianownik, liczba pojedyncza, rodzaj męski żywotny',
			 2: u'Dopełniacz, liczba pojedyncza, rodzaj męski żywotny',
			 3: u'Celownik, liczba pojedyncza, rodzaj męski żywotny',
			 4: u'Biernik, liczba pojedyncza, rodzaj męski żywotny',
			 5: u'Narzędnik, liczba pojedyncza, rodzaj męski żywotny',
			 6: u'Miejscownik, liczba pojedyncza, rodzaj męski żywotny',
			 7: u'Wołacz, liczba pojedyncza, rodzaj męski żywotny',
			 8: u'Mianownik, liczba pojedyncza, rodzaj męski nieżywotny',
			 9: u'Dopełniacz, liczba pojedyncza, rodzaj męski nieżywotny',
			10: u'Celownik, liczba pojedyncza, rodzaj męski nieżywotny',
			11: u'Biernik, liczba pojedyncza, rodzaj męski nieżywotny',
			12: u'Narzędnik, liczba pojedyncza, rodzaj męski nieżywotny',
			13: u'Miejscownik, liczba pojedyncza, rodzaj męski nieżywotny',
			14: u'Wołacz, liczba pojedyncza, rodzaj męski nieżywotny',
			15: u'Mianownik, liczba pojedyncza rodzaj żeński',
			16: u'Dopełniacz, liczba pojedyncza, rodzaj żeński',
			17: u'Celownik, liczba pojedyncza, rodzaj żeński',
			18: u'Biernik, liczba pojedyncza, rodzaj żeński',
			19: u'Narzędnik, liczba pojedyncza, rodzaj żeński',
			20: u'Miejscownik, liczba pojedyncza, rodzaj żeński',
			21: u'Wołacz, liczba pojedyncza, rodzaj żeński',
			22: u'Mianownik, liczba pojedyncza, rodzaj nijaki',
			23: u'Dopełniacz, liczba pojedyncza, rodzaj nijaki',
			24: u'Celownik, liczba pojedyncza, rodzaj nijaki',
			25: u'Biernik, liczba pojedyncza, rodzaj nijaki',
			26: u'Narzędnik, liczba pojedyncza, rodzaj nijaki',
			27: u'Miejscownik, liczba pojedyncza, rodzaj nijaki',
			28: u'Wołacz, liczba pojedyncza, rodzaj nijaki',
			29: u'Mianownik, liczba mnoga, rodzaj męskoosobowy',
			30: u'Dopełniacz, liczba mnoga, rodzaj męskoosobowy',
			31: u'Celownik, liczba mnoga, rodzaj męskoosobowy',
			32: u'Biernik, liczba mnoga, rodzaj męskoosobowy',
			33: u'Narzędnik, liczba mnoga, rodzaj męskoosobowy',
			34: u'Miejscownik, liczba mnoga, rodzaj męskoosobowy',
			35: u'Wołacz, liczba mnoga, rodzaj męskoosobowy',
			36: u'Mianownik, liczba mnoga, rodzaj niemęskoosobowy',
			37: u'Dopełniacz, liczba mnoga, rodzaj niemęskoosobowy',
			38: u'Celownik, liczba mnoga, rodzaj niemęskoosobowy',
			39: u'Biernik, liczba mnoga, rodzaj niemęskoosobowy',
			40: u'Narzędnik, liczba mnoga, rodzaj niemęskoosobowy',
			41: u'Miejscownik, liczba mnoga, rodzaj niemęskoosobowy',
			42: u'Wołacz, liczba mnoga, rodzaj niemęskoosobowy',
			43: u'Stopień wyższy',
			44: u'Stopień najwyższy',
		},
	'D': { #liczebnik
			 1: u'Mianownik, liczba pojedyncza, rodzaj męski osobowy',
			 2: u'Dopełniacz, liczba pojedyncza, rodzaj męski osobowy',
			 3: u'Celownik, liczba pojedyncza, rodzaj męski osobowy',
			 4: u'Biernik, liczba pojedyncza, rodzaj męski osobowy',
			 5: u'Narzędnik, liczba pojedyncza, rodzaj męski osobowy',
			 6: u'Miejscownik, liczba pojedyncza, rodzaj męski osobowy',
			 7: u'Wołacz, liczba pojedyncza, rodzaj męski osobowy',
			 8: u'Mianownik, liczba pojedyncza, rodzaj męski nieosobowy',
			 9: u'Dopełniacz, liczba pojedyncza, rodzaj męski nieosobowy',
			10: u'Celownik, liczba pojedyncza, rodzaj męski nieosobowy',
			11: u'Biernik, liczba pojedyncza, rodzaj męski nieosobowy',
			12: u'Narzędnik, liczba pojedyncza, rodzaj męski nieosobowy',
			13: u'Miejscownik, liczba pojedyncza, rodzaj męski nieosobowy',
			14: u'Wołacz, liczba pojedyncza, rodzaj męski nieosobowy',
			15: u'Mianownik, liczba pojedyncza, rodzaj męski nieżywotny',
			16: u'Dopełniacz, liczba pojedyncza, rodzaj męski nieżywotny',
			17: u'Celownik, liczba pojedyncza, rodzaj męski nieżywotny',
			18: u'Biernik, liczba pojedyncza, rodzaj męski nieżywotny',
			19: u'Narzędnik, liczba pojedyncza, rodzaj męski nieżywotny',
			20: u'Miejscownik, liczba pojedyncza, rodzaj męski nieżywotny',
			21: u'Wołacz, liczba pojedyncza, rodzaj męski nieżywotny',
			22: u'Mianownik, liczba pojedyncza, rodzaj żeński',
			23: u'Dopełniacz, liczba pojedyncza, rodzaj żeński',
			24: u'Celownik, liczba pojedyncza, rodzaj żeński',
			25: u'Biernik, liczba pojedyncza, rodzaj żeński',
			26: u'Narzędnik, liczba pojedyncza, rodzaj żeński',
			27: u'Miejscownik, liczba pojedyncza, rodzaj żeński',
			28: u'Wołacz, liczba pojedyncza, rodzaj żeński',
			29: u'Mianownik, liczba pojedyncza, rodzaj nijaki',
			30: u'Dopełniacz, liczba pojedyncza, rodzaj nijaki',
			31: u'Celownik, liczba pojedyncza, rodzaj nijaki',
			32: u'Biernik, liczba pojedyncza, rodzaj nijaki',
			33: u'Narzędnik, liczba pojedyncza, rodzaj nijaki',
			34: u'Miejscownik, liczba pojedyncza, rodzaj nijaki',
			35: u'Wołacz, liczba pojedyncza, rodzaj nijaki',
			36: u'Mianownik, liczba mnoga, rodzaj męskoosobowy',
			37: u'Dopełniacz, liczba mnoga, rodzaj męskoosobowy',
			38: u'Celownik, liczba mnoga, rodzaj męskoosobowy',
			39: u'Biernik, liczba mnoga, rodzaj męskoosobowy',
			40: u'Narzędnik, liczba mnoga, rodzaj męskoosobowy',
			41: u'Miejscownik, liczba mnoga, rodzaj męskoosobowy',
			42: u'Wołacz, liczba mnoga, rodzaj męskoosobowy',
			43: u'Mianownik, liczba mnoga, rodzaj niemęskoosobowy',
			44: u'Dopełniacz, liczba mnoga, rodzaj niemęskoosobowy',
			45: u'Celownik, liczba mnoga, rodzaj niemęskoosobowy',
			46: u'Biernik, liczba mnoga, rodzaj niemęskoosobowy',
			47: u'Narzędnik, liczba mnoga, rodzaj niemęskoosobowy',
			48: u'Miejscownik, liczba mnoga, rodzaj niemęskoosobowy',
			49: u'Wołacz, liczba mnoga, rodzaj niemęskoosobowy',
		},
	'E': { #zaimek
			 1: u'Mianownik, liczba pojedyncza',
			 2: u'Dopełniacz, liczba pojedyncza',
			 3: u'Celownik, liczba pojedyncza',
			 4: u'Biernik, liczba pojedyncza',
			 5: u'Narzędnik, liczba pojedyncza',
			 6: u'Miejscownik, liczba pojedyncza',
			 7: u'Wołacz, liczba pojedyncza',
			 8: u'Mianownik, liczba mnoga',
			 9: u'Dopełniacz, liczba mnoga',
			10: u'Celownik, liczba mnoga',
			11: u'Biernik, liczba mnoga',
			12: u'Narzędnik, liczba mnoga',
			13: u'Miejscownik, liczba mnoga',
			14: u'Wołacz, liczba mnoga'
		},
	'F': { #przysłówek
			1: u'Stopień równy',
			2: u'Stopień wyższy',
			3: u'Stopień najwyższy'
		},
	'G': { #nieodmienne
			1: 'Nieodmienny'
		},
}
