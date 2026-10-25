from setuptools import setup, find_packages

setup(name='LumOpt',
      version='0.0.1',
      description='Continuous Adjoint Optimization wrapper for electromagnetic solvers',
      author='Christopher Lalau-Keraly',
      author_email='chriskeraly@gmail.com',
      install_requires=[
            'numpy',
            'scipy',
            'matplotlib'
      ],
      packages=find_packages(include=["lumopt", "lumopt.*"]),
      )
