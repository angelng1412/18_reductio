import string

file = open("sleepyhollow.txt", "r")
text = file.read()
words = [word.strip(string.punctuation) for word in text.split()]

def freq(word):
    temp = [1 for x in words if x == word]
    return reduce(lambda a, b : a + b, temp)

print "schoolhouse: ", freq("schoolhouse")
print "horse: ", freq("horse")


def totalfreq(words):
    temp = [freq(word) for word in words] 
    return reduce(lambda a, b : a + b, temp)

print "the, rider: ", totalfreq(["the", "horse"])
print "horse, schoolhouse: ", totalfreq(["horse", "schoolhouse"])


def mostfreq():
    return reduce(lambda a, b : a if freq(a) > freq(b) else b, words)

print "most frequent: ", mostfreq()
