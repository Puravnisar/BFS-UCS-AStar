import time
start_time = time.time() # To measure the overall execution time for the search
import math
import heapq
p=open("input1.txt","r") # Open the input text file
data=list()
data1= p.readlines() # Read all the lines in the input
count=0
for line in data1:
    count+=1
    data.append(line.split())         
queue=list()
w= int(data[1][0]) # Width of the input grid
h= int(data[1][1]) # Height of the input grid
parent=[[ -1 for i in range(w)] for j in range(h)] # Creating an array to maintain the parent nodes of the input grid 
adj =list()
landing=[int(data[2][0]),int(data[2][1])] # Getting the landing location in the input grid
threshold=int(data[3][0]) # Storing the maximum allowed elevation difference bewtween two points
no_of_targets=int(data[4][0]) # Reading total number of targets 
targetsfound=0 # Initializing the number of targets found
targetsite=list() # Creating a list to maintian target points
for i in range(5,5+no_of_targets):
    targetsite.append([int(data[i][0]),int(data[i][1])])
for i in range(5+no_of_targets,count): #Converting the character data to integer 
   for j in range(w):            
       data[i][j]=int(data[i][j])
   adj.append(data[i])     
result=["FAIL" for i in range(no_of_targets)] #Intializing the result array
visited=[[0 for i in range(w)] for j in range(h)] 
v= landing
queue.append(v)
p.close()
       
def BFS():
    global targetsfound,result
    visited[int(landing[1])][int(landing[0])]=1
    while(1):        
        if not queue:
           break
        else: 
              v=queue.pop(0)
        if(v in targetsite):
           targetsfound+=1
           index= targetsite.index(v)
           result[index]="PASS"
        if(targetsfound == no_of_targets):
            break
        else:
            j=v[0]
            i=v[1] 
            if(i-1 >= 0 and i-1 <h and j>=0 and j<w):
               if(visited[i-1][j]==0): 
                  if(abs(adj[i-1][j]-adj[i][j])<= threshold):
                       queue.append([j,i-1])
                       parent[i-1][j]= [j,i]
                       visited[i-1][j]=1
            if(i-1 >= 0 and i-1 <h and j+1>=0 and j+1<w):
               if(visited[i-1][j+1]==0): 
                  if(abs(adj[i-1][j+1]-adj[i][j])<= threshold):
                       queue.append([j+1,i-1])
                       parent[i-1][j+1]= [j,i]
                       visited[i-1][j+1]=1  
            if(i >= 0 and i<h and j+1>=0 and j+1<w):
               if(visited[i][j+1]==0): 
                  if(abs(adj[i][j+1]-adj[i][j])<= threshold):
                       queue.append([j+1,i])
                       parent[i][j+1]= [j,i]
                       visited[i][j+1]=1
            if(i+1 >= 0 and i+1 <h and j+1>=0 and j+1<w):
               if(visited[i+1][j+1]==0): 
                  if(abs(adj[i+1][j+1]-adj[i][j])<= threshold):
                       queue.append([j+1,i+1])
                       parent[i+1][j+1]= [j,i]
                       visited[i+1][j+1]=1
            if(i+1 >= 0 and i+1 <h and j>=0 and j<w):
               if(visited[i+1][j]==0): 
                  if(abs(adj[i+1][j]-adj[i][j])<= threshold):
                       queue.append([j,i+1])
                       parent[i+1][j]= [j,i]
                       visited[i+1][j]=1
            if(i+1 >= 0 and i+1 <h and j-1>=0 and j-1<w):
               if(visited[i+1][j-1]==0): 
                  if(abs(adj[i+1][j-1]-adj[i][j])<= threshold):
                       queue.append([j-1,i+1])
                       parent[i+1][j-1]= [j,i]
                       visited[i+1][j-1]=1
            if(i >= 0 and i <h and j-1>=0 and j-1<w):
               if(visited[i][j-1]==0): 
                  if(abs(adj[i][j-1]-adj[i][j])<= threshold):
                       queue.append([j-1,i])
                       parent[i][j-1]= [j,i]
                       visited[i][j-1]=1
            if(i-1 >= 0 and i-1 <h and j-1>=0 and j-1<w):
               if(visited[i-1][j-1]==0): 
                  if(abs(adj[i-1][j-1]-adj[i][j])<= threshold):
                       queue.append([j-1,i-1])
                       parent[i-1][j-1]= [j,i]
                       visited[i-1][j-1]=1
    counter=range(no_of_targets) 
    final = result
    for i in counter:
     if(result[i]!="FAIL"):
          v=targetsite[i]
          y=v[0]
          x=v[1]
          final[i]=(str(v[0]) + "," + str(v[1]))
          r=parent[x][y]
          while(r!= -1):
               a= r[1]
               b= r[0] 
               final[i]=str(r[0])+","+str(r[1])+" "+final[i]
               x=a
               y=b
               r=parent[x][y]
    o=open("output.txt","w+")
    wc=0
    while(wc < no_of_targets-1):
          o.write(final[wc]+"\n")
          wc+=1
    o.write(final[wc])
    o.close()
    
                 
if __name__ == '__main__': 
     if("BFS" in data[0]):
        BFS()
     elif ("UCS" in data[0]):
        UCS()
     else: 
        Astar()

print(time.time() - start_time)         