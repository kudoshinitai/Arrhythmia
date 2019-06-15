def XuLyTrunglap(dict_data):
    print("------------TIẾN TRÌNH XỬ LÝ TRÙNG LẶP--------------")
    list_dict={}
    isFirstRun= True
    # Chuyển đổi dict_data theo cột thành dạng dữ liệu theo hàng
    for attribute in list(dict_data.keys()):
        col_data=dict_data[attribute]
        for row in list(col_data.keys()):
            if(isFirstRun):
                list_dict[row]=[]
            list_dict[row].append(col_data[row])
        isFirstRun=False
    # Dùng set để loại bỏ trùng lặp
    setData=set([])
    for row in list(list_dict.keys()):
        setData.add(tuple(list_dict[row])) #Trước khi đưa vào set phải chuyển sang tuple.
    print("-Số dòng trước xử lý trùng lặp: ",len(list_dict))
    print("-Số dòng sau khi xử lý trùng lặp: ",len(setData))
    print("=>Số dòng trùng lặp đã xóa: ",len(list_dict)-len(setData))
    print("-------------------------------------------------------");
    # print(set)
    #tái cấu trúc set --> dict
    dict_data_processed ={}
    isFirstRun=True
    count_row=0
    for str_row_data in setData:
        list_row_data=list(str_row_data)
        # print(list_row_data)
        count_col=0
        for attribute in dict_data.keys():
            if(isFirstRun):
                dict_data_processed[attribute]={}
            dict_data_processed[attribute][count_row]=list_row_data[count_col]
            count_col+=1
        isFirstRun=False
        count_row+=1
    return dict_data_processed