#-*-coding:utf-8-*-
import copy
"""
词语接龙：给定开始的词语和结束的词语，搜索词语字典中词语，只修改其中的一个词汇，实现接龙
1. 开始和结束词汇必须是所给的词汇
2. 每个词汇在一次接龙中只会出现一次
input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
output:  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
"""

def wordLadder2(beginWord,endWord,wordL):
    """
    :param beginWord:str
    :param endWord: str
    :param wordList: list
    :return: list, array<array>
    """
    def findWord(target, wordlist):
        if target != None:
            cnt = 0
            i = 0
            flag = True
            n = len(target)
            for j in range(n):
                if target[j] != endWord[j]:
                    cnt += 1
            if cnt == 1:
                return cnt, endWord, wordlist
            while i < len(wordlist) and flag:
                cnt = 0
                if len(wordlist[i]) == n:
                    for j in range(n):
                        if target[j] != wordlist[i][j]:
                            cnt += 1
                print '--', i, target, wordlist[i], cnt
                if cnt != 1:
                    i += 1
                else:
                    flag = False
                    #wordlist.pop(i)
            if flag == False:
                word = wordlist[i]
                print '++', i, target, word, wordlist
                wordlist.pop(i)
                return i, word, wordlist
            else:
                return i, None, None
        else:
            return None, None, None
    def listAppend(dele, word, wordlist):
        res = [beginWord, word]
        while wordlist != None and dele < len(wordlist) and word != endWord and wordlist != []:
            dele, word, wordlist = findWord(word, wordlist)
            res.append(word)
            print '==', dele, word, wordlist, res
        if word == endWord:
            result.append(res)
    result = []
    delete = 0
    wordLt = copy.deepcopy(wordL)
    i = 0
    while wordLt != None and delete <= len(wordLt):
        print '!!!!!!!!!!!!!', i, wordL
        delete, Word, wordLt = findWord(beginWord, wordLt)
        print delete, Word, wordL, result
        wordLL = copy.deepcopy(wordL)
        listAppend(delete, Word, wordLL)
        i += 1
    return result

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print wordLadder2(beginWord, endWord, wordList)