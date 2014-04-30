import sys

def fix_with(line):
    new_line = [];
    
    for i in range(0, len(line)):
        if line[i].split('_')[0] != "'":
            new_line.append(line[i]);
#    print 'before: ', line
#    print 'after: ', new_line
    return new_line

def count_tokens(without_pos, with_pos):
    without_data = open(without_pos).read();
    with_data = open(with_pos).read();
    tokens = 0;
    line_num = 0;
    for line in without_data.split('\n'):
        
        without_tokens = len(line.split(' '));
        with_tokens = len(with_data.split('\n')[line_num].split(' '));
        if without_tokens != with_tokens:
            new_with = fix_with(with_data.split('\n')[line_num].split(' '));
            if len(new_with) == without_tokens:
                print 'fixed!'
            else:    
                print `without_tokens` + 'vs' + `with_tokens`
                print line
                print with_data.split('\n')[line_num]
                print
        line_num += 1;
    print

if __name__=='__main__':
    count_tokens(sys.argv[1], sys.argv[2]);
