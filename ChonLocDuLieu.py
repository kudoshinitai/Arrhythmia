def removeData(dict_data,attr): #Truyền vào tên thuộc tính cần xoá
    print("*Thao tác : Xoá dữ liệu của thuộc tính \"" + attr + "\"");
    #Tìm kiếm xem thuộc tính có tồn tại trong CSDL không
    flag=0;  # Đánh dấu thuộc tính có được tìm thấy hay không.
    for key in dict_data.keys():
        if (key==attr):
            del dict_data[attr];
            print("=> Kết quả : Xoá thành công");
            flag=1; # Đã tìm thấy và xoá
            break;
    if (flag==0):
            print("=> Kết quả : Xoá không thành công \n(Error : Thuộc tính \""+attr+"\" không được tìm thấy.)")

#Hàm điều khiển việc lọc dữ liệu, truyền vào dữ liệu kiểu từ điển, và danh sách các thuộc tính cần loại bỏ
def ChonLocDuLieu(dict_data, list_attr):
    print("---------------TIẾN TRÌNH CHỌN LỌC DỮ LIỆU--------------")
    numAttrPre=len(dict_data);
    for attr in list_attr:
        removeData(dict_data,attr);
    print("=>Số thuộc tính trước khi xử lý : ",numAttrPre)
    print("=>Số thuộc tính trước sau khi xử lý : ",len(dict_data))
    print("--------------------------------------------------------")
    return dict_data