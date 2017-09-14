# Translator

In this project I wanna use machine learning create a translator(but use words from self translate, yes self translate style), this need lots data, but I will try first. so there are things I wanna do

 - [ ] create translation data, both language
 - [ ] create ml model, train it
 - [ ] test the ml model

now I have done such things:
* a simple seq2seq model, input and output all just sequences of numbers
* changed the orignal seq2seq model's output to random sequence, so does the decode_target_length
* changed the train function

results:
* about loss stoped at about 1.45
* predicted outputs don'e has same length as target

during translation, words will be encoded to sequence of numbers, so such simple model is the base of how it works
