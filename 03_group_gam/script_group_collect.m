% For saving TODO
mkdir('./../12_group_gam');
mkdir('./../12_group_gam/data_train');
mkdir('./../12_group_gam/data_test');
opts.save_train_dir = './../12_group_gam/data_train/';
opts.save_test_dir  = './../12_group_gam/data_test/';

% For input data TODO
opts.train_dir  =  '../11_gam/data_train/';
opts.test_dir   =  '../11_gam/data_test/';


%for training data
fprintf('================================== Creating File Group of Train File\n');
group_file(opts,1);

%========================================================================================%
function group_file(opts, is_training)

% 01/ Parameter 
fileID = fopen('./mapping_file.log','w');
nfile_every_group = 3;  %TODO

% 01/ Directory 
if is_training   %TODO
    n_file_vec = [78;
                  78; 
                  78;
                  78;
                  78;
                  78;
                  78;
                  78;
                  78;
                  78;
                  78;
                  78;
                  78;
                  78;
                  78;
                 ];  
    data_dir = opts.train_dir;
    save_dir = opts.save_train_dir;    
else
    n_file_vec = [0;   
                  0;   
                  0;   
                  0;   
                  0;   
                  0;   
                  0;   
                  0;   
                  0;   
                  0;   
                  0;   
                  0;   
                  0;   
                  0;   
                  0;   
                 ];  
    data_dir = opts.test_dir;
    save_dir = opts.save_test_dir;    
end
max_num_file = max(n_file_vec);

% 03/ Handle Class
class_dir = dir(data_dir);  
class_name_list = {class_dir.name};  
class_name_list(strncmp(class_name_list,'.',1))=[];
class_name_list = sort(class_name_list);
[nRow, class_num] = size(class_name_list);


for nClass=1:class_num
%for nClass=3:3
    fprintf(fileID,  '\n\n ================= CLASS: %d  \n',nClass);
    fprintf('\n\n ================= CLASS: %d  \n',nClass);

    %01. Handle file 
    class_name=class_name_list{nClass};  
    file_dir=dir([data_dir,class_name,'/']);  
    file_name_list={file_dir.name};  
    file_name_list(strncmp(file_name_list,'.',1))=[];
    [nRow, nFileList] = size(file_name_list);

    %add files to form a list that is multiple of nfile_every_group 
    real_file_num  = n_file_vec(nClass,1);
    group_num = ceil(max_num_file/nfile_every_group);

    need_file_num = group_num*nfile_every_group; 
    add_file_num = need_file_num - real_file_num;
    add_file_list = randi(real_file_num, 1, add_file_num);

    clear file_list_rand;
    file_list_rand = randperm(nFileList);
    file_list_rand = [file_list_rand add_file_list];  %add more files to equal maximum group

    % for verifying
    [nRow, nCol] = size(file_list_rand);
    if (nCol ~= need_file_num)
        fprintf('ERROR: Stop at class: %s due to number of files \n', class_name);
        pause	
    end	
    for i=1:nCol
        if(file_list_rand(1,i) > real_file_num)	    
            fprintf('ERROR: Stop at class: %s due to number of files \n', class_name);
	    pause
        end    
    end

    for nGroup=1:group_num
    %for nGroup=1:1
        save_group_dir = [save_dir,class_name,'/group_',num2str(nGroup)];
	mkdir(save_group_dir);
        stFile = (nGroup-1)*nfile_every_group + 1;
        edFile = nGroup*nfile_every_group;
        fprintf(fileID,  '\n================= GROUP: %d  \n',nGroup);
        fprintf('\n================= GROUP: %d  \n',nGroup);
        for nCpFile=stFile:edFile
	    file_copy = [data_dir, class_name,'/',file_name_list{file_list_rand(nCpFile)}];


            [filepath,new_file_name,ext] = fileparts(file_name_list{file_list_rand(nCpFile)});

            file_name_des = [new_file_name,'_',num2str(nCpFile),'.npy'];

	    file_des  = [save_group_dir, '/', file_name_des];
            fprintf(fileID,  'Original file: %s -- %s \n',file_name_list{file_list_rand(nCpFile)},file_name_des );
            
            copyfile(file_copy, file_des);
        end
    end %end group

    fprintf('================= Finish grouping for class %s \n', class_name);
end %end class

if is_training
    fprintf('================= Finish grouping for training data \n');
end

end %end function
