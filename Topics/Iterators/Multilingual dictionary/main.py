# for e, s, f in zip(english, spanish, french):
#     print(e, s, f)

for words in zip(english, spanish, french):
    print(*words)