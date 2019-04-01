import sys

#variables for counting

LineCount = 0
TokenCount = 1
CharCount = 0
VowelCount = 0

#read from the wiki corpus from standard input
text =  sys.stdin.read()


for c in text:
	CharCount = CharCount + 1
	if c == ' ':
		TokenCount = TokenCount + 1
	if c in 'aeiou':
		VowelCount = VowelCount + 1
	if c == '\n':
		LineCount = LineCount + 1
		
SylCount = VowelCount/TokenCount

print(CharCount)
print(LineCount)
print(SylCount)
print(TokenCount)

#This doesn't work for languages that use many vowels in one syllable (French being my main thought)