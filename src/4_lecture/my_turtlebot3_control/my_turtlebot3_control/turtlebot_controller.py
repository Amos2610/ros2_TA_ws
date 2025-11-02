#!/usr/bin/env python3
# -*-encoding:UTF-8-*-

"""
File: turtlebot_controller.py
Author: Tomoaki Fujino（Kyushu Institute of Technology, Hibikino-Musashi@Home）
"""

# モジュールのインポート(ROS2関連)
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtlebotController(Node):
    """TurtlebotControllerクラス（Nodeクラスを継承）
    指定された周期でTurtleBot3移動制御メッセージトピックをパブリッシュするROS2ノードクラス

    Attributes:
        publisher (Publisher): メッセージをパブリッシュするための ROS2 パブリッシャ
        timer (Timer): 指定された周期でコールバックメソッドを呼び出すためのタイマ
    """

    def __init__(self):
        """クラスの初期化メソッド"""
        # 継承したNodeクラスのコンストラクタをオーバーライド(引数は，'ノード名')
        super().__init__("turtlebot_controller")

        # パブリッシャの宣言
        self.publisher = self.create_publisher(msg_type=Twist, topic="cmd_vel", qos_profile=10)

        # 割り込み用タイマの定義（指定した周期[s]でコールバックメソッドを呼ぶ）
        self.timer = self.create_timer(timer_period_sec=0.1, callback=self.timer_callback)

    def timer_callback(self):
        """割り込み用タイマのコールバックメソッド"""
        # メッセージの定義
        msg = Twist()
        msg.linear.x = 0.05  # [m/s]   # 並進速度
        msg.angular.z = 0.0  # [rad/s] # 旋回速度

        # ログを表示
        self.get_logger().info(str(msg))

        # メッセージをパブリッシュ
        self.publisher.publish(msg)


def main(args=None):
    """Main関数"""
    # ROS2のPythonクライアントライブラリの初期化
    rclpy.init(args=args)

    # TurtlebotControllerクラスのインスタント生成
    node = TurtlebotController()

    # ノードが終了するまで指定したノードを実行
    rclpy.spin(node)

    # 終了処理
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
