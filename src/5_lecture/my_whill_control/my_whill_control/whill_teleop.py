import rclpy
# import roslib; roslib.load_manifest('teleop_twist_keyboard')
import sys, select, termios, tty
from rclpy.node import Node
from geometry_msgs.msg import Twist

# Nodeクラスを継承
class WhillTeleop(Node):
    def __init__(self):
        # Node.__init__を引数node_nameにwhill_teleopを渡して継承
        super().__init__("whill_teleop")
        self.count = 0

        # Node.create_publisher(msg_type, topic)に引数を渡してpublisherを作成
        self.pub = self.create_publisher(Twist, "/whill/controller/cmd_vel",10)
        self.time_period = 1.0

        # Node.create_timer(timer_period_sec, callback)に引数を渡してタイマーを作成
        self.tmr = self.create_timer(self.time_period, self.callback)

        self.get_logger().info("Teleop started: w/x 前後, a/d 回転, s 停止, q 終了")

    def callback(self):
        self.count += 1

        # std_msgs.msg.Stringのインスタンス化
        msg = Twist()
        
        # keyを格納
        key = getKey()
        
        # msgにデータを格納
        if key == "w":
            msg.linear.x = 1.0
        elif key == "x":
            msg.linear.x = -1.0
        elif key == "a":
            msg.angular.z = 1.0
        elif key == "d":
            msg.angular.z = -1.0
        elif key == "s":
            msg.linear.x = 0.0
        elif key == "1":
            msg.angular.z = 3.14
        elif key == "q":
            # Nodeを破壊
            node.destroy_node()
            # RCLを終了
            rclpy.shutdown()

        # Node.get_logger().info(message)で表示したい内容を引数messageに渡す
        self.get_logger().info("Publishing: {0}".format(msg))

        # msgを公開
        self.pub.publish(msg)

def getKey():
    # 標準入力をrawモードに設定
    settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin.fileno())
    try:
        # 入力を監視してキーを読み取る
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
    finally:
        # 終了後に設定を戻す
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main():
    # rclpy.init()でRCLを初期化
    rclpy.init()

    # Nodeのインスタンス化
    node = WhillTeleop()

    try:
        # Node処理をループさせ実行
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Keyboard interrupt received. Exiting...")
    finally:
        # Nodeを破壊
        node.destroy_node()
        # RCLを終了
        rclpy.shutdown()



if __name__ == "__main__":
    main()
