from tasks import commonFunctions
from tasks.big_task import functions as big_task_functions 
from tasks.report_task import functions as report_task_functions

'''
This file contains the dictionary to task functions so that
they can be called from strings, i.e.
task_functions[<bucket>][<function_label>](**kwargs)
'''

task_functions = {
    'big_task': {
        'get_title_str': big_task_functions.get_title_str,
        'get_imgs': big_task_functions.get_imgs,
        'get_observacao': big_task_functions.get_observacao,
    },
    'report_task': {
        'get_status': report_task_functions.get_status,
    },
    'common': {
        'get_arg': commonFunctions.get_arg,
    }
}