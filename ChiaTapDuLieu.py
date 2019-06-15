import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def ChiaTapDuLieu(dict_data,test_size,train_size):
    print("-----------TIẾN TRÌNH PHÂN CHIA TẬP DỮ LIỆU------------")
    print(f'*Thao tác : Chia tập dữ liệu theo tỉ lệ {train_size*100}% : {test_size*100}% ')
    #Thay đổi định dạng tập dữ liệu
    df=pd.DataFrame.from_dict(dict_data)
    dict_data=df.to_dict(orient="split")
    list_data_target=dict_data['data']
    list_data=[]
    list_target=[]
    for data_target in list_data_target :
        list_target.append(data_target[-1])
        del data_target[-1]
        list_data.append(data_target)
    arr_data=np.asarray(list_data)
    arr_target=np.asarray(list_target)
    data_train,data_test,target_train,target_test=train_test_split(arr_data,arr_target,test_size=test_size,train_size=train_size);
    print("-Tổng số dòng dữ liệu :",len(dict_data['data'])," (dòng)")
    print("-Tập huấn luyện có :",len(data_train)," (dòng)")
    print("-Tập kiểm thử có :",len(data_test)," (dòng)")
    print("=>Phân chia thành công !")
    print("-------------------------------------------------------")
    return np.asarray([data_train,data_test,target_train,target_test])