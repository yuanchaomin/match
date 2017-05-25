# -*- coding: utf-8 -*-
"""
Created on Tue May 16 03:16:21 2017

@author: Chaomin
"""
import json
import sys
import random

s = {
	"ExpressionType": "Not",
	"Child": {
		"ExpressionType": "Or",
		"LeftOperand": {"ExpressionType": "Equals", "LeftOperand": "Borrower.Name", "RightOperand": "Kym"},
		"RightOperand": {
			"ExpressionType": "And",
			"LeftOperand": {"ExpressionType": "GreaterThan", "LeftOperand": "Borrower.Age", "RightOperand": 18},
			"RightOperand": {"ExpressionType": "LessThan", "LeftOperand": "LoanAmount", "RightOperand": 10000}
		}
	}
}


def test_func(value):
    x = value
    if x < 1:
        return 
    else:
        print(x)
    return test_func(value - 1)

age_list = ['30','40','50']
purpose_list = ['car','house','others']
qualification_list = ['BS','MS','PHD']
term_list = ['6m','12m','18m']
loan_amount_list = ['5000','10000','50000']
income_list_list = ['50000','60000','70000']
occupation_lits = ['engineering','manager','others']
amount_of_property_list = ['50000','60000','70000']

operation_list = ['greater_than','less_than','equals']

attributes_dict = {
        'age':['30','40','50'],
        'purpose':['car','house','others'],
        'qualification':['BS','MS','PHD'],
        'term' :['6m','12m','18m'],
        'loan_amount': ['5000','10000','50000'],
        'income_list':['50000','60000','70000'],
        'occupation' :['engineering','manager','others'],
        'amount_of_property' :['50000','60000','70000'],
        
        'operation':['greater_than','less_than','equals']}

def random_number():
    return random.randrange(0,3) 


def simple_predicate_generator(dict_):
    left_operand = random.choice(list(dict_.keys()))
    
    output_dict = {}
    output_dict['left_operand'] = left_operand
    output_dict['right_operand'] = random.choice(dict_[left_operand])
    
    if left_operand == ('purpose' or 'occupation'):
        output_dict['expression_type'] = dict_['operation'][2]
    elif left_operand == 'term':
        output_dict['expression_type'] =  random.choice(dict_['operation'])
    else:
        output_dict['expression_type'] = random.choice(dict_['operation'][:3])
        
    
    return output_dict


