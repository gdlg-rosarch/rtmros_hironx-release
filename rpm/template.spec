Name:           ros-hydro-rtmros-hironx
Version:        1.0.34
Release:        0%{?dist}
Summary:        ROS rtmros_hironx package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rtmros_hironx/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-hironx-calibration
Requires:       ros-hydro-hironx-moveit-config
Requires:       ros-hydro-hironx-ros-bridge
BuildRequires:  ros-hydro-catkin

%description
The rtmros_hironx package is an operating interface via ROS and OpenRTM, for
Hiro and NEXTAGE OPEN dual-armed robots from Kawada Industries Inc. NOTE for
Hiro users: Utilizing this opensource controller for Hiro requires installation
both on Controller Box (QNX-based) and Vision PC (Ubuntu Linux), and the steps
for it are not shared publicly in order to avoid any possible inconvenience that
can easily be caused by slight mis-operation during installation. Please contact
TORK for an advice.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Aug 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.34-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.33-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.32-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.31-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.30-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.29-0
- Autogenerated by Bloom

* Fri Feb 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.28-0
- Autogenerated by Bloom

* Tue Nov 04 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.27-0
- Autogenerated by Bloom

* Tue Oct 07 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.26-0
- Autogenerated by Bloom

* Fri Oct 03 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.25-0
- Autogenerated by Bloom

* Tue Sep 16 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.24-0
- Autogenerated by Bloom

* Tue Sep 02 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.23-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.22-0
- Autogenerated by Bloom

* Mon Aug 11 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.21-0
- Autogenerated by Bloom

* Thu Jul 31 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.20-0
- Autogenerated by Bloom

* Tue Jul 29 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.19-1
- Autogenerated by Bloom

* Mon Jul 28 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.19-0
- Autogenerated by Bloom

