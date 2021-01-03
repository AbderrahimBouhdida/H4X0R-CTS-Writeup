p1c = """θαιςτςυεοωαεςνεες
τιειαιθτττνεφσναζ
σιοσμνγτιοθθεαεεω
ξγτςτϊμταιστααβςν
αετθςσθοοθξξμεττω
ωτξνυςετεδσεδηεμι
μθοθδωξιεγδιαϊιωτ
οτωουιμπδστοοαξον
δχυεοπγσεςετθδογτ"""
p2c = """βιεςυαανεβγιξηουτ
ςσεξστττφεαμαιιοσ
τετξζηειοιεθξεξξθ
χαθγιοοαγξλνδοδδτ
εεθφιοσχςχοεξιοςτ
ςεεψωεσξμιεαξεοηξ
θειςδπβττδονηωδδχ
ωττσβςσμυοθπφηιτπ
θαοθθομιιατδεαεοφ"""
p3c = """τσαμμωτθμεσατπαςσ
ιτασωςςενατξψνασσ
"""

def dec(greek):
	letters = ""
	for x in greek:
		try:		
			letters = letters + chr(ord(x) - 848)
		except :
			continue
	return letters

def partI(cipher):
	lst = ["X"] * 153
	count = 1
	pos = 0
	start = 1

	test = ""

	lst[0] = cipher[0]
	for i in cipher[1:]:
		

		if pos == 152 :
			pos = start
			lst[count] = cipher[pos]
			count += 1
			continue

		if pos in range(136,154):
			
			start = start + 1
			pos = start
			if start == 17:
				break
			lst[count] = cipher[pos]
			count += 1
			continue

		if (pos + 2) % 17 == 0 or (pos +1) % 17 == 0:
			pos = pos + 2
			lst[count] = cipher[pos]
			count += 1
			continue 
		pos = pos + 19
		lst[count] = cipher[pos]
		count += 1
	tmp = ''.join(lst)
	out = ''
	for x in range(len(tmp)):
		out = out + tmp[x]
		if (x+1) % 17 == 0 and x > 1:
			out = out + '\n'

	return out
def partII(cipher):
	lst = ["X"] * 153

	pos = 0
	start = 1
	count = 1
	lst[0] = cipher[0]
	for i in cipher[1:]:
		

		if pos == 152 :
			pos = start
			lst[count] = cipher[pos]
			count += 1
			continue

		if pos in range(136,154):
			start = start + 1
			pos = start
			if start == 34:
				start = 17
				pos = start
			if start == 19:
				break
			if start == 11:
				start = start + 19
				pos = start
			lst[count] = cipher[pos]
			count += 1
			continue

		if (pos + 2) % 17 == 0 or (pos +1) % 17 == 0:
			pos = pos + 2
			lst[count] = cipher[pos]
			count += 1
			continue 
		pos = pos + 19
		lst[count] = cipher[pos]
		count += 1
	lst[-6:] = cipher[11:17]
	tmp = ''.join(lst)
	out = ''
	for x in range(len(tmp)):
		out = out + tmp[x]
		if (x+1) % 17 == 0 and x > 1:
			out = out + '\n'

	return out




def partIII(last):
	lst = ["X"]*34
	lst[:4] = reversed(last[:4])
	lst[4:8] = last[4:8]
	lst[8:10] = reversed(last[8:10])
	lst[10:12] = reversed(last[10:12])
	lst[12:16] = last[12:16]
	lst[16:19] = reversed(last[16:19])
	lst[19:21] = reversed(last[19:21])
	lst[21:29] = reversed(last[21:29])
	lst[29:34] = last[29:34]
	tmp = ''.join(lst)
	out = ''
	for x in range(len(tmp)):
		out = out + tmp[x]
		if (x+1) % 17 == 0 and x > 1:
			out = out + '\n'

	return out

print(partI(dec(p1c)))
print(partII(dec(p2c)))
print(partIII(dec(p3c)))