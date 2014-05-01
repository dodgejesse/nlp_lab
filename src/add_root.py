import sys

def add_root_to_trees(data):
    out = '';
    sentence = '';
    for line in data.split('\n'):
        if line == '':
            out = out + add_head_to_sentence(sentence) + '\n';
            sentence = '';
        else:
            sentence += line + '\n';

    return out

def add_head_to_sentence(sent):
    if sent == '\n':
        return '';
#    print sent
    head_num = -1;
    out_sent = '';
    for i in range(0, len(sent.split('\n'))):
        if sent.split('\n')[i] == '':
            continue;
        columns = sent.split('\n')[i].split('\t');
        if columns[0] == columns[6] and columns[3] != 'PUNC':
            head_num = i;
    for token in sent.split('\n'):
        if token == '':
            continue;
        columns = token.split('\t');
#        print columns
        if columns[0] == columns[6] and columns[3] != 'PUNC':
            columns[6] = '0';
        elif columns[0] == columns[6]:
            columns[6] = `head_num + 1`;
        out_sent += columns[0];
        for i in range(1, len(columns)):
            out_sent += '\t' + columns[i];
        out_sent += '\n';
#    sys.exit(0);
    return out_sent;
    
        

if __name__=='__main__':
    anno_data = open(sys.argv[1]).read();
    new_data = add_root_to_trees(anno_data);
    out_file = open(sys.argv[2], 'w');
    out_file.write(new_data);
