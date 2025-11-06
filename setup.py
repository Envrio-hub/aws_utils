from setuptools import setup, find_packages

setup(
    name='aws_utils',
    version='1.1.0',
    description='A library that provides utilities to manage AWS Secrets Manager and Key Management Service',
    author='Ioannis Tsakmakis, Nikolaos Kokkos',
    author_email='itsakmak@envrio.org, nkokkos@envrio.org',
    packages=find_packages(),
    python_requires='>=3.12',
    install_requires=[ 
        'boto3>=1.36.7',
        'envrio_logger @ git+ssh://git@github.com/Envrio-hub/envrio_logger.git@0.1.2'
    ],
    classifiers=[  
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.12',
        'Framework :: Flask',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
