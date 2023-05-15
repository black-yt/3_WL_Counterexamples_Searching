import numpy as np
from itertools import permutations

# hash in color initialization 
# sub_A_all[i] --> color_all[i]
color_all = []
color_max = 0
sub_A_all = []

# hash in aggregation
# case_all[i] --> color_all_agg[i]
color_all_agg = []
color_max_agg = 0
case_all = []

def subgraph_A(A, index):
    subgraph_nodes_count = len(index)
    sub_A = np.zeros([subgraph_nodes_count, subgraph_nodes_count])
    for i in range(subgraph_nodes_count):
        for j in range(subgraph_nodes_count):
            sub_A[i, j] = A[index[i], index[j]]
            
    return sub_A


def get_index(index_count, nodes_count, k):
    index = []
    for i in range(0, k):
        index.append(0)
    for i in range(0, k):
        index_count, index[k - i - 1] = divmod(index_count, nodes_count)
    return index


def k_wl_test(A1, A2, k):
    nodes_count = A1.shape[0]
    size = []
    for i in range(0, k):
        size.append(nodes_count)
    k_tuples_1 = np.zeros(size)
    k_tuples_2 = np.zeros(size)
    
    global color_all, color_max, sub_A_all
    # color initialization A1===================================    
    index_count = 0
    while index_count < nodes_count**k:
        index_now = get_index(index_count, nodes_count, k)
        index_count = index_count + 1
        flag_is_colored = 0
        for perm in permutations(range(k), k):
            if flag_is_colored == 1:
                break
            index_pai = list(np.zeros([k, 1],dtype=int))#[0, 0, 0]
            for iii in range(0, k):  
                index_pai[iii] = index_now[perm[iii]]
            sub_A_pai = list(subgraph_A(A1, index_pai).flatten())
            if sub_A_pai in sub_A_all:
                if k == 2:
                    k_tuples_1[index_now[0], index_now[1]] = color_all[sub_A_all.index(sub_A_pai)]
                if k == 3:
                    k_tuples_1[index_now[0], index_now[1], index_now[2]] = color_all[sub_A_all.index(sub_A_pai)]
                if k == 4:
                    k_tuples_1[index_now[0], index_now[1], index_now[2], index_now[3]] = color_all[sub_A_all.index(sub_A_pai)]
                flag_is_colored = 1
        
        if flag_is_colored == 0:
            sub_A_all.append(sub_A_pai)
            color_max = color_max + 1
            color_all.append(color_max)
            if k == 2:
                k_tuples_1[index_now[0], index_now[1]] = color_max
            if k == 3:
                k_tuples_1[index_now[0], index_now[1], index_now[2]] = color_max
            if k == 4:
                k_tuples_1[index_now[0], index_now[1], index_now[2], index_now[3]] = color_max
    
    # color initialization A2===================================    
    index_count = 0
    while index_count < nodes_count**k:
        index_now = get_index(index_count, nodes_count, k)
        index_count = index_count + 1
        flag_is_colored = 0
        for perm in permutations(range(k), k):
            if flag_is_colored == 1:
                break
            index_pai = list(np.zeros([k, 1],dtype=int))#[0, 0, 0]
            for iii in range(0, k):  
                index_pai[iii] = index_now[perm[iii]]
            sub_A_pai = list(subgraph_A(A2, index_pai).flatten())
            if sub_A_pai in sub_A_all:
                if k == 2:
                    k_tuples_2[index_now[0], index_now[1]] = color_all[sub_A_all.index(sub_A_pai)]
                if k == 3:
                    k_tuples_2[index_now[0], index_now[1], index_now[2]] = color_all[sub_A_all.index(sub_A_pai)]
                if k == 4:
                    k_tuples_2[index_now[0], index_now[1], index_now[2], index_now[3]] = color_all[sub_A_all.index(sub_A_pai)]
                flag_is_colored = 1
        
        if flag_is_colored == 0:
            sub_A_all.append(sub_A_pai)
            color_max = color_max + 1
            color_all.append(color_max)
            if k == 2:
                k_tuples_2[index_now[0], index_now[1]] = color_max
            if k == 3:
                k_tuples_2[index_now[0], index_now[1], index_now[2]] = color_max
            if k == 4:
                k_tuples_2[index_now[0], index_now[1], index_now[2], index_now[3]] = color_max
    
    # print('t = 0')
    if list(np.sort(k_tuples_1.flatten())) != list(np.sort(k_tuples_2.flatten())):
        print('non-isomorphic')
        return 0
    
    global color_all_agg, color_max_agg, case_all
    # color aggregation===================================
    k_tuples_1_t = np.zeros_like(k_tuples_1) 
    k_tuples_2_t = np.zeros_like(k_tuples_2) 
    
    flag_stop = 0
    for t in range(1, nodes_count**k + 1):
        if flag_stop == 1:
            break
        print('t =', t)
        
        # A1 color aggregation===================================
        index_count = 0
        while index_count < nodes_count**k:
            index_now = get_index(index_count, nodes_count, k)
            index_count = index_count + 1
            
            if k == 2:
                neighbor_1th = list(np.sort(k_tuples_1[:,index_now[1]]))
                neighbor_2th = list(np.sort(k_tuples_1[index_now[0],:]))
                case_now = [k_tuples_1[index_now[0], index_now[1]], neighbor_1th, neighbor_2th]
            if k == 3:
                neighbor_1th = list(np.sort(k_tuples_1[:, index_now[1], index_now[2]]))
                neighbor_2th = list(np.sort(k_tuples_1[index_now[0], :, index_now[2]]))
                neighbor_3th = list(np.sort(k_tuples_1[index_now[0], index_now[1], :]))
                case_now = [k_tuples_1[index_now[0], index_now[1], index_now[2]], neighbor_1th, neighbor_2th, neighbor_3th]
            if k == 4:
                neighbor_1th = list(np.sort(k_tuples_1[:, index_now[1], index_now[2], index_now[3]]))
                neighbor_2th = list(np.sort(k_tuples_1[index_now[0], :, index_now[2], index_now[3]]))
                neighbor_3th = list(np.sort(k_tuples_1[index_now[0], index_now[1], :, index_now[3]]))
                neighbor_4th = list(np.sort(k_tuples_1[index_now[0], index_now[1], index_now[2], :]))
                case_now = [k_tuples_1[index_now[0], index_now[1], index_now[2], index_now[3]], neighbor_1th, neighbor_2th, neighbor_3th, neighbor_4th]
            
            if case_now in case_all:
                if k == 2:
                    k_tuples_1_t[index_now[0], index_now[1]] = color_all_agg[case_all.index(case_now)]
                if k == 3:
                    k_tuples_1_t[index_now[0], index_now[1], index_now[2]] = color_all_agg[case_all.index(case_now)]
                if k == 4:
                    k_tuples_1_t[index_now[0], index_now[1], index_now[2], index_now[3]] = color_all_agg[case_all.index(case_now)]
            else:
                color_max_agg = color_max_agg + 1
                color_all_agg.append(color_max_agg)
                case_all.append(case_now)
                if k == 2:
                    k_tuples_1_t[index_now[0], index_now[1]] = color_max_agg
                if k == 3:
                    k_tuples_1_t[index_now[0], index_now[1], index_now[2]] = color_max_agg
                if k == 4:
                    k_tuples_1_t[index_now[0], index_now[1], index_now[2], index_now[3]] = color_max_agg
            
        if list(k_tuples_1_t.flatten()) == list(k_tuples_1.flatten()):
            print('Graph 1 reach equilibrium')
            flag_stop = 1
        # print(k_tuples_1_t)
        k_tuples_1 = k_tuples_1_t
        k_tuples_1_t = np.zeros_like(k_tuples_1)
        
        # A2 color aggregation===================================
        index_count = 0
        while index_count < nodes_count**k:
            index_now = get_index(index_count, nodes_count, k)
            index_count = index_count + 1
            
            if k == 2:
                neighbor_1th = list(np.sort(k_tuples_2[:,index_now[1]]))
                neighbor_2th = list(np.sort(k_tuples_2[index_now[0],:]))
                case_now = [k_tuples_2[index_now[0], index_now[1]], neighbor_1th, neighbor_2th]
            if k == 3:
                neighbor_1th = list(np.sort(k_tuples_2[:, index_now[1], index_now[2]]))
                neighbor_2th = list(np.sort(k_tuples_2[index_now[0], :, index_now[2]]))
                neighbor_3th = list(np.sort(k_tuples_2[index_now[0], index_now[1], :]))
                case_now = [k_tuples_2[index_now[0], index_now[1], index_now[2]], neighbor_1th, neighbor_2th, neighbor_3th]
            if k == 4:
                neighbor_1th = list(np.sort(k_tuples_2[:, index_now[1], index_now[2], index_now[3]]))
                neighbor_2th = list(np.sort(k_tuples_2[index_now[0], :, index_now[2], index_now[3]]))
                neighbor_3th = list(np.sort(k_tuples_2[index_now[0], index_now[1], :, index_now[3]]))
                neighbor_4th = list(np.sort(k_tuples_2[index_now[0], index_now[1], index_now[2], :]))
                case_now = [k_tuples_2[index_now[0], index_now[1], index_now[2], index_now[3]], neighbor_1th, neighbor_2th, neighbor_3th, neighbor_4th]
            
            if case_now in case_all:
                if k == 2:
                    k_tuples_2_t[index_now[0], index_now[1]] = color_all_agg[case_all.index(case_now)]
                if k == 3:
                    k_tuples_2_t[index_now[0], index_now[1], index_now[2]] = color_all_agg[case_all.index(case_now)]
                if k == 4:
                    k_tuples_2_t[index_now[0], index_now[1], index_now[2], index_now[3]] = color_all_agg[case_all.index(case_now)]
            else:
                color_max_agg = color_max_agg + 1
                color_all_agg.append(color_max_agg)
                case_all.append(case_now)
                if k == 2:
                    k_tuples_2_t[index_now[0], index_now[1]] = color_max_agg
                if k == 3:
                    k_tuples_2_t[index_now[0], index_now[1], index_now[2]] = color_max_agg
                if k == 4:
                    k_tuples_2_t[index_now[0], index_now[1], index_now[2], index_now[3]] = color_max_agg
            
        if list(k_tuples_2_t.flatten()) == list(k_tuples_2.flatten()):
            print('Graph 2 reach equilibrium')
            flag_stop = 1
        # print(k_tuples_2_t)
        k_tuples_2 = k_tuples_2_t
        k_tuples_2_t = np.zeros_like(k_tuples_2)
        
        if list(np.sort(k_tuples_1.flatten())) != list(np.sort(k_tuples_2.flatten())):
            print('non-isomorphic')
            return 0
    
    # print('============hash===========')
    # for i in range(0, len(case_all)):
    #     print(case_all[i], 'color:', color_all_agg[i])
    
    if list(np.sort(k_tuples_1.flatten())) != list(np.sort(k_tuples_2.flatten())):
        print('non-isomorphic')
        return 0
    print('maybe isomorphic')
    return 1
    