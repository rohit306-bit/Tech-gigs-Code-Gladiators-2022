import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here


#iterate the loop for the test case
for _ in range(int(input())):
    #input defined in above problem
    N=int(input()) #no.of gifts to be bought
    G=int(input()) #no.of gifts available on shop
    #create a list to insert the amount of money of each gifts
    gift_price=list(map(int,input().split()))
    #now sort the above list
    gift_price.sort()
    #now easily get the sum from minimum cost
    min_money=sum(gift_price[:N])
    print(min_money)
