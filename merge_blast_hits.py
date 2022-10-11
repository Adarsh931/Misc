# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:44:03 2022

@author: Adarsh singh 

A function to merge overlapping blast hits for different databases or hits through various methods based on start and end of the hit

Input is list of list of start and end of hits where start is always smaller than end

"""
#import pandas as pd

def merge_blast_hits(li):
    #Making hits in order
    for i in range(len(li)):
        if li[i][0] > li[i][1]:
            li[i] = [li[i][1], li[i][0]]
    #print(li)
    mod_hit = sorted(li, key=lambda x: x[0])
    #print(mod_hit)
    hit_gap = 1
    count = 1
    new_count = 0
    new_hit = list([mod_hit[new_count]])
    #print(new_hit)
    while(True):
        if count >= len(mod_hit):
            break
        elif mod_hit[count][0] - new_hit[new_count][1] <= hit_gap:
            #print("Overlap!!")
            new_hit[new_count] = [min(new_hit[new_count][0], mod_hit[count][0]), max(new_hit[new_count][1], mod_hit[count][1])]
            count += 1
        else:
            new_hit.append(mod_hit[count])
            new_count += 1
            count += 1
        #print(new_hit)
    return(new_hit)

if __name__ == '__main__':
    #Making sure start is less than end
    hits = [[1,5], [10, 7], [3, 9], [4, 15], [20, 25]]
    final_hit = merge_blast_hits(hits)
