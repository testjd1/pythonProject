"""
0. DB에 저장할 테이블 생성
1. 사용자 입력 받아 확인
2. 모든 연락처 출력하기
3. 연락처 삭제하기
"""

import cx_Oracle as oci

class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
    # (1)
    # 이름, 전화번호, 이메일, 주소를 입력받아
    # Contact 객체를 생성하고 DB 에 입력
    name = input('이름 : ')
    phone_number = input('전번 : ')
    email = input('이메일 : ')
    addr = input('주소 : ')
    # return Contact(name, phone_number, email, addr)

    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')

    sql = "INSERT INTO MEMBER2 VALUES (:0, :1, :2, :3)"
    val = (name, phone_number, email, addr)
    cursor = conn.cursor()
    cursor.execute(sql, val)
    cursor.close()
    conn.commit()  # 잊지말자
    conn.close()

def print_contact():
    # 넘겨받은 테이블 명의 데이터 화면에 출력
    # 1. 연결객체 얻어오기 ( Connection )
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장
    sql = '''select * from MEMBER2'''

    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()

    # 4. 실행
    cursor.execute(sql)
    datas = cursor.fetchall()
    # 5. cursor 객체 닫기
    cursor.close()
    # 6. 연결객체 닫기
    conn.close()

    # print(datas)
    for row in datas:
        print(row)
    print('-'*20)
def delete_contact(name):
    # 넘겨받은 테이블 명의 데이터 화면에 출력
    # 1. 연결객체 얻어오기 ( Connection )
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장
    sql = "delete from MEMBER2 where name ='{}'".format(name)

    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()

    # 4. 실행
    cursor.execute(sql)
    # 5. cursor 객체 닫기
    cursor.close()
    conn.commit()  # 잊지말 것
    # 6. 연결객체 닫기
    conn.close()

def run():
    contact_list = []
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            set_contact()
        elif menu==2: # 출력을 선택하면
            print_contact()
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)


if __name__ == "__main__":
    run()