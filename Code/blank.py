input = "THE"


def one(input):
	word = ' '
	for char in input:
		word = word + char + char
	return word