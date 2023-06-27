class Node:
    def __init__(self, state, depth, maximizing_player):
        self.state = state
        self.depth = depth
        self.maximizing_player = maximizing_player
        self.children = []
        self.value = None

    def generate_children(self):

    # Gera os possíveis movimentos a partir do estado atual
    # Cria um nó filho para cada movimento
    # Atualiza self.children

    def evaluate(self):

    # Implemente uma função de avaliação para atribuir um valor ao estado atual
    # Quanto maior o valor, melhor para o jogador que está maximizando
    # Quanto menor o valor, melhor para o jogador que está minimizando
    # Atualize self.value

    def is_terminal(self):

    # Verifica se o nó é um estado terminal (fim do jogo ou profundidade máxima atingida)
    # Retorna True ou False

    def find_best_move(self):
        best_move = None
        best_value = float('-inf') if self.maximizing_player else float('inf')

        for child in self.children:
            child.evaluate()

            if self.maximizing_player and child.value > best_value:
                best_value = child.value
                best_move = child.move
            elif not self.maximizing_player and child.value < best_value:
                best_value = child.value
                best_move = child.move

        return best_move


def make_decision(board):
    root = Node(board, 0, True)
    root.generate_children()
    best_move = root.find_best_move()
    return best_move
