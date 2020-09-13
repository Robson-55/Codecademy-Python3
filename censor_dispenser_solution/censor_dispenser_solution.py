# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_function(word,email):
  return email.replace(word,"--")
#print(censor_function("learning algorithms",email_one))

def censor_lists(lists,email):
  for item in lists:
    email=email.replace(item,'---')
  return email

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

#print(censor_lists(proprietary_terms,email_two))

def censor_double(negatives,email):
  for negative in negatives:
    if email.count(negative)>1:
      email=email.replace(negative,'++++')
  email=censor_lists(proprietary_terms,email_three)
  return email

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#print(censor_double(negative_words,email_three))

def final_censor(list1,list2,email):
  email_list=email.split()
  i=0
  for word in email_list:
    for negative in list1:
      if negative==word:
        email_list[i]='N!!!!'
        email_list[i-1]='+++++'
        email_list[i+1]='+++++'
    for item in list2:
      if item==word:
        email_list[i]='---'
        email_list[i-1]='+++++'
        email_list[i+1]='+++++'
    i+=1
  email_list=" ".join(email_list)
  return email_list

print(final_censor(negative_words,proprietary_terms,email_four))













