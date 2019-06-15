from .XuLyTrungLap import XuLyTrunglap
import math as m

def XuLyDuLieuNhieu(dict_data):
    print("-------------TIẾN TRÌNH XỬ LÝ DỮ LIỆU NHIỄU----------------")
    print("*CÁC THUỘC TÍNH GÂY NHIỄU CẦN XỬ LÝ :");
    ############ GĐ1 : TỪ KẾT QUẢ PHÂN TÍCH SUY RA CÁC THUỘC TÍNH NHIỄU ########
    ## ProductRelated : Có 311 loại
    # Min: 0.0 | Max: 705.0
    # -> Giỏ [0;720]
    # Độ rộng : 20
    ## Administrative_Duration, Informational_Duration, ProductRelated_Duration :
    # -->Giá trị liên tục sẽ gây nhiễu cây quyết định
    # --> Dùng kỹ thuật xử lý làm rời rạc hóa dữ liệu.

    #Đối với ProductRelated_Duration
    # + Min : 0 ms - Max : 63973.52223 ms
    # --> Chọn khoảng [0-65000] (ms)
    # ĐỘ rộng giỏ 500. (Vì dữ liệu phân bố không đều và tập trung ở vùng thấp)

    #Administrative_Duration
    #Min :  0.0 |  Max : 3398.75
    # Khoảng [0-3500]
    #-> Độ rộng giỏ :100

    #Informational_Duration
    #Min :  0.0 |  Max : 2549.375
    #->Giỏ [0;2600]
    #-> ĐỘ rộng giỏ : 100

    ## BounceRates, ExitRates
    #Min :  0.0 (1%) |  Max : 0.2 (20%)
    #Độ chênh lệch rất nhỏ, Chỉ làm tròn số
    #Độ rộng giỏ : 0.01 (1%)

    ## PageValues : Giá trị liên tục nên sẽ gây nhiễu cây quyết định
    # --> Dùng kỹ thuật Bining và Smoothing
    # + Min : 0 - Max : 361,7637419
    # --> Chọn khoảng [0-400] - Độ rộng giỏ : 50
    # ==> Gán nhãn : Là string của khoảng đó

    #######################################################################################################################
    # ---- GIAI ĐOẠN 2 : XỬ LÝ CÁC THUỘC TÍNH GÂY NHIỄU
    # Group1=["Administrative","Informational", "ProductRelated"]   # Nhớm nhiễu 1
    Group1=["Administrative_Duration", "Informational_Duration"]
    Group2=["ProductRelated_Duration"]
    Group3=["BounceRates", "ExitRates"]
    Group4=["PageValues"]
    Group5=["ProductRelated"]
    print("Nhóm 1 : ",Group1)
    print("Nhóm 2 : ",Group2)
    print("Nhóm 3 : ",Group3)
    print("Nhóm 4 : ",Group4)
    print("Nhóm 5 : ",Group5)
    #ĐỊNH NGHĨA HÀM XỬ LÝ THEO PHƯƠNG PHÁP BINNING VÀ SMOOTHING (KHÔNG LÀM TRƠN BẰNG GIÁ TRI TRUNG BÌNH CỦA GIỎ MÀ GÁN NHÃN CHO GIỎ)
    #Định nghĩa hàm chia giỏ --> Trả về nhãn của giỏ (String)
    def getBasketLabel1(width_basket,value,min_value): #Truyền vào độ rộng giỏ và giá trị cần phân giỏ, giá trị min của giỏ
        if(value==min_value):  # Trường hợp đặt biệt (Vì không con giỏ nào bên dưới nên cho nó vào giỏ [min_value;min_value+width_baske]
            right_value=min_value+width_basket;
        else:
            right_value=m.ceil(value/width_basket)*width_basket #Giá trị bên phải của giỏ
        left_value=right_value-width_basket #Giá trị bên trái của giỏ
        #Xác định khoảng --> Chuyển sang String --> Trả về
        label="" #Nhãn của giỏ:
        if(value<=min_value+width_basket): #Nếu giá trị nằm trong giỏ đầu tiên thì cận bên trái của khoảng là "["
            label="["+str(left_value)+"-"
        else:
            label="("+str(left_value)+"-"
        label+=str(right_value)+"]"

        return label

    def countValue(dict_data, attr): #Thống kế các giá trị kèm theo là số lần xuât hiện của giá trị đó trên 1 thuộc tính
        dict_values ={}
        for col in  dict_data[attr].keys():
            value=dict_data[attr][col]
            if value in dict_values.keys():
                dict_values[value]=dict_values[value]+1
            else :
                dict_values[value]=1
        return dict_values
    #Hàm trả về giá trị trung bình của giỏ --> Làm trơn Smoothing
    #Hàm gán giỏ 1 - Phương pháp bining và smoothing
    def pointLableForBasket1(list_attribute, data_set, width_basket, min_value):
        for Attribute in list_attribute: #Duyệt lần lượt các thuộc tính cần xử lý
            col_data = data_set[Attribute]  # Lấy lần lượt cột dữ liệu của các thuộc tính nhiễu
            dict_period={} #Khởi tạo biến lưu các giỏ và value là tổng giá trị của giỏ --> Mục đích để làm trơn
            count_value=len(col_data) #Tính số lượng các giá trị
            #GĐ1 : Chia giỏ
            for row in col_data.keys(): # Duyệt lần lượt giá trị từng hàng của cột dữ liệu
                label=getBasketLabel1(width_basket,col_data[row],min_value)
                if(label in dict_period.keys()):
                    dict_period[label]+=col_data[row];
                else:
                    dict_period[label]=col_data[row];
                col_data[row]=label
            # GĐ2 : Làm trơn
            dict_values=countValue(data_set,Attribute)
            for row in col_data.keys():
                label=col_data[row]
                # col_data[row]=round(dict_period[label]/dict_values[label],2)
                if (Attribute=="BounceRates"or Attribute=="ExitRates"):
                    #Nếu là giá trị % thì nhân 100 --> Số quá nhỏ.
                    col_data[row]=(dict_period[label]/dict_values[label])*100
                else:
                    col_data[row]=round(dict_period[label]/dict_values[label],2)

    #Hàm gán giỏ 2 - Phương pháp rời rạc hóa dữ liệu
    # min_width_basket : Khoảng cách của giỏ nhó nhất trong các giỏ, list_label : danh sách các nhãn sẽ gán cho giỏ,
    # các giá trị trong list_label được sắp xếp tương ứng với thứ tự các giỏ chia theo khoảng cách nhỏ nhất.
    # VD : Trường hợp xử lý Group2 thì các giỏ sẽ được chia lại và gán như sau :
    # Để áp dụng giải thuật sẽ thực hiện trong hàm pointLabelForBasket2 thì Các thuộc tính trong Group 2 được chia lại
    # Khoảng cách giỏ : 5000 ms - Số giỏ : 13 giỏ - min : 0 ms
    # [0-5000] : Very Short
    # (5000-10000] :Short
    # (10000-15000] : Short
    # ... Tương tự
    # ĐỊNH NGHĨA HÀM CHO PHƯƠNG PHÁP RỜI RẠC HÓA DỮ LIỆU
    # def getBasketLabel2(min_width_basket,value,min_value,list_label): #Truyền vào độ rộng giỏ và giá trị cần phân giỏ, giá trị min của giỏ
    #     if (value==min_value): # TRường hợp đặc biệt. Vì không còn giỏ nào thấp hơn nên gán cho value vào giỏ [min_value- min_value+min_width_basket]
    #         num_basket=1 # Số thứ tự giỏ mà value thuộc vào
    #     else :
    #         num_basket=m.ceil(value/min_width_basket)
    #     label=list_label[num_basket-1] #Tham chiếu để lấy nhãn của giỏ , -1 là vì trong list thì chỉ số giỏ 1 là 0.
    #     return label
    # def pointLabelForBasket2(list_attribute, data_set,min_width_basket,min_value,list_label):
    #     for Attribute in list_attribute: #Duyệt lần lượt các thuộc tính cần xử lý
    #         col_data = data_set[Attribute]  # Lấy lần lượt cột dữ liệu của các thuộc tính nhiễu
    #         for row in col_data.keys(): # Duyệt lần lượt giá trị từng hàng của cột dữ liệu
    #             label=getBasketLabel2(min_width_basket,col_data[row],min_value,list_label)
    #             col_data[row] = label

    #Xử lý nhiễu - Theo phương pháp Bining và Smoothing
    print("-Thao tác : Xử lý nhóm 1")
    pointLableForBasket1(Group1,dict_data,100,0)
    # print(data_set["PageValues"])
    print("=>Xử lý thành công")

    print("-Thao tác : Xử lý nhóm 2")
    pointLableForBasket1(Group2,dict_data,500,0)
    # print(data_set["PageValues"])
    print("=>Xử lý thành công")

    print("-Thao tác : Xử lý nhóm 3")
    pointLableForBasket1(Group3,dict_data,0.01,0.0)
    print("=>Xử lý thành công")

    print("-Thao tác : Xử lý nhóm 4")
    pointLableForBasket1(Group4,dict_data, 50, 0)
    print("=>Xử lý thành công")

    print("-Thao tác : Xử lý nhóm 5")
    pointLableForBasket1(Group5,dict_data, 20, 0)
    print("=>Xử lý thành công")
    print("-----------------------------------------------------------")
    ###########   ---- GIAI ĐOẠN 3 : XỬ LÝ TRÙNG LẶP SAU KHI XỬ LÝ NHIỄU -----------------------------
    XuLyTrunglap(dict_data);
    return dict_data