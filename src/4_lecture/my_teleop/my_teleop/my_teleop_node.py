import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
# from rclpy.exceptions import ExternalShutdownException # 適切なインポートがないためコメントアウト


class MyTeleop(Node):
    def __init__(self):
        super().__init__('my_teleop_node')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        # self.timer = self.create_timer(0.01, self.timer_callback) # タイマーを削除
        self.vel = Twist()
        self.vel.linear.x = 0.0
        self.vel.angular.z = 0.0

    # タイマーではなく、キー入力時に直接呼び出すメソッド
    def process_key(self, key):
        if key == 'f':
            self.vel.linear.x = 2.0
            self.vel.linear.y = 0.0
            self.vel.linear.z = 0.0
            self.vel.angular.x = 0.0
            self.vel.angular.y = 0.0
            self.vel.angular.z = 0.0

        elif key == 'b':
            self.vel.linear.x -= 2.0
        elif key == 'l':
            self.vel.angular.z += 1.0
        elif key == 'r':
            self.vel.angular.z -= 1.0
        elif key == 's':
            self.vel.linear.x = 0.0
            self.vel.angular.z = 0.0
        else:
            print('入力キーが違います．')
            return  # 不正なキーの場合はパブリッシュしない

        self.publisher.publish(self.vel)
        self.get_logger().info(f'並進速度={self.vel.linear.x} 角速度={self.vel.angular.z}')


def main():
    rclpy.init()
    node = MyTeleop()

    print('f:ただ前進, b:後退, l:左回転, r:右回転, s:停止。終了はCtrl+C')

    try:
        # rclpy.spin(node) の代わりに、ループ内でキー入力を待ち続けます
        while rclpy.ok():
            key = input('f, b, r, l, sキー入力後にEnterキーを押下 <<')
            node.process_key(key)
    except KeyboardInterrupt:
        print('Ctrl+Cが押されました．ノードを停止します。')
    # except ExternalShutdownException: # 適切にインポートされていない可能性
    #     sys.exit(1)
    finally:
        # 終了時に速度をゼロにパブリッシュしておくと安全です
        node.vel.linear.x = 0.0
        node.vel.angular.z = 0.0
        node.publisher.publish(node.vel)
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()