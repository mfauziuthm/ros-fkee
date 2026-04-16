from setuptools import find_packages, setup

package_name = 'node_temp_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mfauzi',
    maintainer_email='mfauzi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'temp_sensor = node_temp_py.temp_sensor:main',
            'temp_display = node_temp_py.temp_display:main',     
        ],
    },
)
