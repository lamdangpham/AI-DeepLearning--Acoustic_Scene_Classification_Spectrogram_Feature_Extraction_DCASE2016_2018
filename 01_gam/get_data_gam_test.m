
function get_data_gam_test(opts, is_train)  

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

file_dir = [data_dir, '/'];
file_struct = dir(file_dir);
file_name_list = {file_struct.name};  
file_name_list(strncmp(file_name_list,'.',1))=[];%remove files that start with a dot  
[nRow, file_num] = size(file_name_list);
%--------------------------------------------------------------------------------  
 
for nFile = 1:file_num  
    file_name = file_name_list{nFile};
    [filepath,new_file_name,ext] = fileparts(file_name);
    new_file_name = [new_file_name, '.mat'];
    des_file  = [save_dir, '/',new_file_name];

    % 02/ Read draw audio file
    [org_wave,fs]=audioread([file_dir, file_name_list{nFile}]); 
    wave = org_wave(:,1) + eps; 
    [D,~] =  gammatonegram(wave, fs, window_size, hop_size, gam_fil_num, min_freq, fs/2, gam_opt);

    % 05/ Save the whole spectrogram into one file
    clear data;
    data = D;
    save(des_file, 'data') ;  
    if(mod(nFile,100) == 0)
        fprintf('Done extracting testing features for file %s \n',file_name);  
    end
end % end of all files

fprintf('======================= Done extracting testing features \n');  

end %function  
