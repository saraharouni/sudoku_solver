import pygame
import argparse
import time

class BruteForceSolver:
    """
    Classe représentant un solveur de Sudoku utilisant une approche de force brute.
    """

    def __init__(self, filename, calculate_algorithm_time=True):
        """
        Initialise le solveur de Sudoku par force brute.

        Args:
            filename (str): Le chemin vers le fichier Sudoku à résoudre.
            calculate_algorithm_time (bool): Indique si le temps d'exécution de l'algorithme doit être calculé.

        Attributes:
            grid (list[list[int]]): La grille Sudoku.
            original_grid (list[list[int]]): Une copie de la grille de base.
            N (int): La taille de la grille Sudoku (généralement 9x9).
            calculate_algorithm_time (bool): Indique si le temps d'exécution de l'algorithme doit être calculé.
            execution_time_algorithm (float): Le temps d'exécution de l'algorithme en secondes.
        """
        self.grid = self.load_grid(filename)
        self.original_grid = [row[:] for row in self.grid]  # Créez une copie de la grille de base
        self.N = 9
        self.calculate_algorithm_time = calculate_algorithm_time
        self.execution_time_algorithm = 0.0

    def load_grid(self, filename):
        """
        Charge une grille Sudoku à partir d'un fichier.

        Args:
            filename (str): Le chemin vers le fichier contenant la grille Sudoku.

        Returns:
            list[list[int]]: La grille Sudoku sous forme d'une liste de listes d'entiers.
        """
        with open(filename, 'r') as file:
            lines = file.readlines()

        char_lists = []
        for line in lines:
            line = [int(char) if char != '_' else 0 for char in line.strip()]
            char_lists.append(line)

        return char_lists

    def printing_with_color(self, solved_grid, solve_completed):
        """
        Affiche la grille Sudoku avec des couleurs pour mettre en évidence les valeurs résolues.

        Args:
            solved_grid (list[list[int]]): La grille Sudoku résolue.
            solve_completed (bool): Indique si la résolution est terminée.
        """
        for i in range(self.N):
            for j in range(self.N):
                num = self.grid[i][j]
                color = '\033[0m' if num != 0 and (not solve_completed or num == self.original_grid[i][j]) else '\033[91m'
                print(f'{color}{num}', end=" ")
            print()

    def printing(self):
        """
        Affiche la grille Sudoku.
        """
        for i in range(self.N):
            for j in range(self.N):
                print(self.grid[i][j], end=" ")
            print()

    def isSafe(self, row, col, num):
        """
        Vérifie si un numéro peut être placé en toute sécurité dans une case donnée.

        Args:
            row (int): L'indice de ligne de la case.
            col (int): L'indice de colonne de la case.
            num (int): Le numéro à placer dans la case.

        Returns:
            bool: True si le numéro peut être placé en toute sécurité, False sinon.
        """
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
        """
        Résout la grille Sudoku en utilisant une approche de force brute.

        Cette méthode remplit la grille en explorant toutes les combinaisons possibles
        pour chaque case, sans suivi de backtracking.

        Conditions de sortie :
            - Si la grille est correctement remplie, la méthode retourne True, indiquant
              qu'une solution a été trouvée.
            - Si aucune solution n'est trouvée après avoir exploré toutes les combinaisons,
              la méthode retourne False.

        Mécanisme de résolution :
            - La méthode utilise une boucle imbriquée pour parcourir toutes les cases.
            - Pour chaque case, elle teste toutes les combinaisons de chiffres de 1 à 9
              jusqu'à ce qu'une combinaison valide soit trouvée.
            - Si une combinaison valide est trouvée, elle passe à la case suivante.
            - Si aucune combinaison valide n'est trouvée pour une case donnée, la méthode
              retourne False et s'arrête.
        """
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
        else:
            print("No solution exists")