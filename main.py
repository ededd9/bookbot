def main():
    #print(readText())
    print(countWords())
    reportdict = dict(sorted(countChars().items(),key=lambda item: item[-1],reverse=True))

    
    for word in reportdict:
        print(f"The '{word}' character was found {reportdict[word]} times")
    
def readText():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
def countWords():
    words = readText().split()
    return len(words)
    return count
def countChars():
    loweredwords = readText().lower()
    dict = {}
    for word in loweredwords:
        if word in dict:
            dict[word]+=1
        else:
            dict[word] = 1
    return dict






main()
