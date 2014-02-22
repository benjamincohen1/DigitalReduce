import random, sys
def main():
	wordsFile = open('wordsEn.txt')
	largeFile = open('out.txt', 'w')
	words = []

	for x in wordsFile:
		words.append(x.strip())
	l = len(words)

	for x in xrange(int(sys.argv[1])):
		for y in xrange(int(sys.argv[1])):
			largeFile.write(words[random.randint(0,l) - 1] + " ")


if __name__ == "__main__":
	main()
