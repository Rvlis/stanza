from stanza.server import CoreNLPClient
import os

# example text
print('---')
print('input text')
print('')

# text = "Chris Manning is a nice person. Chris wrote a simple sentence. He also gives oranges to people."

text = "PyTables is built on top of the HDF5 library, using the Python language and the NumPy package."

print(text)

# set up the client
print('---')
print('starting up Java Stanford CoreNLP Server...')

# set up the client
# with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','ner','parse','depparse','coref'], timeout=60000, memory='4G', be_quiet=True) as client:
with CoreNLPClient(annotators=['tokenize','ssplit','pos','parse','depparse'], timeout=60000, memory='4G', be_quiet=True) as client:   
    # submit the request to the server
    ann = client.annotate(text)

    # print("ann is ", ann)
    # os.system("pause")
    # get the first sentence
    sentence = ann.sentence[0]
    print("sentence is ", sentence)
    os.system("pause")

    # get the dependency parse of the first sentence
    # print('---')
    # print('dependency parse of first sentence')
    # dependency_parse = sentence.basicDependencies
    # print(dependency_parse)
    # os.system("pause")

    # HDSKG's method
    print('---')
    print('enhanced++ dependency parse of first sentence')
    enhanced_plus_plus_dependency_parse = sentence.enhancedPlusPlusDependencies
    print(enhanced_plus_plus_dependency_parse)
    os.system("pause")

    # get the constituency parse of the first sentence
    # print('---')
    # print('constituency parse of first sentence')
    # constituency_parse = sentence.parseTree
    # print(constituency_parse)
    # os.system("pause")

    # get the first subtree of the constituency parse
    # print('---')
    # print('first subtree of constituency parse')
    # print(constituency_parse.child[0])
    # os.system("pause")
    
    # get the value of the first subtree
    # print('---')
    # print('value of first subtree of constituency parse')
    # print(constituency_parse.child[0].value)
    # os.system("pause")

    # get the first token of the first sentence
    print('---')
    print('first token of first sentence')
    token = sentence.token[0]
    print(token)
    os.system("pause")

    # get the part-of-speech tag
    print('---')
    print('part of speech tag of token')
    token.pos
    print(token.pos)
    os.system("pause")

    # get the named entity tag
    print('---')
    print('named entity tag of token')
    print(token.ner)
    os.system("pause")

    # get an entity mention from the first sentence
    # print('---')
    # print('first entity mention in sentence')
    # print(sentence.mentions[0])
    # os.system("pause")

    # access the coref chain
    # print('---')
    # print('coref chains for the example')
    # print(ann.corefChain)
    # os.system("pause")

    # Use tokensregex patterns to find who wrote a sentence.
    # pattern = '([ner: PERSON]+) /wrote/ /an?/ []{0,3} /sentence|article/'
    pattern = "([tag: NNP]{1,}) ([ tag:/VB.*/ ]) /an?/ ([pos:JJ]{0,3}) /sentence|article/"
    matches = client.tokensregex(text, pattern)
    print("tokensregex matches is ", matches)
    # sentences contains a list with matches for each sentence.
    assert len(matches["sentences"]) == 3
    # length tells you whether or not there are any matches in this
    assert matches["sentences"][1]["length"] == 1
    # You can access matches like most regex groups.
    # print("sentence is ",["sentences"][1]["0"]["text"])
    matches["sentences"][1]["0"]["text"] == "Chris wrote a simple sentence"
    matches["sentences"][1]["0"]["1"]["text"] == "Chris"

    # # Use semgrex patterns to directly find who wrote what.
    # pattern = '{word:wrote} >nsubj {}=subject >dobj {}=object'
    # matches = client.semgrex(text, pattern)
    # # print("semgrex matches is", matches)
    # # sentences contains a list with matches for each sentence.
    # assert len(matches["sentences"]) == 3
    # # length tells you whether or not there are any matches in this
    # assert matches["sentences"][1]["length"] == 1
    # # You can access matches like most regex groups.
    # matches["sentences"][1]["0"]["text"] == "wrote"
    # matches["sentences"][1]["0"]["$subject"]["text"] == "Chris"
    # matches["sentences"][1]["0"]["$object"]["text"] == "sentence"

