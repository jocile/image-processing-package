from setuptools import setup, find_packages


def read_file(filename):
    """Leitura de arquivos com tratamento de erros."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")
        raise
    except Exception as e:
        print(f"Erro ao ler arquivo {filename}: {str(e)}")
        raise


def sanitize_requirements(requirements_file):
    """Sanitização de requisitos, removendo linhas vazias e comentários."""
    lines = [line.strip()
             for line in read_file(requirements_file).splitlines()]
    return [line for line in lines if line and not line.startswith("#")]


# Definição da versão
VERSION = "0.0.1"

setup(
    name="image-processing",
    version=VERSION,
    author="Jocile",
    author_email="jocilecam@gmail.com",
    description="Image Processing Package using skimage",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/jocile/image-processing-package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",  # Adicionado classifier
        "Topic :: Image Processing",  # Adicionado classifier
    ],
    install_requires=sanitize_requirements("requirements.txt"),
    python_requires=">=3.5",
)
