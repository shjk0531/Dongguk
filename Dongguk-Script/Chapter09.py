# cofee = 0


# def coffee_machine(button):
#     print()
#     print("#1. (자동으로) 뜨거운 물을 준비한다.")
#     print("#2. (자동으로) 종이컵을 준비한다.")

#     if button == 1:
#         print("#3. (자동으로) 보통커피를 탄다.")
#     elif button == 2:
#         print("#3. (자동으로) 설탕커피를 탄다.")
#     elif button == 3:
#         print("#3. (자동으로) 블랙커피를 탄다.")
#     else:
#         print("#3. (자동으로) 아무거나 탄다.\n")

#     print("#4. (자동으로) 물을 붓는다.")
#     print("#5. (자동으로) 스푼으로 젓는다.")
#     print()


# cofee = int(input("어떤 커피 드릴까요? (1:보통, 2:설탕, 3:블랙)"))
# coffee_machine(cofee)
# print("손님~ 커피 여기 있습니다.")


# cofee = 0


# def coffee_machine(button):
#     print()
#     print("#1. (자동으로) 뜨거운 물을 준비한다.")
#     print("#2. (자동으로) 종이컵을 준비한다.")

#     if button == 1:
#         print("#3. (자동으로) 보통커피를 탄다.")
#     elif button == 2:
#         print("#3. (자동으로) 설탕커피를 탄다.")
#     elif button == 3:
#         print("#3. (자동으로) 블랙커피를 탄다.")
#     else:
#         print("#3. (자동으로) 아무거나 탄다.\n")

#     print("#4. (자동으로) 물을 붓는다.")
#     print("#5. (자동으로) 스푼으로 젓는다.")
#     print()


# cofee = int(input("A손님, 어떤 커피 드릴까요? (1:보통, 2:설탕, 3:블랙)"))
# coffee_machine(cofee)
# print("A손님~ 커피 여기 있습니다.")
# cofee = int(input("B손님, 어떤 커피 드릴까요? (1:보통, 2:설탕, 3:블랙)"))
# coffee_machine(cofee)
# print("B손님~ 커피 여기 있습니다.")
# cofee = int(input("C손님, 어떤 커피 드릴까요? (1:보통, 2:설탕, 3:블랙)"))
# coffee_machine(cofee)
# print("C손님~ 커피 여기 있습니다.")


def coffee_make(name):

    coffee = 0

    def coffee_machine(button):
        print()
        print("#1. (자동으로) 뜨거운 물을 준비한다.")
        print("#2. (자동으로) 종이컵을 준비한다.")

        if button == 1:
            print("#3. (자동으로) 아메리카노를 탄다.")
        elif button == 2:
            print("#3. (자동으로) 카페라떼를 탄다.")
        elif button == 3:
            print("#3. (자동으로) 카푸치노를 탄다.")
        elif button == 4:
            print("#3. (자동으로) 에스프레소를 탄다.")
        else:
            print("#3. (자동으로) 아무거나 탄다.\n")

        print("#4. (자동으로) 물을 붓는다.")
        print("#5. (자동으로) 스푼으로 젓는다.")
        print()

    cofee = int(
        input("%s씨, 어떤 커피 드릴까요? (1:아메리카노, 2:카페라떼, 3:카푸치노, 4:에스프레소) " % name))
    coffee_machine(cofee)
    print("%s씨~ 커피 여기 있습니다." % name)


coffee_make("로제")
coffee_make("리사")
coffee_make("지수")
coffee_make("제니")
