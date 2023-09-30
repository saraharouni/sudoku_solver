import pygame
import argparse
import time
import random

class BruteForceSolver:
    def __init__(self, filename, calculate_algorithm_time=True):
        self.grid = self.load_grid(filename)
        self.original_grid = [row[:] for row in self.grid]
        self.N = 9
        self.calculate_algorithm_time = calculate_algorithm_time
        self.execution_time_algorithm = 0.0

    def load_grid(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        char_lists = []
        for line in lines:
            line = [int(char) if char != '_' else 0 for char in line.strip()]
            char_lists.append(line)

        return char_lists

    def printing_with_color(self, solved_grid, solve_completed):
        for i in range(self.N):
            for j in range(self.N):
                num = self.grid[i][j]
                color = '\033[0m' if num != 0 and (not solve_completed or num == self.original_grid[i][j]) else '\033[91m'
                print(f'{color}{num}', end=" ")
            print()

    def printing(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.grid[i][j], end=" ")
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

    def generate_random_grid(self):
        empty_cells = [(i, j) for i in range(self.N) for j in range(self.N) if self.grid[i][j] == 0]
        random.shuffle(empty_cells)
        return self.solve_random(empty_cells)

    def solve_random(self, empty_cells):
        if not empty_cells:
            return True

        i, j = empty_cells.pop()
        nums = list(range(1, 10))
        random.shuffle(nums)
        for num in nums:
            if self.isSafe(i, j, num):
                self.grid[i][j] = num
                if self.solve_random(empty_cells):
                    return True
                self.grid[i][j] = 0
        empty_cells.append((i, j))
        return False

    def solveSudoku(self):
        while not self.isSolved():
            empty_cells = [(i, j) for i in range(self.N) for j in range(self.N) if self.grid[i][j] == 0]
            random.shuffle(empty_cells)
            if not self.solve_random(empty_cells):
                # Si la génération aléatoire échoue, réinitialiser la grille et recommencer
                self.grid = [row[:] for row in self.original_grid]

    def isSolved(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[i][j] == 0 or not self.isSafe(i, j, self.grid[i][j]):
                    return False
        return True

def display_sudoku_grid(solver, original_grid, solve_completed):
    pygame.init()
    WIDTH, HEIGHT = 600, 700
    GRID_SIZE = WIDTH // 9
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku Solver BRUTE FORCE")
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

        screen.fill(WHITE)

        for i in range(9 + 1):
            line_thickness = 2 if i % 3 == 0 else 1
            pygame.draw.line(screen, BLACK, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE), line_thickness)
            pygame.draw.line(screen, BLACK, (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT - 100), line_thickness)

        font = pygame.font.Font(None, 36)
        for i in range(9):
            for j in range(9):
                num = original_grid[i][j] if not solve_clicked else solver.grid[i][j]
                color = BLACK if num != 0 and (not solve_completed or num == original_grid[i][j]) else RED
                text = font.render(str(num) if num != 0 else "", True, color)
                text_rect = text.get_rect(center=(j * GRID_SIZE + GRID_SIZE / 2, i * GRID_SIZE + GRID_SIZE / 2))
                screen.blit(text, text_rect)

        pygame.draw.rect(screen, GREEN, (WIDTH // 2 - 50, HEIGHT - 60, 100, 50))
        font = pygame.font.Font(None, 36)
        text = font.render("Solve", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 35))
        screen.blit(text, text_rect)
        pygame.display.flip()

    pygame.quit()

def main():
    parser = argparse.ArgumentParser(description="Sudoku Solver")
    parser.add_argument("filename", help="Chemin vers le fichier Sudoku à résoudre")
    parser.add_argument("--no-algorithm-time", action="store_false", dest="calculate_algorithm_time", default=True,
                        help="Ne pas calculer le temps d'exécution de l'algorithme")
    args = parser.parse_args()
    solver = BruteForceSolver(args.filename, calculate_algorithm_time=args.calculate_algorithm_time)
    solve_completed = False
    display_sudoku_grid(solver, solver.original_grid, solve_completed)

if __name__ == "__main__":
    main()
