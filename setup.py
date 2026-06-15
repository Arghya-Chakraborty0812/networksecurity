'''
Define the configuration of the project like dependencies, entry points, etc. 
This file is used by pip to install the package and its dependencies.
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    Read the requirements.txt file and return a list of dependencies.
    '''
    requirement_list:List[str] = []
    try: 
        with open('requirements.txt') as file:
            # Read lines from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                # Strip whitespace and ignore empty lines
                requirement = line.strip()
                #ignore empty lines and comments
                if requirement and requirement != '-e.':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_list
print(get_requirements())

setup(
    name="Network Security",
    version="0.0.1",
    author="Arghya Chakraborty",
    author_email="arghya0812@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)