phrase = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of" \
         " forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently" \
         " rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door" \
         " - Only this, and nothing more."
text = phrase.split(" ")
counts = dict()
for word in text:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
