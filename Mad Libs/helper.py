''' get_keys() function: returns a list containing all keys inside the formatString
    formatString is a format string with embedded dictionary keys.
    Source: http://anh.cs.luc.edu/handsonPythonTutorial/madlib2.html
    '''
def get_keys(formatString):
    keyList = list()
    end = 0
    n = formatString.count('{')                   # counts number of '{' brackets
    for i in range(n):                      
        start = formatString.find('{', end) + 1   # finds next '{', then skips it
        end = formatString.find('}', start)       # finds next '}' 
        key = formatString[start : end]           # saves string (key) between brackets
        keyList.append(key)                       # adds key to list  
    return set(keyList) # removes duplicates: no duplicates in a set
