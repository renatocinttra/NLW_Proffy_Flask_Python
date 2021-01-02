from setuptools import setup, find_packages
""" Este arquivo será responsável em permitir que aplicação seja instalada através do 'pip install' """

def read(filename):
    """Funçao responsável em ler os arquivos 'requirements.txt' e pegar o conteúdo do arquivo para posterior uso no 'setup.py'"""
    return[
        req.strip() # Comando retira o /n após a leitura do conteúdo do arquivo
        for req
        in open(filename).readlines()
    ]

setup(
    name="Proffy",
    version="0.1.0",
    description="Education",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)