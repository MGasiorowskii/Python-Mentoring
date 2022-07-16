import string

phrase = "Darkness comprise, evil wishes The dream wheel propped with the star axle Will stop the progress of the sky" \
         "Cause earth turns and drags us Into the heat The hardness of the shell of human aims The strength of melted "\
         "thoughts. Of shivering, hands Elektronic? visions of associations Putting time ! into. back gear."

signs = string.punctuation

for sign in signs:
    phrase = phrase.replace(sign, "")

text = phrase.split(" ")
revers_text = text[::-1]

print(revers_text)
