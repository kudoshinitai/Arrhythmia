def PhanTichDuLieu(dict_data):
    # Thống kê các giá trị min và max của các thuộc tính tính để xác định các thuộc tính có khả năng gây nhiễu
    def Min_Max(dict):
        print("Kiểu dữ liệu : ", type(dict[0]))
        Min=Max=dict[0];
        for index in dict.keys():
            if(Min>dict[index]):
                Min=dict[index]
            if(Max<dict[index]):
                Max=dict[index]
        return [Min,Max]
    #Hàm tính giá trị trung bình của 1 thuộc tính
    def Average(dict):
        if type(dict[0]) is int or type(dict[0]) is float:
            sum=0;
            for index in dict.keys():
                sum+=int(dict[index])
            return sum/len(dict)
        return None;
    #Hàm đếm số lượng giá trị của 1 thuộc tính
    def countValue(dict_data, attr): #Thống kế các giá trị kèm theo là số lần xuât hiện của giá trị đó trên 1 thuộc tính
        dict_values ={}
        for col in  dict_data[attr].keys():
            value=dict_data[attr][col]
            if value in dict_values.keys():
                dict_values[value]=dict_values[value]+1
            else :
                dict_values[value]=1
        return dict_values
    #Hàm tím giá trị phổ biến
    def searchPopularValue(dict_values):
        popularValue=list(dict_values.keys())[0]
        for value in dict_values:
            if dict_values[popularValue]<dict_values[value]:
                popularValue=value
        return [popularValue,dict_values[popularValue]]
    print("--------------TIẾN TRÌNH PHÂN TÍCH DỮ LIỆU---------------")
    for attr in dict_data.keys():
        print("-------------" + attr + "----------------")
        dict_values=countValue(dict_data,attr);
        listValue= Min_Max(dict_data[attr]);
        listMaxAppearValue=searchPopularValue(dict_values)
        print("Number of Values :",len(dict_values))
        print("Min : ",listValue[0],"|  Max :",listValue[1])
        print("Average: ",Average(dict_data[attr]))
        print("Popular Value : ",listMaxAppearValue[0],"|  Frequency : ",listMaxAppearValue[1])
        print(dict_values)
    print("----------------------------------------------------------")

def PhanTichDuLieuClass(arrTarget):
    count=0
    for value in arrTarget:
        if (value==True):
            count +=1
    print("True Class :",count)
    print("False Class :",len(arrTarget)-1)