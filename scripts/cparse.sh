STANFORD_PATH="/Users/chris/Documents/School/CL2_Fall/StatNLP/Project/AMRParsing/stanfordnlp/stanford-parser"

java -Xmx1800m -cp $STANFORD_PATH/stanford-parser-3.3.1-models.jar:$STANFORD_PATH/stanford-parser.jar edu.stanford.nlp.parser.lexparser.LexicalizedParser -tokenized -sentences newline edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz $1
