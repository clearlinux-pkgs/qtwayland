#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtwayland
Version  : 5.13.1
Release  : 18
URL      : http://download.qt.io/official_releases/qt/5.13/5.13.1/submodules/qtwayland-everywhere-src-5.13.1.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.13/5.13.1/submodules/qtwayland-everywhere-src-5.13.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtwayland-lib = %{version}-%{release}
Requires: qtwayland-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : fontconfig-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : qtbase-staticdev

%description
This is the QtWayland module.
The QtWayland module consists of two parts:
Wayland platform plugin:
Enables Qt applications to be run as Wayland clients.

%package dev
Summary: dev components for the qtwayland package.
Group: Development
Requires: qtwayland-lib = %{version}-%{release}
Provides: qtwayland-devel = %{version}-%{release}
Requires: qtwayland = %{version}-%{release}

%description dev
dev components for the qtwayland package.


%package lib
Summary: lib components for the qtwayland package.
Group: Libraries
Requires: qtwayland-license = %{version}-%{release}

%description lib
lib components for the qtwayland package.


%package license
Summary: license components for the qtwayland package.
Group: Default

%description license
license components for the qtwayland package.


%prep
%setup -q -n qtwayland-everywhere-src-5.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1568396609
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtwayland
cp LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtwayland/LICENSE.FDL
cp LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtwayland/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtwayland/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtwayland/LICENSE.GPL3-EXCEPT
cp LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtwayland/LICENSE.LGPL3
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/bin/qtwaylandscanner
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qtwaylandclient-config_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qtwaylandclientglobal_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwayland-hardware-integration.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwayland-qt-key-unstable-v1.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwayland-qt-windowmanager.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwayland-server-buffer-extension.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwayland-surface-extension.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwayland-text-input-unstable-v2.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwayland-touch-extension.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwayland-wayland.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwayland-xdg-output-unstable-v1.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandabstractdecoration_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandbuffer_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandclientbufferintegration_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandclientbufferintegrationfactory_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandclientbufferintegrationplugin_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandclientextension_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandclipboard_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandcursor_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylanddatadevice_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylanddatadevicemanager_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylanddataoffer_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylanddatasource_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylanddecorationfactory_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylanddecorationplugin_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylanddisplay_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylanddnd_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandextendedsurface_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandhardwareintegration_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandinputcontext_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandinputdevice_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandinputdeviceintegration_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandinputdeviceintegrationfactory_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandinputdeviceintegrationplugin_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandintegration_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandnativeinterface_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandqtkey_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandscreen_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandserverbufferintegration_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandserverbufferintegrationfactory_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandserverbufferintegrationplugin_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandshellintegration_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandshellintegrationfactory_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandshellintegrationplugin_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandshellsurface_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandshm_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandshmbackingstore_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandshmwindow_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandsubsurface_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandtouch_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandwindow_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/qwaylandwindowmanagerintegration_p.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/wayland-hardware-integration-client-protocol.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/wayland-qt-key-unstable-v1-client-protocol.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/wayland-qt-windowmanager-client-protocol.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/wayland-server-buffer-extension-client-protocol.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/wayland-surface-extension-client-protocol.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/wayland-text-input-unstable-v2-client-protocol.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/wayland-touch-extension-client-protocol.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/wayland-wayland-client-protocol.h
/usr/include/qt5/QtWaylandClient/5.13.1/QtWaylandClient/private/wayland-xdg-output-unstable-v1-client-protocol.h
/usr/include/qt5/QtWaylandClient/QWaylandClientExtension
/usr/include/qt5/QtWaylandClient/QWaylandClientExtensionTemplate
/usr/include/qt5/QtWaylandClient/QtWaylandClient
/usr/include/qt5/QtWaylandClient/QtWaylandClientDepends
/usr/include/qt5/QtWaylandClient/QtWaylandClientVersion
/usr/include/qt5/QtWaylandClient/qtwaylandclient-config.h
/usr/include/qt5/QtWaylandClient/qtwaylandclientglobal.h
/usr/include/qt5/QtWaylandClient/qtwaylandclientversion.h
/usr/include/qt5/QtWaylandClient/qwaylandclientexport.h
/usr/include/qt5/QtWaylandClient/qwaylandclientextension.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qtwaylandcompositor-config_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-hardware-integration.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-ivi-application.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-qt-key-unstable-v1.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-qt-windowmanager.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-scaler.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-server-buffer-extension.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-text-input-unstable-v2.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-touch-extension.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-viewporter.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-wayland.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-xdg-decoration-unstable-v1.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-xdg-shell-unstable-v5_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-xdg-shell-unstable-v6.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwayland-server-xdg-shell.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandcompositor_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandcompositorextension_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylanddestroylistener_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandinputmethodcontrol_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandiviapplication_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandivisurface_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandivisurfaceintegration_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandkeyboard_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandkeymap_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandoutput_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandoutputmode_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandpointer_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandqtwindowmanager_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandquickhardwarelayer_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandquickitem_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandquickshellsurfaceitem_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandseat_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandshell_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandsurface_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandtextinput_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandtextinputmanager_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandtouch_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandutils_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandview_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandviewporter_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandwlscaler_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandwlshell_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandwlshellintegration_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandxdgdecorationv1_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandxdgshell_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandxdgshellv5_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandxdgshellv5integration_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandxdgshellv6_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwaylandxdgshellv6integration_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlbuffermanager_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlclientbuffer_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlclientbufferintegration_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlclientbufferintegrationfactory_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlclientbufferintegrationplugin_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwldatadevice_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwldatadevicemanager_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwldataoffer_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwldatasource_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlhardwarelayerintegration_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlhardwarelayerintegrationfactory_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlhardwarelayerintegrationplugin_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlhwintegration_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlqtkey_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlqttouch_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlregion_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlserverbufferintegration_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlserverbufferintegrationfactory_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/qwlserverbufferintegrationplugin_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-hardware-integration-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-ivi-application-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-qt-key-unstable-v1-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-qt-windowmanager-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-scaler-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-server-buffer-extension-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-text-input-unstable-v2-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-touch-extension-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-viewporter-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-wayland-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-xdg-decoration-unstable-v1-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-xdg-shell-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-xdg-shell-unstable-v5-server-protocol_p.h
/usr/include/qt5/QtWaylandCompositor/5.13.1/QtWaylandCompositor/private/wayland-xdg-shell-unstable-v6-server-protocol.h
/usr/include/qt5/QtWaylandCompositor/QWaylandBufferRef
/usr/include/qt5/QtWaylandCompositor/QWaylandClient
/usr/include/qt5/QtWaylandCompositor/QWaylandCompositor
/usr/include/qt5/QtWaylandCompositor/QWaylandCompositorExtension
/usr/include/qt5/QtWaylandCompositor/QWaylandCompositorExtensionTemplate
/usr/include/qt5/QtWaylandCompositor/QWaylandDestroyListener
/usr/include/qt5/QtWaylandCompositor/QWaylandDrag
/usr/include/qt5/QtWaylandCompositor/QWaylandInputMethodControl
/usr/include/qt5/QtWaylandCompositor/QWaylandIviApplication
/usr/include/qt5/QtWaylandCompositor/QWaylandIviSurface
/usr/include/qt5/QtWaylandCompositor/QWaylandKeyboard
/usr/include/qt5/QtWaylandCompositor/QWaylandKeymap
/usr/include/qt5/QtWaylandCompositor/QWaylandObject
/usr/include/qt5/QtWaylandCompositor/QWaylandOutput
/usr/include/qt5/QtWaylandCompositor/QWaylandOutputMode
/usr/include/qt5/QtWaylandCompositor/QWaylandPointer
/usr/include/qt5/QtWaylandCompositor/QWaylandQtWindowManager
/usr/include/qt5/QtWaylandCompositor/QWaylandQuickCompositor
/usr/include/qt5/QtWaylandCompositor/QWaylandQuickExtension
/usr/include/qt5/QtWaylandCompositor/QWaylandQuickItem
/usr/include/qt5/QtWaylandCompositor/QWaylandQuickOutput
/usr/include/qt5/QtWaylandCompositor/QWaylandQuickShellSurfaceItem
/usr/include/qt5/QtWaylandCompositor/QWaylandQuickSurface
/usr/include/qt5/QtWaylandCompositor/QWaylandResource
/usr/include/qt5/QtWaylandCompositor/QWaylandSeat
/usr/include/qt5/QtWaylandCompositor/QWaylandShell
/usr/include/qt5/QtWaylandCompositor/QWaylandShellSurface
/usr/include/qt5/QtWaylandCompositor/QWaylandShellSurfaceTemplate
/usr/include/qt5/QtWaylandCompositor/QWaylandShellTemplate
/usr/include/qt5/QtWaylandCompositor/QWaylandSurface
/usr/include/qt5/QtWaylandCompositor/QWaylandSurfaceGrabber
/usr/include/qt5/QtWaylandCompositor/QWaylandSurfaceRole
/usr/include/qt5/QtWaylandCompositor/QWaylandTextInput
/usr/include/qt5/QtWaylandCompositor/QWaylandTextInputManager
/usr/include/qt5/QtWaylandCompositor/QWaylandTouch
/usr/include/qt5/QtWaylandCompositor/QWaylandView
/usr/include/qt5/QtWaylandCompositor/QWaylandViewporter
/usr/include/qt5/QtWaylandCompositor/QWaylandWlScaler
/usr/include/qt5/QtWaylandCompositor/QWaylandWlShell
/usr/include/qt5/QtWaylandCompositor/QWaylandWlShellSurface
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgDecorationManagerV1
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgPopup
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgPopupV5
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgPopupV6
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgShell
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgShellV5
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgShellV6
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgSurface
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgSurfaceV5
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgSurfaceV6
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgToplevel
/usr/include/qt5/QtWaylandCompositor/QWaylandXdgToplevelV6
/usr/include/qt5/QtWaylandCompositor/QtWaylandCompositor
/usr/include/qt5/QtWaylandCompositor/QtWaylandCompositorDepends
/usr/include/qt5/QtWaylandCompositor/QtWaylandCompositorVersion
/usr/include/qt5/QtWaylandCompositor/qtwaylandcompositor-config.h
/usr/include/qt5/QtWaylandCompositor/qtwaylandcompositorglobal.h
/usr/include/qt5/QtWaylandCompositor/qtwaylandcompositorversion.h
/usr/include/qt5/QtWaylandCompositor/qwaylandbufferref.h
/usr/include/qt5/QtWaylandCompositor/qwaylandclient.h
/usr/include/qt5/QtWaylandCompositor/qwaylandcompositor.h
/usr/include/qt5/QtWaylandCompositor/qwaylandcompositorextension.h
/usr/include/qt5/QtWaylandCompositor/qwaylanddestroylistener.h
/usr/include/qt5/QtWaylandCompositor/qwaylanddrag.h
/usr/include/qt5/QtWaylandCompositor/qwaylandexport.h
/usr/include/qt5/QtWaylandCompositor/qwaylandinputmethodcontrol.h
/usr/include/qt5/QtWaylandCompositor/qwaylandiviapplication.h
/usr/include/qt5/QtWaylandCompositor/qwaylandivisurface.h
/usr/include/qt5/QtWaylandCompositor/qwaylandkeyboard.h
/usr/include/qt5/QtWaylandCompositor/qwaylandkeymap.h
/usr/include/qt5/QtWaylandCompositor/qwaylandoutput.h
/usr/include/qt5/QtWaylandCompositor/qwaylandoutputmode.h
/usr/include/qt5/QtWaylandCompositor/qwaylandpointer.h
/usr/include/qt5/QtWaylandCompositor/qwaylandqtwindowmanager.h
/usr/include/qt5/QtWaylandCompositor/qwaylandquickchildren.h
/usr/include/qt5/QtWaylandCompositor/qwaylandquickcompositor.h
/usr/include/qt5/QtWaylandCompositor/qwaylandquickextension.h
/usr/include/qt5/QtWaylandCompositor/qwaylandquickitem.h
/usr/include/qt5/QtWaylandCompositor/qwaylandquickoutput.h
/usr/include/qt5/QtWaylandCompositor/qwaylandquickshellsurfaceitem.h
/usr/include/qt5/QtWaylandCompositor/qwaylandquicksurface.h
/usr/include/qt5/QtWaylandCompositor/qwaylandresource.h
/usr/include/qt5/QtWaylandCompositor/qwaylandseat.h
/usr/include/qt5/QtWaylandCompositor/qwaylandshell.h
/usr/include/qt5/QtWaylandCompositor/qwaylandshellsurface.h
/usr/include/qt5/QtWaylandCompositor/qwaylandsurface.h
/usr/include/qt5/QtWaylandCompositor/qwaylandsurfacegrabber.h
/usr/include/qt5/QtWaylandCompositor/qwaylandtextinput.h
/usr/include/qt5/QtWaylandCompositor/qwaylandtextinputmanager.h
/usr/include/qt5/QtWaylandCompositor/qwaylandtouch.h
/usr/include/qt5/QtWaylandCompositor/qwaylandview.h
/usr/include/qt5/QtWaylandCompositor/qwaylandviewporter.h
/usr/include/qt5/QtWaylandCompositor/qwaylandwlscaler.h
/usr/include/qt5/QtWaylandCompositor/qwaylandwlshell.h
/usr/include/qt5/QtWaylandCompositor/qwaylandxdgdecorationv1.h
/usr/include/qt5/QtWaylandCompositor/qwaylandxdgshell.h
/usr/include/qt5/QtWaylandCompositor/qwaylandxdgshellv5.h
/usr/include/qt5/QtWaylandCompositor/qwaylandxdgshellv6.h
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QWaylandEglPlatformIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QWaylandIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QWaylandXCompositeEglPlatformIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QWaylandXCompositeGlxPlatformIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClientConfig.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClientConfigVersion.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_DmaBufServerBufferPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_DrmEglServerBufferPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_QWaylandBradientDecorationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_QWaylandEglClientBufferPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_QWaylandFullScreenShellV1IntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_QWaylandIviShellIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_QWaylandWlShellIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_QWaylandXCompositeEglClientBufferPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_QWaylandXCompositeGlxClientBufferPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_QWaylandXdgShellIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_QWaylandXdgShellV5IntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_QWaylandXdgShellV6IntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandClient/Qt5WaylandClient_ShmServerBufferPlugin.cmake
/usr/lib64/cmake/Qt5WaylandCompositor/Qt5WaylandCompositorConfig.cmake
/usr/lib64/cmake/Qt5WaylandCompositor/Qt5WaylandCompositorConfigVersion.cmake
/usr/lib64/cmake/Qt5WaylandCompositor/Qt5WaylandCompositor_DmaBufServerBufferIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandCompositor/Qt5WaylandCompositor_DrmEglServerBufferIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandCompositor/Qt5WaylandCompositor_QWaylandDmabufClientBufferIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandCompositor/Qt5WaylandCompositor_QWaylandEglClientBufferIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandCompositor/Qt5WaylandCompositor_QWaylandEglStreamBufferIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandCompositor/Qt5WaylandCompositor_QWaylandXCompositeEglClientBufferIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandCompositor/Qt5WaylandCompositor_QWaylandXCompositeGlxClientBufferIntegrationPlugin.cmake
/usr/lib64/cmake/Qt5WaylandCompositor/Qt5WaylandCompositor_ShmServerBufferIntegrationPlugin.cmake
/usr/lib64/libQt5WaylandClient.prl
/usr/lib64/libQt5WaylandClient.so
/usr/lib64/libQt5WaylandCompositor.prl
/usr/lib64/libQt5WaylandCompositor.so
/usr/lib64/pkgconfig/Qt5WaylandClient.pc
/usr/lib64/pkgconfig/Qt5WaylandCompositor.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_waylandclient.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_waylandclient_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_waylandcompositor.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_waylandcompositor_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5WaylandClient.so.5
/usr/lib64/libQt5WaylandClient.so.5.13
/usr/lib64/libQt5WaylandClient.so.5.13.1
/usr/lib64/libQt5WaylandCompositor.so.5
/usr/lib64/libQt5WaylandCompositor.so.5.13
/usr/lib64/libQt5WaylandCompositor.so.5.13.1
/usr/lib64/qt5/plugins/platforms/libqwayland-egl.so
/usr/lib64/qt5/plugins/platforms/libqwayland-generic.so
/usr/lib64/qt5/plugins/platforms/libqwayland-xcomposite-egl.so
/usr/lib64/qt5/plugins/platforms/libqwayland-xcomposite-glx.so
/usr/lib64/qt5/plugins/wayland-decoration-client/libbradient.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-client/libdmabuf-server.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-client/libdrm-egl-server.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-client/libqt-plugin-wayland-egl.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-client/libshm-emulation-server.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-client/libxcomposite-egl.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-client/libxcomposite-glx.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-server/libdmabuf-server.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-server/libdrm-egl-server.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-server/liblinux-dmabuf-unstable-v1.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-server/libqt-plugin-wayland-egl.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-server/libshm-emulation-server.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-server/libwayland-eglstream-controller.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-server/libxcomposite-egl.so
/usr/lib64/qt5/plugins/wayland-graphics-integration-server/libxcomposite-glx.so
/usr/lib64/qt5/plugins/wayland-shell-integration/libfullscreen-shell-v1.so
/usr/lib64/qt5/plugins/wayland-shell-integration/libivi-shell.so
/usr/lib64/qt5/plugins/wayland-shell-integration/libwl-shell.so
/usr/lib64/qt5/plugins/wayland-shell-integration/libxdg-shell-v5.so
/usr/lib64/qt5/plugins/wayland-shell-integration/libxdg-shell-v6.so
/usr/lib64/qt5/plugins/wayland-shell-integration/libxdg-shell.so
/usr/lib64/qt5/qml/QtWayland/Compositor/libqwaylandcompositorplugin.so
/usr/lib64/qt5/qml/QtWayland/Compositor/plugins.qmltypes
/usr/lib64/qt5/qml/QtWayland/Compositor/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtwayland/LICENSE.FDL
/usr/share/package-licenses/qtwayland/LICENSE.GPL2
/usr/share/package-licenses/qtwayland/LICENSE.GPL3
/usr/share/package-licenses/qtwayland/LICENSE.GPL3-EXCEPT
/usr/share/package-licenses/qtwayland/LICENSE.LGPL3
