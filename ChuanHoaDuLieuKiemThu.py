import math as m

def XacDinhGio(width_basket, value, min_value):  # Truyền vào độ rộng giỏ và giá trị cần phân giỏ, giá trị min của giỏ
    if (
            value == min_value):  # Trường hợp đặt biệt (Vì không con giỏ nào bên dưới nên cho nó vào giỏ [min_value;min_value+width_baske]
        right_value = min_value + width_basket;
    else:
        right_value = m.ceil(value / width_basket) * width_basket  # Giá trị bên phải của giỏ
    left_value = right_value - width_basket  # Giá trị bên trái của giỏ
    #Trả về giá trị bên trái và bên phải của giỏ
    return [left_value,right_value]

# Hàm trả về giá trị trung bình của giỏ --> Làm trơn Smoothing
# Hàm gán giỏ 1 - Phương pháp bining và smoothing
def GanGiaTriTrungBinh(list_attribute, data_set, width_basket, min_value, data_request):
    count=0;
    for attr in data_set.keys():  # Duyệt lần lượt các thuộc tính cần xử lý
        if(attr in list_attribute):
            col_data = data_set[attr]  # Lấy lần lượt cột dữ liệu của các thuộc tính nhiễu
            # Xác định giá trị trung bình của giỏ mà các giá trị request thuộc vào
            basket = XacDinhGio(width_basket, data_request[count], min_value)
            isFound=False   #NẾU GIÁ TRỊ CHƯA TỪNG XUẤT HIỆN TRONG CSDL --> SẼ CÓ GIÁ TRỊ -1111 --> KHÔNG THỂ PHÂN LỚP -->LẤY GIÁ TRỊ NHÓM GẦN NHẤT CHIA VÀO
            for row in col_data.keys():
                if (attr=="BounceRates" or attr=="ExitRates"):
                    if (basket[0]*100 <= col_data[row] and col_data[row] <= basket[1]*100):
                        data_request[count] = col_data[row]
                        isFound=True
                else:
                    if (basket[0] <= col_data[row] and col_data[row] <= basket[1]):
                        data_request[count] = col_data[row]
                        isFound=True
            if (isFound==False): #Trường hợp nó là dữ liệu sai hoặc mới so với CSDL --> Chọn giá trị gần nhất
                min_distance=m.fabs(col_data[0]-data_request[count]*100)  # Khởi tạo khoảng cách
                index=0
                for row in col_data.keys():
                    new_distance=m.fabs(col_data[row]-data_request[count]*100)
                    if (min_distance>new_distance):  # Tìm được phần tử gần hơn
                        min_distance=new_distance
                        index=row
                data_request[count]=col_data[index]
        count+=1
    return data_request
Group1=["Administrative_Duration", "Informational_Duration"]
Group2=["ProductRelated_Duration"]
Group3=["BounceRates","ExitRates"]
Group4=["PageValues"]
def ChuanHoaDuLieu(dict_data,data_request):
    print("--------------TIẾN TRÌNH CHUẨN HOÁ DỮ LIỆU------------")
    print("-Dữ liệu trước khi chuẩn hoá :\n",data_request)
    GanGiaTriTrungBinh(Group1,dict_data,100,0,data_request)
    GanGiaTriTrungBinh(Group2,dict_data,500,0,data_request)
    GanGiaTriTrungBinh(Group3,dict_data,0.01,0.0,data_request)
    GanGiaTriTrungBinh(Group4,dict_data, 50, 0,data_request)
    print("-Dữ liệu sau khi chuẩn hoá :\n",data_request)
    #KIỂM TRA CHUẨN HOÁ CÓ THÀNH CÔNG KHÔNG --THÀNH CÔNG NẾU KHÔNG CÓ GIÁ TRỊ NÀO LÀ -1111
    print("=>Chuẩn hoá thành công!")
    print("------------------------------------------------------")
    return data_request