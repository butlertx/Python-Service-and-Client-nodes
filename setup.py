from setuptools import setup

package_name = 'py_srvcli'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='terran',
    maintainer_email='terran@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'service = py_srvcli.add_two_ints_server:main',
                             'client = py_srvcli.add_two_ints_client:main',
        ],
    },
)
