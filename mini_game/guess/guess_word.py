import random
def main():
    word="mareeswaran"
    length=len(word)
    dash=get_int(word)
    word1,word2=split_word(dash,word,length)
    check=get_ans(word1,word2)
    result=check_word(word,check)
    print("Correct Answer is :",word)


def get_int(word):
    length=len(word)
    dash=random.randint(0,length)
    return dash

def split_word(dash,word,length):
    word1,word2=word[0:dash-1],word[dash:length]
    return word1,word2

def get_ans(word1,word2):
    print(f"word : {word1}_{word2}")
    ans=input("guess the missing letter: ")
    result=word1+ans+word2
    return result
    
def check_word(word,check):
    if word==check:
        print("correct answer")
    else:
        print("wrong answer")

main()
