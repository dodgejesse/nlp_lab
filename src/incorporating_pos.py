import sys


def output_combination(anno_data, pos_data, loc):
    token_counter = 0;
    conll_lines = anno_data.split('\n')
    out = '';
    
#    print len(pos_data.split('\n'))
    for line in pos_data.split('\n'):
#        print line
        if len(line.split(' ')) > 30:
            continue;
        for token in line.split(' '):
            out_line_conll = conll_lines[token_counter].split('\t');
            pos = token.split('_')[1];
#            print out_line_conll
#            print token
#            print
            out_line_conll[3] = pos;
            out_line_conll[7] = '_';
            out_line = out_line_conll[0];
            for i in range(1, len(out_line_conll)):
                out_line = out_line + '\t' + out_line_conll[i]
            print out_line
            out += out_line + '\n';
            token_counter += 1;
        out = out + '\n';
        token_counter += 1;
    return out;

if __name__=='__main__':
    anno_data = open(sys.argv[1]).read();
    pos_data = open(sys.argv[2]).read();
    combined_text = output_combination(anno_data, pos_data, sys.argv[3])
    out_file = open(sys.argv[3], 'w');
    out_file.write(combined_text);
