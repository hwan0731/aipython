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

     def calculate(num1, num2, operator):
    """두 숫자와 연산자를 입력받아 결과를 반환하는 함수"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "0으로 나눌 수 없습니다."
        return num1 / num2
    else:
        return "지원하지 않는 연산자입니다."

result = calculate(10, 5, '+')
print(result)  # 출력: 15

result = calculate(10, 5, '/')
print(result)  # 출력: 2.0

result = calculate(10, 0, '/')
print(result)  # 출력: 0으로 나눌 수 없습니다.   

# ASCII 아트를 출력하는 함수들
def print_cat_ascii_art():
    """고양이 ASCII 아트를 출력하는 함수"""
    print("""
    /\\_/\\
   ( o.o )
    > ^ <
    """)

def print_dog_ascii_art():
    """강아지 ASCII 아트를 출력하는 함수"""
    print("""
     / \\__
    (    @\\___
     /         O
    /   (_____/
    /_____/   U
    """)

def print_rabbit_ascii_art():
    """토끼 ASCII 아트를 출력하는 함수"""
    print("""
     (\\(\\ 
    (=':')
    (")_(")
    """)

def display_menu():
    """메뉴를 표시하는 함수"""
    print("\n그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("0. 종료")

def get_user_choice():
    """사용자 입력을 받아 정수로 변환하는 함수"""
    try:
        return int(input("선택: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        return -1  # 잘못된 입력의 경우 -1 반환

def process_choice(choice):
    """사용자 선택에 따라 적절한 동작을 수행하는 함수"""
    if choice == 0:
        print("프로그램을 종료합니다.")
        return False  # 프로그램 종료를 위해 False 반환
    elif choice == 1:
        print("고양이 그림")
        print_cat_ascii_art()
    elif choice == 2:
        print("강아지 그림")
        print_dog_ascii_art()
    elif choice == 3:
        print("토끼 그림")
        print_rabbit_ascii_art()
    elif choice == -1:
        # 잘못된 입력은 이미 get_user_choice에서 메시지 출력했으므로 아무것도 하지 않음
        pass
    else:
        print("1, 2, 3, 0 중에서 입력해주세요.")
    
    return True  # 계속 실행을 위해 True 반환

def main():
    """메인 함수: 프로그램의 주요 로직을 담당"""
    running = True
    
    while running:
        display_menu()
        choice = get_user_choice()
        running = process_choice(choice)

# 프로그램 실행
if __name__ == "__main__":
    main()


# ASCII 아트를 출력하는 함수들
def print_cat_ascii_art():
    """고양이 ASCII 아트를 출력하는 함수"""
    print(r"""
    /\_/\
   ( o.o )
    > ^ <
    """)

def print_dog_ascii_art():
    """강아지 ASCII 아트를 출력하는 함수"""
    print(r"""
     / \__
    (    @\___
     /         O
    /   (_____/
    /_____/   U
    """)

def print_rabbit_ascii_art():
    """토끼 ASCII 아트를 출력하는 함수"""
    print(r"""
     (\\(\ 
    (=':')
    (")_(")
    """)

def display_menu():
    """메뉴를 표시하는 함수"""
    print("\n그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("0. 종료")

def get_user_choice():
    """사용자 입력을 받아 정수로 변환하는 함수"""
    try:
        return int(input("선택: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        return -1  # 잘못된 입력의 경우 -1 반환

def process_choice(choice):
    """사용자 선택에 따라 적절한 동작을 수행하는 함수"""
    if choice == 0:
        print("프로그램을 종료합니다.")
        return False  # 프로그램 종료를 위해 False 반환
    elif choice == 1:
        print("고양이 그림")
        print_cat_ascii_art()
    elif choice == 2:
        print("강아지 그림")
        print_dog_ascii_art()
    elif choice == 3:
        print("토끼 그림")
        print_rabbit_ascii_art()
    elif choice == -1:
        # 잘못된 입력은 이미 get_user_choice에서 메시지 출력했으므로 아무것도 하지 않음
        pass
    else:
        print("1, 2, 3, 0 중에서 입력해주세요.")
    
    return True  # 계속 실행을 위해 True 반환

def main():
    """메인 함수: 프로그램의 주요 로직을 담당"""
    running = True
    
    while running:
        display_menu()
        choice = get_user_choice()
        running = process_choice(choice)

# 프로그램 실행
if __name__ == "__main__":
    main()


# ASCII 아트를 출력하는 함수들
def print_cat_ascii_art():
    """고양이 ASCII 아트를 출력하는 함수"""
    print(r"""
    /\_/\
   ( o.o )
    > ^ <
    """)

def print_dog_ascii_art():
    """강아지 ASCII 아트를 출력하는 함수"""
    print(r"""
     / \__
    (    @\___
     /         O
    /   (_____/
    /_____/   U
    """)

def print_rabbit_ascii_art():
    """토끼 ASCII 아트를 출력하는 함수"""
    print(r"""
     (\\(\ 
    (=':')
    (")_(")
    """)

def display_menu():
    """메뉴를 표시하는 함수"""
    print("\n그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("0. 종료")

def get_user_choice():
    """사용자 입력을 받아 정수로 변환하는 함수"""
    try:
        return int(input("선택: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        return -1  # 잘못된 입력의 경우 -1 반환

def process_choice(choice):
    """사용자 선택에 따라 적절한 동작을 수행하는 함수"""
    if choice == 0:
        print("프로그램을 종료합니다.")
        return False  # 프로그램 종료를 위해 False 반환
    elif choice == 1:
        print("고양이 그림")
        print_cat_ascii_art()
    elif choice == 2:
        print("강아지 그림")
        print_dog_ascii_art()
    elif choice == 3:
        print("토끼 그림")
        print_rabbit_ascii_art()
    elif choice == -1:
        # 잘못된 입력은 이미 get_user_choice에서 메시지 출력했으므로 아무것도 하지 않음
        pass
    else:
        print("1, 2, 3, 0 중에서 입력해주세요.")
    
    return True  # 계속 실행을 위해 True 반환

def main():
    """메인 함수: 프로그램의 주요 로직을 담당"""
    running = True
    
    while running:
        display_menu()
        choice = get_user_choice()
        running = process_choice(choice)

# 프로그램 실행
if __name__ == "__main__":
    main()
