import sys
user_info ={}
donation_list = [['나미야 집화점의 기적', '히가시노 게이고']]

def login():
    login_input = input("0: 종료하기  1: 로그인  2: 회원가입 > ")
    if login_input == '0':
        sys.exit(0)

    elif login_input == '1':
        ID = input("ID를 입력해주세요 > ")
        PW = input("PW를 입력해주세요 > ")
        encode_ID2 = ID.encode('utf-8')
        for i in user_info: 
            if encode_ID2 == i and PW == user_info[encode_ID2]:#아이디,패스워드 일치하면
                print("로그인 되었습니다.") 
                while 1 : main_screen()

    elif login_input == '2':
        ID = input("ID를 입력해주세요 > ")
        PW = input("PW를 입력해주세요 > ")
        encode_ID = ID.encode('utf-8')#유니코드로 변환
        user_info[encode_ID] = PW #아이디, 패스워드 딕셔너리에 저장
       
    else:
        print("다시 입력하세요")

def main_screen():
    print("추천도서")
    print("'조회', '대여', '반납', '기증', '나의정보'")
    select = input("원하는 기능을 입력해주세요. > ")
    if select == '조회':
        #조회 기능 함수
        print("되나")
    elif select == '대여':
        #대여기능함수
        print("되나")
    elif select == '반납':
        #반납기능 함수
        print("되나")
    elif select == '기증':
        donation()
    elif select == '나의정보':
        #나의정보기능 함수
        print("되나")
    else:
        print("다시 입력해주세요.")

def donation():
    donat_book = input("기증한 책 정보를 입력해주세요. > ")  
while 1 :login()
