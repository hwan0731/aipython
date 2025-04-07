def print_cat_ascii_art():
    print("""
       /\_/\  
      ( o.o ) 
      > ^ <
    """)

def print_dog_ascii_art():
    print("""
      / \\__
     (    @\\___
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
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    n = int(input("선택: "))

    if n == 1: 
        print("고양이 그림")
        print_cat_ascii_art()
    elif n == 2: 
        print("강아지 그림")
        print_dog_ascii_art()
    elif n == 3:
        print("토끼 그림")
        print_rabbit_ascii_art()
    else: 
        print("잘못 입력했습니다. 1, 2, 3 중 하나를 입력하세요.")

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

def print_cat_ascii_art():
    """고양이 ASCII 아트를 출력하는 함수"""
    print('''
  /\_/\\
 ( o.o )
  > ^ <
    ''')

def print_dog_ascii_art():
    """강아지 ASCII 아트를 출력하는 함수"""
    print('''
  / \__
 (    @\___
 /         O
/   (_____/
/_____/   U
    ''')

def print_rabbit_ascii_art():
    """토끼 ASCII 아트를 출력하는 함수"""
    print('''
  (\\(\\ 
  (-.-)
  o_(")(")
    ''')

def main():
    count = 0
    
    # 5번 반복하기 위한 반복문
    while count < 5:
        print(f"\n실행 {count + 1}/5")
        print("그림 출력 프로그램")
        print("=====================")
        print("1. 고양이")
        print("2. 강아지")
        print("3. 토끼")
        try:
            n = int(input("선택: "))

            if n == 1: 
                print("고양이 그림")
                print_cat_ascii_art()
            elif n == 2: 
                print("강아지 그림")
                print_dog_ascii_art()
            elif n == 3:
                print("토끼 그림")
                print_rabbit_ascii_art()
            else:
                print("1, 2, 3 중에서 선택해주세요.")
                continue  # 잘못된 입력이면 카운트 증가 없이 다시 시작
        except ValueError:
            print("숫자를 입력해주세요.")
            continue  # 숫자가 아닌 입력이면 카운트 증가 없이 다시 시작
        
        count += 1  # 성공적으로 실행 후 카운트 증가

    print("\n프로그램을 종료합니다.")

if __name__ == "__main__":
    main()

def print_cat_ascii_art():
    print("""
    /\\_/\\
   ( o.o )
    > ^ <
    """)

def print_dog_ascii_art():
    print("""
     / \\__
    (    @\\___
     /         O
    /   (_____/
    /_____/   U
    """)

def print_rabbit_ascii_art():
    print("""
     (\\(\\
    (='.') 
    (")_(")
    """)

def main():
    while True: # 무한 반복 (계속 참)
        print("\n그림 출력 프로그램")
        print("=====================")
        print("1. 고양이")
        print("2. 강아지")
        print("3. 토끼")
        print("0. 종료")
        
        try:
            n = int(input("선택(0을 입력하면 종료): "))
            # 0 이 입력되면 프로그램 종료 
            if n == 0:
                print("프로그램을 종료합니다.")
                break
            elif n == 1: 
                print("고양이 그림")
                print_cat_ascii_art()
            elif n == 2: 
                print("강아지 그림")
                print_dog_ascii_art()
            elif n == 3:
                print("토끼 그림")
                print_rabbit_ascii_art()
            else:
                print("잘못된 선택입니다. 0-3 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")

if __name__ == "__main__":
        main()

