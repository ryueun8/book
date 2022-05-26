import sys

result=[] #검색결과 저장
basket=[] #장바구니에 저장
user_info =[]
plus=0
donation_list = [['나미야 집화점의 기적', '히가시노 게이고'], ['작별인사', '김영하'], ['불편한 편의점', '김호연']]
BookList=[[1, '작별인사', '김영하', 1],
          [2, '이기적 유전자', '리처드 도킨스', 1],
          [3, '게놈 익스프레스', '조진호', 1],
          [4, '데미안', '헤르만 헤세', 1],
          [5, '언어의 온도', '이기주', 1],
          [6, '나미야 잡화점의 기적', '히가시노 게이고', 1],
          [7, '인간 실격', '다자이 오사무', 1]]

class information:
    global user_info
    def user_plus(self, ID, PW, name, phone):        
        global plus
        user_info.append([])
        user_info[plus].append(ID)
        user_info[plus].append(PW)
        user_info[plus].append(name)
        user_info[plus].append(phone)
        plus += 1
        print(user_info)


def login():
    login_input = input("0: 종료하기  1: 로그인  2: 회원가입 > ")
    if login_input == '0':
        sys.exit(0)

    elif login_input == '1':#로그인
        print("ID,PW를 잊어버리셨으면 '분실'을 입력해주세요.")
        ID = input("ID를 입력해주세요 > ")
        PW = input("PW를 입력해주세요 > ")
        if ID == '분실' or PW == '분실':
            print("\n아이디, 패스워드 찾기")
            lose = input("전화번호를 입력해주세요. > ")
            for i in range(len(user_info)):
                if lose == user_info[i][3]:
                    print("{0}님의 ID와 PW는 {1}, {2}입니다".format(user_info[i][2], user_info[i][0], user_info[i][1]))

        #encode_ID2 = ID.encode('utf-8')
        
        for i in range(5): 
            if ID == user_info[i][0] and PW == user_info[i][1]:#아이디,패스워드 일치하면
                print("로그인 되었습니다.") 
                while 1 : main_screen()
            else:
                break

        if ID == '분실' or PW == '분실':
            print("\n아이디, 패스워드 찾기")
            lose = input("전화번호를 입력해주세요. > ")
            for i in range(len(user_info)):
                if lose == user_info[i][3]:
                    print("{0}님의 ID와 PW는 {1}, {2}입니다".format(user_info[i][2], user_info[i][0], user_info[i][1]))

    elif login_input == '2':#회원가입
        
        name = input("이름을 입력해주세요. > ")
        phone = input("전화번호를 입력해주세요. > ")
        ID = input("ID를 입력해주세요 > ")
        PW = input("PW를 입력해주세요 > ")
        #encode_ID = ID.encode('utf-8')#유니코드로 변환
        a = information()
        a.user_plus(ID, PW, name, phone)

    else:
        print("다시 입력하세요")

def donation():
    while 1:
        global donation_list
        donate_check =0
        donate_book = input("기증할 책 이름을 입력해주세요. > ")  
        for i in range(3):
            if donation_list[i][0] == donate_book:
                print("{0} 기증했습니다.".format(donation_list[i][0]))
                donate_check += 1
                break
        if donate_check == 0:
            print("다시입력해주세요.")  
            continue
        elif donate_check > 0:
            break

def rental():                                #대여 함수
    print(basket)
    user_input = str(input('대여하시겠습니까? y/n'))
    if user_input == 'y' or user_input == 'Y':
        for i in range(0, len(BookList)):
            for j in range(0, len(basket)):
                if basket[j] == BookList[i][1]:
                    print(basket[j])
                    BookList[i][3] = 0
                    print("대여완료")
                    del basket[:]
    elif user_input == 'n' or user_input == 'N':
        print('메인으로 돌아갑니다')
        return None


def SearchBookName(user_input):                      #책명 조회 함수
    for i in range(0, len(BookList)):
        if user_input in BookList[i][1]:
            if BookList[i][3] == 1:
                result.append(BookList[i][1])
                # print(result) #테스트
                ShoppingBasket()
            elif BookList[i][3] == 0:
                print(BookList[i][1], end="")
                print(" 대여중")


def SearchBookAuthor(user_input):                      #저자 조회 함수
    for i in range(0, len(BookList)):
        if user_input in BookList[i][2]:
            if BookList[i][3] == 1:
                result.append(BookList[i][1])
                # print(result) #테스트
                ShoppingBasket()
            elif BookList[i][3] == 0:
                print(BookList[i][1], end="")
                print(" 대여중")


def ShoppingBasket():                                #장바구니 추가 함수
    print(result)
    user_input = input('장바구니에 추가하시겠습니까? y/n ')
    if user_input == 'y' or user_input == 'Y':
        basket.append(result[0])
        print(basket)  # 테스트
        del result[:]


def menu():                                             #조회 함수
        print('1. 제목')
        print('2. 작가')
        user_input = int(input('선택: '))
        if user_input == 1:
            user_input = input('제목: ')
            SearchBookName(user_input)
        elif user_input == 2:
            user_input = input('작가: ')
            SearchBookAuthor(user_input)

def book_return():
    print("책이 일괄 반납됩니다.")
    for i in range(0, len(BookList)):
        BookList[i][3] = 1

def main_screen():
    print("추천도서 : ")
    print("'조회', '대여', '반납', '기증', '나의정보'")
    select = input("원하는 기능을 입력해주세요. > ")
    if select == '조회':
        menu()
    elif select == '대여':
        rental()
    elif select == '반납':
        book_return()
        #반납기능 함수
    elif select == '기증':
        donation()
    elif select == '나의정보':
        #나의정보기능 함수
        print("되나")
    else:
        print("다시 입력해주세요.")

while 1 :login()
