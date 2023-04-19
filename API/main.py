from flask import Flask, request
import nltk
from nltk.tree import Tree
from itertools import combinations
import json


app = Flask(__name__)

#Open parahrases in browser
@app.route('/')
def get():
    with open('../expected-result-example.json') as f:
        paraphrases = json.load(f)
    return paraphrases
        
#Find all NP and  Generate paraphrases
@app.route('/paraphrases')
def query_example():
    # Find all NP
    
    tree = request.args.get('tree')
    tree = Tree.fromstring(tree)
    np_groups = []
    for subtree in tree.subtrees():
        if subtree.label() == 'NP' and len(subtree.leaves()) > 1:
            np_groups.append(subtree)
            
    # Generate paraphrases
     
    num_np_children = len(np_groups)

    for i, j in combinations(range(num_np_children), 2):
        np1, np2 = np_groups[i], np_groups[j]
        new_children = [child for child in tree if child not in (np1, np2)]
        new_children.insert(i, np2)
        new_children.insert(j, np1)
        new_node = nltk.tree.Tree(tree.label(), new_children)

    return f"<h1>Find all NP:</h1>  {np_groups}\n <h1>Generate parahrases</h1> {new_node}"
        


if __name__ == "__main__":
    app.run(debug=True)

