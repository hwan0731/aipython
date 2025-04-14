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


from rich import print
from rich.console import Console

console = Console()

def print_colored_ascii_art(ascii_art, color="sky_blue1"):
    """
    rich 라이브러리를 사용하여 ASCII 아트에 색상을 적용하여 출력하는 함수

    Args:
        ascii_art (str): 출력할 ASCII 아트 문자열
        color (str, optional): 적용할 색상. 기본값은 "sky_blue1".
    """
    lines = ascii_art.splitlines()
    for line in lines:
        console.print(f"[{color}]{line}[/{color}]")

def print_cat_ascii_art():
    """색상이 적용된 고양이 ASCII 아트를 출력하는 함수"""
    ascii_art = """
      /\\_/\\
     ( o.o )
      > ^ <
    """
    print_colored_ascii_art(ascii_art, color="light_coral")

def print_dog_ascii_art():
    """색상이 적용된 강아지 ASCII 아트를 출력하는 함수"""
    ascii_art = """
       / \\__
      (    @\\___
       /       O
      /  (_____/
      /_____/   U
    """
    print_colored_ascii_art(ascii_art, color="deep_sky_blue1")

def print_rabbit_ascii_art():
    """색상이 적용된 토끼 ASCII 아트를 출력하는 함수"""
    ascii_art = """
        (\\(\\
       (='.')
      (\")_(\")
    """
    print_colored_ascii_art(ascii_art, color="light_green")

def display_menu():
    """메뉴를 표시하는 함수"""
    console.print("\n[bold]그림 출력 프로그램[/bold]")
    console.print("[bold]=====================[/bold]")
    console.print("1. 고양이")
    console.print("2. 강아지")
    console.print("3. 토끼")
    console.print("0. 종료")

def get_user_choice():
    """사용자 입력을 받아 정수로 변환하는 함수"""
    try:
        return int(input("선택: "))
    except ValueError:
        console.print("[red]숫자를 입력해주세요.[/red]")
        return -1  # 잘못된 입력의 경우 -1 반환

def process_choice(choice):
    """사용자 선택에 따라 적절한 동작을 수행하는 함수"""
    if choice == 0:
        console.print("프로그램을 종료합니다.")
        return False  # 프로그램 종료를 위해 False 반환
    elif choice == 1:
        console.print("[bold]고양이 그림[/bold]")
        print_cat_ascii_art()
    elif choice == 2:
        console.print("[bold]강아지 그림[/bold]")
        print_dog_ascii_art()
    elif choice == 3:
        console.print("[bold]토끼 그림[/bold]")
        print_rabbit_ascii_art()
    elif choice == -1:
        # 잘못된 입력은 이미 get_user_choice에서 메시지 출력했으므로 아무것도 하지 않음
        pass
    else:
        console.print("[red]1, 2, 3, 0 중에서 입력해주세요.[/red]")

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

    from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.color import Color
from rich.style import Style
import random

console = Console()

def random_color():
    """랜덤 컬러 코드를 반환하는 함수"""
    colors = ["red", "green", "blue", "magenta", "cyan", "yellow", "purple", "orange", "pink", 
              "spring_green1", "deep_sky_blue1", "light_coral", "medium_purple1", "gold1"]
    return random.choice(colors)

def rainbow_text(text, style=""):
    """텍스트의 각 문자에 무지개 색상을 적용하는 함수"""
    rainbow_colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    result = ""
    for i, char in enumerate(text):
        if char.strip():  # 공백이 아닌 경우에만 색상 적용
            color = rainbow_colors[i % len(rainbow_colors)]
            result += f"[{color}]{char}[/{color}]"
        else:
            result += char
    
    if style:
        return f"[{style}]{result}[/{style}]"
    return result

def gradient_color(text, start_color, end_color, style=""):
    """텍스트에 그라데이션 색상을 적용하는 함수"""
    # 텍스트 각 문자에 그라데이션 효과를 적용
    result = Text()
    for i, char in enumerate(text):
        progress = i / (len(text) - 1) if len(text) > 1 else 0
        # 두 색상 사이의 중간 색상 계산
        color = Color.from_rgb(
            int(start_color[0] + (end_color[0] - start_color[0]) * progress),
            int(start_color[1] + (end_color[1] - start_color[1]) * progress),
            int(start_color[2] + (end_color[2] - start_color[2]) * progress)
        )
        result.append(char, Style(color=color))
    
    return result

def print_cat_ascii_art(style_mode="normal"):
    """고양이 ASCII 아트를 출력하는 함수"""
    if style_mode == "normal":
        print(Panel.fit("""
  /\\_/\\ 
 ( o.o )
 > ^ <  
""", title="[bold]고양이[/bold]", border_style="cyan"))
    
    elif style_mode == "rainbow":
        print(Panel.fit(f"""
  {rainbow_text("/\\_/\\")}
 {rainbow_text("( o.o )")}
 {rainbow_text("> ^ <")}
""", title=rainbow_text("고양이", "bold"), border_style="magenta"))
    
    elif style_mode == "gradient":
        # 파란색에서 핑크색으로 그라데이션
        blue = (30, 144, 255)  # 파란색 RGB
        pink = (255, 105, 180)  # 핑크색 RGB
        
        cat_lines = [
            "  /\\_/\\ ",
            " ( o.o )",
            " > ^ <  "
        ]
        
        panel_content = "\n"
        for line in cat_lines:
            panel_content += str(gradient_color(line, blue, pink)) + "\n"
        
        console.print(Panel(panel_content, title="[bold]고양이[/bold]", border_style="bright_blue"))
    
    elif style_mode == "random":
        c1, c2, c3 = random_color(), random_color(), random_color()
        print(f"""
  [{c1}]/\\_/\\[/{c1}]
 [{c2}]( o.o )[/{c2}]
 [{c3}]> ^ <[/{c3}]
""")

def print_dog_ascii_art(style_mode="normal"):
    """강아지 ASCII 아트를 출력하는 함수"""
    if style_mode == "normal":
        print(Panel.fit("""
   / \\__  
  (    @\\___
   /       O
  /  (_____/
  /_____/   U
""", title="[bold]강아지[/bold]", border_style="green"))
    
    elif style_mode == "rainbow":
        print(Panel.fit(f"""
   {rainbow_text("/ \\__")}  
  {rainbow_text("(    @\\___")}
   {rainbow_text("/       O")}
  {rainbow_text("/  (_____/")}
  {rainbow_text("/_____/   U")}
""", title=rainbow_text("강아지", "bold"), border_style="yellow"))
    
    elif style_mode == "gradient":
        # 초록색에서 노란색으로 그라데이션
        green = (34, 139, 34)  # 초록색 RGB
        yellow = (255, 215, 0)  # 노란색 RGB
        
        dog_lines = [
            "   / \\__  ",
            "  (    @\\___",
            "   /       O",
            "  /  (_____/",
            "  /_____/   U"
        ]
        
        panel_content = "\n"
        for line in dog_lines:
            panel_content += str(gradient_color(line, green, yellow)) + "\n"
        
        console.print(Panel(panel_content, title="[bold]강아지[/bold]", border_style="bright_green"))
    
    elif style_mode == "random":
        c1, c2, c3, c4, c5 = [random_color() for _ in range(5)]
        print(f"""
   [{c1}]/ \\__[/{c1}]  
  [{c2}](    @\\___[/{c2}]
   [{c3}]/       O[/{c3}]
  [{c4}]/  (_____/[/{c4}]
  [{c5}]/_____/   U[/{c5}]
""")

def print_rabbit_ascii_art(style_mode="normal"):
    """토끼 ASCII 아트를 출력하는 함수"""
    if style_mode == "normal":
        print(Panel.fit("""
   (\\(\\
  (='.') 
  (\")_(")
""", title="[bold]토끼[/bold]", border_style="magenta"))
    
    elif style_mode == "rainbow":
        print(Panel.fit(f"""
   {rainbow_text("(\\(\\")}
  {rainbow_text("(='.')")}
  {rainbow_text("(\")_(\"")}
""", title=rainbow_text("토끼", "bold"), border_style="purple"))
    
    elif style_mode == "gradient":
        # 보라색에서 분홍색으로 그라데이션
        purple = (128, 0, 128)  # 보라색 RGB
        pink = (255, 182, 193)  # 분홍색 RGB
        
        rabbit_lines = [
            "   (\\(\\",
            "  (='.') ",
            "  (\")_(\""
        ]
        
        panel_content = "\n"
        for line in rabbit_lines:
            panel_content += str(gradient_color(line, purple, pink)) + "\n"
        
        console.print(Panel(panel_content, title="[bold]토끼[/bold]", border_style="bright_magenta"))
    
    elif style_mode == "random":
        c1, c2, c3 = random_color(), random_color(), random_color()
        print(f"""
   [{c1}](\\(\\[/{c1}]
  [{c2}](='.')[/{c2}]
  [{c3}](\")_(\")[/{c3}]
""")

def print_animated_ascii(animal):
    """간단한 애니메이션 효과로 아스키 아트를 출력"""
    import time
    styles = ["normal", "rainbow", "gradient", "random"]
    
    for style in styles:
        console.clear()
        if animal == "cat":
            print_cat_ascii_art(style)
        elif animal == "dog":
            print_dog_ascii_art(style)
        elif animal == "rabbit":
            print_rabbit_ascii_art(style)
        time.sleep(0.7)  # 각 스타일 간 딜레이

def main():
    count = 0
    style_options = ["normal", "rainbow", "gradient", "random", "animated"]
    
    # 5번 반복하기 위한 반복문
    while count < 5:
        console.clear()
        print(f"\n[bold cyan]실행 {count + 1}/5[/bold cyan]")
        print(rainbow_text("아스키 아트 출력 프로그램", "bold"))
        print("[bold]" + "=" * 30 + "[/bold]")
        print("[bright_yellow]1.[/bright_yellow] 고양이")
        print("[bright_yellow]2.[/bright_yellow] 강아지")
        print("[bright_yellow]3.[/bright_yellow] 토끼")
        print("[bold]" + "-" * 30 + "[/bold]")
        
        # 스타일 선택 메뉴 추가
        print(rainbow_text("스타일 선택", "bold"))
        for i, style in enumerate(style_options):
            print(f"[bright_blue]{i+1}.[/bright_blue] {style}")
        
        try:
            animal = int(input("[bright_green]동물 선택 (1-3): [/bright_green]"))
            style_num = int(input("[bright_green]스타일 선택 (1-5): [/bright_green]"))
            
            # 스타일 유효성 검사
            if not (1 <= style_num <= len(style_options)):
                print("[red]유효하지 않은 스타일 번호입니다.[/red]")
                continue
            
            style = style_options[style_num-1]
            
            if not (1 <= animal <= 3):
                print("[red]1, 2, 3 중에서 선택해주세요.[/red]")
                continue
            
            console.clear()
            
            if style == "animated":
                if animal == 1:
                    print_animated_ascii("cat")
                elif animal == 2:
                    print_animated_ascii("dog")
                elif animal == 3:
                    print_animated_ascii("rabbit")
            else:
                if animal == 1: 
                    print("[bold]고양이 그림[/bold]")
                    print_cat_ascii_art(style)
                elif animal == 2: 
                    print("[bold]강아지 그림[/bold]")
                    print_dog_ascii_art(style)
                elif animal == 3:
                    print("[bold]토끼 그림[/bold]")
                    print_rabbit_ascii_art(style)
            
            input("\n[italic]계속하려면 Enter 키를 누르세요...[/italic]")
            
        except ValueError:
            print("[red]숫자를 입력해주세요.[/red]")
            input("\n[italic]계속하려면 Enter 키를 누르세요...[/italic]")
            continue
        
        count += 1

    print("\n" + rainbow_text("프로그램을 종료합니다. 감사합니다!", "bold"))

if __name__ == "__main__":
    main()

