#아스키 코드 그림 출력 하기

print("그림 출력 프로그램")
print("=====================")
print("1. 고양이")
print("2. 강아지")
print("3. 토끼")
print("선택: ")
n = int(input("선택))"))
# 만약에 1을 입력하면 1번 캐릭터 출력 
if n == 1: 
    print("고양이 그림")
# 만약에 2를 입력하면 2반 캐릭터 출력 
elif n == 2: 
    print("강아지")
# 3을 입력하면 3번 캐릭터 출력 
elif n == 3:
    print("토끼")
# 잘못입력하면 잘못 입력했다고 출력
else: 
    print("잘못입력")

def print_cat_ascii_art():
    print("""
       /\_/\  
      ( o.o ) 
      > ^ <
    """)

def print_dog_ascii_art():
    print("""
      / __
     (    @___
     /         O
    /   (_____/
/_____/ U
    """)

def print_rabbit_ascii_art():
    print("""
     (\(\ 
     (-.-)
    o_(")(")
    """)

def main():
    print("고양이 아스키 아트:")
    print_cat_ascii_art()

    print("강아지 아스키 아트:")
    print_dog_ascii_art()
    
    print("토끼 아스키 아트:")
    print_rabbit_ascii_art()

if __name__ == "__main__":
    main()





def print_ascii_art(choice):
    if choice == 1:
        print("""
          1번 캐릭터
          O
         /|\\
         / \\
        """)
    elif choice == 2:
        print("""
          2번 캐릭터
          O
         /|\\
         / \\
        """)
    elif choice == 3:
        print("""
          3번 캐릭터
          O
         /|\\
         / \\
        """)
    else:
        print("잘못 입력했습니다. 1, 2, 3 중 하나를 입력하세요.")

def main():
    try:
        user_input = int(input("숫자를 입력하세요 (1, 2, 3): "))
        print_ascii_art(user_input)
    except ValueError:
        print("숫자를 입력해야 합니다. 1, 2, 3 중 하나를 입력하세요.")

if __name__ == "__main__":
    main()
