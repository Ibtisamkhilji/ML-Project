from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements.
    """
    HYPE_E_DOT = '-e .'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read all lines
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='IbtisamKhilji',
    author_email='ibtisamkhilji@gmail.com',
    packages=find_packages(),  # Call the function
    install_requires=get_requirements('requirements.txt')
)