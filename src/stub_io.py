"""Io-luokan stub
"""

class StubIO:

    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)

    def read(self, prompt=None):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return "q"

    def add_input(self, value):
        self.inputs.append(value)
