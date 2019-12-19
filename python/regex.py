class FiniteAutomata:
    def __init__(self):
        self.fa_type = None
        self.states = []
        self.startstate = None
        self.finalstates = []
        self.transitions = []
    
    def index_offset(self, offset: int):
        self.startstate += offset
        self.states = list(map(lambda x: x+offset, self.states))
        self.finalstates = list(map(lambda x: x+offset, self.finalstates))
        transitions = []
        for node_0, node_1, edge in self.transitions:
            transitions.append((node_0+offset, node_1+offset, edge))
        self.transitions = transitions

    def __str__(self):
        sink = 'FA Type: {}'.format(self.fa_type)
        sink += '\nstates: ' + ','.join(map(str, self.states)) 
        sink += '\nstartstate: ' + str(self.startstate)
        sink += '\nfinalstates: ' + ','.join(map(str, self.finalstates))
        sink += '\ntransitions:'
        for node_0, node_1, edge in self.transitions:
            sink += '\n\t{} -> {}: {}'.format(node_0, node_1, edge)

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
        fa.transitions.append((0, 1, char))
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
        fa.transitions = a.transitions + b.transitions
        fa.transitions.append((a.finalstates[0], b.startstate, None))

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
        fa.transitions = [
            (0, a.startstate, None),
            (0, b.startstate, None),
            (a.finalstates[0], finalstate, None),
            (b.finalstates[0], finalstate, None),
        ]
        fa.transitions += a.transitions + b.transitions
        
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
        fa.transitions = [
            (0, a.startstate, None),
            (a.finalstates[0], finalstate, None),
            (a.finalstates[0], a.startstate, None),
            (0, finalstate, None),
        ]
        fa.transitions += a.transitions

        return fa


def regex2nfa(regex: str):
    pass

def main():
    a = FiniteAutomata.base('a')
    b = FiniteAutomata.base('b')
    print(FiniteAutomata.concatention(a, b))
    a = FiniteAutomata.base('a')
    b = FiniteAutomata.base('b')
    print(FiniteAutomata.alternation(a, b))
    a = FiniteAutomata.base('a')
    b = FiniteAutomata.base('b')
    print(FiniteAutomata.kleene_closure(a))
    


if __name__ == "__main__":
    main()