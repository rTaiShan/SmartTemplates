from jinja2 import Environment, FileSystemLoader, meta
from tasks.taskFunctions import task_functions
from json import loads

from tools.io import read_from_file

class Task:
    '''
    Used to render a Smart Template specified by html_source and variables.
    '''
    def __init__(self, 
                 task_name : str, 
                 html_source : str, 
                 variables : dict, 
                 base_path : str, 
                 enabled=True, 
                 task_code : str=None, 
                 functions_code : str=None
                 ) -> None:
        self.task_name = task_name
        self.task_code = "_".join((task_name.lower().split())) if task_code is None else task_code
        self.functions_code = self.task_code if functions_code is None else functions_code
        self.html_source = html_source
        self.base_path = base_path
        self.variables = variables
        self.enabled = enabled

    def __str__(self):
        return f"Task {self.task_code}"
    
    def __repr__(self):
        return self.__str__()
    

    def run(self, force=False) -> str:
        '''
        Renders Smart Template based on html and the variables specified
        '''
        if (not force) and (not self.enabled):
            return
        vars = {}
        for name, params in self.variables.items():
            params_split = params['function'].split(".")
            # Enable the use of common functions among tasks
            if params_split[0] == 'common':
                val = task_functions['common'][".".join(params_split[1::])](**params['args'])
            else:
                val = task_functions[self.functions_code][params['function']](**params['args'])
            vars.update({name: val})
        
        env = Environment(loader=FileSystemLoader(self.base_path))

        template_str = read_from_file(self.base_path + self.html_source)
        template = env.from_string(template_str)
        html_str = template.render(**vars)
        return html_str
    

def get_tasks(path="tasks\\tasks.json", filter_enabled=False) -> list[Task]:
    '''
    Reads json from path, interpreting it as a list of tasks. Returns the tasks it finds.
    '''
    tasks = loads(read_from_file(path))
    tasks = tasks if not filter_enabled else [t for t in tasks if t['enabled']]
    return [
        Task(
            task_name=task.get('task_name'),
            html_source=task.get('html_source'),
            functions_code=task.get('functions_code'),
            variables=task.get('variables'),
            enabled=task.get('enabled'),
            base_path=task.get('base_path'),
            ) for task in tasks
        ]
