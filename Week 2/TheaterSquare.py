from math import ceil

if __name__=="__main__":

    n,m,a = map(int,input().split())
    A = ceil(n/a)
    B = ceil(m/a)
    print(int(A*B))