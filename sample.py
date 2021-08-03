import file2list as fl

lis1=fl.file_to_list('sample_read.txt')
print('lis1='+repr(lis1))
fl.list_to_file(lis1,'sample_write.txt')
lis2=fl.file_to_list('sample_write.txt')
print('lis2='+repr(lis2))
