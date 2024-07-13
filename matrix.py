#Matrix

def matrix(ma):
    #print(ma)
    #print(len(ma))
    for i in ma:
        for j in i:
            print(j,'\t',end="")
        print('')

mat=[
    [1,2,5,4,42],
    [3,2,5,8,98],
    [5,6,4,7,88]
]
matrix(mat)