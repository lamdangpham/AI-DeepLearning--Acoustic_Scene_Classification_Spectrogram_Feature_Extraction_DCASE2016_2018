import os
from get_data_cqt_train import get_data_cqt_train
from get_data_cqt_test import get_data_cqt_test

data_train_dir  =  "./../data_train/"
data_test_dir   =  "./../data_test/"

store_dir       = "./../11_cqt"
store_train_dir = "./../11_cqt/data_train"
store_test_dir  = "./../11_cqt/data_test"

if not os.path.exists(store_dir):
    os.makedirs(store_dir)

if not os.path.exists(store_train_dir):
    os.makedirs(store_train_dir)

if not os.path.exists(store_test_dir):
    os.makedirs(store_test_dir)

#For Testing
get_data_cqt_test(data_test_dir, store_test_dir, 0)

#For Training 
get_data_cqt_train(data_train_dir, store_train_dir, 1)

