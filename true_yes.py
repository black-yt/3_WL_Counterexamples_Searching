from itertools import permutations
import numpy as np

def subgraph_A(A, index):
    subgraph_nodes_count = len(index)
    sub_A = np.zeros([subgraph_nodes_count, subgraph_nodes_count])
    for i in range(subgraph_nodes_count):
        for j in range(subgraph_nodes_count):
            sub_A[i, j] = A[index[i], index[j]]
            
    return sub_A

def true_yes(A1, A2):
    nodes_count = A1.shape[0]
    if list(np.sort(A1.flatten())) != list(np.sort(A2.flatten())):
        print('non-isomorphic for sure')
        return 0
    if list(np.sort(np.sum(A1, 0))) != list(np.sort(np.sum(A2, 0))):
        print('non-isomorphic for sure')
        return 0
    
    if nodes_count <= 8: 
        for perm in permutations(range(nodes_count), nodes_count):
            A2_new = subgraph_A(A2, list(perm))
            if list(A2_new.flatten()) == list(A1.flatten()):
                print('isomorphic for sure')
                return 1
    else:
        index_1 = []
        half_nodes_count = int(nodes_count/2)
        for i in range(half_nodes_count):
            index_1.append(i)
        half_A1 = subgraph_A(A1, index_1)
        for perm in permutations(range(nodes_count), half_nodes_count):
            index_2 = list(perm)
            half_A2 = subgraph_A(A2, index_2)
            if list(half_A1.flatten()) == list(half_A2.flatten()):
                print('isomorphic for sure')
                return 1
    
    print('non-isomorphic for sure')
    return 0

def true_yes_no_print(A1, A2):
    nodes_count = A1.shape[0]
    if list(np.sort(A1.flatten())) != list(np.sort(A2.flatten())):
        return 0
    for perm in permutations(range(nodes_count), nodes_count):
        A2_new = np.zeros([nodes_count, nodes_count])
        for i in range(nodes_count):
            for j in range(nodes_count):
                A2_new[i, j] = A2[perm[i], perm[j]]
                
        if list(A2_new.flatten()) == list(A1.flatten()):
            return 1
        
    return 0