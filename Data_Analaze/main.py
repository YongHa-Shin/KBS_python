import pandas as pd
import matplotlib as mat

# 1차원 데이터 Series
temp = pd.Series([-20, -10, 10, 20], index = ['Jan', 'Feb', 'Mar', 'Apr'])
# print(temp['Jan'])

# 2차원 데이터 DataFrame
data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190]
}

# temp2 = pd.DataFrame(data, index = [1,2,3,4,5,6,7,8])
# print(temp2)
# print("\n")

# print(temp2.index)
# temp2.index.name = '지원번호'
# print(temp2)

# temp2.reset_index(drop=True, inplace=True) # 실제 데이터에 바로 반영
# print(temp2.index)
# print(temp2)

# # DataFrame 지정한 column 으로 index를 설정
# temp2.set_index('이름', inplace=True)
# print(temp2)

# # index 정렬 -> index를 기준으로 오름차순, 내림차순 정렬
# print(temp2.sort_index()) # 오름차순
# print(temp2.sort_index(ascending=False)) # 내림차순

# 4. 파일 저장 및 쓰기 excel, csv, txt
# df = pd.DataFrame(data, index = [1,2,3,4,5,6,7,8])
# df.index.name = '지원번호'
# print(df)

# df.to_csv('score.csv', encoding='utf-8')
# df.to_csv('score2.csv', encoding='utf-8', index=False)
# df.to_csv('score.txt', encoding='utf-8', sep='\t') # tap으로 column을 정렬하고 txt파일로 저장
# df.to_excel('score.xlsx') # Excel 파일로 저장

# csv 파일 열기
df = pd.read_csv('score.csv')
print(df)

# txt 파일 열기
df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')
print(df)