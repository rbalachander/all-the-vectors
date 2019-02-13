# read in the vectors.txt file
# create a  list of vectors
# scale the first and last vector by 3
# add them all together and find
# that new vector
# find the norm of the final vector
# also find the dot product between the 2nd and 3rd vector
from vector import Vector
vectors = []
with open('vectors.txt') as f:
    for line in f:
        vector = list(map(int,(line.strip().split(','))))
        vectors.append(vector)
    print(vectors)

    # scale the first and last vector
    for x in range(len(vectors)):
        print(vectors[x])

        

    
        
        
       