from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement = [req.replace('\n', '') for req in requirement]
        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    
    return requirement



setup(
    name="ML Project",
    version="0.0.1",
    author="Abhay Mittal",
    author_email="abhay-72005@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') 
)