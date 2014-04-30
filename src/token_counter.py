import sys

def get_many_tokens(loc):
	fr_data = open(loc)

	counter = 0
	sentence_counter = 0
	output = ""
	first_two_k = True;
	for i,sent in enumerate(fr_data):
		if len(sent.split(' ')) > 30:
			continue
		output += sent
		sentence_counter += 1
		counter += len(sent.split(' '))
		if counter > 2000 and first_two_k:
			first_two_k = False;
			output = ""
			sentence_counter = 0;
		elif counter > 4000 and not first_two_k:
			print 'breaking on sentence ', i
			print 'with this many tokens: ', counter
			print 'from this many sentences: ', sentence_counter
			return output

def put_in_conll_format(text):
	conll = ""
	for line in text.split('\n'):
		token_counter = 0
		for token in line.split(' '):
			token_counter += 1
			if sys.argv[3] == 'pos':
				t = token.split('_')[0];
				pos = token.split('_')[1];
				conll += `token_counter` + '\t' + t + '\t' + pos + '\t_' * 3 + '\t' + `token_counter` + '\t_' * 3 + '\n'
			else:
				conll += `token_counter` + '\t' + token + '\t_' * 4 + '\t' + `token_counter` + '\t_' * 3 + '\n'
		conll += '\n'
	return conll

def save(text):
	fr_out = open('../1000lines/europarl-v7.fr-en.fr.2000-4000token.conll', 'w')
	fr_out.write(text)
	fr_out.close()


if __name__=='__main__':
	out = get_many_tokens(sys.argv[1])
	print len(out)
	conll = put_in_conll_format(out)
	save(conll)
