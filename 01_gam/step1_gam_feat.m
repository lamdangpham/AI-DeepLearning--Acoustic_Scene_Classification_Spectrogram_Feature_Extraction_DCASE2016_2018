addpath(genpath('./gam_featset'))

% 01/ Draw data directory %TODO
opts.data_train_dir  =  './../data_train/';
opts.data_test_dir   =  './../data_test/';

% 02/ Saved whole spectrogram directory %TODO
mkdir('./../11_gam')
mkdir('./../11_gam/data_train')
mkdir('./../11_gam/data_test')
opts.save_train_dir  =  './../11_gam/data_train/';
opts.save_test_dir   =  './../11_gam/data_test/';

% 03/ Call function to generate spectrogram

%for testing data
fprintf('================================== Creating Testing File\n');
get_data_gam_test(opts,0);

%for training data
fprintf('================================== Creating Training File\n');
get_data_gam_train(opts,1);
