from setuptools import find_packages,setup



setup(
    name='mlproject',
    version='0.0.1',
    author="Richard Lee",
    author_email='richardleelovestoprogram@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')

)