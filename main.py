def average(list):
    return(sum(list)/len(list))

list = [77,63,75,64,73,75,114,69,54,72,58,98,12,84,110,47,73]
print('평균값:',average(list))

a = int(input("확진자 수를 입력해주세요"))
if a > average(list):
    print("이상입니다.")

if a < average(list):
    print("이하입니다.")