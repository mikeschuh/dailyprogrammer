#
import sys


class ToDoList:
    
    def __init__(self, name):
        self.thelist = []
        self.name = name
    
    def print(self):
        print(self.name)
        print("--------")
        for i in range(len(self.thelist)):
            print("%02i. %s" % (i+1, self.thelist[i]))
        print()
        
    def add_item(self, item):
        self.thelist.append(item)
    
    def remove_item(self, num):
        del(self.thelist[num-1])
        #self.thelist = self.thelist.remove(num)
    
    
        
        
        


def test():
    
    mylist = ToDoList("mylist")
    mylist.add_item("Laundry")
    mylist.add_item("Dishes")
    mylist.print()
    mylist.remove_item(1)
    mylist.print()
    
    
    

if __name__ == "__main__":
    test()
