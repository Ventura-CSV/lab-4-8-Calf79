def main():
    plist = []
    ##################################################
    # Comlete your code here
    ##################################################
    begin = int(input(f'Enter 1st Value'))
    end = int(input(f'Enter 2nd Value greater than 1st'))
    for num in range(begin,end):
        if num>1: 
            for i in range(2,num):
                if num%i ==0:
                    break
                else:
                    plist.append(num)
                    print(num)
if __name__ == '__main__':
    main()
