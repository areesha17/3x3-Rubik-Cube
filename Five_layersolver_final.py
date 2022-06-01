###Rotation_Functions###

def rotation(matrix,clockwise=True):
    m=[[None, None, None], [None, None, None], [None, None, None]]
    for x in range(3):
        for y in range(3):
            m[y][x]=matrix[x][y]
    if clockwise==True:
        for x in range(3):
            m[x]=m[x][::-1]
    else:
        m=m[::-1]
    return m

def U(matrix,ind,reverse=False):
    if ind==0:
        s=0
    elif ind==2:
        s=5
    if reverse==False:
        matrix[1][ind],matrix[2][ind],matrix[3][ind],matrix[4][ind]=matrix[4][ind],matrix[1][ind],matrix[2][ind],matrix[3][ind]
    else:
        matrix[1][ind],matrix[2][ind],matrix[3][ind],matrix[4][ind]=matrix[2][ind],matrix[3][ind],matrix[4][ind],matrix[1][ind]
    if (ind==0 and reverse==False) or (ind==2 and reverse==True):
        matrix[s]=rotation(matrix[s],False)
    elif (ind==0 and reverse==True) or (ind==2 and reverse==False):
        matrix[s]=rotation(matrix[s],True)
    return matrix

def V(matrix,ind,reverse=False):
    if ind==0:
        s=1
    elif ind==2:
        s=3
    for x in range(3):
        if reverse==True:
            matrix[0][x][ind],matrix[2][x][ind],matrix[5][x][ind],matrix[4][2-x][2-ind]=matrix[2][x][ind],matrix[5][x][ind],matrix[4][2-x][2-ind],matrix[0][x][ind]
        else:
            matrix[0][x][ind],matrix[2][x][ind],matrix[5][x][ind],matrix[4][2-x][2-ind]=matrix[4][2-x][2-ind],matrix[0][x][ind],matrix[2][x][ind],matrix[5][x][ind]
    if (ind==0 and reverse==False) or (ind==2 and reverse==True):
        matrix[s]=rotation(matrix[s],True)
    elif (ind==0 and reverse==True) or (ind==2 and reverse==False):
        matrix[s]=rotation(matrix[s],False)
    return matrix

def W(matrix,ind,reverse=False):    #ind is the index of row of white face which is rotating
    ind=2-ind
    if ind==0:
        s=4
    elif ind==2:
        s=2
    for x in range(3):
        if reverse==True:
            matrix[0][ind][x],matrix[3][x][2-ind],matrix[5][2-ind][2-x],matrix[1][2-x][ind]=matrix[1][2-x][ind],matrix[0][ind][x],matrix[3][x][2-ind],matrix[5][2-ind][2-x]
        else:
            matrix[0][ind][x],matrix[3][x][2-ind],matrix[5][2-ind][2-x],matrix[1][2-x][ind]=matrix[3][x][2-ind],matrix[5][2-ind][2-x],matrix[1][2-x][ind],matrix[0][ind][x]
    if (ind==0 and reverse==False) or (ind==2 and reverse==True):
        matrix[s]=rotation(matrix[s],True)
    elif (ind==0 and reverse==True) or (ind==2 and reverse==False):
        matrix[s]=rotation(matrix[s],False)
    return matrix

###Cube_Input_and_Formation###

def validity_formation(cube_input):
    color_check=[]
    for color in cube_input:
        if color not in color_check:
            color_check.append(color)
    indicator=True
    for each_color in color_check:
        if cube_input.count(each_color)==9:
            pass
        else:
            indicator=False
    if indicator:
        top_1_white=[0,1,2,3,4,5,6,7,8]
        left_2_green=[9,10,11,21,22,23,33,34,35]
        front_3_red=[12,13,14,24,25,26,36,37,38]
        right_4_blue=[15,16,17,27,28,29,39,40,41]
        back_5_orange=[18,19,20,30,31,32,42,43,44]
        bottom_6_yellow=[45,46,47,48,49,50,51,52,53]
        initial_state=[]
        initial_state.append(top_1_white)
        initial_state.append(left_2_green)
        initial_state.append(front_3_red)
        initial_state.append(right_4_blue)
        initial_state.append(back_5_orange)
        initial_state.append(bottom_6_yellow)
        ###
        temp1=[]
        temp2=[]
        rubik_cube=[]
        count=0
        for each_side in initial_state:
            for indexes in each_side:
                temp1.append(cube_input[indexes])
                count+=1
                if count==3:
                    temp2.append(temp1)
                    count=0
                    temp1=[]
            rubik_cube.append(temp2)
            temp2=[]
        return (rubik_cube)
    else:
        return ('Invalid State')

###String_From_State###

def string_maker(cube):
    string=''
    for row in cube[0]:
        for color in row:
            string+=color
    for row in range(3):
        for x in range(1,5):
            for color in cube[x][row]:
                string+=color
    for row in cube[5]:
        for color in row:
            string+=color
    return string

###Graph_Making_and_Solver###

def five_level_solver(cube_input_u,cube_input_s):
    solved_cube=validity_formation(cube_input_s)
    unsolved_cube=validity_formation(cube_input_u) 
    solved_cube_string=string_maker(solved_cube)
    unsolved_cube_string=cube_input_u
    if unsolved_cube!='Invalid State':
        stack1=[]
        stack2=[]
        stack1.append(solved_cube_string)
        cube_graph=dict() 
        for x in range(5):
            while stack1:
                vary=stack1.pop()
                if len(cube_graph)==0:
                    cube_graph[vary]=[None,None]
                    stack2.append(vary)
                else:
                    stack2.append(vary)
            while stack2:
                var=stack2.pop()
                var1=validity_formation(var)
                var2=validity_formation(var)
                var3=validity_formation(var)
                var4=validity_formation(var)
                var5=validity_formation(var)
                var6=validity_formation(var)
                var7=validity_formation(var)
                var8=validity_formation(var)
                var9=validity_formation(var)
                var10=validity_formation(var)
                var11=validity_formation(var)
                var12=validity_formation(var)
                #
                state1=['U1',string_maker(U(var1,0,False))]
                if state1[1] not in cube_graph:
                    cube_graph[state1[1]]=[state1[0],var]
                stack1.append(state1[1])
                #
                state2=['U2',string_maker(U(var2,2,False))]
                if state2[1] not in cube_graph:
                    cube_graph[state2[1]]=[state2[0],var]
                stack1.append(state2[1])
                #
                state3=['U`1',string_maker(U(var3,0,True))]
                if state3[1] not in cube_graph:
                    cube_graph[state3[1]]=[state3[0],var]
                stack1.append(state3[1])
                #
                state4=['U`2',string_maker(U(var4,2,True))]
                if state4[1] not in cube_graph:
                    cube_graph[state4[1]]=[state4[0],var]
                stack1.append(state4[1])
                #
                state5=['V1',string_maker(V(var5,0,False))]
                if state5[1] not in cube_graph:
                    cube_graph[state5[1]]=[state5[0],var]
                stack1.append(state5[1])
                #
                state6=['V2',string_maker(V(var6,2,False))]
                if state6[1] not in cube_graph:
                    cube_graph[state6[1]]=[state6[0],var]
                stack1.append(state6[1])
                #
                state7=['V`1',string_maker(V(var7,0,True))]
                if state7[1] not in cube_graph:
                    cube_graph[state7[1]]=[state7[0],var]
                stack1.append(state7[1])
                #
                state8=['V`2',string_maker(V(var8,2,True))]
                if state8[1] not in cube_graph:
                    cube_graph[state8[1]]=[state8[0],var]
                stack1.append(state8[1])
                #
                state9=['W1',string_maker(W(var9,0,False))]
                if state9[1] not in cube_graph:
                    cube_graph[state9[1]]=[state9[0],var]
                stack1.append(state9[1])
                #
                state10=['W2',string_maker(W(var10,2,False))]
                if state10[1] not in cube_graph:
                    cube_graph[state10[1]]=[state10[0],var]
                stack1.append(state10[1])
                #
                state11=['W`1',string_maker(W(var11,0,True))]
                if state11[1] not in cube_graph:
                    cube_graph[state11[1]]=[state11[0],var]
                stack1.append(state11[1])
                #
                state12=['W`2',string_maker(W(var12,2,True))]
                if state12[1] not in cube_graph:
                    cube_graph[state12[1]]=[state12[0],var]
                stack1.append(state12[1])
        if unsolved_cube_string in cube_graph:
            moves=[]
            var=cube_graph[unsolved_cube_string][1]
            moves.append(cube_graph[unsolved_cube_string][0])
            while var!=None:
                if cube_graph[var][0]!=None:
                    moves.append(cube_graph[var][0])
                var=cube_graph[var][1]
            final_moves=[]
            for each_move in range(len(moves)):
                if len(moves[each_move])==3:
                    string=moves[each_move][0]+moves[each_move][2]
                    final_moves.append(string)
                else:
                    string=moves[each_move][0]+'`'+moves[each_move][1]
                    final_moves.append(string)
            print(final_moves)
            print(solved_cube)
        else:
            print('Cube can not be solved under five moves.')
    else:
        return 'Invalid State'
print('Output is going to take around 5-10 seconds')
solved_cube='wwwwwwwwwgggrrrbbbooogggrrrbbbooogggrrrbbboooyyyyyyyyy'
fivetimestangled='wwbwwbbowggwrbgryyooowggrrwrbrbobwoogggrrrbobyyyyyyogy'
five_level_solver(fivetimestangled,solved_cube)
