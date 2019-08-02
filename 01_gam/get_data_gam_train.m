
function get_data_gam_train(opts, is_train)  

%=================== Parameters for Gammatone filter Spectrogram
gam_fil_num = 128;     
window_size = 0.04;    
hop_size    = 0.0053;  
min_freq    = 10;      
gam_opt     = 1;       

%=================== Behavior

% 01/ Setup directory
if is_train %train  
    data_dir = opts.data_train_dir;  
    save_dir = opts.save_train_dir;  
else        %test  
    data_dir = opts.data_test_dir;  
    save_dir = opts.save_test_dir;  
end  

% 02/ Handle class
class_struct = dir(data_dir);  
class_name_list = {class_struct.name};  
class_name_list(strncmp(class_name_list,'.',1))=[];%remove files that start with a dot  
[nRow, class_num] = size(class_name_list);

for nClass=1:class_num
    % Handle file directory 
    class_name=class_name_list{nClass};  
    class_save_dir = [save_dir, class_name];
    mkdir(class_save_dir);

    file_dir = [data_dir, class_name,'/'];
    file_struct = dir(file_dir);
    file_name_list = {file_struct.name};  
    file_name_list(strncmp(file_name_list,'.',1))=[];%remove files that start with a dot  
    [nRow, file_num] = size(file_name_list);
    %--------------------------------------------------------------------------------  
     
    tic % Star timer     
    for nFile = 1:file_num  
        file_name = file_name_list{nFile};
        [filepath,new_file_name,ext] = fileparts(file_name);
        new_file_name = [new_file_name, '.mat'];
	des_file  = [class_save_dir, '/',new_file_name];

        % 02/ Read draw audio file
        [org_wave,fs]=audioread([file_dir, file_name_list{nFile}]); 

        % 03/ Read one main channel, could gennerate many spectrogram due to channel number, channel mean, difference between channels  
	wave = org_wave(:,1) + eps; 
        [D,~] =  gammatonegram(wave, fs, window_size, hop_size, gam_fil_num, min_freq, fs/2, gam_opt);

        % 05/ Save the whole spectrogram into one file
        clear data;
        data = D;
        save(des_file, 'data') ;  

    end % end of all files in a class  
    
    if is_train  
        fprintf('Done extracting training features for class %d: %s \n', nClass, class_name_list{nClass});  
    else
        fprintf('Done extracting testing features for class %d: %s \n', nClass, class_name_list{nClass});  
    end 

end %end all classes


end %function  
