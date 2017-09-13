# Translator

In this project I wanna use machine learning create a translator(but use words from self translate, yes self translate style), this need lots data, but I will try first. so there are things I wanna do

[ ] create translation data, both language
[ ] create ml model, train it
[ ] test the ml model

now I have done(just copy other code) such things:
* a simple seq2seq model, input and output all just numbers
* in the seq2seq model I changed the orignal model's output as random sequence too
  __so I have to change the loss function and maybe also train way__

during translation, words will be encoded to sequence of numbers, so such simple model is the base of how it works
