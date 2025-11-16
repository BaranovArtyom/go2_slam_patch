import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2

class PC2Relay(Node):
    def __init__(self):
        super().__init__('pc2_relay')

        self.pc2_sub = self.create_subscription(
            PointCloud2,
            '/robot0/point_cloud2',
            self.callback,
            10
        )

        self.pc2_pub = self.create_publisher(
            PointCloud2,
            '/robot0/point_cloud2_fixed',
            10
        )

        self.get_logger().info("PC2 relay started")

    def callback(self, msg):
        # FIX TIMESTAMP
        msg.header.stamp = self.get_clock().now().to_msg()

        # FIX FRAME
        msg.header.frame_id = "robot0/lidar_link"

        self.pc2_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = PC2Relay()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
