def matchingStrings(strings, queries,r=0):
    result = [] 
    for q in queries: 
        result.append(strings.count(q)) 
    return result

