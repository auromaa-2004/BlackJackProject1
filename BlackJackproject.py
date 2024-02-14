from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def play_blackjack():
    return """
    <pre>
     _     _            _    _            _    
    | |   | |          | |  (_)          | |   
    | |__ | | __ _  ___| | ___  __ _  ___| | __
    | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   <| | (_| | (__|   < 
    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                            _/ |                
                           |__/ 

    Welcome to BlackJack Game.
    Clicking on hit will lead to draw another card.
    Clicking on stand will lead a pass to the computer.<br>

    </pre>
    <a href="/play">Play Blackjack</a>
    """

@app.route('/play', methods=['GET', 'POST'])
def play_blackjack_game():
    
    import random 

    def blackjack():
        stri=""
        string=""
        if request.method == 'POST':
            cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
            user_card1=cards[random.randint(0,12)]
            user_card2=cards[random.randint(0,12)]
            me=[]
            me.append(user_card1)
            me.append(user_card2)
            user_current_score=me[0]+me[1]
            stri=""
            
            string+=f"Your cards:{me}, current score={user_current_score}<br>"
            comp_card1=cards[random.randint(0,12)]
            comp=[]
            comp.append(comp_card1)
            comp_score=comp[0]
            comp_str=""
            user_str=""
            stri+=f"Computer's first card={' '.join([str(elem) for elem in comp])}<br>"
            user_choice = request.form.get('choice')
            if user_current_score!=21:
                
                total_score=0
                total_comp=0
                next=[]
                if user_choice == 'hit':
                    next=[]
                    
                    while (user_choice != 'stand') and (total_score<21):
                        current_score=0
                        next.append(cards[random.randint(0,12)])
                        x=len(next)
                        for i in range(0,x):
                            current_score=current_score+next[i]
                            total_score=current_score+user_current_score        
                        stri+=f"Your cards:{[','.join([str(elem) for elem in me])+','+','.join([str(elem) for elem in next])]}, current score={total_score}<br>"
                        stri+=f"Computer's first card={' '.join([str(elem) for elem in comp])}<br>"
                        if total_score>21:
                            user_str=user_str+"you lose"
                            stri+="you lose"
                            break
                        elif total_score==21:
                            user_str=user_str+"you win"
                            stri+="you win"
                            break    
                    user_choice = request.form.get('choice')
                    
                    if user_str!="you lose" and user_str!="you win":
                        next_comp=[]
                        total_comp=0
                        y=len(next_comp)
                        while total_comp<17 and y<4:
                            current_comp_score=0
                            next_comp.append(cards[random.randint(0,12)])
                            y=len(next_comp)
                            for j in range(0,y):
                                current_comp_score=current_comp_score+next_comp[j]
                                total_comp=comp_score+current_comp_score
                        stri+=f"Your final hand:{[','.join([str(elem) for elem in me])+','+','.join([str(elem) for elem in next])]}, final score={total_score}<br>"
                        stri+=f"Computer's final hand={','.join([str(elem) for elem in comp])+','+','.join([str(elem) for elem in next_comp])}, final score={total_comp}<br>"   

                        if total_comp<=21 and total_comp>total_score:
                            stri+="You Lose<br>"
                        elif total_comp>21:
                            stri+="You Win<br>"
                        elif total_score>21:
                            stri+="You Lose<br>"
                        elif total_score<=21 and total_score>total_comp:   
                            stri+="You Win<br>"
                        elif total_score==total_comp:
                            stri+="Draw<br>"
                        


                elif user_choice == 'stand':
                    next_comp=[]
                    total_comp=0
                    y=len(next_comp)
                    while total_comp<17 and y<4:
                        current_comp_score=0
                        next_comp.append(cards[random.randint(0,12)])
                        y=len(next_comp)
                        for j in range(0,y):
                            current_comp_score=current_comp_score+next_comp[j]
                            total_comp=comp_score+current_comp_score

                    stri+=f"Your final hand:{[','.join([str(elem) for elem in me])]}, final score={user_current_score}<br>"
                    stri+=f"Computer's final hand={','.join([str(elem) for elem in comp])+','+','.join([str(elem) for elem in next_comp])}, final score={total_comp}<br>"  

                    if total_comp<=21 and total_comp>user_current_score:
                        stri+="You lose<br>"
                    elif total_comp>21:
                        stri+="you win<br>" 
                    elif user_current_score>total_comp:
                        stri+="you win<br>"
                    elif user_current_score==total_comp:
                        stri+="Draw<br>"  

            if user_current_score==21:
                stri+="You won<br>"
            return stri
        stri+= """
            <form method="post">
            <button type="submit" name="choice" value="hit">HIT</button>
            <button type="submit" name="choice" value="stand">STAND</button>
        </form>
        """
        return stri+string
        # return string
    return blackjack()

if __name__ == '__main__':
    app.run(debug=True)
