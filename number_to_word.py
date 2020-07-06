#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

one = [ "", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ","ten ","eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
ten = [ "", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
listhindi = ["","एक","दो","तीन","चार","पांच","छह","सात","आठ","नौ","दस","ग्यारह","बारह","तेरह","चौदह","पंद्रह","सोलह",'सत्रह','अठारह','उन्नीस','बीस','इकीस','बाईस','तेइस','चौबीस','पच्चीस','छब्बीस','सताइस','अट्ठाइस','उनतीस','तीस','इकतीस','बतीस','तैंतीस','चौंतीस','पैंतीस','छतीस','सैंतीस','अड़तीस','उनतालीस','चालीस','इकतालीस','बयालीस','तैतालीस','चवालीस','पैंतालीस','छयालिस','सैंतालीस','अड़तालीस','उनचास','पचास','इक्यावन','बावन','तिरपन','चौवन','पचपन','छप्पन','सतावन','अठावन','उनसठ','साठ','इकसठ','बासठ','तिरसठ','चौंसठ','पैंसठ','छियासठ','सड़सठ','अड़सठ','उनहतर','सत्तर','इकहतर','बहतर','तिहतर','चौहतर','पचहतर','छिहतर','सतहतर','अठहतर','उन्नासी','अस्सी','इक्यासी','बयासी','तिरासी','चौरासी','पचासी','छियासी','सतासी','अट्ठासी','नवासी', 'नब्बे','इक्यानवे','बानवे','तिरानवे','चौरानवे','पचानवे','छियानवे','सतानवे','अट्ठानवे','निन्यानवे','एक सौ']
listmarathi=[" ","एक","दोन","तीन","चार","पाच","सहा","सात","आठ","नऊ","दहा","अकरा","बारा","तेरा","चौदा","पंधरा","सोळा","सतरा","अठरा","एकोणीस","वीस","एकवीस","बावीस","तेवीस","चोवीस","पंचवीस","सव्वीस","सत्तावीस","अठ्ठावीस","एकोणतीस","तीस","एकतीस","बत्तीस","तेहेतीस","चौतीस","पस्तीस","छत्तीस","सदतीस","अडतीस","एकोणचाळीस","चाळीस","एक्केचाळीस","बेचाळीस","त्रेचाळीस","चव्वेचाळीस","पंचेचाळीस","सेहेचाळीस","सत्तेचाळीस","अठ्ठेचाळीस","एकोणपन्नास","पन्नास","एक्कावन्न","बावन्न","त्रेपन्न","चोपन्न","पंचावन्न","छप्पन्न","सत्तावन्न","अठ्ठावन्न","एकोणसाठ","साठ","एकसष्ठ","बासष्ठ","त्रेसष्ठ","चौसष्ठ","पासष्ठ","सहासष्ठ","सदुसष्ठ","अडुसष्ठ","एकोणसत्तर","सत्तर","एक्काहत्तर","बाहत्तर","त्र्याहत्तर","चौर्‍याहत्तर","पंच्याहत्तर","शहात्तर","सत्याहत्तर","अठ्ठ्याहत्तर","एकोण ऐंशी","ऐंशी","एक्क्याऐंशी","ब्याऐंशी","त्र्याऐंशी","चौऱ्याऐंशी","पंच्याऐंशी","शहाऐंशी","सत्त्याऐंशी","अठ्ठ्याऐंशी","एकोणनव्वद","नव्वद","एक्क्याण्णव","ब्याण्णव","त्र्याण्णव","चौऱ्याण्णव","पंच्याण्णव","शहाण्णव","सत्त्याण्णव","अठ्ठ्याण्णव","नव्व्याण्णव","शंभर"]

	
def numToWords(n, s):  # n is 1 or 2 digit number and s if for 'thousand' , 'hundred', 'lakh' , crore
	str2=""
	if (n > 19):        
		str2 += ten[n // 10] + one[n % 10]
	else: 
		str2 += one[n] 
	if (n):         # if n is non-zero
		str2 += s
	return str2

def convertToEnglish(n): 
	output =" " 			# Function to print a given number in words 
	output += numToWords((n // 10000000),"crore ")    # for ten millions and hundred millions places
	output +=numToWords(((n // 100000) % 100),"lakh ")   # for hundred thousands  and one millions places 
	output +=numToWords(((n // 1000) % 100),"thousand ") #for  thousands and tens thousands places  
	output +=numToWords(((n // 100) % 10), "hundred ")   # hfor hundreds places 
	output += numToWords((n % 100), "")  # handles digits at ones and tens places
	return output

def hindinumbers(n,s):
	str2 = " "
	if ( n <= 100 ):
		str2 += listhindi[n]
	elif (n == 0):
		print(" शून्य 0/100")
	else:
		str2 +=converttohindi(n)
	if (n):
		str2 += s
	return str2

def converttohindi(n): 
	output =""
	output += hindinumbers((n // 10000000),"करोड़ ")    # for ten millions and hundred millions places
	output += hindinumbers(((n // 100000) % 100),"लाख ")   # for hundred thousands  and one millions places 
	output += hindinumbers(((n // 1000) % 100),"हज़ार ") #for  thousands and tens thousands places  
	output += hindinumbers(((n // 100) % 10),"सौ ")   # hfor hundreds places 
	output += hindinumbers((n % 100), "")  # handles digits at ones and tens places
	return output
	
def converttomarathi(n): 
	output =""
	output +=marathinumbers((n // 10000000),"कोटी ")    # for ten millions and hundred millions places
	output += marathinumbers(((n // 100000) % 100),"लाख ")
	output += marathinumbers(((n // 1000) % 100),"हजार ") #for  thousands and tens thousands places  
	output += marathinumbers(((n // 100) % 10),"शे ")   # hfor hundreds places 
	output +=marathinumbers((n % 100), "")  # handles digits at ones and tens places
	return output

def marathinumbers(n,s):
	str2 = " "
	if ( n <= 100 ):
		str2 += listmarathi[n]
	elif (n == 0):
		print(" शून्य ")
	else:
		str2 += converttomarathi(n)
	if (n):
		str2 += s
	return str2

def main():
	value=float(input(" \n\n enter amount:"))
	n=int(value)
	decimal=str(value).split('.')  #spliting inetegers
	decimal=int(decimal[1])
	f = open("result.txt", mode = 'a', encoding='utf-8')# opening a file for writing with encoding
	f.write("\nAMOUNT=")
	f.writelines(str(value))
	while(1):
		print("****select language:*********** \n 1. English \n 2. Hindi \n 3. Marathi \n 4. exit ")
		choice=input("your choice:")
		if(choice == '1'):
			result=convertToEnglish(n)
			f.write("\n")
			f.write(str(result))
			f.write(str(decimal))
			f.write("/100")
			print(result,decimal,"/100")
		if(choice == '2'):
			result=converttohindi(n)
			f.write("\n")
			f.write(str(result))
			f.write(str(decimal))
			f.write("/100")
			print(result,decimal,"/100")

		if(choice == '3'):
			result=converttomarathi(n)
			f.write("\n")
			f.write(str(result))
			f.write(str(decimal))
			f.write("/100")
			print(result,decimal,"/100")
		if(choice == '4'):
			exit()
	f.close()

if __name__ == "__main__":
	main()

