import networkx as nx
import numpy as np
import scipy

def iterate_graph(gsp, rows):
    f = open("p0.05-100kgraph.txt", "w")
    indices = gsp.indices   #[4 5 8 5 0 7 1 3 6 5 8 4 9 1 6 7]
    indptr = gsp.indptr     #[0 1 3 3 4 6 9 11 13 15 16]
    print indptr
    print indices
    count = 0
    for i in range(0, rows ):
        row_nzero_eles = indptr[i+1] - indptr[i]
        #print row_nzero_eles
        f.write(str(i))
        f.write(" "+ str(row_nzero_eles))
        for j in range(0, row_nzero_eles):
            if (row_nzero_eles == 0):
                print "000000"
            #print  str(i) + " " +  str(indices[count])
            f.write(" " + str(indices[count]))
            count = count + 1
        f.write("\n")
        f.flush()

# probabililty of any edge                                    
p = 0.05 # Alter as necessary                                  

# number of nodes                                             
n = 100000 # Alter as necessary                                 

g = nx.erdos_renyi_graph(n, p,False)                          
gsp = nx.to_scipy_sparse_matrix(g)                            

#print g.edges()                                              
print gsp.todense()                                           
iterate_graph(gsp, 100000)                                      
#print gsp.todense() 
