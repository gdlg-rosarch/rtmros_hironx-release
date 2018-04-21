# Script generated with Bloom
pkgdesc="ROS - ROS-OpenRTM interfacing package for the opensource version of Kawada's Hiro/NEXTAGE dual-arm robot. NOTE: This package is multi-license -- pay attention to file header in each file where license is declared. For Creative Commons nc 4.0 applied, see <a href="http://creativecommons.org/licenses/by-nc/4.0">here</a>. <p>This package also contains some sensor driver software (as of April 2016 they are the following force sensors such as <a href="http://www.wacoh-tech.com/products/dynpick/wdf-6m200-3.html">Dynpick</a> and <a href="http://www.jr3.com/products.html">JR3</a>) for QNX. These drivers are stored in this robot-specific package for not many reasons than they are slightly customized for the robot. So if you can separate those as a standalone, generic package that'll be appreciated (please just let us know if you will).</p>"
url='http://ros.org/wiki/hironx_ros_bridge'

pkgname='ros-kinetic-hironx-ros-bridge'
pkgver='2.1.0_1'
pkgrel=1
arch=('any')
license=('BSD'
'CreativeCommons-by-nc-4.0'
)

makedepends=('gnuplot'
'ros-kinetic-catkin'
'ros-kinetic-control-msgs'
'ros-kinetic-hrpsys-ros-bridge'
'ros-kinetic-mk'
'ros-kinetic-rosbash'
'ros-kinetic-rosbuild'
'ros-kinetic-roslang'
'ros-kinetic-roslib'
'ros-kinetic-roslint'
'unzip'
)

depends=('gnuplot'
'ros-kinetic-control-msgs'
'ros-kinetic-hrpsys-ros-bridge'
'ros-kinetic-moveit-commander'
'ros-kinetic-openni2-launch'
'ros-kinetic-rosbash'
'ros-kinetic-roslang'
'ros-kinetic-roslib'
'ros-kinetic-rospy'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=hironx_ros_bridge
source=()
md5sums=()

prepare() {
    cp -R $startdir/hironx_ros_bridge $srcdir/hironx_ros_bridge
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

