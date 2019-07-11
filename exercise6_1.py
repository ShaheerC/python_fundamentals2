def wrap_text(word, symbols):
    return "{}{}{}".format(symbols, word, symbols[::-1])

print(wrap_text("hello", "==="))
print(wrap_text("new message", "---===###"))