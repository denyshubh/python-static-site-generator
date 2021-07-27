'''
Site Class: 

Args:
Methods:

'''
from pathlib import (
    Path,
    PurePath,
)

class Site:
    '''
    '''
    def __init__(self, source, dest) -> None:
        self.source = Path(source)
        self.dest = Path(dest)
    
    def create_dir(self):
        '''
        '''
        directory = f'{self.dest}/{PurePath.relative_to(self.source)}'
        Path.mkdir(directory, parents=True, exist_ok=True)
    
    def build(self):
        '''
        '''
        Path.mkdir(self.dest, parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir()




    
