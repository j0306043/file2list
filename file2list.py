import ast;

def list_to_file(lst,file_name):
    with open(file_name,'w') as f:
        for element in lst:
            f.write(repr(element)+'\n')
    return

def file_to_list(file_name):
    lst = []
    with open(file_name,'r') as f:
        for line in f:
            lst.append(ast.literal_eval(line.rstrip('\n')))
    return lst

if __name__ == '__main__':
    print('This is file2list.py.')
