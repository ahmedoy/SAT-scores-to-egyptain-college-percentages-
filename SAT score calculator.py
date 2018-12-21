

def calculate_score(s1,s1_c,s2,s2_c,gp,gp_c):
    sat1_final = (s1/1600)*s1_c
    print('SAT 1 final after multiplying by ' + str(s1_c) +  ' is :  ' + str(sat1_final) )
    print()
    sat2_final = (s2/1600)*s2_c
    print('SAT 2  final after multiplying by ' + str(s2_c) +  ' is :  ' + str(sat2_final) )
    print()
    gpa_final = gp*gp_c
    print('of course gpa is the same but we multiply by  ' + str(gp_c) + ' so it becomes a percentage')
    print(str(gpa_final))
    print()
    total_score = gpa_final + sat1_final + sat2_final
    print('Your total score for entering egyptian colleges is : ' + str(total_score) )






while True:



    try:

        #sat 1
            
        #sat 1 limits
        sat1_max_limit = 1600.0
        sat1_bonus_minimum = 1090.0
        sat1_min_limit = 400.0    
            
        print('Type your SAT 1 score  from  ' + str(sat1_min_limit) + '  to  '  + str(sat1_max_limit))
        sat1 = float(input())
        #sat constant if score higher than 1090
        sat1_high_const = 69.0
        #sat constant if score lower than 1090 
        sat1_low_const = 60.0






        #sat 2
        #sat 2 limits
        sat2_max_limit = 1600.0
        sat2_bonus_minimum = None
        sat2_min_limit = 400.0

        print()
        print('Type your SAT 2 score  from  ' + str(sat2_min_limit) + '  to  '  + str(sat2_max_limit))
        sat2 = float(input())
        #sat 2 currently has only one constant
        sat2_const = 15.0




        #GPA
        #gpa limits
        gpa_max_limit = 4.0
        gpa_bonus_minimum = None
        gpa_min_limit = 0.0

        print()
        print('Type your GPA  from  ' + str(gpa_min_limit) + '  to  '  + str(gpa_max_limit))
        gpa = float(input())
        #gpa constant which is not realy a constant but it turns it into percentage
        gpa_const = 10.0

    except:
       print('please enter something valid NUMBERS only')
       print()
       print('------------------------------------------------------------------------------------------------------------------------------------------------')
       print()       
       continue
        


    #checking if the scores are logical
    if sat1 >= sat1_bonus_minimum  and sat1 <= sat1_max_limit and  sat2 >= sat2_min_limit and sat2 <= sat2_max_limit and  gpa  >= gpa_min_limit and gpa <= gpa_max_limit :
        print('Your marks are logical , calculating ......................')
        print('your score is above 1090 in sat 1 so your bonus is ' +  str(sat1_high_const) + ' multiplied by your score ')
        calculate_score(sat1 , sat1_high_const , sat2 , sat2_const , gpa , gpa_const)
        print('press enter to try another scores')
        waiting = input()
        
    elif sat1 >= sat1_min_limit  and sat1 < sat1_bonus_minimum and  sat2 >= sat2_min_limit and sat2 <= sat2_max_limit  and  gpa  >= gpa_min_limit and gpa <= gpa_max_limit :
        print('Your marks are logical , calculating ......................')
        print('your score is below 1090 in sat 1 so your bonus is ' +  str(sat1_low_const) + ' multiplied by your score ')
        calculate_score(sat1 , sat1_low_const , sat2 , sat2_const , gpa, gpa_const)
        print('press enter to try another scores')
        waiting = input()

    else:
        print('please check that your inputs are in the ranges')
        print()
        print('------------------------------------------------------------------------------------------------------------------------------------------------')
        print()
        continue




    print()
    print('------------------------------------------------------------------------------------------------------------------------------------------------')
    print()
    
    


