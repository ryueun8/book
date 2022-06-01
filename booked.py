import sys
import random
import os
import time
import sqlite3
import datetime
from datetime import date

conn = sqlite3.connect('book.db')
cur = conn.cursor()

# save_book = []
# book_cnt = 0
result = []  # 검색결과 저장
basket = []  # 장바구니에 저장
# user_info =[]
# plus=0
userID = ''


# donation_list = [['앨리스 죽이기', '코바야시 야스미'], ['거울나라의 앨리스', '루이스 캐럴'], ['앨리스 지금이야', '김종원']]
# #배열 마지막, 1:대여가능 2:대여중
# BookList=[[1, '작별인사', '김영하', 1],
#           [2, '이기적 유전자', '리처드 도킨스', 1],
#           [3, '게놈 익스프레스', '조진호', 1],
#           [4, '데미안', '헤르만 헤세', 1],
#           [5, '언어의 온도', '이기주', 1],
#           [6, '나미야 잡화점의 기적', '히가시노 게이고', 1],
#           [7, '인간 실격', '다자이 오사무', 1]]

# class information:
#     global user_info
#     def user_plus(self, ID, PW, name, phone):
#         global plus
#         user_info.append([])
#         user_info[plus].append(ID)
#         user_info[plus].append(PW)
#         user_info[plus].append(name)
#         user_info[plus].append(phone)
#         plus += 1
#         print(user_info)


def login():
    global userID
    cur.execute("SELECT * FROM userInfo")
    user_info = cur.fetchall()

    login_input = input("0: 종료하기  1: 로그인  2: 회원가입 > ")
    if login_input == '0':
        sys.exit(0)

    elif login_input == '1':  # 로그인
        print("ID,PW를 잊어버리셨으면 '분실'을 입력해주세요.")
        ID = input("ID를 입력해주세요 > ")

        if ID == '분실':
            print("\n아이디, 패스워드 찾기")
            lose = int(input("전화번호를 입력해주세요. > "))
            for search in user_info:
                if lose == search[3]:
                    print("{0}님의 ID와 PW는 {1}, {2}입니다".format(search[0], search[2], search[3]))
                    return
                else:
                    print("일치하는 회원정보가 없습니다.\n")
                    return

        PW = input("PW를 입력해주세요 > ")

        if PW == '분실':
            print("\n아이디, 패스워드 찾기")
            lose = int(input("전화번호를 입력해주세요. > "))
            for search in user_info:
                if lose == search[3]:
                    print("{0}님의 ID와 PW는 {1}, {2}입니다".format(search[0], search[2], search[3]))
                    return
                else:
                    print("일치하는 회원정보가 없습니다.\n")
                    return

        for search in user_info:
            print(search)
            if ID == search[2] and PW == search[3]:  # 아이디,패스워드 일치하면
                userID = ID
                print("로그인 되었습니다.")
                time.sleep(0.5)
                os.system('clear')
                while 1: main_screen()
            else:
                pass

    elif login_input == '2':  # 회원가입

        name = input("이름을 입력해주세요. > ")
        phone = input("전화번호를 입력해주세요. > ")
        ID = input("ID를 입력해주세요 > ")
        PW = input("PW를 입력해주세요 > ")
        cur.execute('insert into userInfo values (?, ?, ?, ?, ?, ? ,?)', (name, phone, ID, PW, None, None, None))
        conn.commit()

    else:
        print("다시 입력하세요")


def donation():  # 기증
    cur.execute("SELECT * FROM book")
    don_book = cur.fetchall()
    while 1:
        donate_check = 0
        book_name = input("기증할 책 이름을 입력해주세요. > ")
        book_writer = input("기증할 책의 저자 이름을 입력해주세요. >")

        for search in don_book:
            if search[1] == book_name:
                if search[2] == book_writer:
                    print("{0} 기증했습니다.".format(search[1]))
                    donate_check += 1
                    last_num = don_book[-1][0]
                    print(don_book[-1][0])
                    last_num += 1
                    print(last_num)
                    cur.execute('insert into book values (?, ?, ?, ?)', (last_num, book_name, book_writer, 1))
                    conn.commit()
                    break

        if donate_check == 0:
            print("다시입력해주세요.")
            continue
        elif donate_check > 0:
            break


def rental():  # 대여 함수
    global book_cnt
    k = 1
    print(basket)
    user_input = str(input('대여하시겠습니까? y/n  > '))
    cur.execute("SELECT Num, Title, Author FROM book")
    rentDate = date.today()
    rentDate = rentDate.isoformat()  # 문자열로 변환시켜줌

    row = cur.fetchall()
    if user_input == 'y' or user_input == 'Y':
        for i in row:
            for j in basket:
                if i[0] == j[0]:
                    data = 'book' + (str(k))
                    ID_BookName_Date = str(j[0]) + '/' + j[1] + '/' + rentDate
                    print(data)
                    print(userID)
                    print(ID_BookName_Date)
                    cur.execute("update book set Rental = '0' where Num=?", (j[0],))
                    query = "update userInfo set %s = ? where userID = ?" % data
                    cur.execute(query, (ID_BookName_Date, userID))
                    conn.commit()
                    k += 1
        del basket[:]
        #         if basket[j] == BookList[i][1]:
        #             print(basket[j])
        #             BookList[i][3] = 0
        #             for k in range(len(BookList)):
        #                 if BookList[k][3] == 0:
        #                     book_cnt += 1
        #             if book_cnt > 3:
        #                 print(book_cnt)
        #                 print("3권 이상 대여할 수 없습니다.")
        #                 BookList[i][1] == 1
        #             else:
        #                 print("대여완료")
        #                 del basket[:]
        # print(BookList)

    elif user_input == 'n' or user_input == 'N':
        print('메인으로 돌아갑니다')
        return None


def SearchBookName(user_input):  # 책명 조회 함수
    arg = '%' + user_input + '%'
    cur.execute("SELECT Num, Title, Author FROM book WHERE Rental=1 and Title like ?", (arg,))
    row = cur.fetchall()
    for i in row:
        result.append(i)
        # elif BookList[i][3] == 0:
        #     print(BookList[i][1], end="")
        #     print(" 대여중")
    ShoppingBasket()


def SearchBookAuthor(user_input):  # 저자 조회 함수
    arg = '%' + user_input + '%'
    cur.execute("SELECT Num, Title, Author FROM book WHERE Rental=1 and Title like ?", (arg,))
    row = cur.fetchall()
    for i in row:
        result.append(i)
        # if BookList[i][3] == 1:
        # result.append(BookList[i][1])
        # print(result) #테스트12
        # ShoppingBasket()
        # elif BookList[i][3] == 0:
        # print(BookList[i][1], end="")
        # print(" 대여중")
    ShoppingBasket()


def ShoppingBasket():  # 장바구니 추가 함수
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


def menu():  # 조회 함수
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


def book_return():  # 반납
    global userID
    print(userID)
    return_choice = input("1. 책제목  2. 도서 고유번호  > ")
    if return_choice == '1':
        re_book = input("반납할 책의 제목을 입력해주세요. > ")
        cur.execute("SELECT book1, book2, book3 FROM userInfo where userID= ?", (userID,))
        turn_book = cur.fetchone()
        turn_book = list(turn_book)
        for i in range(1, 4):
            divide = turn_book[i - 1].split('/')
            if turn_book[i - 1] == None:
                break
            if re_book in turn_book[i - 1]:
                print("반납되었습니다.")
                print(divide)
                cur.execute("update book set Rental = ? where Num = ?", (1, divide[0]))
                conn.commit()
                query = "update userInfo set book%d = NULL where userID = ?" % i
                cur.execute(query, (userID,))
                conn.commit()
                break

            else:
                print("대여중인 책이 아닙니다.")
                break

    if return_choice == '2':
        re_book_num = input("반납할 책의 고유번호를 입력해주세요. > ")
        cur.execute("SELECT book1, book2, book3 FROM userInfo where userID= ?", (userID,))
        turn_book = cur.fetchone()
        print(turn_book)
        turn_book = list(turn_book)
        for i in range(1, 4):
            if turn_book[i - 1] == None:
                break
            if re_book_num in turn_book[i - 1]:
                print("반납되었습니다.")
                re_book_num = int(re_book_num)
                cur.execute("update book set Rental = ? where Num = ?", (1, re_book_num))
                conn.commit()
                query = "update userInfo set book%d = NULL where userID = ?" % i
                cur.execute(query, (userID,))
                conn.commit()
                break
            else:
                print("대여중인 책이 아닙니다.")


def mine_info():
    global save_book
    print("=======나의정보=======")
    print("대여중인 도서 리스트")
    # for i in range(len(BookList)):
    #     if BookList[i][3] == 0:
    #         print("-{0}".format(BookList[i][1]))
    # print("")
    print("대여 후 반납한 도서 리스트")
    print("-{0}\n".format(save_book))
    print("연체 조회 정보")
    print("연체된 책이 없습니다.")
    print("")
    user_input = input("정보 변경을 원하시나요? (y/n) >")
    # if user_input == 'y':
    #     ID = input("ID를 입력해주세요. > ")
    #     for i in range(len(user_info)):
    #         if ID == user_info[i][0]:
    #             change = input("비밀번호를 변경하시겠습니까. (y/n) > ")
    #             if change == 'y':
    #                 change_PW = input("변결할 PW > ")
    #                 user_info[i][1] = change_PW
    #                 print(user_info)
    #             elif change == 'n':
    #                 pass

    # elif user_input == 'n':
    #     pass
    print("======================")

def suggestion():
    cur.execute("SELECT COUNT(*) FROM book")
    mexnum = int(cur.fetchall()[0][0])
    i = random.randint(0, mexnum)
    j = random.randint(0, mexnum)
    cur.execute(f"SELECT Num, Title, Author FROM book WHERE Num = {i}")
    cho1 = cur.fetchall()
    cur.execute(f"SELECT Num, Title, Author FROM book WHERE Num = {j}")
    cho2 = cur.fetchall()
    print("\n------추천도서------ ")
    print(cho1)
    print(cho2)
    print("--------------------\n")




def main_screen():
    suggestion()
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


while 1: login()