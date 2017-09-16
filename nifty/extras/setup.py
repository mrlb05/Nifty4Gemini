from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='nifty-gemini',
      version='0.1.3',
      description='Gemini NIFS data reduction pipeline.',
      long_description=readme(),
      url='https://github.com/Nat1405/newer-nifty',
      author='Nat Comeau',
      author_email='ncomeau@gemini.edu',
      license='MIT',
      packages=['Nifty'],
      scripts=[
            'Nifty/Nifty.py',
            'Nifty/nifsSort.py',
            'Nifty/nifsBaselineCalibration.py',
            'Nifty/nifsReduce.py',
            'Nifty/nifsMerge.py',
            'Nifty/nifsUtils.py'
      ],
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
