%define		package	wpmu
%define		plugin	new-blog-defaults
Summary:	WordPressMU plugin to set the defaults for all new blogs created on server
Name:		wpmu-plugin-%{plugin}
Version:	1.5.2
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://downloads.wordpress.org/plugin/wpmu-new-blog-defaults.zip
# Source0-md5:	180a282b1baaec33b68b3bcab842ea71
URL:		http://wordpress.org/extend/plugins/wpmu-new-blog-defaults/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
Requires:	wpmu >= 2.9.1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wp_root		%{_datadir}/wpmu
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/mu-plugins
%define		_sysconfdir	/etc/webapps/wpmu

%description
This plugin does the following:

Adds a new submenu to the site admin screen called "New Blog
Defaults".

Allows the site administrator to visual set defaults for each of the
major blog sections:
- General Settings
- Writing Settings
- Reading Settings
- Discussion Settings
- Privacty Settings
- Permalinks
- Miscellaneous Settings
- Theme
- Bonus Settings

%prep
%setup -qn wpmu-%{plugin}
%undos readme.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{wp_content},%{pluginsdir},%{_sysconfdir}}
cp -a cets_blog_defaults.php $RPM_BUILD_ROOT%{pluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{pluginsdir}/*.php
