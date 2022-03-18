# Recursive Python function to solve the tower of hanoi
 
def Move(n , source, destination, auxiliary):
    if n==1:
        print (source," --> ",destination)
        return
    Move(n-1, source, auxiliary, destination)
    print (source," --> ",destination)
    Move(n-1, auxiliary, destination, source)

def main():
    print("Please enter how many disks to move:")
    disks = int(input())
    if disks > 0:
       Move(disks, 1, 3, 2)
    else:
       print("Must be greater than zero.") 

if __name__== "__main__" :
    main()
