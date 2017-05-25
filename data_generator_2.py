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

logic_linkage_list = ['or','and','not']

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

def complex_predicate_generator(depth, simple_predicate_generator_f, attribute_dict):
    state = random.randrange(0,3)
    if depth < 1:
        return simple_predicate_generator_f(attribute_dict)
    else:
        if state == 0:
            result_dict = {"expression_type" : "or"}
            random_number = random.randrange(0,3)
            if random_number == 0:
                result_dict["left_operand"] = complex_predicate_generator(depth - 1)
                result_dict["right_operand"] = complex_predicate_generator(depth - 1)
            elif random_number == 1:
                result_dict["left_operand"] = complex_predicate_generator(depth - 1)
                result_dict["right_operand"] = simple_predicate_generator_f(attribute_dict)
            elif random_number == 2:
                result_dict["left_operand"] = simple_predicate_generator_f(attribute_dict)
                result_dict["right_operand"] = complex_predicate_generator(depth - 1)
                
        if state == 1:
            result_dict = {"expression_type" : "and"}
            random_number = random.randrange(0,3)
            if random_number == 0:
                result_dict["left_operand"] = complex_predicate_generator(depth - 1)
                result_dict["right_operand"] = complex_predicate_generator(depth - 1)
            elif random_number == 1:
                result_dict["left_operand"] = complex_predicate_generator(depth - 1)
                result_dict["right_operand"] = simple_predicate_generator_f(attribute_dict)
            elif random_number == 2:
                result_dict["left_operand"] = simple_predicate_generator_f(attribute_dict)
                result_dict["right_operand"] = complex_predicate_generator(depth - 1)
        
        if state == 2:
            result_dict = {"exoression_type": "not"}
            random_number = random.randrange(0,2)
            if random_number == 0:
                result_dict["child"] = simple_predicate_generator_f(attribute_dict)
            else:
                result_dict["child"] = complex_predicate_generator(depth - 1)
        
    return result_dict