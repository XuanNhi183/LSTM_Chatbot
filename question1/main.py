from linklist import Linklist
from node import Node

print("add <data> at beg")
print("add <data> at end")
print("add <data> after <index>")
print("add <data> before <index>")
print("delete head")
print("delete tail")
print("delete node <index>")
print("delete data <data>")
print('count number of nodes')
print("sum")
print("average")
print("max")
print("min")
print("sort")
print("insert <data>")
print("search data <data>")
print("array")

def main():
    link_list = Linklist()
    while True:
        link_list.display()
        print()
        print("---------------")
        reponse = input("your reponse: ")
        answer = reponse.split()
        
        if answer[0] == 'quit':
            break

        # add Node to the list
        if answer[0] == 'add':
            data = answer[1]
            new_node = Node(data)
            if answer[2] == 'at':
                if answer[3] == 'end':
                    link_list.addToTail(new_node)
                elif answer[3] == 'beg':
                    link_list.addToHead(new_node)
                else:
                    pass
            elif answer[2] == 'after':
                link_list.addAfter(new_node, int(answer[3]))
            elif answer[2] == 'before':
                if answer[3] == '1':
                    link_list.addToHead(new_node)
                else:
                    link_list.addBefore(new_node, int(answer[3]))
            else:
                pass

        # delete Node from the list
        elif answer[0] == 'delete':
            if answer[1] == 'head':
                link_list.deleteFromHead()
            elif answer[1] == 'tail':
                link_list.deleteFromTail()
            elif answer[1] == 'node':
                if int(answer[2]) == 1:
                    link_list.deleteFromHead()
                else:
                    pass
            elif answer[1] == 'data':
                link_list.Delete_firstnode_data(answer[2])
            else:
                pass
        
        # sorting
        elif answer[0] == 'sort':
            link_list.sort()
        
        # insert
        elif answer[0] == 'insert':
            data = answer[1]
            new_node = Node(data)
            link_list.addToTail(new_node)
            link_list.sort()
        
        # check sorting
        elif answer[0] == 'check':
            print(link_list.sorted())

        # search node in the list
        elif answer[0] == 'search':
            print(link_list.search(answer[2]))

        # average of the data number in the list
        elif answer[0] == 'average':
            print("average = ", link_list.avg(link_list.Sum()))

        # count node in the list
        elif answer[0] == 'count':
            print(link_list.count())

        # sum all the data number in the list
        elif answer[0] == 'sum':
            print("sum of nodes in linklist = ", link_list.Sum())
        
        elif answer[0] == 'max':
            print(link_list.Max())
        
        elif answer[0] == 'min':
            print(link_list.Min())        
        
        # change the list into form of an array
        elif answer[0] == 'array':
            print(link_list.toArray())
            
        # handling of error reponse
        else:
            print("i dont know what u meaned, pls write ur reponse again: ")

main()