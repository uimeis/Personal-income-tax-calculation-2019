pay = input('请输入税前工资(元)：')
insurance = input('请输入保险和公积金扣除金额(元)：')
attach = input('请输入专项金额(元)：')
month = input('请输入缴税月份：')

def tax_amount(pay, insurance, attach, month):
    deduction_amount_list = []
    for i in range(month):
        cardinal_number = (pay - 5000 - insurance - attach) * (i+1)
        if cardinal_number <= 36000:
            deduction_amount = cardinal_number * 0.03
        elif 3600 < cardinal_number <= 144000:
            deduction_amount = cardinal_number * 0.1 - 2520
        elif 144000 < cardinal_number <= 300000:
            deduction_amount = cardinal_number * 0.2 - 16920
        elif 300000 < cardinal_number <= 420000:
            deduction_amount = cardinal_number * 0.25 - 31920
        elif 420000 < cardinal_number <= 660000:
            deduction_amount = cardinal_number * 0.3 - 52920
        elif 660000 < cardinal_number <= 960000:
            deduction_amount = cardinal_number * 0.35 - 85920
        elif 960000 < cardinal_number:
            deduction_amount = cardinal_number * 0.45 - 181920
        deduction_amount_list.append(deduction_amount)
    if month == 1:
        pay_taxes = deduction_amount_list[0]
    else:
        pay_taxes = deduction_amount_list[-1] - deduction_amount_list[-2]
    if pay_taxes < 0:
        pay_taxes = 0
    pay_taxes_total = deduction_amount_list[-1]
    if pay_taxes_total < 0:
        pay_taxes_total = 0
    wage = pay - pay_taxes - insurance
    return('本月缴税：{}'.format(pay_taxes), '总缴税：{}'.format(pay_taxes_total), '本月工资：{}'.format(wage))

print(tax_amount(int(pay), int(insurance), int(attach), int(month)))
