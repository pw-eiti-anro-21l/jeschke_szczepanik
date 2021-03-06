import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'lab4'

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
            'jint_srv = lab4.jint_control_srv:main',
            'jint_cli = lab4.jint:main',
            'oint_srv = lab4.oint_control_srv:main',
            'oint_cli = lab4.oint:main'
        ],
    },
)
