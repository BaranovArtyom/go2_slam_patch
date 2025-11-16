import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
import tf2_ros
from rclpy.time import Time

class LidarTFBroadcaster(Node):
    def __init__(self):
        super().__init__('lidar_tf_broadcaster')
        self.br = tf2_ros.TransformBroadcaster(self)
        self.timer = self.create_timer(0.05, self.broadcast)

    def broadcast(self):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'robot0/base_link'
        t.child_frame_id = 'robot0/lidar_link'

        # No offset
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.br.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = LidarTFBroadcaster()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
