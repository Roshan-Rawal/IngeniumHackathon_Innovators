from flask import Flask, request, render_template
import os
import json
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("pt.html")



@app.route('/getresult',methods=['POST'])
def getresult():
    if request.method == "POST":
        # try:

        print("########",request.args)

        body = request.data
        a = json.loads(body.decode('utf-8'))
        print(a)

        with open("pt_1.csv","r",encoding="utf8") as fp:
            c1 = NaiveBayesClassifier(fp)

        #w = c1.classify(a)
        prob_list = c1.prob_classify(a)
        print(prob_list.max())
        ab = prob_list.max()
        print("Ex ",round(prob_list.prob("Ex"),3))
        print("In", round(prob_list.prob("In"),3))

        #if w==''

        #print(w)    
       

        # if ans is not None:   
        #   return ans
        # else:
        #   return 'none'
        # except:
        #   return "excetions"
        #return str(a)
    return str(ab)
            

if __name__ == '__main__':
    app.run(debug = True)
