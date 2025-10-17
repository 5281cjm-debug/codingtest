broken_isbn = input('').split('*')
star_num = '0'
restored_isbn = broken_isbn[0]+star_num+broken_isbn[-1][:-1]#*을 기준으로 앞 + *추측 + *기준 뒤(검증수제외)
checknum = int(broken_isbn[-1][-1]) #검증수

#홀수자릿수의 수는 그대로 두고 짝수자릿수의 수는 3을 곱한 리스트 생성 
to_isbn_check_num_list = [int(isbn_num) if idx_isbn % 2 == 0 else int(isbn_num) * 3 for idx_isbn,isbn_num in enumerate(restored_isbn)]
#리스트 합으로 체크하기 위한 준비
sum_isbn_check_list = sum(to_isbn_check_num_list)

while (sum_isbn_check_list + checknum) % 10 != 0:
    star_num = str(int(star_num)+1)
    restored_isbn = broken_isbn[0]+star_num+broken_isbn[-1][:-1] #*을 기준으로 앞 + *추측 + *기준 뒤(검증수제외)
    to_isbn_check_num_list = [int(isbn_num) if idx_isbn % 2 == 0 else int(isbn_num) * 3 for idx_isbn,isbn_num in enumerate(restored_isbn)]
    sum_isbn_check_list = sum(to_isbn_check_num_list)
print(star_num) 