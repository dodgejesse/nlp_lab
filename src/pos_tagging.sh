#to pos tag the 200token test dataset.

java -mx300m -classpath stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTagger -model models/french.tagger -textFile /home/jesse/CMU/nlp_lab/datasets/europarl/2000token/europarl-v7.fr-en.fr.2000token > /home/jesse/CMU/nlp_lab/datasets/europarl/2000token/europarl-v7.fr-en.fr.2000token.pos


