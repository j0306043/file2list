import ast;

def list_to_file(lst,file_name):
    with open(file_name,'w') as f:
        for element in lst:
            f.write(repr(element)+'\n')
    return

def file_to_list(file_name):
    with open(file_name,'r') as f:
        return [ast.literal_eval(line.rstrip('\n')) for line in f if line[0] != '#']

if __name__ == '__main__':
    print('This is file2list.py.')
