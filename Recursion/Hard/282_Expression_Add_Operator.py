def addOperators(self, num, target):
    result = []
    def backtrack(index,total,path,previous):
        if index == len(num):
            if total == target:
                result.append(path)
            return
        for i in range(index,len(num)):
            if i > index and num[index] == '0':
                break
            current_string = num[index:i+1]
            current_num = int(current_string)
            if index == 0:
                backtrack(i + 1,current_num,current_string,current_num)
            else:
                backtrack(i + 1,total + current_num,path + '+' + current_string,current_num)
                backtrack(i + 1,total - current_num, path + '-' + current_string ,-current_num)
                backtrack(i + 1, total - previous + previous * current_num,path + '*' + current_string,previous * current_num )
    backtrack(0,0,'',0)
    return result