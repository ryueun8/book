import sys
import random
import os
import time
import sqlite3

conn = sqlite3.connect ('book.db')
cur = conn.cursor()

save_book = []
book_cnt = 0  
result=[] #검색결과 저장
basket=[] #장바구니에 저장
user_info =[]
plus=0
donation_list = [['앨리스 죽이기', '코바야시 야스미'], ['거울나라의 앨리스', '루이스 캐럴'], ['앨리스 지금이야', '김종원']]
#배열 마지막, 1:대여가능 2:대여중
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

    elif login_input == '1':    #로그인
        print("ID,PW를 잊어버리셨으면 '분실'을 입력해주세요.")
        ID = input("ID를 입력해주세요 > ")
        PW = input("PW를 입력해주세요 > ")
        if ID == '분실' or PW == '분실':
            print("\n아이디, 패스워드 찾기")
            lose = input("전화번호를 입력해주세요. > ")
            for i in range(len(user_info)):
                if lose == user_info[i][3]:
                    print("{0}님의 ID와 PW는 {1}, {2}입니다".format(user_info[i][2], user_info[i][0], user_info[i][1]))
        
        for i in range(5): 
            if ID == user_info[i][0] and PW == user_info[i][1]:#아이디,패스워드 일치하면
                print("로그인 되었습니다.")
                time.sleep(0.5)
                os.system('clear') 
                while 1 : main_screen()
            else:
                break

        if ID == '분실' or PW == '분실':
            print("\n아이디, 패스워드 찾기")
            lose = input("전화번호를 입력해주세요. > ")
            for i in range(len(user_info)):
                if lose == user_info[i][3]:
                    print("{0}님의 ID와 PW는 {1}, {2}입니다".format(user_info[i][2], user_info[i][0], user_info[i][1]))

    elif login_input == '2':        #회원가입
        
        name = input("이름을 입력해주세요. > ")
        phone = input("전화번호를 입력해주세요. > ")
        ID = input("ID를 입력해주세요 > ")
        PW = input("PW를 입력해주세요 > ")
        # cur.execute('insert into userInfo values (?, ?, ?, ?)', (name, phone, ID, PW))
        # conn.commit()
        a = information()
        a.user_plus(ID, PW, name, phone)

    else:
        print("다시 입력하세요")

def donation():  #기증
    while 1:
        global donation_list
        donate_check =0
        donate_book = input("기증할 책 이름을 입력해주세요. > ")

        for i in range(len(donation_list)):
            if donation_list[i][0] == donate_book:
                print("{0} 기증했습니다.".format(donation_list[i][0]))
                donate_check += 1    
                last_num = BookList[-1][0]
                last_num += 1
                BookList.append(donation_list[i])
                BookList[-1].insert(0, last_num)    
                BookList[-1].append('1')
                del donation_list[i] #기증한 책 도네이션 리스트에서 삭제
                print("책리스트 확인")
                print(BookList)
                print("끝")
                break

        if donate_check == 0:
            print("다시입력해주세요.")  
            continue
        elif donate_check > 0:
            break

def rental(): #대여 함수
    global book_cnt                      
    print(basket)
    user_input = str(input('대여하시겠습니까? y/n  > '))
    if user_input == 'y' or user_input == 'Y':
        for i in range(0, len(BookList)):
            for j in range(0, len(basket)):  
                if basket[j] == BookList[i][1]:
                    print(basket[j])
                    BookList[i][3] = 0
                    for k in range(len(BookList)):
                        if BookList[k][3] == 0:
                            book_cnt += 1
                    if book_cnt > 3:
                        print(book_cnt)
                        print("3권 이상 대여할 수 없습니다.")
                        BookList[i][1] == 1
                    else:
                        print("대여완료")
                        del basket[:] 
        print(BookList)  

    elif user_input == 'n' or user_input == 'N':
        print('메인으로 돌아갑니다')
        return None


def SearchBookName(user_input):                      #책명 조회 함수
    arg ='%' + user_input +'%'
    cur.execute("SELECT Num, Title, Author FROM book WHERE Rental=1 and Title like ?", (arg, ))
    row=cur.fetchall()
    for i in row:
        result.append(i)
            # elif BookList[i][3] == 0:
            #     print(BookList[i][1], end="")
            #     print(" 대여중")
    ShoppingBasket()

def SearchBookAuthor(user_input):  #저자 조회 함수
    arg ='%' + user_input +'%'
    cur.execute("SELECT Num, Title, Author FROM book WHERE Rental=1 and Title like ?", (arg, ))
    row=cur.fetchall()
    for i in row:
        result.append(i)
            # if BookList[i][3] == 1:
                # result.append(BookList[i][1])
                #print(result) #테스트12
                # ShoppingBasket()
            # elif BookList[i][3] == 0:
                # print(BookList[i][1], end="")
                # print(" 대여중")
    ShoppingBasket()

def ShoppingBasket():                                #장바구니 추가 함수
    print(result)
    while 1:
        user_input = int(input('장바구니에 추가할 책의 번호를 입력해주세요 '))
        for i in range(0, len(result)):
            if user_input == result[i][0]:
                basket.append(result[i])
                os.system('clear')
                print(basket, end="")
                print('장바구니에 담았습니다')
                time.sleep(2)
                del result[:]
                break
            else:
                print("잘못 입력하셨습니다.")
        break


def menu():                                             #조회 함수
        print('1. 제목')
        print('2. 작가')
        user_input = input('선택: ') 
        if user_input == '1':
            user_input = input('제목: ')
            SearchBookName(user_input)
        elif user_input == '2':
            user_input = input('작가: ')
            SearchBookAuthor(user_input)
        else:
            print("잘못 입력하셨습나다.")

def book_return():
    global save_book
    return_choice = input("1. 책제목  2. 도서 고유번호  > ")
    if return_choice == '1':
        re_book = input("반납할 책의 제목을 입력해주세요. > ")
        for i in range(len(BookList)):
            if re_book == BookList[i][1]:
                if BookList[i][3] == 0: #대여중인 책일때
                    print("반납되었습니다.")
                    save_book.append(BookList[i][1])
                    BookList[i][3] = 1 
                else:
                    print("대여중인 책이 아닙니다.")
                    break    

    if return_choice == '2':
        re_book_num = int(input("반납할 책의 고유번호를 입력해주세요. > "))
        for i in range(len(BookList)):
            if re_book_num == BookList[i][0]:
                if BookList[i][3] == 0:
                    print("반납되었습니다.")
                    save_book.append(BookList[i][1])
                    BookList[i][3] = 1 
                else:
                    print("대여중인 책이 아닙니다.")
                    break 

def mine_info():
    global save_book
    print("=======나의정보=======")
    print("대여중인 도서 리스트")
    for i in range(len(BookList)):
        if BookList[i][3] == 0:
            print("-{0}".format(BookList[i][1]))
    print("")
    print("대여 후 반납한 도서 리스트")
    print("-{0}\n".format(save_book))
    print("연체 조회 정보")
    print("연체된 책이 없습니다.")
    print("")
    user_input = input("정보 변경을 원하시나요? (y/n) >")
    if user_input == 'y':
        ID = input("ID를 입력해주세요. > ")
        for i in range(len(user_info)):
            if ID == user_info[i][0]:
                change = input("비밀번호를 변경하시겠습니까. (y/n) > ")
                if change == 'y':
                    change_PW = input("변결할 PW > ")
                    user_info[i][1] = change_PW
                    print(user_info)
                elif change == 'n':
                    pass

    elif user_input == 'n':
        pass
    print("======================")

def main_screen():
    i=random.randint(0,2)
    j=random.randint(3,5)

    print(" ")
    print("------추천도서------ ")
    print("{0:^14}".format(BookList[i][1]))
    print("{0:^14}".format(BookList[j][1]))
    print("--------------------")
    print(" ")

    print("'조회', '대여', '반납', '기증', '나의정보'")
    select = input("원하는 기능을 입력해주세요. > ")
    if select == '조회':
        menu()
    elif select == '대여':
        rental()
    elif select == '반납':
        book_return()
    elif select == '기증':
        donation()
    elif select == '나의정보':
        mine_info()
    else:
        print("다시 입력해주세요.")

while 1 :login()