import os
from get_data_mel_train import get_data_mel_train
from get_data_mel_test import get_data_mel_test

data_train_dir  =  "./../data_train/"
data_test_dir   =  "./../data_test/"

store_dir       = "./../11_mel"
store_train_dir = "./../11_mel/data_train"
store_test_dir  = "./../11_mel/data_test"

if not os.path.exists(store_dir):
    os.makedirs(store_dir)

if not os.path.exists(store_train_dir):
    os.makedirs(store_train_dir)

if not os.path.exists(store_test_dir):
    os.makedirs(store_test_dir)

#For Testing
get_data_mel_test(data_test_dir, store_test_dir, 0)

#For Training 
get_data_mel_train(data_train_dir, store_train_dir, 1)

