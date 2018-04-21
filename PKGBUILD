# Script generated with Bloom
pkgdesc="ROS - The rtmros_hironx package is an operating interface via ROS and OpenRTM, for Hiro and <a href="http://nextage.kawada.jp/en/">NEXTAGE OPEN</a> dual-armed robots from Kawada Industries Inc. <br/><br/> NOTE for Hiro users: Utilizing this opensource controller for Hiro requires installation both on Controller Box (QNX-based) and Vision PC (Ubuntu Linux), and the steps for it are not shared publicly in order to avoid any possible inconvenience that can easily be caused by slight mis-operation during installation. Please contact <a href="http://opensource-robotics.tokyo.jp/?page_id=56&amp;lang=en">TORK</a> for an advice."
url='http://ros.org/wiki/rtmros_hironx/'

pkgname='ros-kinetic-rtmros-hironx'
pkgver='2.1.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-hironx-calibration'
'ros-kinetic-hironx-moveit-config'
'ros-kinetic-hironx-ros-bridge'
)

conflicts=()
replaces=()

_dir=rtmros_hironx
source=()
md5sums=()

prepare() {
    cp -R $startdir/rtmros_hironx $srcdir/rtmros_hironx
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

