class binarynode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)
        # Print own value
        ret += "\n" + ("    "*depth) + str(self.value)
        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)
        return ret

    def traversal(self):
        self.traversalInt(self,'')

    def traversalInt(self,node,code):
        if node.left is None and node.right is None:
            print(node.value[0],code)
        else:
            self.traversalInt(node.left,code+'0')
            self.traversalInt(node.right,code+'1')


print('Insert letters. 0 is exit')
count = 1
ultralistlist = []
del ultralistlist[:]

# while True:
#     print 'Insert letter',count
#     currletter = raw_input()
#     if currletter <> '0':
#         print 'Insert probability for', currletter
#         ultralistlist.append([currletter, float(raw_input()),0,0,0])
#         count+=1
#     else: break
ultralistlist=[binarynode(('a', 0.37), None, None),binarynode(('b', 0.22), None, None),binarynode(('c', 0.16), None, None),
               binarynode(('d', 0.14), None, None),binarynode(('e', 0.11), None, None)]


checker = 1
# for sign in ultralistlist:
#     checker -= sign.value[1]
# if checker0:
#     print checker

for sign in ultralistlist:
    print(sign)

print('')

while len(ultralistlist)>1:
    ultralistlist.sort(key=lambda x: x.value[1])
    currsign = ultralistlist[0]
    nextsign = ultralistlist[1]
    newnode=binarynode((currsign.value[0]+nextsign.value[0],currsign.value[1]+nextsign.value[1]),currsign,nextsign)
    ultralistlist.append(newnode)
    ultralistlist=ultralistlist[2:]

for sign in ultralistlist:
    print (sign)
    sign.traversal()


print('')
