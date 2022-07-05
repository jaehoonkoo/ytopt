import os

from pprint import pformat
from collections import OrderedDict

class Problem:
    """Problem specification for ytopt"""

    def __init__(self, app_name, app_exe, args_template):
        self.app_name = app_name
        self.app_exe = app_exe
        self.args_template = args_template
        self.num_params = self.args_template.count("{}")
        self.__space = [None for _ in range(self.num_params)]
        self.__def_values = [None for _ in range(self.num_params)]
        self.resources = OrderedDict(
            num_nodes=None,
            ranks_per_node=None,
            threads_per_rank=None,
            threads_per_core=None,
            cpu_binding=None,
            env=None)
        print ('=======================',self.args_template,self.app_exe)
    def __str__(self):
        return repr(self)

    def __repr__(self):

        rep_args_frmt = f'command format: \n "{self.app_exe} {self.args_template}"'
        starting_cmd = f'starting point: \n "{self.args_template.format(*self.__def_values)}"'
        rep_space = ""
        ln = len(str(self.num_params))
        for i,v in enumerate(self.__space):
            tmp = '  {:'+str(ln)+'}: {} \n'
            rep_space += tmp.format(i, v)

        resources = "resources dimensions:\n"
        for r in self.resources:
            resources += f" {r}: {str(self.resources[r])}\n"

        rep = f'{rep_args_frmt}\n\n{starting_cmd}\n\napplication dimensions:\n{rep_space}\n{resources}'
        return rep

    def spec_dim(self, p_id, p_space, default=None):
        """Add a dimension to the search space.
        Args:
            p_id (int): id of parameter.
            p_space (Object): space corresponding to the new dimension.
            default: default value of the new dimension, it must be compatible with the ``p_space`` given.
        """
        # assert type(p_id) is int, f'p_id must be int type, got {type(p_id)} !'
        assert type(p_space) is tuple or type(p_space) is list, f'p_space must be tuple or list type, got {type(p_space)} !'
        self.__space[p_id] = p_space
        self.__def_values[p_id] = default

    @property
    def starting_point(self):
        """Starting point of the search space.
        """
        return self.__def_values

    @property
    def starting_point_asdict(self):
        dd = {str(k):v for k,v in enumerate(self.__def_values)}
        for k in self.resources:
            if self.resources[k] is not None \
                and (type(self.resources[k]) is list \
                    or type(self.resources[k]) is tuple):
                dd[k] = self.resources[k][0]
        return dd

    @property
    def space(self):
        dd = {str(k):v for k,v in enumerate(self.__space)}
        for k in self.resources:
            if self.resources[k] is not None \
                and (type(self.resources[k]) is list \
                    or type(self.resources[k]) is tuple):
                dd[k] = self.resources[k]
        return dd

    @property
    def params(self):
        return [i for i in range(self.num_params)]

    def args_format(self, x):
        return self.args_template.format(*x)

    def checkcfg(self):
        assert type(self.args_template) is str, f"args_frmt must be of type str when it is of type {type(self.args_template)}"
        assert sum(map(lambda x: x == None, self.space)) == 0, f"you still have unspecified parameters"
