import string

phrase = "Darkness comprise, on wishes The dream wheel propped with the star in Will stop the progress of the sky" \
         "Cause earth turns and drags us Into the heat The hardness of the shell of human aims The strength of melted "\
         "thoughts. Of' under, hands Elektronic? visions; of associations for time! into. back gear."

words = ["and", "in", "on", "under", "for"]
signs = string.punctuation

for sign in signs:
    phrase = phrase.replace(sign, "")

text = phrase.split(" ")

print(f"Długość textu: {len(text)}")

for word in text:

    if word.istitle():
        print(word, end=" ")
print()

flag = False
for word, index in enumerate(text):

    if word in words:
        print(f"word: {word}  index: {index}")
        flag = True

if not flag:
    print(f"Lack of words from list {words} in text")

text.sort()
print(text)
