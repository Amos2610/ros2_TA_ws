# ===================================
# ROS 2 Humble + Ubuntu 22.04 基本環境
# ====================================
# ベースイメージを指定(Ubuntu 22.04)
FROM ubuntu:22.04

# 環境変数設定
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
ENV ROS_DISTRO=humble

# 基本的なツールのインストール
RUN apt-get update && apt-get install -y curl \
                                        gnupg \
                                        lsb-release \
                                        build-essential \
                                        git
# ROS2の鍵 & リポジトリ追加
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
 | gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" \
 > /etc/apt/sources.list.d/ros2.list

# Navigation2，SLAMに必要なパッケージのインストール
RUN apt update && apt install -y ros-humble-cartographer \
                ros-humble-cartographer-ros \
                ros-humble-navigation2 \
                ros-humble-nav2-bringup \
                ros-humble-xacro

# 必要なROS 2 Humbleのインストール
RUN apt-get update && apt-get install -y \
    ros-humble-desktop \
    python3-rosdep \
    python3-colcon-common-extensions \
    python3-pip \
    # Gazebo Ignitionのインストール
    ros-humble-ros-ign-gazebo \
    ros-humble-ros-ign-bridge \
    ros-humble-ros-gz \
    ignition-fortress \
    && rm -rf /var/lib/apt/lists/*

# ROS 2の初期化
RUN rosdep init && rosdep update

# 起動時に自動でROS 2を読み込む
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# ワークディレクトリを作成
WORKDIR /root/ros2_ws

# デフォルトコマンド
CMD ["bash"]