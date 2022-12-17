def letter_uppercase(text: str):
    text_list = []
    change = True
    for letter in text:
        text_list.append(letter)
    for i in range(len(text_list)):
        # check for everything but the i. Because for everything but the i
        # we can know to put an upper from the last position
        if change and text_list[i] != " ":
            text_list[i] = text_list[i].upper()
            change = False
        if (text_list[i] == "?") or (text_list[i] == "!") or (text_list[i] == "."):
            change = True
        # check for the i to turn it to I.
        if text_list[i] == " " and (text_list[i - 1] == "i") and (text_list[i - 2] == " "):
            text_list[i - 1] = text_list[i - 1].upper()
    changed_text = str()
    for i in range(len(text_list)):
        changed_text += text_list[i]
    return changed_text


text_global = input("Enter a str: ")
print(letter_uppercase(text_global))