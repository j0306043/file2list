import file2list as fl

lis1=fl.file_to_list('test_read.txt')
print('lis1='+repr(lis1))
fl.list_to_file(lis1,'test_write.txt')
lis2=fl.file_to_list('test_write.txt')
print('lis2='+repr(lis2))
