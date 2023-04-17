# python3

def read_input():
    
    comand = input()
    if comand[0] == 'I':
        searchFor = input().rstrip()
        text = input().rstrip()
    elif comand[0] == 'F':
        file = open('./tests/'+'06','r')
        searchFor = file.readline().rstrip()
        text = file.readline().rstrip()
    if 1<=len (searchFor)<=len (text)<=(5*10**5):
        return (text, searchFor)
    else:
        exit()

def print_occurrences (output):

    print(' '.join (map (str, output)))

def get_occurrences (patern, text):
    
    copy = patern
    location = 0
    cutoff = 0
    occurances = []
    while cutoff<len(patern):
        location = copy.find (text)
        if (location<0):
            break
        occurances.append (location+cutoff)

        copy = copy[location+1:len(copy)]
        cutoff = cutoff + location+1
    return occurances

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
