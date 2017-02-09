Name:           ros-indigo-hironx-ros-bridge
Version:        1.1.20
Release:        0%{?dist}
Summary:        ROS hironx_ros_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hironx_ros_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       gnuplot
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-hrpsys-ros-bridge
Requires:       ros-indigo-moveit-commander
Requires:       ros-indigo-openni2-launch
Requires:       ros-indigo-pr2-controllers-msgs
Requires:       ros-indigo-rosbash
Requires:       ros-indigo-roslang
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
Requires:       ros-indigo-tf
BuildRequires:  gnuplot
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-hrpsys-ros-bridge
BuildRequires:  ros-indigo-mk
BuildRequires:  ros-indigo-pr2-controllers-msgs
BuildRequires:  ros-indigo-rosbash
BuildRequires:  ros-indigo-rosbuild
BuildRequires:  ros-indigo-roslang
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-roslint
BuildRequires:  unzip

%description
ROS-OpenRTM interfacing package for the opensource version of Kawada's
Hiro/NEXTAGE dual-arm robot. NOTE: This package is multi-license -- pay
attention to file header in each file where license is declared. For Creative
Commons nc 4.0 applied, see here. This package also contains some sensor driver
software (as of April 2016 they are the following force sensors such as Dynpick
and JR3) for QNX. These drivers are stored in this robot-specific package for
not many reasons than they are slightly customized for the robot. So if you can
separate those as a standalone, generic package that'll be appreciated (please
just let us know if you will).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Feb 09 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.20-0
- Autogenerated by Bloom

* Thu Jan 12 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.19-0
- Autogenerated by Bloom

* Fri Oct 28 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.18-0
- Autogenerated by Bloom

* Thu Oct 13 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.17-0
- Autogenerated by Bloom

* Mon Jul 11 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.16-0
- Autogenerated by Bloom

* Thu Jun 02 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.15-0
- Autogenerated by Bloom

* Thu May 19 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.14-0
- Autogenerated by Bloom

* Mon May 16 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.13-1
- Autogenerated by Bloom

* Mon May 16 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.13-0
- Autogenerated by Bloom

* Thu May 05 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.12-0
- Autogenerated by Bloom

* Thu Feb 18 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.11-0
- Autogenerated by Bloom

* Fri Feb 12 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.10-0
- Autogenerated by Bloom

* Fri Feb 05 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.7-0
- Autogenerated by Bloom

* Wed Feb 03 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.6-0
- Autogenerated by Bloom

* Tue Jan 26 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.5-0
- Autogenerated by Bloom

* Mon Jan 25 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.4-0
- Autogenerated by Bloom

* Wed Dec 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.3-0
- Autogenerated by Bloom

* Wed Nov 11 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.2-0
- Autogenerated by Bloom

* Mon Nov 02 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.1-0
- Autogenerated by Bloom

* Wed Oct 21 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-0
- Autogenerated by Bloom

* Fri Sep 11 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.37-0
- Autogenerated by Bloom

* Mon Aug 24 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.36-0
- Autogenerated by Bloom

* Fri Aug 14 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.35-0
- Autogenerated by Bloom

* Tue Aug 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.34-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.33-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.32-0
- Autogenerated by Bloom

* Sun May 31 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.31-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.30-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.29-0
- Autogenerated by Bloom

* Fri Feb 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.28-0
- Autogenerated by Bloom

