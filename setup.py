from setuptools import setup, find_packages

setup(
    name="sliding-puzzle",
    version="0.1.0",
    description="Un jeu de puzzle coulissant avec algorithmes de résolution",
    author="Votre Nom",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Aucune dépendance à signaler pour le moment 
    ],
    python_requires=">=3.6",
)