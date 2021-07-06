#Creator Name: FAHAD ISHAQ

import random 
def main():#main function which includes the display menu at the front end
    global continues
    global grid
    global player1
    global player2
    print('\t WELCOME TO TIC TAC GAME BY FAHAD ISHAQ!\t')
    grid=[1,2,3,4,5,6,7,8,9]
    display_grid()#Displays the board on which out game takes place 
    continues=True#assigning continues true so that it can be used in the winning conditions 
    
    print('_________________________________________________')
    #followings are the three different modes in which a player wants to play
    print('\t PRESS 1 TO PLAY IN SINGLE PLAYER MODE\t')
    print('\t PRESS 2 TO PLAY IN TWO PLAYERS MODE\t')
    print('\t PRESS 3 TO PLAY A TOURNAMENT\t')
    print('\t PRESS 0 TO EXIT THE GAME\t')
    print('_________________________________________________')
    
    op=eval(input('Enter your choice:'))#Enter your choice whatever a user wants to play he just types the int nummber of the corresponding game to play the game
    if op==1:
        sub_menu()#calling one player game function
        
    elif op==2:
        two_players_game()#calling two players game function 
    elif op==3:
        tournament_game()#calling tournament game function
    elif op==0:
        exit()       #exiting the game 
    



def display_grid():#I have created a function for displaying grid aas it is called most of the times in the entire code so it has saved my time
    
    print('\t\t',grid[0],"|",grid[1],"|",grid[2],'\t\t')
    print("\t\t _________\t\t")
    print('\t\t',grid[3],"|",grid[4],"|",grid[5],'\t\t')
    print("\t\t _________\t\t")
    print('\t\t',grid[6],"|",grid[7],"|",grid[8],'\t\t')
    
def one_player_game():#Defining a function for one player game
    
    global grid #making grid global so that it can be used for all the functions called in the one_player_game() function.
    
    grid=[1,2,3,4,5,6,7,8,9]
    
    
    global continues#I have made continues global so that it can be used for all the functions called in this one_player_game() function.
    continues=True
    print('\tWELCOME TO TIC TAC SINGLE PLAYER HARD MODE\t')
    global player1#making player1 global
    
    global player2 #making player2 global 
    display_grid()#caling this function for displaying the grid 

    player1=str(input("Enter your name:"))
    print("The symbol assigned to",player1," is (O)")
    player2='Computer'
    print("The symbol assigned to ",player2, "is (X)")
    
    toss=random.randint(0,1)#making toss for one player game 
    
    print('Toss is :',toss)
    if toss==0:
        toss="o"#assigning toss a value o if it is 0, so that to make the first move of the players according to the toss.
        print(player1,"Wins the toss")
        print(player1,"will take the first move")
    else:
        toss="x"#assigning toss a value x if it is 1 so that to make the first move of the players according to the toss.
        print("COMPUTER wins the toss")
        print("COMPUTER will take the first move")
    
        
    for i in range(1,10):#I have used a for loop here that is used for 9 times
            #I have assigned the turns to the players according to the toss
        #if toss is 'o' then first turn will be of player1 then turn 2 will be of player 2 and 3 will be of player3 and so on 
        if (i==1 or i==3 or i==5  or i==7 or i==9)and toss=='o':
            player1_turn()#calling player1 function for player 1 turns
            display_grid()
        elif (i==2 or i==4 or i==6 or i==8)and toss=='o':
            
            computer_turn()#calling computer_turns function for computer turns
            display_grid()
            
        win()#calling winning conditions for checking the winning of a player
        
        if continues==False:#If any of the winning condition satisfies then game ends here. else continues
            
            print('****Game OVER****')
            break 
        if (i==2 or i==4 or i==6 or i==8)and toss=='x':#if player2 wins the toss then in this case second turn will be of player1 then 4th then 6th then 8th turn will be of player1
            
            player1_turn()#calling player's turns function
            display_grid()
        elif (i==1 or i==3 or i==5 or i==7 or i==9)and toss=='x':#if player2 that is computer here wins the toss then first turn will be of computer and then 3rd,5th 7th and 9th turn will be of player2.
            
            computer_turn()#calling computer's turns function 
            display_grid()#calling function on the indentation of the loop so that it will be executed after each selection sattement.
          
    else:#if none of the winning conditions satisfies till the 9 moves are completed then in this case the game is draw between the two playerds
        
        print('GAME DRAW')
        print('**** GAME OVER****')
    one_player_again()#calling this function for dislpaying a menu of ,playing again,back to the main menu, and exiting the game, after the game ends.
    


def player1_turn():#created a function for the player1's turns so that it can be used just by simply calling it at the respective places.
    print(player1,'s','Turn')
    print('_____________')
    #I am using loop here so that to avoid the loss of the turns until the given condition satisfies.
       
    a=1
    while a==1:
        
        player_turn=eval(input("Choose a position from 1-9:"))
        
        symbol='O'
    
        if player_turn in grid:#if the entered stuff by the player1 is the grid then it will be executed 
            if player_turn==1:#if the player enters 1 then it will place the symbol at grid[0] which means at position 1 and similarly all the conditions works accordingly 
                grid[0]=symbol
            elif player_turn==2:
                grid[1]=symbol
            elif player_turn==3:
                grid[2]=symbol
            elif player_turn==4:
                grid[3]=symbol
            elif player_turn==5:
                grid[4]=symbol
            elif player_turn==6:
                grid[5]=symbol
            elif player_turn==7:
                grid[6]=symbol
            elif player_turn==8:
                grid[7]=symbol
            elif player_turn==9:
                grid[8]=symbol
            a=0#if the entered stuff by the user is in the grid then thile loop stops
        
        else:
            a=1#if the entered stuff by the player is not in the grid then the loop continues, until the given condition satisfies
            print('Invalid Entity')



def computer_turn():
    print(player2,'s','Turn')
    print('____________')
    symbol='X'
    k=1
    #This is the code for mid position if mid position is empty then computer will firstly place it's symbol at the mid position as there are the maximum chances of the player to win as diagonally,vertically and horizontally.
    if grid[4]!='O' and grid[4]!='X':
        grid[4]='X'
 
     #If the center is already occupied then computer will check the
        #firstly we will check that is there any chance of winnning for the computer game.
    elif grid[0]==grid[1]=='X' and grid[2]!='X' and grid[2]!='O':#these three conditions  will check for the position 3 in the grid.
        grid[2]='X'
    elif grid[5]==grid[8]=='X' and grid[2]!='X' and grid[2]!='O':
        grid[2]='X'
    elif grid[4]==grid[6]=='X' and grid[2]!='X' and grid[2]!='O':
        grid[2]='X'
        
    elif grid[0]==grid[2]=='X' and grid[1]!='X' and grid[1]!='O':#these two conditions will check for position2 in the grid.
        grid[1]='X'
    elif grid[4]==grid[7]=='X' and grid[1]!='X' and grid[1]!='O':
        grid[1]='X'
        
    elif grid[1]==grid[2]=='X' and grid[0]!='X' and grid[0]!='O':#these three will check for the position3 in the grid.
        grid[0]='X'
    elif grid[4]==grid[8]=='X' and grid[0]!='X' and grid[0]!='O':
        grid[0]='X'
    elif grid[3]==grid[6]=='X' and grid[0]!='X' and grid[0]!='O':
        grid[0]='X'
        
    elif grid[0]==grid[6]=='X' and grid[3]!='X' and grid[3]!='O':#these two will check for the position4 in the grid.
        grid[3]='X'
    elif grid[4]==grid[5]=='X' and grid[3]!='X' and grid[3]!='O':
        grid[3]='X'
        
        #this will check for the position 5 in the grid.
    elif (grid[3]==grid[5]=='X' or grid[1]==grid[7]=='X' or grid[2]==grid[6]=='X' or grid[0]==grid[8]=='X')and grid[4]!='X' and grid[4]!='O':#it will checks the centre position that is the second row and the second column at the position grid[4] that is the position 5 in the display board. it will check the second row, second column and the diagonals. if any of the 4 conditions satisfies then computer will place it's symbol at position 5 in the display board. 
        grid[4]='X'
        
    elif grid[4]==grid[3]=='X' and grid[5]!='X' and grid[5]!='O':#these two conditions will check for the position6 in the grid.
        grid[5]='X'
    elif grid[3]==grid[8]=='X' and grid[5]!='X' and grid[5]!='O':
        grid[5]='X'
        
    elif grid[0]==grid[3]=='X' and grid[6]!='X' and grid[6]!='O':#these three will check for the position7 in the grid.
        grid[6]='X'
    elif grid[4]==grid[2]=='X' and grid[6]!='X' and grid[6]!='O':
        grid[6]='X'
    elif grid[7]==grid[8]=='X' and grid[6]!='X' and grid[6]!='O':
        grid[6]='X'
        
    elif grid[6]==grid[8]=='X' and grid[7]!='X' and grid[7]!='O':#these two will check for the position8 in the grid 
        grid[7]='X'
    elif grid[1]==grid[4]=='X' and grid[7]!='X' and grid[7]!='O':
        grid[7]='X'
        
    elif grid[6]==grid[7]=='X' and grid[8]!='X' and grid[8]!='O':#these three will check for the position 9 in the grid.
        grid[8]='X'
    elif grid[0]==grid[4]=='X' and grid[8]!='X' and grid[8]!='O':
        grid[8]='X'
    elif grid[2]==grid[5]=='X' and grid[8]!='X' and grid[8]!='O':
        grid[8]='X'
    

            #these all conditions will check for rows,columns and for the diagonals.
    elif (grid[0]==grid[1]=='O' or grid[5]==grid[8]=='O' or grid[6]==grid[4]=='O')and grid[2]!='X' and grid[2]!='O':#it checks the first row and the third  column with respect to the grid[2] position that is the position 3 in the display board. if any of the two conditions satisfies then computer places it's symbol at position 3 in in the display board.
        grid[2]='X'
    elif (grid[0]==grid[2]=='O' or grid[4]==grid[7]=='O')and grid[1]!='X' and grid[1]!='O':#it checks the first row and the second column with respect to the grid[1] position that is the position 2 in the display board. If any of the two conditions satisfies then computer places it's symbol at position 2 in thedisplay board.
        grid[1]='X'
    elif (grid[1]==grid[2]=='O' or grid[3]==grid[6]=='O' or grid[8]==grid[4]=='O')and grid[0]!='X' and grid[0]!='O':#it checks the first row and the first column with respect to the position grid[0] that is the position 1 in the display board. If any of the two conditions satisfies then computer places it's symbol at position 1 in the display board.
        grid[0]='X'
    elif (grid[3]==grid[4]=='O' or grid[2]==grid[8]=='O')and grid[5]!='X' and grid[5]!='O':#it checks the second row and the third column with respect to the position grid[5] that is the position 6 in the display board. if any of the two conditions satisfies then computer places it's symbol at position 6 in the display board.
        grid[5]='X'
    elif (grid[4]==grid[5]=='O' or grid[0]==grid[6]=='O')and grid[3]!='X' and grid[3]!='O' :#it checks the second row and the first column with respect to the position grid[3] that is the position 4 in the display board. if any of the two conditions satisfies then computer will place it's symbol at position 4 in the display board.
        grid[3]='X'
    
    elif (grid[3]==grid[5]=='O' or grid[1]==grid[7]=='O' or grid[2]==grid[6]=='O' or grid[0]==grid[8]=='O')and grid[4]!='X' and grid[4]!='O':#it will checks the centre position that is the second row and the second column at the position grid[4] that is the position 5 in the display board. it will check the second row, second column and the diagonals. if any of the 4 conditions satisfies then computer will place it's symbol at position 5 in the display board. 
        grid[4]='X'
    elif (grid[6]==grid[7]=='O' or grid[2]==grid[5]=='O' or grid[0]==grid[4]=='O' or grid[5]==grid[6]=='O')and grid[8]!='X' and grid[8]!='O':#it checks the third row ,diagonal and  the third column with respect to the position grid[8] that is the position 9  in the display board. if any of the three conditions satisfies then computer will place it's symbol at position 9 in the display board.
        grid[8]='X'
    elif (grid[7]==grid[8]=='O' or grid[0]==grid[3]=='O' or grid[2]==grid[4]=='O' or grid[2]==grid[7]=='O' or grid[0]==grid[7]=='O')and grid[6]!='X' and grid[6]!='O' :#it  checks the third row, diagonal and the first column with reseect to the position grid[7] that is the position 7 in the display board. if any of the three conditions satisfies then computer wil place it's symbol at position 7 in the display board. 
        grid[6]='X'
    elif (grid[6]==grid[8]=='O' or grid[1]==grid[4]=='O' or grid[2]==grid[6]=='O' or grid[0]==grid[8]=='O')and grid[7]!='X' and grid[7]!='O' :#it checks the third row and the second column with respect to the position grid[7] that is the position 8 in the display board. if any of the two conditions satisfies then computer will place it's symbol at position 8 in the display board. 
        grid[7]='X'
                #checking the corners and the mid 
    elif grid[4]!='O' and grid[4]!='X' and grid[4]!='O':#if mid is not filled yet then computer will place it's symbol at the position 5 thet is the mid position in the display board.
        grid[4]='X'
    elif grid[0]!='O' and grid[0]!='X' and grid[0]!='O':#if corner 1 is not filled yet then computer will place it's symbol at position 1 in the display board.
        grid[0]='X'
    elif grid[2]!='O' and grid[2]!='X' and grid[2]!='O':#if corner 2 is not filled yet then computer will place it's symbol at position 3 in the display boatrd.
        grid[2]='X'
    elif grid[6]!='O' and grid[6]!='X' and grid[6]!='O':#if corner 3 is not filled yet then computer will place it's symbol at positioon 7 in the display board.
        grid[6]='X'
    elif grid[8]!='O' and grid[8]!='X' and grid[8]!='O':#if corner 4 is not filled yet then computer will place it's symbol at position 9 in the display board.
        grid[8]='X'
    else:
        a=1#assigning a value 1 
        while a==1:#loop winn continue until a==1
            num=random.randint(1,9)#randomly generates a number between 1 and 9.
            symbol='X'
            if num in grid:#check if the randomly generated number is in the grid.
                
                if num==1:
                    grid[0]=symbol
                elif num==2:
                    grid[1]=symbol
                elif num==3:
                    grid[2]=symbol
                elif num==4:
                    grid[3]=symbol
                elif num==5:
                    grid[4]=symbol
                elif num==6:
                    grid[5]=symbol
                elif num==7:
                    grid[6]=symbol
                elif num==8:
                    grid[7]=symbol
                elif num==9:
                    grid[8]=symbol
                a=2#if the randomly generated number is in the grid then loop breaks.
            else:
                a==1#if the ranomly grnerated number is not in the grid then loop continues until the number becomes available in the grid.
            
      
def player2_turn():#player2 function works same like player1 just the symbol is changed here. The code execution method is same for the both.
    
    print(player2,'s','Turn')
    print('____________')
    a=1
    while a==1:
        
        player_turn=eval(input("Choose a position from 1-9:"))
        
        symbol='X'
    
        if player_turn in grid:
            if player_turn==1:
                grid[0]=symbol
            elif player_turn==2:
                grid[1]=symbol
            elif player_turn==3:
                grid[2]=symbol
            elif player_turn==4:
                grid[3]=symbol
            elif player_turn==5:
                grid[4]=symbol
            elif player_turn==6:
                grid[5]=symbol
            elif player_turn==7:
                grid[6]=symbol
            elif player_turn==8:
                grid[7]=symbol
            elif player_turn==9:
                grid[8]=symbol
            a=0#breaks the loop
        
        else:
            a=1#continues the loop 
            print('Invalid Entity')

    
    

def two_players_game():
    global grid
    global player1
    global player2
    global toss
    global game
    global continues
    continues=True
    grid=[1,2,3,4,5,6,7,8,9]
    
    print('\tWELCOME TO TIC TAC MULTIPLAYERS MODE\t')

    display_grid()
    player1=str(input("Enter the name of first player:"))
    print("The symbol assigned to",player1," is (O)")
    player2=str(input('Enter the name of second player:'))
    print("The symbol assigned to ",player2, "is (X)")
    toss=random.randint(0,1)
    print('Toss is :',toss)
    if toss==0:
        toss="o"
        print(player1,"Wins the toss")
        print(player1,"will take the first move")
    else:
        toss="x"
        print(player2," wins the toss")
        print(player2," will take the first move")
    for i in range(1,10):
            
        if (i==1 or i==3 or i==5  or i==7 or i==9)and toss=='o':
            player1_turn()
            display_grid()
        elif (i==2 or i==4 or i==6 or i==8)and toss=='o':
            player2_turn()
            display_grid()
        win()
        if continues==False:
            print('****GAME OVER****')
            break 
        if (i==2 or i==4 or i==6 or i==8)and toss=='x':
            player1_turn()
            display_grid()
        elif (i==1 or i==3 or i==5 or i==7 or i==9)and toss=='x':
            
            player2_turn()
            display_grid()
          
    else:
        print('GAME DRAW')
        print('**** GAME OVER****')
    two_players_again()#calling the menu that displays after one game ends.



def tournament_game():
    global player2
    global player1
    global grid
    grid=[1,2,3,4,5,6,7,8,9]
    
    print('\tWELCOME TO TIC TAC TOURNAMENT BEST OF THREE\t')
    display_grid()
    player1=str(input('Enter the name of the player1:'))
    print('The symbol assigned to',player1,'is O')
    
    player2=str(input('Enter the name of the player2:'))
    print('The symbol assigned to',player2,'is X')
   
    i=0#initially assigning 0 to i.
    
    x=0#initially assigning 0 to x.
    
    o=0#initially assigning 0 to o.

    while i<=2:
        if i==0:
            
            print('\t\t   GAME 1\t\t')

        elif i==1:
            
            print('\t\t   GAME 2\t\t')
        else:
            
            print('\t\t   GAME 3\t\t')
        game()#calling the game function for the execution of the code.
        if winner=='x':#if winner is x then there will be an increment in the value of x.
            x=x+1
        
            
        elif winner=='o':#if winner is o then there will be an increment in the value of o.
            o=o+1
        if x==2:#if player 2 wins the two games in the first two attempts then tournament ends 
            break
        elif o==2:#if player1 wins two games in the first two attempts then turnament ends
            break 
        
            
            
        i=i+1#increasing the value of i so that loop continue until i becomes 2.
        
    if x>o:#if winnings of x are more than o then player1 wins the tournament.
        print(player2,'Wins the tournament')
        print('****GAME OVER****')
    elif o>x:#if winnings of o are more than x then player2 wins the
        print(player2,'Wins the tournament')
        print('GAME OVER****')
    else:
        print('Tournament Draws!')
        print('****GAME OVER****')
    tournament_again()#Calling menu after the tournament game ends.

def game():
    global grid
    global player1
    global player2
    global toss
    global game
    global continues 
    continues=True
    grid=[1,2,3,4,5,6,7,8,9]
    
    display_grid()
    toss=random.randint(0,1)
    print('The toss is:',toss)
    if toss==0:
        toss="o"
        print(player1,"Wins the toss")
        print(player1,"will take the first move")
    else:
        toss="x"
        print(player2," Wins the toss")
        print(player2," will take the first move")
    play()
def play():
    
    for i in range(1,10):
        
        
        if (i==1 or i==3 or i==5  or i==7 or i==9)and toss=='o':
            player1_turn()
            display_grid()
        elif (i==2 or i==4 or i==6 or i==8)and toss=='o':
            player2_turn()
            display_grid()
        
        win()

        
        
        if continues==False:
            break
        
        
        if (i==2 or i==4 or i==6 or i==8)and toss=='x':
            player1_turn()
            display_grid()
        elif (i==1 or i==3 or i==5 or i==7 or i==9)and toss=='x':
            
            player2_turn()
            display_grid()     
    else:
        print('GAME DRAW')
        print('**** GAME OVER****')
           
def one_player_easy():
    global t 
    
    global grid #making grid global so that it can be used for all the functions called in the one_player_game() function.
    
    grid=[1,2,3,4,5,6,7,8,9]
    
    
    global continues#I have made continues global so that it can be used for all the functions called in this one_player_game() function.
    continues=True
    print('\tWELCOME TO TIC TAC SINGLE PLAYER EASY MODE\t')
    global player1#making player1 global
    
    global player2 #making player2 global 
    display_grid()#caling this function for displaying the grid 

    player1=str(input("Enter your name:"))
    print("The symbol assigned to",player1," is (O)")
    player2='Computer'
    print("The symbol assigned to ",player2, "is (X)")
    
    toss=random.randint(0,1)#making toss for one player game 
    
    print('Toss is :',toss)
    if toss==0:
        toss="o"#assigning toss a value o if it is 0, so that to make the first move of the players according to the toss.
        print(player1,"Wins the toss")
        print(player1,"will take the first move")
    else:
        toss="x"#assigning toss a value x if it is 1 so that to make the first move of the players according to the toss.
        print("COMPUTER wins the toss")
        print("COMPUTER will take the first move")
    
        
    for i in range(1,10):#I have used a for loop here that is used for 9 times
            #I have assigned the turns to the players according to the toss
        #if toss is 'o' then first turn will be of player1 then turn 2 will be of player 2 and 3 will be of player3 and so on 
        if (i==1 or i==3 or i==5  or i==7 or i==9)and toss=='o':
            player1_turn()#calling player1 function for player 1 turns
            display_grid()
        elif (i==2 or i==4 or i==6 or i==8)and toss=='o':
            
            computer_turn1()#calling computer_turns function for computer turns
            display_grid()
            
        win()#calling winning conditions for checking the winning of a player
        
        if continues==False:#If any of the winning condition satisfies then game ends here. else continues
            
            print('****Game OVER****')
            break 
        if (i==2 or i==4 or i==6 or i==8)and toss=='x':#if player2 wins the toss then in this case second turn will be of player1 then 4th then 6th then 8th turn will be of player1
            
            player1_turn()#calling player's turns function
            display_grid()
        elif (i==1 or i==3 or i==5 or i==7 or i==9)and toss=='x':#if player2 that is computer here wins the toss then first turn will be of computer and then 3rd,5th 7th and 9th turn will be of player2.
            
            computer_turn1()#calling computer's turns function 
            display_grid()#calling function on the indentation of the loop so that it will be executed after each selection sattement.
          
    else:#if none of the winning conditions satisfies till the 9 moves are completed then in this case the game is draw between the two playerds
        
        print('GAME DRAW')
        print('**** GAME OVER****')
    one_player_again1()#calling this function for dislpaying a menu of ,playing again,back to the main menu, and exiting the game, after the game ends.
    

    
def one_player_medium():
     
    global grid #making grid global so that it can be used for all the functions called in the one_player_game() function.
    
    grid=[1,2,3,4,5,6,7,8,9]
    
    
    global continues#I have made continues global so that it can be used for all the functions called in this one_player_game() function.
    continues=True
    print('\tWELCOME TO TIC TAC SINGLE PLAYER MEDIUM MODE\t')
    global player1#making player1 global
    
    global player2 #making player2 global 
    display_grid()#caling this function for displaying the grid 

    player1=str(input("Enter your name:"))
    print("The symbol assigned to",player1," is (O)")
    player2='Computer'
    print("The symbol assigned to ",player2, "is (X)")
    
    toss=random.randint(0,1)#making toss for one player game 
    
    print('Toss is :',toss)
    if toss==0:
        toss="o"#assigning toss a value o if it is 0, so that to make the first move of the players according to the toss.
        print(player1,"Wins the toss")
        print(player1,"will take the first move")
    else:
        toss="x"#assigning toss a value x if it is 1 so that to make the first move of the players according to the toss.
        print("COMPUTER wins the toss")
        print("COMPUTER will take the first move")
    
        
    for i in range(1,10):#I have used a for loop here that is used for 9 times
            #I have assigned the turns to the players according to the toss
        #if toss is 'o' then first turn will be of player1 then turn 2 will be of player 2 and 3 will be of player3 and so on 
        if (i==1 or i==3 or i==5  or i==7 or i==9)and toss=='o':
            player1_turn()#calling player1 function for player 1 turns
            display_grid()
        elif (i==2 or i==4 or i==6 or i==8)and toss=='o':
            
            computer_turn2()#calling computer_turns function for computer turns
            display_grid()
            
        win()#calling winning conditions for checking the winning of a player
        
        if continues==False:#If any of the winning condition satisfies then game ends here. else continues
            
            print('****Game OVER****')
            break 
        if (i==2 or i==4 or i==6 or i==8)and toss=='x':#if player2 wins the toss then in this case second turn will be of player1 then 4th then 6th then 8th turn will be of player1
            
            player1_turn()#calling player's turns function
            display_grid()
        elif (i==1 or i==3 or i==5 or i==7 or i==9)and toss=='x':#if player2 that is computer here wins the toss then first turn will be of computer and then 3rd,5th 7th and 9th turn will be of player2.
            
            computer_turn2()#calling computer's turns function 
            display_grid()#calling function on the indentation of the loop so that it will be executed after each selection sattement.
          
    else:#if none of the winning conditions satisfies till the 9 moves are completed then in this case the game is draw between the two playerds
        
        print('GAME DRAW')
        print('**** GAME OVER****')
    one_player_again2()#calling this function for dislpaying a menu of ,playing again,back to the main menu, and exiting the game, after the game ends.
    

    


    
def computer_turn2():
    print(player2,'s','Turn')
    print('____________')
    symbol='X'
    q=1
    #This is the code for mid position if mid position is empty then computer will firstly place it's symbol at the mid position as there are the maximum chances of the player to win as diagonally,vertically and horizontally.
    if grid[4]!='O' and grid[4]!='X':
        grid[4]='X'
 
     #If the center is already occupied then computer will check the
    elif grid[0]==grid[1]=='X' and grid[2]!='X' and grid[2]!='O':#these three conditions  will check for the position 3 in the grid.
        grid[2]='X'
    elif grid[5]==grid[8]=='X' and grid[2]!='X' and grid[2]!='O':
        grid[2]='X'
    elif grid[4]==grid[6]=='X' and grid[2]!='X' and grid[2]!='O':
        grid[2]='X'
        
    elif grid[0]==grid[2]=='X' and grid[1]!='X' and grid[1]!='O':#these two conditions will check for position2 in the grid.
        grid[1]='X'
    elif grid[4]==grid[7]=='X' and grid[1]!='X' and grid[1]!='O':
        grid[1]='X'
        
    elif grid[1]==grid[2]=='X' and grid[0]!='X' and grid[0]!='O':#these three will check for the position3 in the grid.
        grid[0]='X'
    elif grid[4]==grid[8]=='X' and grid[0]!='X' and grid[0]!='O':
        grid[0]='X'
    elif grid[3]==grid[6]=='X' and grid[0]!='X' and grid[0]!='O':
        grid[0]='X'
        
    elif grid[0]==grid[6]=='X' and grid[3]!='X' and grid[3]!='O':#these two will check for the position4 in the grid.
        grid[3]='X'
    elif grid[4]==grid[5]=='X' and grid[3]!='X' and grid[3]!='O':
        grid[3]='X'
    

            #rows,columns diagnol checker two spaces
    elif (grid[0]==grid[1]=='O' or grid[5]==grid[8]=='O')and grid[2]!='X' and grid[2]!='O':#it checks the first row and the third  column with respect to the grid[2] position that is the position 3 in the display board. if any of the two conditions satisfies then computer places it's symbol at position 3 in in the display board.
        grid[2]='X'
    elif (grid[0]==grid[2]=='O' or grid[4]==grid[7]=='O')and grid[1]!='X' and grid[1]!='O':#it checks the first row and the second column with respect to the grid[1] position that is the position 2 in the display board. If any of the two conditions satisfies then computer places it's symbol at position 2 in thedisplay board.
        grid[1]='X'
    elif (grid[1]==grid[2]=='O' or grid[3]==grid[6]=='O' )and grid[0]!='X' and grid[0]!='O':#it checks the first row and the first column with respect to the position grid[0] that is the position 1 in the display board. If any of the two conditions satisfies then computer places it's symbol at position 1 in the display board.
        grid[0]='X'
    elif (grid[3]==grid[4]=='O' )and grid[5]!='X' and grid[5]!='O':#it checks the second row and the third column with respect to the position grid[5] that is the position 6 in the display board. if any of the two conditions satisfies then computer places it's symbol at position 6 in the display board.
        grid[5]='X'
    elif (grid[4]==grid[5]=='O')and grid[3]!='X' and grid[3]!='O' :#it checks the second row and the first column with respect to the position grid[3] that is the position 4 in the display board. if any of the two conditions satisfies then computer will place it's symbol at position 4 in the display board.
        grid[3]='X'
    
    elif (grid[3]==grid[5]=='O'  )and grid[4]!='X' and grid[4]!='O':#it will checks the centre position that is the second row and the second column at the position grid[4] that is the position 5 in the display board. it will check the second row, second column and the diagonals. if any of the 4 conditions satisfies then computer will place it's symbol at position 5 in the display board. 
        grid[4]='X'
    elif (grid[6]==grid[7]=='O' )and grid[8]!='X' and grid[8]!='O':#it checks the third row ,diagonal and  the third column with respect to the position grid[8] that is the position 9  in the display board. if any of the three conditions satisfies then computer will place it's symbol at position 9 in the display board.
        grid[8]='X'
    elif (grid[7]==grid[8]=='O' or grid[0]==grid[3]=='O' )and grid[6]!='X' and grid[6]!='O' :#it  checks the third row, diagonal and the first column with reseect to the position grid[7] that is the position 7 in the display board. if any of the three conditions satisfies then computer wil place it's symbol at position 7 in the display board. 
        grid[6]='X'
    elif (grid[6]==grid[8]=='O' or grid[1]==grid[4]=='O')and grid[7]!='X' and grid[7]!='O' :#it checks the third row and the second column with respect to the position grid[7] that is the position 8 in the display board. if any of the two conditions satisfies then computer will place it's symbol at position 8 in the display board. 
        grid[7]='X'
                #checking the corners and the mid 
    elif grid[4]!='O' and grid[4]!='X' and grid[4]!='O':#if mid is not filled yet then computer will place it's symbol at the position 5 thet is the mid position in the display board.
        grid[4]='X'
    elif grid[0]!='O' and grid[0]!='X' and grid[0]!='O':#if corner 1 is not filled yet then computer will place it's symbol at position 1 in the display board.
        grid[0]='X'
    elif grid[2]!='O' and grid[2]!='X' and grid[2]!='O':#if corner 2 is not filled yet then computer will place it's symbol at position 3 in the display boatrd.
        grid[2]='X'
    elif grid[6]!='O' and grid[6]!='X' and grid[6]!='O':#if corner 3 is not filled yet then computer will place it's symbol at positioon 7 in the display board.
        grid[6]='X'
    elif grid[8]!='O' and grid[8]!='X' and grid[8]!='O':#if corner 4 is not filled yet then computer will place it's symbol at position 9 in the display board.
        grid[8]='X'
    else:#there is a very rare chance of this selection statement, if none of the above conditions are satisfies then computer will randomly generates a number, either 0 or 1. 
        while q==1:
            num=random.randint(1,9)
            if num in grid:
                q=2
                if num==1:
                    grid[0]=symbol
                elif num==2:
                    grid[1]=symbol
                elif num==3:
                    grid[2]=symbol
                elif num==4:
                    grid[3]=symbol
                elif num==5:
                    grid[4]=symbol
                elif num==6:
                    grid[5]=symbol
                elif num==7:
                    grid[6]=symbol
                elif num==8:
                    grid[7]=symbol
                elif num==9:
                    grid[8]=symbol
            else:
                q=1



def one_player_again():#submenu for single player mode.
    print('______________________________________________________________')

    print('\t IF YOU WANT TO PLAY AGAIN , ENTER y ')
    print('\t IF YOU WANT TO RETURN BACK TO THE MAIN MENU, ENTER m')
    print('\t IF YOU WANT TO QUIT THE GAME, ENTER e')
    print('______________________________________________________________')
    menu=str(input('Enter your choice:'))
    if menu=='y':
        return one_player_game()#returning to the  one_player_game function for playing one player game again
    elif menu=='m':
        return main()#returning to the main function 
    else:
        exit()#exiting the game
def one_player_again1():#submenu for single player mode.
    print('______________________________________________________________')

    print('\t IF YOU WANT TO PLAY AGAIN , ENTER y ')
    print('\t IF YOU WANT TO RETURN BACK TO THE MAIN MENU, ENTER m')
    print('\t IF YOU WANT TO QUIT THE GAME, ENTER e')
    print('______________________________________________________________')
    menu=str(input('Enter your choice:'))
    if menu=='y':
        return one_player_easy()#returning to the  one_player_game function for playing one player game again
    elif menu=='m':
        return main()#returning to the main function 
    else:
        exit()#exiting the game
def one_player_again2():#submenu for single player mode.
    print('______________________________________________________________')

    print('\t IF YOU WANT TO PLAY AGAIN , ENTER y ')
    print('\t IF YOU WANT TO RETURN BACK TO THE MAIN MENU, ENTER m')
    print('\t IF YOU WANT TO QUIT THE GAME, ENTER e')
    print('______________________________________________________________')
    menu=str(input('Enter your choice:'))
    if menu=='y':
        return one_player_medium()#returning to the  one_player_game function for playing one player game again
    elif menu=='m':
        return main()#returning to the main function 
    else:
        exit()#exiting the game
def two_players_again():#sub menu for two players mode.
    print('______________________________________________________________')
    print('\t IF YOU WANT TO PLAY AGAIN TWO PLAYERS GAME, ENTER y ')
    print('\t IF YOU WANT TO RETURN BACK TO THE MAIN MENU, ENTER m')
    print('\t IF YOU WANT TO QUIT THE GAME, ENTER e')
    print('______________________________________________________________')
    menu=str(input('Enter your choice:'))
    if menu=='y':
        return two_players_game()#returning to the two players game function again for playing two players game again.
    elif menu=='m':
        return main()#returning to the main function.
    else:
        exit()#exiting the game 
def tournament_again():#sub menu for tournament mode.
    print('______________________________________________________________')
    print('\t IF YOU WANT TO PLAY AGAIN TOURNAMENT GAME, ENTER y ')
    print('\t IF YOU WANT TO RETURN BACK TO THE MAIN MENU, ENTER m')
    print('\t IF YOU WANT TO QUIT THE GAME, ENTER e')
    print('______________________________________________________________')
    menu=str(input('Enter your choice:'))
    if menu=='y':
       
        tournament_game()#returning to the tournament game function for playing tournament game again
    elif menu=='m':
        return main()#returning to the main function.
    else:
        exit()
def sub_menu():
    print('______________________________________________________________')
    print('\t IF YOU WANT TO PLAY IN EASY MODE PRESS 1 ')
    print('\t IF YOU WANT TO PLAY IN MEDIUM MODE PRESS 2')
    print('\t IF YOU WANT TO PLAY IN HARD MODE PRESS 3')
    print('______________________________________________________________')
    op=eval(input('Enter your choice:'))
    if op==1:
        one_player_easy()
    elif op==2:
        one_player_medium()
    elif op==3:
        one_player_game()
    
def computer_turn1():#computer's turn in simple single player's mode.
    print(player2,'s','Turn')
    print('____________')
    symbol='X'
    a=1
    while a==1:
        num=random.randint(1,9)#randomly generating a number between 1 and 9 
        if num in grid:#If the number is in the grid then the loops ends.
            a=2
            
            if num==1:
                grid[0]=symbol
            elif num==2:
                grid[1]=symbol
            elif num==3:
                grid[2]=symbol
            elif num==4:
                grid[3]=symbol
            elif num==5:
                grid[4]=symbol
            elif num==6:
                grid[5]=symbol
            elif num==7:
                grid[6]=symbol
            elif num==8:
                grid[7]=symbol
            elif num==9:
                grid[8]=symbol
        else:#If randomly generated number is not in the list then loops continues until it generates a number that is present in the list.
            a=1




def win():#defining winning conditions function
    global continues
    global winner
    winner=0#assigning winner initially 0 value
    if continues:
        #Winning conditions for player1 
        if (grid[0]=='O' and grid[1]=='O' and grid[2]=='O') or (grid[3]=='O' and grid[4]=='O' and grid[5]=='O')or(grid[6]=='O' and grid[7]=='O' and grid[8]=='O')or(grid[0]=='O' and grid[3]=='O' and grid[6]=='O')or (grid[1]=='O' and grid[4]=='O'and grid[7]=='O')or(grid[2]=='O' and grid[5]=='O' and grid[8]=='O')or (grid[0]=='O' and grid[4]=='O' and grid[8]=='O')or(grid[2]=='O' and grid[4]=='O' and grid[6]=='O'):
                print(player1,'Is the winner of this game')
                winner='o'#if player1 wins the game then winner='o'
                continues=False#continue condition becomes false for ending the game.
                return continues #returning the value of continues
                
        #winning conditions for player2 
        elif (grid[0]=='X' and grid[1]=='X' and grid[2]=='X') or (grid[3]=='X' and grid[4]=='X' and grid[5]=='X')or(grid[6]=='X' and grid[7]=='X' and grid[8]=='X')or(grid[0]=='X' and grid[3]=='X' and grid[6]=='X')or (grid[1]=='X' and grid[4]=='X'and grid[7]=='X')or(grid[2]=='X' and grid[5]=='X' and grid[8]=='X')or (grid[0]=='X' and grid[4]=='X' and grid[8]=='X')or(grid[2]=='X' and grid[4]=='X' and grid[6]=='X'):
        
            print(player2,"is the winner of this game")
            winner='x'#if player2 wins the game then winner='x'
            continues=False#continues condition becomes false
            return continues#returning the value of continues 


    
main()#calling the main function for the execution of the code.
        
    
