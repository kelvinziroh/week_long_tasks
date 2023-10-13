from collections import defaultdict

def compute_first_set(grammar):
    first = defaultdict(set)
    
    for non_terminal in grammar:
        compute_first_set_recursive(grammar, non_terminal, first)
    
    return first

def compute_first_set_recursive(grammar, symbol, first):
    if symbol in first:
        return
    
    for production in grammar[symbol]:
        first_symbol = production[0]
        
        if first_symbol.islower() or first_symbol == 'epsilon':
            first[symbol].add(first_symbol)
        elif first_symbol.isupper():
            compute_first_set_recursive(grammar, first_symbol, first)
            first[symbol] |= first[first_symbol]
            
            if 'epsilon' in first[first_symbol]:
                first[symbol].remove('epsilon')
                
        if 'epsilon' not in first[first_symbol]:
            break

def compute_follow_set(grammar, start_symbol, first):
    follow = defaultdict(set)
    follow[start_symbol].add('$')
    
    for non_terminal in grammar:
        for production in grammar[non_terminal]:
            for i, symbol in enumerate(production):
                if symbol.isupper():
                    if i < len(production) - 1:
                        first_of_next = first[production[i + 1]]
                        follow[symbol] |= (first_of_next - {'epsilon'})
                        
                        if 'epsilon' in first_of_next:
                            follow[symbol] |= follow[non_terminal]
                    else:
                        follow[symbol] |= follow[non_terminal]
                        
    return follow

def construct_ll1_table(grammar, start_symbol):
    ll1_table = defaultdict(dict)
    first = compute_first_set(grammar)
    follow = compute_follow_set(grammar, start_symbol, first)
    
    for non_terminal in grammar:
        for production in grammar[non_terminal]:
            first_of_production = set()
            
            for symbol in production:
                if symbol.islower() or symbol == 'epsilon':
                    first_of_production.add(symbol)
                    break
                elif symbol.isupper():
                    first_of_production |= first[symbol]
                    
                    if 'epsilon' not in first[symbol]:
                        break
            
            for terminal in first_of_production:
                if terminal != 'epsilon':
                    ll1_table[non_terminal][terminal] = production
    
            if 'epsilon' in first_of_production:
                for terminal in follow[non_terminal]:
                    ll1_table[non_terminal][terminal] = production
    
    return ll1_table

def display_ll1_table(ll1_table):
    print("LL(1) Parsing Table:")
    for non_terminal in ll1_table:
        for terminal in ll1_table[non_terminal]:
            print(f"{non_terminal} -> {ll1_table[non_terminal][terminal]}\t for {terminal}")
    
# Example CFG
example_grammar = {
    'S': ['aA', 'bB'],
    'A': ['c', 'epsilon'],
    'B': ['d', 'epsilon']
}

start_symbol = 'S'

ll1_table = construct_ll1_table(example_grammar, start_symbol)
display_ll1_table(ll1_table)
