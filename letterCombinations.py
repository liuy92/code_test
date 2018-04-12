#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
输入相应的元素组合，得到所有键盘对应的元素的可能组合值
input: "23"
output:["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""

def letterCombinations(digits):
    """
    :param digits:string
    :return: list(string)
    """
    phone_dict = dict(zip(['1','2','3','4','5','6','7','8','9','*','0','#'], [None,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz','+','@','$']))
    def getVal(res, si):
        vi = phone_dict.get(si)
        if vi != None:
            if len(res) == 0:
                return list(vi)
            else:
                res_new = []
                for vj in vi:
                    for j in res:
                        res_new.append(j+vj)
                return res_new
        else:
            return res
