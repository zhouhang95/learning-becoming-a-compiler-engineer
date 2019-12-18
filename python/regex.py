class FiniteAutomata:
    def __init__(self):
        self.fa_type = None
        self.states = []
        self.startstate = None
        self.finalstates = []
        self.transitions = {}
    
    def index_offset(self, offset: int):
        self.startstate += offset
        self.states = list(map(lambda x: x+offset, self.states))
        self.finalstates = list(map(lambda x: x+offset, self.finalstates))
        transitions = {}
        for k, v in self.transitions.items():
            transitions[(k[0]+offset, k[1]+offset)] = v
        self.transitions = transitions

    def __str__(self):
        sink = 'FA Type: {}'.format(self.fa_type)
        sink += '\nstates: ' + ','.join(map(str, self.states)) 
        sink += '\nstartstate: ' + str(self.startstate)
        sink += '\nfinalstates: ' + ','.join(map(str, self.finalstates))
        sink += '\ntransitions:'
        for k, v in self.transitions.items():
            sink += '\n\t{} -> {}: {}'.format(k[0], k[1], v)

        return sink

    def to_dfa(self):
        assert self.fa_type == 'NFA'
        pass

    def to_min_dfa(self):
        assert self.fa_type == 'DFA'

        pass

    def to_regex(self, method=''):
        pass



    @staticmethod
    def base(char: str):
        fa = FiniteAutomata()
        fa.fa_type = 'NFA'
        fa.startstate = 0
        fa.states.extend([0, 1])
        fa.finalstates.append(1)
        fa.transitions[(0, 1)] = char
        return fa

    @staticmethod
    def concatention(a, b):
        a_len = len(a.states)
        b.index_offset(a_len)

        fa = FiniteAutomata()
        fa.fa_type = 'NFA'
        fa.startstate = 0
        fa.states = a.states + b.states
        fa.finalstates = b.finalstates
        fa.transitions.update(a.transitions)
        fa.transitions.update(b.transitions)
        fa.transitions[(a.finalstates[0], b.startstate)] = 'epsilon'

        return fa

    
    @staticmethod
    def alternation(a, b):
        a_len = len(a.states)
        b_len = len(b.states)
        a.index_offset(1)
        b.index_offset(1 + a_len)

        fa = FiniteAutomata()
        fa.fa_type = 'NFA'
        fa.startstate = 0
        finalstate = 1 + a_len + b_len
        fa.states = a.states + b.states + [0, finalstate]
        fa.finalstates = [finalstate]
        fa.transitions = {
            (0, a.startstate): 'epsilon',
            (0, b.startstate): 'epsilon',
            (a.finalstates[0], finalstate): 'epsilon',
            (b.finalstates[0], finalstate): 'epsilon',
        }
        fa.transitions.update(a.transitions)
        fa.transitions.update(b.transitions)
        
        return fa
    
    @staticmethod
    def kleene_closure(a):
        a_len = len(a.states)
        a.index_offset(1)
        fa = FiniteAutomata()
        fa.fa_type = 'NFA'
        fa.startstate = 0
        finalstate = 1 + a_len
        fa.states = a.states + [0, finalstate]
        fa.finalstates = [finalstate]
        fa.transitions = {
            (0, a.startstate): 'epsilon',
            (a.finalstates[0], finalstate): 'epsilon',
            (a.finalstates[0], a.startstate): 'epsilon',
            (0, finalstate): 'epsilon',
        }
        fa.transitions.update(a.transitions)

        return fa

    @staticmethod
    def positive_closure(a):
        a_len = len(a.states)
        a.index_offset(1)
        fa = FiniteAutomata()
        fa.fa_type = 'NFA'
        fa.startstate = 0
        finalstate = 1 + a_len
        fa.states = a.states + [0, finalstate]
        fa.finalstates = [finalstate]
        fa.transitions = {
            (0, a.startstate): 'epsilon',
            (a.finalstates[0], finalstate): 'epsilon',
            (a.finalstates[0], a.startstate): 'epsilon',
        }
        fa.transitions.update(a.transitions)
        
        return fa

def regex2nfa(regex: str):
    pass

def main():
    a = FiniteAutomata.base('a')
    b = FiniteAutomata.base('b')
    print(FiniteAutomata.kleene_closure(a))
    


if __name__ == "__main__":
    main()