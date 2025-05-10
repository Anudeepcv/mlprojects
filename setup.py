from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def getrequirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
           requirements.remove(HYPEN_E_DOT)
    
    return requirements
        
setup(
    name='mlproject',
    version='0.0.1',
    author='Anudeep',
    author_email='anudeepcv2001@gmail.com',
    packages=find_packages(),
    install_requires=getrequirements('requirements.txt')
)