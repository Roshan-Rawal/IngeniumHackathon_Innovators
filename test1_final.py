from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

# b = TextBlob("I havv goood speling !")
# print(b.correct())

with open("pt_1.csv","r",encoding="utf8") as fp:
    c1 = NaiveBayesClassifier(fp)

In = input("Enter the text: ")

#a = c1.classify(In) 

prob_list = c1.prob_classify(In)
print(prob_list.max())
print("Ex ",round(prob_list.prob("Ex"),3))
print("In", round(prob_list.prob("In"),3))
#print(round(prob_list.prob("In"),3)
#print(a)  

