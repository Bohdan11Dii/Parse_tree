from flask import Flask, request, jsonify
import nltk
from nltk.tree import Tree
from itertools import combinations
from flask_restful import Api, Resource
import json


app = Flask(__name__)
api = Api()


with open('../expected-result-example.json') as f:
        paraphrases = json.load(f)
for item in paraphrases["paraphrases"]:
    for key, value in item.items():
        # print(key)
        pass


# @app.route('/paraphrase')
def paraphrase_tree(tree_string, limit=20):
  
    tree = Tree.fromstring(s)
    
    # Find all NP groups
    np_groups = []
    for subtree in tree.subtrees():
        if subtree.label() == 'NP' and len(subtree.leaves()) > 1:
            np_groups.append(subtree)
    
    print({"tree":np_groups } )
    
    
    # Generate paraphrases
    num_np_children = len(np_groups)

    for i, j in combinations(range(num_np_children), 2):
        np1, np2 = np_groups[i], np_groups[j]
        new_children = [child for child in tree if child not in (np1, np2)]
        new_children.insert(i, np2)
        new_children.insert(j, np1)
        new_node = nltk.tree.Tree(tree.label(), new_children)
    # print(new_node)


paraphrase_tree("(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (NNS clubs)) (, ,) (NP (JJ trendy) (NNS bars)) (CC and) (NP (JJ Catalan) (NNS restaurants))))))))")




    


# output.draw()