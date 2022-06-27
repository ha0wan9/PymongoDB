from typing import Callable, List
import mypy.api

def check_type(value, typ):
    program_text = 'from typing import *; v: {} = {}'.format(typ, repr(value))
    normal_report, error_report, exit_code = mypy.api.run(['-c', program_text])
    return exit_code == 0
