import re

class Counts():
    def __init__(self,input):
        self.wordCount(input)
        self.sentenceCount(input)
        self.exclamationCount(input)
        self.atSymbol(input)
        self.hashtag(input)
        self.dollar(input)
        self.percentage(input)
        self.caret(input)
        self.signWord(input)
        self.asterisk(input)
        self.braces(input)
        self.interrogative(input)

    def wordCount(self,input):
        space = re.compile('\s')
        result = space.findall(input)
        print("WordCount : ",len(result)+1)

    def sentenceCount(self,input):
        Dot = re.compile('\.')
        result = Dot.findall(input)
        print("sentenceCount : ",len(result))

    def exclamationCount(self,input):
        Exclamation = re.compile('\!')
        result = Exclamation.findall(input)
        print("exclamationCount : ",len(result))

    def atSymbol(self,input):
        at = re.compile('\@')
        result = at.findall(input)
        print("atSysmbols : ",len(result))

    def hashtag(self,input):
        Hash = re.compile('\#')
        result = Hash.findall(input)
        print("Hashes : ",len(result))

    def dollar(self,input):
        at = re.compile('\$')
        result = at.findall(input)
        print("Dollar : ",len(result))

    def percentage(self,input):
        percent = re.compile('\%')
        result = percent.findall(input)
        print("percentage : ",len(result))

    def caret(self,input):
        caret = re.compile('\^')
        result = caret.findall(input)
        print("caret  : ",len(result))

    def signWord(self,input):
        sign = re.compile('\&')
        result = sign.findall(input)
        print("signWord : ",len(result))

    def asterisk(self,input):
        asterisk = re.compile('\*')
        result = asterisk.findall(input)
        print("Asterisk : ",len(result))

    def braces(self,input):
        braces = re.compile(r'(\()([a-z]{0,10000000})(\))')
        result = braces.findall(input)
        print("Brace words : ",len(result))

    def interrogative(self,input):
        question = re.compile('\?')
        result = question.findall(input)
        print("Interragative : ",len(result))

sentence = input('Enter sentence: ')
result = Counts(sentence)













