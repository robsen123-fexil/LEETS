class last_word:
    def solution(self, s:str)->int:
        splt=s.split()
        lastindex=splt[-1]
        count=0
        for i in lastindex:
            count+=1
        return count    
