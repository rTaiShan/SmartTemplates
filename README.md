# Jinja Smart Templates

This respository aims to provide a solid platform for custom, dynamically generated HTML using Python and Jinja.

## Basic Operation

The proccess through which each HTML is rendered is called a Task.

A Task consists of three parts:

* Jinja Template: This HTML file defines the layout of the task. It includes standard HTML features such as structuring and presentation, but also variable fields.
* Task Functions: The set of python functions used to generate the variables.
* Task Definition: This defines the behavior of the task, associating the template, the functions and their arguments.

## Task Definition
Tasks are defined by default in tasks/tasks.json

A Task Definition is as such:

```json
{
        "task_name": "Big Task",
        "task_code": "big_task",
        "functions_code": "big_task",
        "enabled": true,
        "html_source": "big_task\\template.html",
        "base_path": "tasks\\",
        "variables": {
            "title_str": {
                "function": "get_title_str",
                "args": {
                    "start_date": 2
                }
            },
            "imgs": {
                "function": "get_imgs",
                "args": {
                    "img_paths": [
                        "media\\image.png",
                        "media\\image.gif"
                    ]
                }
            },
            "observacao": {
                "function": "get_observacao",
                "args": {
                    "codigo": "2"
                }
            }
        }
    },
```

* task_name : A pretty-print name for the task
* task_code : Optional, defines the internal "name" for the task. If not given, it assumes the task_name, replacing all spaces with underscores and lowering all the letters. i.e. "Big Task" -> "big_task".
* functions_code : Defines the bucket of functions for the task. This way, different tasks may reuse the same functions. See the tasks associated with "report_task"
* enabled : Unless specified, a task where enabled==False won't run.
* base_path : The base path to look for templates. Useful for inheritance.
* html_source : The path of the html template will be defined by base_path + html_source
* variables : All the variables in the template. A variable is defined by a function and its arguments.
  * function : The label of the function. More on this in the "Task Functions" section.
  * args : Set of named arguments for the function. It is later called like f(**kwargs).

## Jinja Template

Jinja allows the insertion of variables, conditional and branching statements in html, making for a very powerful tool. However, not much knowledge is needed to get started making your own Smart Templates.

* Jinja allows inheritance between html files. Thus it is possible to, for instance, define the fonts in a file and use them in another. See the files "index.html" and any "template.html".
  * Notice {% extends "index.html" %}, {% block content %}, {% endblock %}. Those signify that "template.html" inherits from index.html and that it overrides the block **named** "content".
* Jinja allows the placement of variables inside html files.
  * That is done with "{{ <var_name> }}".
  * Variables may be indexed by attributes and regular python notation, i.e. <var_name>.<att_name> and <var_name>[<att_name>]

For more information on Jinja: [Jinja Wiki](https://jinja.palletsprojects.com/en/)

## Task Functions

Task functions are regular python functions. They only take in named args (for now, at least).

They can be defined anywhere, but for organization sake, it is recommended to group the template and the functions in the same folder. See the examples inside "tasks".

After defined, they **must** be included in "tasks.taskFunctions" such that the function object is referenced by the task's function code and the function name in the task definition. i.e. task_functions[<function_code>][<function_name>] = <Python_Function>

If function_name is "common.<rest_of_name>" it will instead look at task_functions['common'][<rest_of_name>], allowing the user to recycle common functions.

See tasks/taskFunctions.py for examples.
