import pandas as pd
import statistics
from.ChonLocDuLieu import ChonLocDuLieu

def XuLyDuLieuSaiThieu(data_set):
    print("------- TIẾN TRÌNH XỬ LÝ DỮ LIỆU SAI THIẾU -----------")
    print("*Thao tác : Thay thế giá trị có tần số xuất hiện nhiều nhất cho giá trị sai & thiếu \n"
          "(Trừ trường hợp sai và thiếu trên thuộc tính Phân lớp) ")

    print("Số dòng dữ liệu trước xử lý :", len(data_set["Administrative"]))
    def Kiem(k):# ham kiem tra xem k co la chuoi hay so , str la True
        list =['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','!','@','#','$','%','^','&','*','(',')','-','_','+','=']
        for i in list:
            if(k.count(i)!=0):
                return True
        return False
    list_sum_err= []
    err=0
    def Sai(k):
        if(list_sum_err.count(k)==0):
            list_sum_err.append(k)
    list_type=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0," ",12.0,13.0," "," "]#chuỗi type của từng thuộc tính theo thứ tự 1 - int " "->string
    i =0
    list_value_Month=["Jan","Feb","Mar","Apr","May","June","Jul","Aug","Sep","Oct","Nov","Dec"]
    list_value_VisitorType=["Returning_Visitor","New_Visitor"]
    list_value_Weekend=['True','False']

    list_value_Weekend2=[True,False]
    for j in list(data_set['Revenue'].keys()):# đi từng giá trị
        if(list_value_Weekend2.count(data_set['Revenue'][j])!=1):#kiểm tra key
            err=err+1
            for g in data_set.keys():#sai xóa hàng
                del  data_set[g][j]
    for k in list(data_set.keys()):#kiểm tra các thuộc tính còn lại
        if(k!="Revenue"):#Khác cột quyết định
            list_err = []#danh sách sai của cột k
            list_true = []  # list đúng -> để tìm giá trị nhiều nhất để set giá trị
            for j in list(data_set[k].keys()):#duyệt từng giá trị trong cột j là vị trí hàng
                if(Kiem(str(data_set[k][j]))==False):
                    data_set[k][j]=float(data_set[k][j])
                else:
                    data_set[k][j]=str(data_set[k][j])
                if(type(list_type[i]) != type(data_set[k][j])):#kiểm tra kiểu
                    list_err.append(j)
                    Sai(str(j))
                elif(type(list_type[i])==type(1.0)):#nếu là kiểu int
                    if(data_set[k][j]>=0):#lớn hơn 0 thì ok
                        list_true.append(j)

                    else:
                        list_err.append(j)
                        Sai(str(j))
                elif(type(list_type[i])==type(" ")):#nếu là kiểu String
                    if(k=="Month"):# nếu là cột Month
                        if(list_value_Month.count(data_set[k][j])==0 ):#kiểm tra giá trị có trong tập đc xđ trước
                            list_err.append(j)
                            Sai(str(j))
                        else:
                            list_true.append(j)
                    elif(k=="VisitorType"):#nếu là cột VisitorType
                        if (list_value_VisitorType.count(data_set[k][j]) == 0):#kiểm tra giá trị có trong tập đc xđ trước
                            list_err.append(j)
                            Sai(str(j))
                        else:
                            list_true.append(j)
                    elif(k=="Weekend"):#nếu là cột Weekend
                        if (list_value_Weekend.count(data_set[k][j]) == 0):#kiểm tra giá trị có trong tập đc xđ trước
                            list_err.append(j)
                            Sai(str(j))
                        else:
                            list_true.append(j)
            if(type(list_type[i])==type(1.0)):
                value =[]
                for b in list_true:#lấy giá trị của các hàng đúng đẫ đc lưu vị trí trong mảng list_true
                    value.append(data_set[k][b])
                f=0
                f = statistics.mean(value)
                for b in list_err:#gán các giá trị sai = giá trị trung bìnb f
                    data_set[k][b]=f
            if(type(list_type[i])==type(" ")):
                max =0;
                value =""
                if (k == "Month"):  # nếu là cột Month
                    for r in list(data_set[k].keys()):
                        if (list_value_Month.count(data_set[k][r]) > max):  # nếu số lần xuất hiện lớn nhất thì gabs max = số lần và value = giátri
                            max = list_value_Month.count(data_set[k][r])
                            value=data_set[k][r]
                elif (k == "VisitorType"):  # nếu là cột VisitorType
                    for r in list(data_set[k].keys()):
                        if (list_value_VisitorType.count(data_set[k][r]) > max):  # nếu số lần xuất hiện lớn nhất thì gabs max = số lần và value = giátri
                            max = list_value_Month.count(data_set[k][r])
                            value = data_set[k][r]
                elif (k == "Weekend"):  # nếu là cột Weekend
                    for r in list(data_set[k].keys()):
                        if (list_value_Weekend.count(data_set[k][r]) > max):  # nếu số lần xuất hiện lớn nhất thì gabs max = số lần và value = giátri
                            max = list_value_Month.count(data_set[k][r])
                            value = data_set[k][r]
                for v in list_err:
                    data_set[k][v]=value
        i=i+1

    print('Số lỗi dữ liệu sai & thiếu đã xử lý :',len(list_sum_err)+err)
    print("Số dòng dữ liệu sau xử lý : ",len(data_set["Administrative"]))
    print("=>Xử lý thành công!")
    print("----------------------------------------------------------")
    return data_set
