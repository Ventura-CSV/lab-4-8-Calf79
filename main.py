def main():
    plist = []
    ##################################################
    # Comlete your code here
    ##################################################
    begin = int(input(f'Enter 1st Value'))
    end = int(input(f'Enter 2nd Value greater than 1st'))
    if begin <=1 or end <1 or begin>end:
        print('Retry')
    else:    
        for num in range(begin,end+1,1):
            prime=True
            if num>1: 
                for i in range(2,num):
                    if (num%i) ==0:
                        prime=False
                        break
                if prime:
                    plist.append(num)
        print(plist)
        return plist
if __name__ == '__main__':
    main()



