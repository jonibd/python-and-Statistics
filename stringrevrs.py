text=input("Enter your text:")
if len(text)>5:
    re_text=text[::-1]
    print("reverse text",re_text)
else:
    print("text length cannot biger 5")
        