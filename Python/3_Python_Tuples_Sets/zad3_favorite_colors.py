def string_to_set(phrase):
    word = ""
    sentence = []
    for sign in phrase:
        if sign != " ":
            word += sign
        else:
            sentence.append(word)
            word = ""
    sentence.append(word)
    return set(sentence)


favorite_colors = "red black pink"
my_favorite_colors = "red green yellow"

favorite_colors_set = string_to_set(favorite_colors)
my_favorite_colors_set = string_to_set(my_favorite_colors)

if my_favorite_colors_set.isdisjoint(favorite_colors_set):
    print("No common favorite colors")
else:
    print("You have some colors in common")
    print(f"Both favorite colors: {my_favorite_colors_set & favorite_colors_set}")
    print(f"User unigue colors: {favorite_colors_set - my_favorite_colors_set}")
    print(f"My unigue colors: {my_favorite_colors_set - favorite_colors_set}")




favorite_colors_set

