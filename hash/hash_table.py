
class Hash_table(object):
    def __init__(self):
        self.hash =[]
        for i in range(13):
            self.hash.append([])
    def insert(self,num):
        ind=num%13
        self.hash[ind].append(num)

    def delete(self,num):
        ind=num%13
        if self.hash[ind]:
            self.hash[ind].remove(num)

    def display(self, key):
        ind=key%13
        if self.hash:
           if self.hash[ind]:
               print ind,
               print self.hash[ind]
           else:
               print 'NO mathcing entry'

