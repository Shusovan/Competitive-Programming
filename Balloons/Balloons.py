def Cost_of_Balloons():
    
    T = int(input())        #.....Number of Test Cases

    for i in range(T):

        cost_1 , cost_2 = (0,0)        #.....initializing the costs as 0    

        green, purple = map(int, input().split())        #.....giving cost of green and purple balloons 

        N = int(input())        #.....Number of participents

        for j in range(N):

            first , second = map(int, input().split())        #.....inserting the scores of participants

            cost_1 += green * first + purple * second        #.....calculating cost of green and purple balloons

            cost_2 += purple * first + green * second        #.....calculating cost of purple and green balloons

        print(min(cost_1, cost_2))        #.....analyzing and printing the minimum cost
        
print(Cost_of_Balloons())