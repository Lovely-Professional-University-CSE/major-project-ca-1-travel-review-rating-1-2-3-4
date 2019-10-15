# major-project-ca-1-travel-review-rating-1-2-3-4
major-project-ca-1-travel-review-rating-1-2-3-4 created by GitHub Classroom
Travel Review Rating
This dataset was fairly small to do any heavy prediction work but I wanted to see if I could predict the rating of the comment  based on the review anyway! To start off I'll bring in the modules I want to use:
i)Sklearn 
ii)Pandas
iii)Numpy
iv)Matplotlib
v)Nltk

Taking a quick look at the data it became clear that were some basic issues that needed to fixed before starting. I noticed that some reviews had a '0' rating and some reviews had a rating above '5', I filtered these records out of the dataset to start and did a bit more cleaning here.
#############################
                                                        INTRODUCTION
In this project we are collecting data in which will classify the data into parts positive review and negative review we will say the positive review as class zero and negative review as class 1 by classify the review we will have a set of data
Now my having set of data will make another class which will add unnecessary word like "is am are their" which are not used for classifying the review
We are having the three classes we are ready to take input from the user in comment section.
First of all we will train our set of data so that machine can understand which are the positive and negative words.
By having training machine using SVM we are having the maximum accuracy of 95%
As this gives the best result we will use SVM in our Project.
Sets of data should be trained again and again for much better accuracy of the machine, as number of training increases the accuracy increases of the machine now we are ready for the testing.Before testing we have already done training of Machines so now it will be able to recognise the word as a positive review on negative review as we will take input from the user will classify them in three parts the words which are in class 0 as positive review the words which are in class 1 as negative review 3rd class which are having the words which are not all positive review not negative review which can cannot be used to classify the to classify the sentence as the positive or negative review now we will separate the data of positive negative review and the third class which having no review now machine can predict the review as positive and negative review depends on the words used by the user in comment section for example
The user writes "it's very good hotel" or " it's very good travel agency" there we will classify the word good as a positive review and the rest of the words are be used in 3rd class which are having no review the good word can predict the sentence as it is a positive review
Another example as sentence like" it is not satisfying the customer" now this sentence can be classified again in posterior review or negative review and words we will find here no positive what all will find the positive word but as a negative what is added like" not" a sentence become negative so here the sentence would be negative this will give a negative review of the comment
So we will use this sets class the review as positive or negative.
