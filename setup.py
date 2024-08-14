from setuptools import setup
from setuptools import find_packages


setup(
    name='httpFetch',
    version='0.1.0',    
    description='A reusable module to consistently fetch HTTP content',
    url='https://github.com/raymondcg/httpFetcher',
    author='Raymond Gillett',
    author_email='raymondcgillett@protonmail.com',
    license='Apache 2.0',
    packages=find_packages(exclude=['test']),
    install_requires=['beautifulsoup4','requests' ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License v2.0',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
