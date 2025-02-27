#tạo ra một danh sách  rỗng để lưu kết quả
j=[]
#duyệt qua tất cả các số trong đoạn từ 200 đến 3200, kiểm tra xem số i có chia hết ch 7 và không chia hết cho bội số của 5 không 
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
        print(','.join(j))
    