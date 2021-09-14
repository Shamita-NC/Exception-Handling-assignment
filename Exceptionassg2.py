#Problem 2
Subject=['Americans','Indians']
Verb=['play','watch']
Object=['Baseball','Cricket']
for sub in Subject:
    for ver in Verb:
        for obj in Object:
            all_sentences=sub+" "+ver+" "+obj
            for i in all_sentences:
                print(i,end='')
            print("\n")