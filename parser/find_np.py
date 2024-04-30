import hanlp

HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)
noun = ["NR","NN","NT","FW"]
before_noun = ["DT","JJ","DEC","DEG"]
determiner = ["DEC","DEG"]
before_det = ["VV","VA"]
stop_word = ["VC","VE","VV","SP","PU"]

# initialize
test_sentence = "以色列安全內閣決定，不對本星期發生的汽車炸彈襲擊事件進行報復。以色列把這次爆炸事件歸咎於巴勒斯坦人，但是以色列受於巴拉克總理全權決定如何回應未來的襲擊事件，這個決定是在星期四晚間的內閣會議中做出的"
category = HanLP(test_sentence,tasks=["tok/fine", "pos/ctb","con"])

token_list = category["tok/fine"]
tag_list = category["pos/ctb"]
tree = category["con"]
np_list = []

# separate np
'''
不可能出現在頭尾的詞性:AD/AS/BA/CC/CS/DEC/DEG/DER/DEV/ETC/EM/IJ/LC/M/MSP/PU/SP/VC/VE/VV
可以出現的:CD/DT/FW/JJ/LB/NN/NOI/NR/NT/OD/P/PN/SB/URL/VA
'''
np = ""
for (i,tag),j in zip(enumerate(tag_list),token_list):
    print("index:",i,",value :",tag)
    if tag in noun: #check if it's a noun
        np = np + j
        print("noun :",np)
    elif(i+1 == len(tag_list)): #the last element
        break
    elif tag in before_noun: #check if it's a ()+noun
        if (tag_list[i+1]) in noun:
            np = np + j
            print("before noun :",np)
        else:
            print(np)
            if((np != "") and (np not in np_list)):np_list.append(np)
            print(np_list)
            np = ""
    elif tag in before_det: #check if it's a ()+DEC
        if tag_list[i+1] in determiner:
            np = np + j
            print("before determiner :",np)
        else:
            print(np)
            if((np != "") and (np not in np_list)):np_list.append(np)
            print(np_list)
            np = ""
    else:
        print(np)
        if((np != "") and (np not in np_list)):np_list.append(np)
        print(np_list)
        np = ""

# final result
print(np_list)
# correct answer
print("correct answer : 以色列安全內閣、本星期發生的汽車炸彈襲擊事件、這次爆炸事件、巴勒斯坦人、巴拉克總理、未來的襲擊事件、這個決定、星期四晚間的內閣會議")

# test
'''
tmp = str(tree)
tmp = token_list[0] + token_list[2]
np_list.append(token_list[0])
np_list.append(token_list[3])
'''
# print(type("VC"))
# print(type(tag_list[0]))