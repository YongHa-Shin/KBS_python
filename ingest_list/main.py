import sys
import time
import shutil
from object_metadata_file_output import metadata_output

print("\n")
print("===========================================================================================================")
print("* 프로그램 이름: 인제스트 MXF_Video 리네이밍 소프트웨어")
print("* 프로그램 버전: 1.0")
print("* 제작목적: mxf형식 비디오의 이름변경, csv 데이터 분류를 '쉽게' 하기 위함이다.")
print("* 제작날짜: 2022.8.25")
print("* 개발언어: Python 3.10.1 64bit")
print("* 개발툴: Visual Studio Code")
print("* 관리자: 뉴스영상콘텐츠부 선상원 촬영기자")
print("* 제작자: 뉴스시스템개발부 신용하")
print("* 저작권: 신용하")
print("===========================================================================================================\n")
print("** 참고사항: 편리함을 추구하기 위해 제작되었을뿐, 프로그램 동작에 문제가 생겼을 때 관리자나 제작자에게 어떠한 책임을 물을 수 없다.\n")

raw_csv_data = ['국내원본.csv', '국내수신본.csv', '국제원본.csv', '국제수신본.csv']
specific_category = []

try:
    f = open("except_category.txt", 'r', encoding="utf-8")

    for line in f:
        specific_category.append(line.strip())
    f.close()
except:
        print("!!Error: except_category.txt is not exist")
        time.sleep(20)
        sys.exit()

print("날짜 입력를 입력하세요. ex) 2022년 8월 1일 -> 2022-08-01 으로 입력")
date = input()

object = metadata_output(date, raw_csv_data, specific_category)
object.main()
index = object.change_mxf_file_name()

while True:
    f = open(date + "_missing_video_file_list.txt", 'w', encoding="utf-8")
    if index[0] == 0 :
        for i in index[1] :
            f.write(i + '\n')
        f.close()
        print("Rename에 실패한 mxf파일이 존재합니다. 다시 시도하겠습니까? (y/n)")
        print("Rename failed MediaID list: " + str(index[1]))
        response = input()
        
        if response == 'y' or response == 'Y' :
            index = object.change_mxf_file_name()
        elif response == 'n' or response == 'N' :
            break
        else :
            print("텍스트가 재대로 입력되지 않았습니다. 'y' or 'n'을 입력하세요.")
    elif index[0] == 1 :
        for i in index[1] :
            shutil.move("mxf_files\\" + i, "mxf_files_converting")
        print("모든 mxf형식의 비디오 리네이밍을 성공 하였습니다!!")
        break
del object

print("20초 후에 자동종료 됩니다.")
time.sleep(20)
sys.exit()