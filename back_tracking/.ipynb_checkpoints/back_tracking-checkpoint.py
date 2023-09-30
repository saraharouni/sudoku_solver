import pygame
import argparse
import time

class BacktrackingSolver:
    def __init__(self, filename, calculate_algorithm_time=True):
        self.grid = self.load_grid(filename)
        self.original_grid = [row[:] for row in self.grid]  # Créez une copie de la grille de base
        self.N = 9
        self.calculate_algorithm_time = calculate_algorithm_time
        self.execution_time_algorithm = 0.0  # Initialisation du temps d'exécution de l'algorithme


    def load_grid(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        char_lists = []
        for line in lines:
            line = [int(char) if char != '_' else 0 for char in line.strip()]
            char_lists.append(line)

        return char_lists

    def printing(self, solved_grid, solve_completed):
        for i in range(self.N):
            for j in range(self.N):
                num = self.grid[i][j]
                color = '\033[0m' if num != 0 and (not solve_completed or num == self.original_grid[i][j]) else '\033[91m'
                print(f'{color}{num}', end=" ")
            print()

    def isSafe(self, row, col, num):
        for x in range(self.N):
            if self.grid[row][x] == num:
                return False

        for x in range(self.N):
            if self.grid[x][col] == num:
                return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + startRow][j + startCol] == num:
                    return False
        return True

    def solveSudoku(self):
        def solve(row, col):
            if (row == self.N - 1 and col == self.N):
                return True

            if col == self.N:
                row += 1
                col = 0

            if self.grid[row][col] > 0:
                return solve(row, col + 1)

            for num in range(1, self.N + 1, 1):
                if self.isSafe(row, col, num):
                    self.grid[row][col] = num
                    if solve(row, col + 1):
                        return True
                    self.grid[row][col] = 0
            return False

        if self.calculate_algorithm_time:
            start_time = time.time()

        if solve(0, 0):
            if self.calculate_algorithm_time:
                end_time = time.time()
                self.execution_time_algorithm = end_time - start_time  # Calcul du temps d'exécution de l'algorithme
            self.printing(self.grid, True)
        else:
            print("No solution exists")

def display_sudoku_grid(solver, original_grid, solved_grid, solve_completed):
    pygame.init()
    # Charger la police Arial avec une taille de 36
    custom_font = pygame.font.SysFont("georgia", 36)
    # Dimensions de la fenêtre Pygame
    WIDTH, HEIGHT = 600, 700
    GRID_SIZE = WIDTH // 9

    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # Création de la fenêtre Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku Solver BACK TRACKING")

    running = True
    solve_clicked = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not solve_clicked:
                if WIDTH // 2 - 50 <= event.pos[0] <= WIDTH // 2 + 50 and HEIGHT - 60 <= event.pos[1] <= HEIGHT - 10:
                    solve_clicked = True
                    solver.solveSudoku()
                    solve_completed = True

        # Effacer l'écran
        screen.fill(WHITE)

        # Dessiner la grille Sudoku (lignes horizontales et verticales)
        for i in range(9 + 1):
            line_thickness = 2 if i % 3 == 0 else 1

            # Dessiner les lignes horizontales
            pygame.draw.line(screen, BLACK, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE), line_thickness)
            # Dessiner les lignes verticales
            pygame.draw.line(screen, BLACK, (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT - 100), line_thickness)

        # Dessiner la grille Sudoku (nombres)
        font = pygame.font.Font(None, 36)
        for i in range(9):
            for j in range(9):
                num = original_grid[i][j] if not solve_clicked else solved_grid[i][j]
                color = BLACK if num != 0 and (not solve_completed or num == original_grid[i][j]) else RED
                text = font.render(str(num) if num != 0 else "", True, color)
                text_rect = text.get_rect(center=(j * GRID_SIZE + GRID_SIZE / 2, i * GRID_SIZE + GRID_SIZE / 2))
                screen.blit(text, text_rect)

        # Dessiner le bouton "Solve"
        pygame.draw.rect(screen, GREEN, (WIDTH // 2 - 50, HEIGHT - 60, 100, 50))
        font = pygame.font.Font(None, 36)
        text = font.render("Solve", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 35))
        screen.blit(text, text_rect)

        # Mettre à jour l'affichage
        pygame.display.flip()

    pygame.quit()

def main():
    parser = argparse.ArgumentParser(description="Sudoku Solver")
    parser.add_argument("filename", help="Chemin vers le fichier Sudoku à résoudre")
    parser.add_argument("--no-algorithm-time", action="store_false", dest="calculate_algorithm_time", default=True,
                        help="Ne pas calculer le temps d'exécution de l'algorithme")
    args = parser.parse_args()
    solver = BacktrackingSolver(args.filename, calculate_algorithm_time=args.calculate_algorithm_time)
    solve_completed = False
    display_sudoku_grid(solver, solver.original_grid, solver.grid, solve_completed)
    solver.printing(solver.grid, solve_completed)
    
if __name__ == "__main__":
    main()
