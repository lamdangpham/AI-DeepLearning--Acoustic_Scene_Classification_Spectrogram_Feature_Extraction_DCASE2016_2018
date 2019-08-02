import os
from get_test_data import get_test_data
from get_train_data import get_train_data
from get_pre_train_data import get_pre_train_data

# For saving data
store_dir           ='./data'
save_train_dir     = './data/data_train/'
save_test_dir      = './data/data_test/'
save_pre_train_dir = './data/data_pre_train/'

if not os.path.exists(store_dir):
    os.makedirs(store_dir)

if not os.path.exists(save_train_dir):
    os.makedirs(save_train_dir)

if not os.path.exists(save_test_dir):
    os.makedirs(save_test_dir)

if not os.path.exists(save_pre_train_dir):
    os.makedirs(save_pre_train_dir)


# For input data
data_train_dir      =  './../12_group_cqt/data_train/'
data_test_dir       =  './../11_cqt/data_test/'   #no group for test data
data_pre_train_dir  =  './../11_cqt/data_train/'   #no group for test data

#for testing data
print('================================== Creating Testing File\n')
get_test_data(save_test_dir,
               data_test_dir
              )

#for training data
print('================================== Creating Training File\n')
get_train_data(save_train_dir,
               data_train_dir
              )

