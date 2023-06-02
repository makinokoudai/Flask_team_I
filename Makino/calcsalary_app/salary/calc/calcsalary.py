from decimal import Decimal , ROUND_HALF_UP,ROUND_UP

salary = 0

def calc_salary(total_salary):
    if total_salary >= 1000000 :
        # 20%の処理
        salary_pulled_100 = total_salary - 1000000 
        taxed_20 = salary_pulled_100 * 0.2
        taxed_10 = 1000000 * 0.1
        
        tax = Decimal(taxed_10+taxed_20).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        
        salary = total_salary - (tax)
        
        return f"給料:{str(total_salary)}の場合、支給額:{str(salary)}円、税額:{str(tax)}円です"
    
    else :
        # 10%の処理
        salary = total_salary - (total_salary * 0.1)
        tax = total_salary * 0.1
        
        return f"給料:{str(total_salary)}の場合、支給額:{str(salary)}円、税額:{str(tax)}円です"
    


