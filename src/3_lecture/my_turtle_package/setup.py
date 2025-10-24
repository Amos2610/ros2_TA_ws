from setuptools import setup

package_name = 'my_turtle_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@domain.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
    data_files=[
        ('share/' + package_name + '/launch', ['launch/myTurtlesim.launch.py']),
        ('share/' + package_name, ['package.xml']),  # package.xmlを追加
    ],
)
