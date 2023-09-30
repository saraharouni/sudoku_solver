import pygame
import argparse
import time
from brute_force.brute_force import BruteForceSolver
from back_tracking.back_tracking import BacktrackingSolver

def display_sudoku_grid_pygame(solver, original_grid, solved_grid, solve_completed):
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
    pygame.display.set_caption("Sudoku Solver")

    running = True
    solve_clicked = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not solve_clicked:
                if WIDTH // 2 - 50 <= event.pos[0] <= WIDTH // 2 + 50 and HEIGHT - 60 <= event.pos[1] <= HEIGHT - 10:
                    solve_clicked = True
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
    parser.add_argument("--solver", choices=["brute_force", "backtracking"], default="brute_force",
                        help="Choisissez le solveur à utiliser (brute_force par défaut)")

    args = parser.parse_args()

    if args.solver == "brute_force":
        solver = BruteForceSolver(args.filename)
    elif args.solver == "backtracking":
        solver = BacktrackingSolver(args.filename)

    solve_completed = False

    # Appel de la méthode de résolution du solveur choisi
    solver.solveSudoku()

    # Affichage de la grille Sudoku dans une fenêtre Pygame
    display_sudoku_grid_pygame(solver, solver.original_grid, solver.grid, solve_completed)

if __name__ == "__main__":
    main()
