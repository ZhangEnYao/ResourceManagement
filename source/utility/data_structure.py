import itertools
import typing_extensions

class LexicographicalOrdering:
    
    def __init__(self, *standard_basis: tuple):

        self.standard_basis = standard_basis
    
    def __gt__(self, comparison: typing_extensions.Self):

        for component, component_comparison in itertools.zip_longest(self.standard_basis, comparison.standard_basis):

            if not component:
                return False
            elif not component_comparison:
                return True
            
            if component > component_comparison:
                return True
            elif component < component_comparison:
                return False
            else:
                continue
        
        return False
    
    def __ge__(self, comparison: typing_extensions.Self):

        if self.standard_basis == comparison.standard_basis:
            return True
        
        else:
            return self.standard_basis.__gt__(comparison.standard_basis)