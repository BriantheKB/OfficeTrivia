print ('Hello Jeff, Welcome to the Slaughterhouse, AKA Office Trivia!')

ans = input ('Are you prepared? (yes/no): ')
score = 0
total_q = 10

if ans.lower() == 'yes' :
    ans = input('1. What city is Dunder Mifflin Located? ')
    if ans.lower() == 'scranton':
        score += 1
        print ('Oh Hell Yea')
    else:
        print ('nope its scranton!')
        

    ans = input('2. Who was Pam engaged to before Jim? ')
    if ans.lower() == 'roy':
        score += 1
        print ('Oh Hell Yea')
    else:
        print ('did you mean roy?')
        

    ans = input('3. Who came up with Suck It? ')
    if ans.lower() == 'david wallace':
        score += 1
        print ('Oh Hell Yea')
    else:
        print ('duh, its david wallace!')


    ans = input('4. Ryan caused the fire at the office warming up what? ')
    if ans.lower() == 'a cheese pita':
        score += 1
        print ('Oh Hell Yea')
    else:
        print ('a cheese pita that caused it all!')

    ans = input('5. Pam and Jims first kiss took place where? ')
    if ans.lower() == 'chilis':
        score += 1
        print ('Oh Hell Yea')
    else:
        print ('Ch ch ch CHilis!')

    ans = input('6. What is the title of Michaels movie? ')
    if ans.lower() == 'threat level midnight':
        score += 1
        print ('Oh Hell Yea')
    else:
        print ('threat level midnight is the correct answer!')

    ans = input('7. What is the name of Pam, Oscar and Tobys club? ')
    if ans.lower() == 'the finer things club':
        score += 1
        print ('Oh Hell Yea')
    else:
        print ('the finer things club would have been correct!')

    ans = input('8. Who was on the jury for the Scranton Strangler case? ')
    if ans.lower() == 'toby':
        score += 1
        print ('Oh Hell Yea')
    else:
        print ('Twas Toby')

    ans = input('9. What nickname does Andy give Jim? ')
    if ans.lower() == 'big tuna':
        score += 1
        print ('Oh Hell Yea')
    else:
        print ('The correct answer is Big Tuna!')

    ans = input('10. Michael likes waking up to the smell of what in the morning? ')
    if ans.lower() == 'bacon':
        score += 1
        print ('Oh Hell Yea')
    else:
        print ('you mean Bacon!')


print ('Thanks for getting ', score, " questions correct!")
mark = (score/total_q) * 100
print ('Your score is: ', mark)
print ('Adios')


        
