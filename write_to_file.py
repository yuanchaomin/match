# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:01:53 2017

@author: Chaomin
"""
import json
import data_generator_3 as d_g

s = d_g.complex_predicate_generator(3, d_g.simple_predicate_generator, d_g.attributes_dict)
dumped = json.dumps(s, sort_keys=True, indent=5)

# with open('sample_data.txt','w') as file:
#     for i in range(0,100):
#         s = d_g.complex_predicate_generator(3, d_g.simple_predicate_generator, d_g.attributes_dict)
#         s['id'] = i
#         dumped_file = json.dumps(s, sort_keys=True, indent=5)
#         file.writelines(dumped_file + '\n\n')

with open('sample_borrowers_data.txt','w') as file:
    for i in range(0,100):
        s = d_g.generate_borrowers_order(d_g.attributes_dict)
        s['id'] = i
        dumpted_file = json.dumps(s, sort_keys=True, indent=5)
        file.writelines(dumpted_file + '\n\n')
