import sys

def ReadInput():
    fname = ""
    mPrefs = {}
    fPrefs = {}
    if len(sys.argv) > 2:
        exit(1)
    else:
        fname = sys.argv[1]
    
    f = open(fname,"r")
    n = int(f.readline())
    
    for i in range(n):
        line = f.readline()
        names = line.split()
        mPrefs[names[0]] = names[1:]
    
    for i in range(n):
        line = f.readline()
        names = line.split()
        fPrefs[names[0]] = names[1:]

    return mPrefs, fPrefs


def GetMatches(mPrefs, fPrefs):
    mMatches = {key: "" for key in mPrefs}
    wMatches = {key: "" for key in fPrefs}
    
    # while unengaged knights exist
    while "" in mMatches.values():
        for k, v in mPrefs.items():
            
            if mMatches[k] == "":
                prop = v.pop(0)
                if wMatches[prop] == "":
                    mMatches[k] = prop
                    wMatches[prop] = k

                else:
                    oldMatch = wMatches[prop]
                    for val in fPrefs[prop]:
                        #if proposer is more desirable than current match
                        if val == k:
                            mMatches[k] = prop
                            wMatches[prop] = k
                            mMatches[oldMatch] = ""
                            break

                        elif val == oldMatch:
                            break

    return mMatches
            
def PrintOutput(matches):
    for key, value in matches.items():
        print(key + " " + value)
    pass

if __name__ == "__main__":
    mPrefs, fPrefs = ReadInput()
    matches = GetMatches(mPrefs, fPrefs)
    PrintOutput(matches)

