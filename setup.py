# find_packages finds all the packages inside the machine learning project directory that we have created
from setuptools import find_packages , setup 
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]: # takes 'file_path' input as str , and also outputs ->List[str] (outputs a list with str values)
    '''this function will return a list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # to mitigate the issue of '\n' , replace it with a blank 
        requirements = [req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) # So that '-e .' is not read while building 
    return requirements

# Details about the project (can be considered as the metadata information about the entire project)
setup(
    name = 'mlproject', 
    version = '0.0.1', # as we keep updating the program , the version will need to be updated
    author='Ritwik', 
    author_email='ritwik1080@gmail.com', 
    packages=find_packages(), # check and see in which folders you have the __init__.py file , thus considering the respective folder as a package and then it will try to build it 
    # after which you can try and import this anywhere you want (eg. importing seaborn , pandas etc )
    # install_requires = ['pandas','numpy','seaborn'] # carry out the installation of the libraries specified 
    install_requires = get_requirements('requirements.txt')
)   