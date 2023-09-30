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

    