from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        # 1. Dynamic TF base_link → lidar_link
        Node(
            package='go2_slam_patch',
            executable='lidar_tf_broadcaster',
            name='lidar_tf_broadcaster',
            output='screen'
        ),

        # 2. PointCloud2 relay
        Node(
            package='go2_slam_patch',
            executable='pc2_relay',
            name='pc2_relay',
            output='screen'
        ),

        # 3. pointcloud → laserscan
        Node(
            package='pointcloud_to_laserscan',
            executable='pointcloud_to_laserscan_node',
            name='pc2laser',
            output='screen',
            remappings=[
                ('/cloud_in', '/robot0/point_cloud2_fixed'),
                ('/scan', '/scan')
            ],
            parameters=[
                {"target_frame": "robot0/lidar_link"},
                {"min_height": -0.5},
                {"max_height": 0.5}
            ]
        ),

        # 4. SLAM Toolbox
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{
                "use_sim_time": True,
                "base_frame": "robot0/base_link",
                "odom_frame": "odom",
                "map_frame": "map"
            }],
            remappings=[
                ('/scan', '/scan')
            ]
        )
    ])
