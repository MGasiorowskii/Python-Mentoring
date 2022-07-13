phrase = "To be, !or not to be is the; opening phrase of a soliloquy given by Prince Hamlet? in the so-callednunnery" \
         " scene of William Shakespeare's play Hamlet:, Act 3, Scene 1."

signs = [",", ".", ":", ";", "!", "?"]

for sign in signs:
    phrase = phrase.replace(sign, "")
print(phrase)

word = ""
sentence = []
for sign in phrase:
    if sign != " ":
        word += sign
    else:
        sentence.append(word)
        word = ""
sentence.append(word)

print("\nTuples")
signs_tuple = tuple(sentence)
print(f"Number of words: {len(signs_tuple)}")

for element in signs_tuple:
    print(element, end=" ")
print()

print(f"First word of phrase: {signs_tuple[0]}")
print(f"Fourth word of phrase: {signs_tuple[3]}")

print("\nSets")
signs_sets = set(sentence)
print(f"Number of elements: {len(signs_sets)}")

for element in signs_sets:
    print(element, end=" ")
print()

i = 1
for element in signs_sets:
    if i == 1:
        print(f"First element of phrase: {element}")
    elif i == 4:
        print(f"Fourth elemnt of phrase: {element}")
    i += 1



