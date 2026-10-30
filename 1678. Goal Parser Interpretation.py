class Solution(object):
    def interpret(self, command):
        a=''
        for i in range(len(command)):
            if command[i]=='G':
                a+='G'
            elif command[i] == '(' and command[i+1] == ')':
                a += 'o'
            elif command[i] == '(' and command[i+1] == 'a':
                a += 'al'
        return a
