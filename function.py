class Function:
    def __init__(self, function_string, function, singularity=None):
        self.f_string = function_string
        self.f = function
        self.s = singularity