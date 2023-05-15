import numpy as np
from k_wl import k_wl_test
from true_yes import true_yes, true_yes_no_print
from itertools import permutations

if __name__ == "__main__":
    aa, bb, cc, dd, ee, ff = 20, 30, 40, 50, 60, 70
    adj_int = np.array([[round(aa**0.7, 4), round(bb**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4), round(ee**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4)],
                        [round(bb**0.7, 4), round(aa**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(ee**0.7, 4), round(dd**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4)],
                        [round(bb**0.7, 4), round(cc**0.7, 4), round(aa**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ee**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4)],
                        [round(cc**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(aa**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4), round(ee**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4)],
                        [round(cc**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(aa**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ee**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4)],
                        [round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(aa**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ee**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4)],
                        [round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4), round(aa**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ee**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4)],
                        [round(cc**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(aa**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ee**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4)],
                        [round(dd**0.7, 4), round(ee**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(aa**0.7, 4), round(bb**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4)],
                        [round(ee**0.7, 4), round(dd**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4), round(aa**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4)],
                        [round(ff**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ee**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(aa**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4)],
                        [round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4), round(ee**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(aa**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4)],
                        [round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ee**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(aa**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4)],
                        [round(ff**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ee**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(aa**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4)],
                        [round(ff**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ee**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4), round(aa**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4)],
                        [round(dd**0.7, 4), round(ff**0.7, 4), round(ee**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(aa**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4)],
                        [round(cc**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(aa**0.7, 4), round(dd**0.7, 4), round(bb**0.7, 4), round(ee**0.7, 4)],
                        [round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4), round(aa**0.7, 4), round(ee**0.7, 4), round(bb**0.7, 4)],
                        [round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(dd**0.7, 4), round(bb**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(bb**0.7, 4), round(ee**0.7, 4), round(aa**0.7, 4), round(dd**0.7, 4)],
                        [round(ff**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(dd**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(ff**0.7, 4), round(cc**0.7, 4), round(bb**0.7, 4), round(ee**0.7, 4), round(bb**0.7, 4), round(dd**0.7, 4), round(aa**0.7, 4)]])
    adj_int = np.array(adj_int * 10000, dtype=int)
                            
    nodes_pair_1 = [0, 1, 2, 3, 4, 5, 6, 7, 16, 18]
    nodes_pair_2 = [9, 8, 15, 14, 13, 12, 11, 10, 19, 17]
    
    get_example = []
    #=============================================================================
    flag = 0 
    try_no = 1
    find_graph_with_nodes = 4 # half
    
    perm_1_index = 0
    for perm_1 in permutations(range(10), find_graph_with_nodes):
        perm_1_index = perm_1_index + 1
        if flag == 1:
            break
        is_this_perm_small_to_big = 1
        for ppp in range(len(list(perm_1)) - 1):
            if perm_1[ppp] > perm_1[ppp + 1]:
                is_this_perm_small_to_big = 0
                break
        if is_this_perm_small_to_big == 0:
            continue
        
        perm_2_index = 0
        for perm_2 in permutations(range(10), find_graph_with_nodes):
            perm_2_index = perm_2_index + 1
            if perm_1_index >= perm_2_index:
                continue
            if flag == 1:
                break
            is_this_perm_small_to_big = 1
            for ppp in range(len(list(perm_2)) - 1):
                if perm_2[ppp] > perm_2[ppp + 1]:
                    is_this_perm_small_to_big = 0
                    break
            if is_this_perm_small_to_big == 0:
                continue
            
            graph_1_half = []
            graph_2_half = []
            for ii in range(find_graph_with_nodes):
                graph_1_half.append(nodes_pair_1[perm_1[ii]])
                graph_2_half.append(nodes_pair_1[perm_2[ii]])
            
            half_count = len(graph_1_half)
            adj_half = np.zeros([half_count, half_count])
            for i in range(0, half_count):
                for j in range(0, half_count):
                    adj_half[i, j] = adj_int[graph_1_half[i], graph_1_half[j]]
            
            A1_half = adj_half
            
            adj_half = np.zeros([half_count, half_count])
            for i in range(0, half_count):
                for j in range(0, half_count):
                    adj_half[i, j] = adj_int[graph_2_half[i], graph_2_half[j]]
            
            A2_half = adj_half
            if true_yes_no_print(A1_half, A2_half) == 1:
                continue
            
            print('++++++++++++++++++++++++++ NO.', try_no, '+++++++++++++++++++++++++')
            try_no = try_no + 1
            
            graph_1_all = graph_1_half
            half_num = len(graph_1_half)
            for i in range(0, half_num):
                if graph_1_half[i] in nodes_pair_1:
                    graph_1_all.append(nodes_pair_2[nodes_pair_1.index(graph_1_half[i])])
                else:
                    graph_1_all.append(nodes_pair_1[nodes_pair_2.index(graph_1_half[i])])

            graph_2_all = graph_2_half
            half_num = len(graph_2_half)
            for i in range(0, half_num):
                if graph_2_half[i] in nodes_pair_1:
                    graph_2_all.append(nodes_pair_2[nodes_pair_1.index(graph_2_half[i])])
                else:
                    graph_2_all.append(nodes_pair_1[nodes_pair_2.index(graph_2_half[i])])
                    
            graph_pair = [graph_1_all, graph_2_all]
            print('===========choose============')
            print(graph_pair)
            
            #=============================================================================  
            choose_nodes = graph_pair[0]
            # picture_choose(points, choose_nodes)
            choose_nodes_count = len(choose_nodes)
            adj_choose = np.zeros([choose_nodes_count, choose_nodes_count])
            for i in range(0, choose_nodes_count):
                for j in range(0, choose_nodes_count):
                    adj_choose[i, j] = adj_int[choose_nodes[i], choose_nodes[j]]
            # print(choose_nodes)
            # print(adj_choose)
            A1 = adj_choose

            choose_nodes = graph_pair[1]
            # picture_choose(points, choose_nodes)
            choose_nodes_count = len(choose_nodes)
            adj_choose = np.zeros([choose_nodes_count, choose_nodes_count])
            for i in range(0, choose_nodes_count):
                for j in range(0, choose_nodes_count):
                    adj_choose[i, j] = adj_int[choose_nodes[i], choose_nodes[j]]
            # print(choose_nodes)
            # print(adj_choose)
            A2 = adj_choose
            #=============================================================================  
            print('===========test============')
            if true_yes(A1, A2) == 1:
                continue
            else:
                if k_wl_test(A1, A2, 3) == 1:
                    get_example.append(graph_pair)
                    flag = flag + 1
                    
    print('===========get examples============')
    for i in range(len(get_example)):
        print(get_example[i])