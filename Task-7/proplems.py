def probability_distribution(list):
    length = len(list)
    result = {}
    for i in list:
        result[i] = result.get(i, 0) + 1
    for key ,value in result.items():
        result[key] = value / length
    return result

def conditional_probability(a,b):
    try:
        prob_B = int(input("U want to calc p(a|b) where B is equal to : "))
        '''if prob_B not in b:
            print("\nplz enter number in ypur list ")
            prob_B = int(input(""))
        '''
        intercept = 0
        length_B_true = 0
        for i in range(0,len(b)):
            if a[i]==b[i] and a[i] == prob_B:
                intercept +=1
            
            if b[i] ==  prob_B:
                length_B_true +=1
        intercept = float(intercept / min(len(a),len(b)))
        prob_B = float(length_B_true / len(B))
        Proba = float(intercept /prob_B)
        return Proba
    except ZeroDivisionError:
        print("Cannot divide by zero!")



def Bayes(a , b, prob_A_given_B):
    bayse = a*prob_A_given_B / b
    return bayse


data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1] 

A = [1, 0, 1, 0, 1]
B = [1, 1, 0, 0, 1]

prior_a = 0.3
prior_b = 0.6
conditional_b_given_a = 0.8

print(f"\nprobability_distribution  = {probability_distribution(data)}\n"
      f"\nconditional_probability P(A|B) is {conditional_probability(A,B)}\n"
      f"\nBayes'theorm is = {Bayes(prior_a,prior_b,conditional_b_given_a)}\n ")
