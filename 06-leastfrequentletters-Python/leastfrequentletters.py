# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequentletters(s):
	# Your code goes here
	s = s.lower()

	u = set(s)

	d = {}
	for i in u:
		if ord(i) <= 122 and ord(i) >= 65:
			d[i] = s.count(i)
	keys = list(d.keys())
	values = list(d.values())

	l = []
	for i in range(len(values)):
		if values[i] == min(values):
			l.append(keys[i])

	l.sort()
