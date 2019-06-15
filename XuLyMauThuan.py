#Mẫu Thuẫn là các thuộc tính đều giống nhau mà thuộc tính quyết định lại khác nhau
# Ý Tưởng:
# B1: Tách file csv thành 2 nhóm dựa trên thuộc tính quyết tính là True và Fasle
# B2: Lấy từng dòng trong nhóm Fasle sang kiểm tra bên nhóm True
# B3: Nếu có 'Xóa' dòng Fasle và dòng True giống nhau mà khác thuộc tính quyết định
# B4: Gộp 2 nhóm thành 1 nhóm sau khi đã xử lý và xuất ra file csv
import pandas as pd;

def XuLyMauThuan(dict_data):
    #Khởi tạo tham sóo
    list_tr = []
    list_true=[]
    list_fa = []
    list_fasle =[]
    set_true=set()
    #1.Chuẩn bị
           #1.1.tạo List_tr
    for row in dict_data.keys():
        # print(type(dict_data[row]))
        if (dict_data[row]["Revenue"]):
            list=[]
            for row_dict_value in dict_data[row].keys():
                list.append(dict_data[row][row_dict_value])
            list_tr.append(list)
    # print(list_tr)#test list_tr
            #1.1.1.Lọc ra thuộc tính quyết định Revenue --> tạo list_true
    for i in range(0,len(list_tr)):
        list=[]
        for j in range(0,len(list_tr[i])-1):
            list.append((list_tr[i][j]))
        list_true.append(list)
    # print(list_true)
            #1.2.tạo List_fa
    for row in dict_data.keys():
        if (dict_data[row]["Revenue"]==False):
            list=[]
            for row_dict_value in dict_data[row].keys():
                list.append(dict_data[row][row_dict_value])
            list_fa.append(list)
            #1.2.1.Lọc ra thuộc tính quyết định Revenue --> tạo list_fasle
    for i in range(0,len(list_fa)):
        list=[]
        for j in range(0,len(list_fa[i])-1):
            list.append((list_fa[i][j]))
        list_fasle.append(list)
    # print(list_fasle)
    #2.Xử lý mẫu thuẫn
            #2.1.Xóa các dòng mẫu thuẫn ở 2 list, true và fasle
    # list_true_check=[]
    # list_fasle_check=[]
    def MauThuan(list_true_check,list_fasle_check):
        for i in range(0,len(list_true_check)):
            for j in range(0,len(list_fasle_check)):
                if (list_fasle_check[j] == list_true_check[i]):#kiểm tra bên list_true có dòng giống với list_fasle
                    # if(list_true_check[-1]==1):#Nếu đã thêm chỉ số thì bỏ qua
                    #     continue
                    if (str(list_true_check[i][-1])=="1"):  #Phải xác định nó là list trước rồi mới truy xuất phần tử cuối cùng . :v
                        continue
                    else:
                        list_true_check[i].append(1)#Thêm chỉ số là 1 vào cuối để đánh dấu dòng mâu thuẫn --> Xóa sau
                    list_fasle_check[j].append(1)    #Đánh dấu mâu thuẫn chứ không xóa nữa (Giải pháp mới)
                    # del list_fasle_check[j]#Xóa dòng bên list_fasle
                    # Lỗi do dòng del trên sinh ra --> Khi xóa thì kích thước mảng thay đổi tuy nhiên thay đổi này sẽ không được
                    # cập nhật ở lệnh len(list_fasle_check) của vòng for --> Lỗi index out of range
                    # => Giải pháp : Không dùng cách đó nữa.
                    # => Đánh dấu các list mâu thuẫn ở cả 2 list true và false . Ở bước tái cấu trúc thì loại bỏ list mâu thuẫn.

    MauThuan(list_true,list_fasle)
    # print(list_fasle)#test list_fasle sau khi xử lý
    # print(list_true)#test list_fasle sau khi xử lý
    #3.Tái cấu trúc file sau khi xử lý

    for i in range(0,len(list_true)):
        list_true[i].append(True)#Thêm thuộc tính quyết để khôi phục lại như ban đầu
    for i in range(0,len(list_fasle)):
        list_fasle[i].append(False)#Thêm thuộc tính quyết để khôi phục lại như ban đầu

    list_original=[]#khởi tạo tham số list ban đầu
    list_original=list_true+list_fasle;#Gộp 2 list
    # print(list_original)#Test list ban đầu
    dict_data_processed={}#Khởi tạo tham số dict mới sau khi xử lý

            #3.1.lấy thuộc tính ban đầu
    list_attribute=[]#Tạo list thuộc tính
    for i in dict_data.keys():
        for j in dict_data[i].keys():
            list_attribute.append(j)
        break
    # print(list_attribute)#test list thuộc tính
            #3.2.khôi phục địng dạng dict_data_processed
    list_conflict=[]   #LƯU  các dòng mâu thuẫn --> Check kết quả
    count=0 # Đếm số dòng mâu thuẫn
    for i in range(0,len(list_original)):
        #Loại bỏ các dòng bị mâu thuẫn
        if(str(list_original[i][-2])=="1"):   #Phải ép sang so sánh chuỗi vì True là 1 False Là != 1
            count+=1
            list_conflict.append(list_original[i])
            continue
        dict_data_processed[i] = {}#Khởi tạo dict với key=i
        row = 0;
        for attribute in list_attribute:
            dict_data_processed[i][attribute] = list_original[i][row]#gán giá trị chào vị trị key=1(key=attribute)
            row+=1;

    ########## XUẤT KẾT QUẢ XỬ LÝ ##########
    print("--------------TIẾN TRÌNH XỬ LÝ MÂU THUẪN DỮ LIỆU --------")
    print("*Số mẫu dữ liệu trước xử lý : ", len(dict_data)," (dòng)")
    print("*Số mẫu dữ liệu sau xử lý : ",len(dict_data_processed)," (dòng)")
    print("=>Số mẫu dữ liệu mâu thuẫn đã xóa : ",count," (dòng)");
    print("---------------------------------------------------------");
    df=pd.DataFrame.from_dict(dict_data_processed,orient="index");
    return df.to_dict()