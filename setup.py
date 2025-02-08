from setuptools import setup, find_packages

def get_requirements() -> list[str]:
    # this function will return list of requirements
    requirement_list: list[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and '-e .'
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirements file not found")

    return requirement_list

setup(
    name="Network Security",
    version="0.1",
    author="Ayrax",
    packages=find_packages(),
    install_requires=get_requirements(),
)
