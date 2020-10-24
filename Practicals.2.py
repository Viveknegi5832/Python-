''' 
   Ques.2 Consider a showroom of electronic products,where there are various salesmen.
   Each sales man is given a commission of 5% , depending on the sales made per month.
   In case the sale done is less than 50000 , then the salesman is not given any commission.
   Write a function to calculate total sales of a salesman in a month , commission and remarks for the salesman.
   Sales done by each sales man per week is to be provided as input. Use tuples/list to store data of salesmen. 
   Assign remarks according to the following criteria: 
   Excellent: Sales>=80000 
   Good: Sales>=60000 and <80000
   Average:Sales>=40000and<40000
   WorkHard:Sales<40000


'''



def Calculate(sale1 , sale2 , sale3 , sale4): # Function for calculating commision and remarks
    total_sales = 0
    commission  = 0
    remarks     = ""
    
    total_sales  = sale1 + sale2 + sale3 + sale4
    
    if total_sales > 50000 :
       commision = int(total_sales * 0.05)
         
    if total_sales >= 80000 :
       remarks = "Excellent"
    elif total_sales >= 60000 and total_sales <80000 :
       remarks = "Good"
    elif total_sales >= 40000 and total_sales < 60000 :
       remarks = "Average sales"
    else :
       remarks = "Work hard"
       
    return total_sales , commision , remarks
    
def main():
    sale1 = int(input("Enter sales of week 1 : "))
    sale2 = int(input("Enter sales of week 2 : "))
    sale3 = int(input("Enter sales of week 3 : "))
    sale4 = int(input("Enter sales of week 4 : "))
    
    total_sales , commision , remarks = Calculate(sale1 , sale2 , sale3 , sale4)
    print()
    print("Total sales : " , total_sales)
    print("Commision   : " , commision )
    print("Remarks     : " , remarks )
    
main()
       
    
   

    