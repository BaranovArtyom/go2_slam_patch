from setuptools import setup
import os
from glob import glob

package_name = 'go2_slam_patch'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # ← ДОБАВИТЬ ЭТО
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arty',
    maintainer_email='artem.brnv@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
	    'lidar_tf_broadcaster = go2_slam_patch.lidar_tf_broadcaster:main',
            'pc2_relay = go2_slam_patch.pc2_relay:main',
        ],
    },
)
