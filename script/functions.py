import numpy as np

# AU PLACARD ?:
def create_random_seq(length=16, num_dots=8):
    seq = []
    current = rd.randint(0, num_dots-1)
    seq.append(current)
    for _ in range(length-1):
        next_dot = rd.randint(0, num_dots-1)
        while next_dot == current:
            next_dot = rd.randint(0, num_dots-1)
        seq.append(next_dot)
        current = next_dot
    return np.asarray(seq)

# VERSION corriger a voir si on garde
def randomize_order2(sequences):
    seq_out = sequences.copy()  #  CORRECTION
    rd.shuffle(seq_out)
    return seq_out

def randomize_start2(sequences):
    seq_out = []
    for seq in sequences:# correction pour randomiser seulement le depart
        offset = rd.randint(0, NUM_OF_DOT - 1)
        rotated_seq = [((pos + offset) % NUM_OF_DOT, direction) for pos, direction in seq]
        seq_out.append(rotated_seq)
    return seq_out

-----

# CREATED IRR SEQ 
def generate_all_possible_sequences(length=3):
   
    # Pour chaque position : 8 choix de point × 2 directions = 16 possibilités par élément
    
    all_sequences = []
    
    def generate_recursive(current_seq, remaining_length):
        if remaining_length == 0:
            all_sequences.append(current_seq[:])
            return
        
        for position in range(NUM_OF_DOT):
            for direction in [1, -1]:
                current_seq.append((position, direction))
                generate_recursive(current_seq, remaining_length - 1)
                current_seq.pop()
    
    generate_recursive([], length)
    return all_sequences


def filter_irregular_sequences(all_sequences, regular_sequences):
    # que les séquences irrégulières valides => Devrait donner 768 séquences selon l'article.

    irregular = []
    
    for seq in all_sequences:
        if is_valid_irregular_sequence(seq, regular_sequences):
            irregular.append(seq)
    
    return irregular

def create_irregular_sequence_pool(regular_sequences, initial_length=3):
    #    Crée le pool complet des 768 séquences irrégulières.
    
    print(f"Generating all possible sequences of length {initial_length}...")
    all_possible = generate_all_possible_sequences(initial_length)
    print(f"Total possible sequences: {len(all_possible)}")
    
    print("Filtering irregular sequences...")
    irregular_pool = filter_irregular_sequences(all_possible, regular_sequences)
    print(f"Valid irregular sequences found: {len(irregular_pool)}")
    
    return irregular_pool

def sample_irregular_sequences(irregular_pool, num_sequences=9):
   #    Sélectionne aléatoirement des séquences du pool.
    
    return rd.sample(irregular_pool, num_sequences)

----
# CONDITIONS 
def is_regular_sequence(seq):#    Vérifie si une séquence est régulière (pattern constant).
    if len(seq) < 2:
        return False
    
    positions = [s[0] for s in seq]
    directions = [s[1] for s in seq]
    
    # Vérifier si la direction est constante
    if len(set(directions)) != 1:
        return False
    
    direction = directions[0]
    
    # Calculer les sauts entre positions consécutives
    jumps = []
    for i in range(len(positions) - 1):
        if direction == 1:  # horaire
            jump = (positions[i+1] - positions[i]) % NUM_OF_DOT
        else:  # antihoraire
            jump = (positions[i] - positions[i+1]) % NUM_OF_DOT
        jumps.append(jump)
    
    # Régulière si tous les sauts sont identiques
    return len(set(jumps)) == 1 and jumps[0] != 0


def has_repetition(seq, max_length=2):#    Vérifie s'il y a des répétitions de sous-séquences.
    positions = [s[0] for s in seq]
    
    # Vérifier répétition immédiate
    for i in range(len(positions) - 1):
        if positions[i] == positions[i+1]:
            return True
    
    # Vérifier patterns répétés
    for length in range(2, min(max_length + 1, len(positions) // 2 + 1)):
        for i in range(len(positions) - 2 * length + 1):
            pattern = positions[i:i+length]
            for j in range(i + length, len(positions) - length + 1):
                if positions[j:j+length] == pattern:
                    return True
    
    return False

def has_symmetry(seq):#    Vérifie s'il y a une symétrie dans la séquence.
    positions = [s[0] for s in seq]
    
    # Symétrie miroir
    if positions == positions[::-1]:
        return True
    
    # Symétrie centrale (points opposés sur l'octogone)
    n = len(positions)
    for i in range(n // 2):
        if (positions[i] + 4) % NUM_OF_DOT != positions[n - 1 - i]:
            break
    else:
        if n > 1:
            return True
    
    return False

ef has_obvious_pattern(seq):#    Détecte des patterns visuels évidents :
    # Alternance simple (ex: 0, 2, 0, 2, 0, 2...)/  Motifs trop prévisibles
    positions = [s[0] for s in seq]
    
    if len(positions) < 4:
        return False
    
    # Vérifier alternance simple (A, B, A, B, A, B...)
    if len(set(positions[::2])) == 1 and len(set(positions[1::2])) == 1 and len(positions) > 3:
        return True
    
      
    # Vérifier si les différences forment un pattern
    differences = [(positions[i+1] - positions[i]) % NUM_OF_DOT for i in range(len(positions) - 1)]
    
    # Pattern de différences identiques par paires
    if len(differences) >= 4:
        pairs = [(differences[i], differences[i+1]) for i in range(0, len(differences)-1, 2)]
        if len(set(pairs)) == 1:
            return True
    
    return False

def is_too_similar_to_regular(seq, regular_sequences):#    Vérifie si la séquence est trop similaire à une séquence régulière.
    #Compare avec toutes les rotations et directions possibles.
    for reg in regular_seqs:
        # Comparaison directe
        if seq == reg:
            return True
        # Comparaison rotation
        for rotation in range(len(seq)):
            if seq == reg[rotation:] + reg[:rotation]:
                return True
        # Comparaison inversion
        if seq == reg[::-1]:
            return True
    return False   

def is_valid_irregular_sequence(seq, regular_sequences):
    """
    Vérifie tous les critères d'irrégularité.
    """
    # Pas régulière
    if is_regular_sequence(seq):
        return False
    
    # Pas de répétitions
    if has_repetition(seq):
        return False
    
    # Pas de symétrie
    if has_symmetry(seq):
        return False
    
    # Ne correspond pas à une séquence régulière
    if has_obvious_pattern(seq):
        return False
    
    return True

    if is_too_similar_to_regular(seq, regular_sequences)
        return False
    
    return True

def init_exp_irr_pool():
   
    # Générer le pool de 768 séquences irrégulières
    irregular_pool = create_irregular_sequence_pool(regular_sequences_base, initial_length=3)
    
    # Vérifier qu'on a bien 768 séquences
    if len(irregular_pool) != 768:
        print(f"WARNING: Expected 768 irregular sequences, got {len(irregular_pool)}")
    
    # Sélectionner 9 séquences irrégulières aléatoirement
    selected_irregular = sample_irregular_sequences(irregular_pool, num_sequences=9)
    
    # Combiner avec les 8 séquences régulières (versions complètes pour l'expérience)
    regular_sequences_full = C_sequences_ez + C_sequences  # Vos vraies séquences
    all_sequences = regular_sequences_full + selected_irregular
    
    # Randomiser positions de départ
    all_sequences = randomize_start(all_sequences)
    
    # Randomiser l'ordre
    rd.shuffle(all_sequences)
    
    return all_sequences
