# 5번 실패
def solution(sentence: str, word: str):
    answer = 0
    list_sentence= sentence.split(" ")
    for e in list_sentence:
        if e == word:
            return answer
        answer+=1
    return -1