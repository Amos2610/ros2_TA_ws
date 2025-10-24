import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        launch.actions.LogInfo(
            msg="Launch turtlesim node and turtle_teleop_key node."),
       
        launch.actions.TimerAction(
            period=3.0,  # 3秒待ってから次のアクションを実行
            actions=[
                launch.actions.LogInfo( 
                    msg="It's been three seconds since launch."
                ),
  
                Node(
                    package='turtlesim',  # パッケージ名
                    executable='turtlesim_node',  # ノードを起動する名前
                    name='turtlesim',  # ノード名
                    output='screen',  # 出力をターミナルに表示
                    parameters=[  # パラメータの設定
                        {
                            'background_r': 255,
                            'background_g': 255,
                            'background_b': 0
                        }
                    ]
                ),
                Node(
                    package='turtlesim',  # 正しいパッケージ名
                    executable='turtle_teleop_key',  # ノードを起動する名前
                    name='teleop',  # ノード名
                    output='screen',  # 出力をターミナルに表示
                    prefix="xterm -e"  # xtermで実行
                )
            ]
        )
    ])
