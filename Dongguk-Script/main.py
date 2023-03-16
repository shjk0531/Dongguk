num = int(input("글자 입력: "), 16)

if num < 2:
    print("2진수 또는 8진수 또는 10진수 또는 16진수 입니다.")
elif num < 8:
    print("8진수 또는 10진수 또는 16진수 입니다.")
elif num < 10:
    print("10진수 또는 16진수 입니다.")
else:
    print("16진수 입니다.")
