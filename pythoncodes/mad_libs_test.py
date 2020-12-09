import random
#from guizero import App, Text, PushButton


def new_insult():
    new_insult = insult_me()
    message.value = new_insult





user_a = input('enter a word')
user_b = input('enter a word')
user_c = input('enter a word')
user_d = input('enter a word')
user_e = input('enter a word')
user_f = input('enter a word')
user_g = input('enter a word')
user_h = input('enter a word')



with open("mad_libs.csv", "r") as f:
    contents = f.readline()
list_a = []
list_b = []
list_c = []

#word_a = random.choice(list_a)
#word_b = random.choice(list_b)
#word_c = random.choice(list_c)

with open("mad_libs.csv", "r") as f:
    for line in f:
        words = line.split(",")
        list_a.append(words[0])
        list_b.append(words[0])
        list_c.append(words[0].strip())

insult = random.choices( user_a, user_b)
insult_b = random.choices(user_d, user_e)
insult_c = random.choices( user_g, user_h)
insult_d = random.choices( user_c, user_f)
print(insult)