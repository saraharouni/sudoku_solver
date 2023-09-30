\# sudoku\_solver

Commande dans la console pour executer le code:

'''

python main.py --solver (**backtracking** ou **brute_force**) grille/(sudoku.txt==)

'''

\# Analyse de la complexité des algorithmes de type brute force et backtracking

\# Grid                    Brute Force     Backtracking  

grille/sudoku.txt          0.0000          0.0000

grille/sudoku2.txt         0.0158          0.0158

grille/sudoku3.txt         0.0000          0.0000

grille/sudoku4.txt         0.0621          0.0625

grille/evilsudoku.txt      0.0314          0.0310

Voici quelques conclusions que l'on peut tirer à partir de ces résultats :

\# Temps d'exécution :

Les temps d'exécution pour la plupart des grilles sont très courts, de l'ordre de millisecondes. Cela signifie que les deux approches, brute force et backtracking, sont très efficaces pour résoudre les grilles de Sudoku, du moins pour les grilles de petite taille.

\# Similitude des performances :

Dans la plupart des cas, les temps d'exécution de la méthode de brute force et de backtracking sont très proches, voire identiques. Cela suggère que, pour ces grilles spécifiques, les deux approches donnent des résultats similaires en termes de rapidité.

\# Puzzles faciles vs. puzzles difficiles :

Les grilles "sudoku.txt" et "sudoku3.txt" ont des temps d'exécution très courts pour les deux méthodes, ce qui indique qu'ils sont relativement faciles à résoudre. En revanche, les grilles "sudoku2.txt", "sudoku4.txt" et "evilsudoku.txt" prennent un peu plus de temps, suggérant qu'ils sont plus difficiles à résoudre.

\# Efficacité de l'algorithme :

Bien que les deux approches aient des performances similaires pour ces grilles spécifiques, il est important de noter que l'efficacité de l'algorithme peut dépendre de la structure de la grilles. Certaines grilles peuvent être plus adaptées à une approche de force brute, tandis que d'autres peuvent bénéficier davantage de l'approche de backtracking.

\# Complexité algorithmique du brute force :

Pour analyser la complexité de cet algorithme, nous pouvons considérer le pire scénario, c'est-à-dire une grille Sudoku qui nécessite d'explorer toutes les combinaisons possibles pour chaque case. Dans un tel cas, chaque case de la grille doit être remplie en testant les chiffres de 1 à 9 jusqu'à ce que la bonne combinaison soit trouvée.

La complexité de l'algorithme est souvent exprimée en notation "big O" (O) et est généralement exprimée comme O(n^n), où "n" est la taille de la grille.

Dans ce cas, "n" est égal à 9 car nous parlons d'une grille Sudoku standard de 9x9.

Soit O(9^9), ce qui signifie une croissance exponentielle du nombre d'opérations avec la taille de la grille.

\# Complexité algorithmique du backtracking :

L'algorithme de type backtracking pour résoudre le Sudoku a une complexité beaucoup plus favorable que l'algorithme de force brute. Sa complexité dépend principalement du nombre de cases vides dans la grille.

Dans le pire cas, lorsque la grille est vide, l'algorithme doit explorer toutes les combinaisons possibles pour chaque case. Cela signifie qu'il doit essayer les chiffres de 1 à 9 pour chaque case vide.

Si "n" est le nombre de cases vides dans la grille, l'algorithme essaiera au maximum 9 choix pour chaque case vide, ce qui donne 9^n combinaisons possibles à explorer.

Par conséquent, la complexité de l'algorithme de backtracking est O(9^n) dans le pire cas, où "n" est le nombre de cases vides.

En résumé, la complexité de l'algorithme de backtracking dépend du nombre de cases vides dans la grille, ce qui donne une complexité théorique de O(9^n) dans le pire cas.
