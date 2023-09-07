"""An object representing the options for splitting the book."""

from pathlib import Path


class Options:
    def __init__(self, n_volumes, year, imprimeurs):
        self.n_volumes = n_volumes
        self.year = year
        self.imprimeurs = imprimeurs
        self.title = "Le Frido"
        self.out_dir = Path('.').resolve() / "output"
