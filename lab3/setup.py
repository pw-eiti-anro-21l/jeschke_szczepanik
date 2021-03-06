import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'lab3'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
        (os.path.join('share', package_name), glob('robot/*')),
        (os.path.join('share', package_name), glob('config/*')),
        (os.path.join('share', package_name), glob('meshes/*'))
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kamil',
    maintainer_email='kamil.szczepanik00@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'kdl = lab3.kdl:main',
            'non_kdl = lab3.non_kdl:main',
            'xyz_pry = lab3.xyz_rpy:main'
        ],
    },
)
