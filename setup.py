from setuptools import setup

setup(
    name='quiver-quant',
    version='0.1.0',    
    description='A package for the Quiver Quantitative alternative data API',
    url='https://github.com/Quiver-Quantitative/python-api',
    author='Christopher Kardatzke',
    author_email='chris@quiverquant.com',
    py_modules=["quiver"],
    install_requires=['pandas',
                      'numpy',                     
                      ],

    classifiers=[       
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)