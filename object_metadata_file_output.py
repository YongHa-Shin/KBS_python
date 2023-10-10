from asyncio.windows_events import NULL
import pandas as pd
import sys
import os 
import time
from datetime import datetime

# 23.10.10 column_list의 '촬영/수신일'을 '촬영일'로 수정
column_list = ['번호', '인제스트 완료시각', '촬영일', '분류', '미디어ID', '제목', '취재기자', '촬영기자', '내용', '영상길이', '메모', '등록위치', '엠바고', '엠바고사유']

class metadata_output:
    def __init__(self, date, raw_csv_data = [], specific_category_list = []) :
        self.date = date
        self.raw_csv_data = raw_csv_data
        self.processed_csv_data = []
        self.temp_data = None
        self.except_data = None
        self.specific_category_list = specific_category_list
        self.date_index = 0

    def main(self):
        self.load_csv_data()
        self.change_index_toDate()
        self.insert_column_division()
        self.check_date()
        while(True):
            if self.date_index == 1 :
                print("입력한 날짜가 존재하지 않습니다. 다시 입력바랍니다.")
                self.date = input()
                self.check_date()
            elif self.date_index == 0 :
                break
        self.except_specific_category()
        self.Ascending_mediaID()
        # self.extract_text_file_dos_command() # 도스 명령어를 추출하는 함수
        self.extract_excel_file_metadata()

    # 1. 리스트에 저장된 csv파일명을 읽는다.
    # 2. 반복문을 사용하여 temp_csv_load에 저장하고 self.processed_csv_data에 append
    # 3. 4개의 csv 데이터를 합치기 위하여 concat으로 합친 후 self.temp_data에 저장
    # 4. 미디어ID를 기준으로 중복 처리
    def load_csv_data(self):  
        try:
            for i in range(len(self.raw_csv_data)) :
                temp_csv_load = pd.read_csv(self.raw_csv_data[i], encoding='cp949')
                self.processed_csv_data.append(temp_csv_load[column_list])
                
            self.temp_data = pd.concat(self.processed_csv_data)
            self.temp_data = self.temp_data.drop_duplicates(['미디어ID']) # 미디어ID를 기준으로 중복처리
        except:
            print("!!Error: load_csv_data()")
            print("20초 후에 자동종료 됩니다.")
            time.sleep(20)
            sys.exit()

    # '인제스트 완료시각'을 기준으로 날짜별로 분류
    def change_index_toDate(self):
        try:
            # '인제스트 완료시각'을 인덱스로 변경하고 index에 저장
            self.temp_data = self.temp_data.set_index('인제스트 완료시각')  
            index = self.temp_data.index

            # temp_data 리셋
            self.temp_data = self.temp_data.reset_index()
            self.temp_data = self.temp_data[column_list]

            # 새로운 매개변수 인덱스 리스트를 만든다.
            new_index_list = []

            # 기존에 '인제스트 완료시각'의 날짜부분만 ex)2022-07-18 인덱스 리스트에 append
            for i in index :
                new_index_list.append(i[0:10])

            # temp_data 인덱스에 날짜부분만 저장해둔 new_index_list를 저장
            self.temp_data.index = new_index_list
        except:
            print("!!Error: change_index_toDate()")
            print("20초 후에 자동종료 됩니다.")
            time.sleep(20)
            sys.exit()

    # 데이터가 원본인지 수신본인지를 판단하고 '구분'이라는 새로운 컬럼을 생성하여 원본/수신본 입력
    def insert_column_division(self):
        try:
            division_list = []
            for i in self.temp_data.loc[:,'제목']:
                if '원본' in i:
                    division_list.append('원본')
                elif '수신본' in i:
                    division_list.append('수신본')
                else:
                    division_list.append('NULL')

            self.temp_data.loc[:, '구분'] = division_list
            # 23.10.10 column_list의 '촬영/수신일'을 '촬영일'로 수정
            self.temp_data = self.temp_data[['번호', '구분', '인제스트 완료시각', '촬영일', '분류', '미디어ID', '제목', '취재기자', '촬영기자', '내용', '영상길이', '메모', '등록위치', '엠바고', '엠바고사유']]
        except:
            print("!!Error: insert_column_division()")
            print("20초 후에 자동종료 됩니다.")
            time.sleep(20)
            sys.exit()

    # 1. 사용자가 입력한 날짜가 csv 데이터 내에 존재할 경우 0을 반환, 존재하지 않을 경우 1을 반환
    # 2. 1을 반환할 경우 데이터에 존재하는 날짜를 입력할 때까지 계속 무한루프
    # 3. 0이 반환 할 때 무한루프가 브레이크 되고, 다음 알고리즘으로 넘어간다.
    def check_date(self):
        try:
            self.date_index = 0 # 입력한 date만 저장 후 인덱스 초기화 0 ~ 
            # self.temp_data = self.temp_data.loc[self.date] # 1개의 데이터만 뽑을 때 데이터프레임이 아닌 시리즈로 나와서 이 문법은 사용할수 없음!!
            self.temp_data = self.temp_data.loc[[self.date], :]
            self.temp_data = self.temp_data.reset_index()
        except:
            self.date_index = 1

    # 1. 제외할 분류명을 분리하는 함수
    # 2. except_data가 제외할 분류명에 관한 데이터, self.temp_data는 필요한 분류명에 관한 데이터
    # 3. 이 후 데이터 정렬에 따른 불필요한 인데스를 삭제한다.
    def except_specific_category(self):
        try:
            self.except_data = self.temp_data[self.temp_data['분류'].isin(self.specific_category_list)] # except_data에 제외시킬 데이터 저장
            self.temp_data = self.temp_data.drop(self.except_data.index) # 제외시킬 데이터를 drop

            del self.except_data['index'] # except_data 'index' 열 삭제
            del self.temp_data['index'] # temp_data 'index' 열 삭제
            del self.except_data['번호'] # except_data '번호' 열 삭제
            del self.temp_data['번호'] # temp_data '번호' 열 삭제
        except:
            print("!!Error: except_specific_category()")
            time.sleep(20)
            sys.exit()

    # 미디어 ID 오름차순 후 불 필요한 인덱스 삭제
    def Ascending_mediaID(self):
        try:
            self.temp_data = self.temp_data.sort_values(by='미디어ID', axis=0)
            self.except_data = self.except_data.sort_values(by='미디어ID', axis=0)
            self.temp_data = self.temp_data.reset_index()

            del self.temp_data['index'] # temp_data 'index' 열 삭제
        except:
            print("!!Error: Ascending_mediaID()")
            time.sleep(20)
            sys.exit()

    # 배치 프로그래밍에 사용될 명령어 텍스트를 추출하는 함수. 이제는 사용될 일이 없겠지만 혹시라도 남겨둘게요.
    def extract_text_file_dos_command(self):
        sizeofdata = len(self.temp_data)
        self.temp_data.rename(columns={'index': '명령어'}, inplace=True)
        dos_command_list = [] # 명령어를 저장할 리스트

        f = open(self.date + "_rename_dos_command_list.txt", 'w', encoding="ANSI") # 텍스트 파일 쓰기모드로 열기

        for i in range(sizeofdata) :
            temp = '''ren "%Dir%*{0}*" "({1})_{0}_({2})_{3}.mxf"''' \
            .format(self.temp_data.loc[i, "미디어ID"], self.temp_data.loc[i, "구분"], self.temp_data.loc[i, "분류"], self.temp_data.loc[i, "제목"])
            dos_command_list.append(temp) 
            f.write(temp+'\n') # 텍스트 저장

        f.close() # 텍스트 파일 닫기
        self.temp_data.loc[:, '명령어'] = dos_command_list # 데이터프레임에 명령어 리스트를 저장

    # 엑셀 파일 추출
    def extract_excel_file_metadata(self):
        try:
            # 추출한 메타데이터 엑셀 파일에 데이터 저장
            file_name = self.date + '_metadata_list.xlsx'
            self.temp_data.to_excel(file_name, index=False)

            # 추출한 메타데이터 list 폴더 내에 엑셀 파일 저장
            except_file_name = self.date + '_except_list.xlsx'
            self.except_data.to_excel("list\\" + except_file_name, index=False)
            self.temp_data.to_excel("list\\" + file_name, index=False)

            print("성공: 엑셀파일 목록이 생성되었습니다.")
        except:
            print("Warnning: 엑셀 파일을 생성할 수 없습니다. 동일한 이름의 엑셀창이 열려있는지 확인해주세요!")

    # 1. mxf_file 내에 파일 리스트를 모두 불러오고 mxf 파일 리스트만 추출한다.
    # 2. 로그를 기록할 텍스트 파일을 뽑는다.
    # 3. mxf 파일을 리네이밍을 한다.
    def change_mxf_file_name(self):
        try:
            file_list = os.listdir("mxf_files") # mxf_files 내에 파일 리스트를 모두 불러온다.
            MXF_list = []
            Success_list = []
            error_list = []

            # 확장자가 mxf인것만 리스트에 저장
            for i in file_list :
                if i.find(".mxf") != -1 :
                    MXF_list.append(i)
                elif i.find(".MXF") != -1 :
                    MXF_list.append(i)

            if MXF_list == [] and len(self.temp_data) != 0 :
                print("MXF 비디오가 폴더 내에 존재하지 않습니다. mxf_files 폴더 내에 MXF 비디오를 넣어주세요!")
                print("20초 후에 자동종료 됩니다.")
                time.sleep(20)
                sys.exit()
                
            sizeofdata = len(self.temp_data)
            today = str(datetime.today().strftime("%Y%m%d"))
            text_name = "rename_" + today + "_log"
            f = open("log\\" + text_name + ".txt", 'a', encoding = "utf-8")
            index = 1 # mxf file rename에 모두 성공할 경우 1을 반환 1개라도 실패할 경우 0을 반환  

            f.write('===============================================================================' + '\n')
            f.write('Start time: ' + str(datetime.today().strftime("%Y-%m-%d %H:%M:%S")) + '\n\n')

            for i in range(sizeofdata) :
                sum = 0
                for j in MXF_list :
                    if self.temp_data.loc[i, "미디어ID"] in j :
                        temp = "{0}_({1})_{2}.mxf" \
                        .format(self.temp_data.loc[i, "미디어ID"], self.temp_data.loc[i, "분류"], self.temp_data.loc[i, "제목"])
                               
                        if j == temp :
                            Success_list.append(temp)
                            continue
                        
                        # 231010 코드 추가
                        # "<",">", "/" 기호를 삭제 해주는 코드
                        temp = temp.replace("<", "").replace(">", "").replace("/", "")

                        os.renames("mxf_files" +'\\'+ j, "mxf_files" +'\\'+ temp) # mxf 비디오 리네임 실행

                        f.write(temp + '\n') # 성공시 로그 텍스트로 남기기
                        f.write("Succeed: MXF_파일 이름변경 성공" +'\n\n')
                        Success_list.append(temp)
                    else :
                        sum += 1
                        if sum == len(MXF_list) :
                            temp = "{0}_({1})_{2}.mxf" \
                            .format(self.temp_data.loc[i, "미디어ID"], self.temp_data.loc[i, "분류"], self.temp_data.loc[i, "제목"])
                            f.write(temp + '\n') # 실패시 로그 텍스트로 남기기
                            f.write("!!Error: MXF_파일이 존재하지 않습니다. 'mxf_file' 디렉토리에 해당 미디어를 넣어주세요." +'\n\n')
                            index = 0
                            error_list.append(self.temp_data.loc[i, "미디어ID"]) # 실패한 미디어 id를 리스트에 저장후 구문이 끝난 후 리스트 반환

            # mxf file rename에 모두 성공할 경우 1을 반환 1개라도 실패할 경우 0을 반환  
            if index == 1 :
                return 1, Success_list
            elif index == 0 :
                return 0, error_list

        except:
            print("!!Error: change_mxf_file_name()")
            time.sleep(20)
            sys.exit()