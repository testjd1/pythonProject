"""
@ 파일 읽고 쓰기
    - 파일을 읽고 쓰기 전에 파일을 열어야 한다
    - fileObj = open ( filename, mode )
            mode 첫번째 글자 - 작업 표시
            r(read)  : 파일 읽기
            w(write) : 파일 쓰기 ( 파일이 없으면 생성하고 파일이 있으면 덮어쓴다 )
            x(write) : 파일 쓰기 ( 파일이 없을 때만 생성하고 쓴다 )
            a(append) : 파일 추가 ( 파일이 있으면 파일의 끝에서부터 추가하여 쓴다 )

            mode 두번째 글자 - 파일 타입
            t : 텍스트(text) 타입 ( 기본값 )
            b : 이진(binary) 타입
            두번째 글자가 없으면 텍스트 타입이다.

            encoding='utf-8' : 한글

    - 파일을 열고 사용 후에는 반드시 닫아야 한다
"""


"""
try :
    f = open('./data/data.txt', 'r', encoding='utf-8')  # f가 파일의 통로
    '''
    쌤 스타일 : 자바였으면 else 가 없으므로 여기다 넣었을듯
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()
    '''
except FileNotFoundError as e:
    print('파일을 찾을 수 없습니다. > ',e)
else:
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()
finally:
    print('종료')
"""
'''
# 자동으로 close() 하기 위해 with 구문 사용


with open('data/data.txt','r',encoding='utf-8') as f:
    while True:
        line = f.readline() # 라인별로 읽음
        if not line: break
        print(line)
'''
"""
try:
    with open('data/data.txt','r',encoding='utf-8') as f:
        content = f.read()  # 전체 다 읽음
        # print(content)
        words = content.split() # 단어별로 리스트화
except Exception as e:
    print('예외')
else:
    print('정상 실행')
finally:    
    print('총 단어수 : ', len(words))
    print('종료')
"""
filename = './data/' + 'data.txt'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()  # 전체 다 읽음
    # print(content)
    words = content.split()  # 단어별로 리스트화
print('총 단어수 : ', len(words))