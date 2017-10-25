# spec file for package sca-patterns-sle15
#
# Copyright (C) 2017 SUSE LLC
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Source developed at:
#  https://github.com/g23guy/sca-patterns-sle15
#
# norootforbuild
# neededforbuild

%define sca_common sca
%define patdirbase /usr/lib/%{sca_common}
%define patdir %{patdirbase}/patterns
%define patuser root
%define patgrp root
%define mode 544
%define category SLE

Name:         sca-patterns-sle15
Summary:      Supportconfig Analysis Patterns for SLE15
URL:          https://github.com/g23guy/sca-patterns-sle15
Group:        System/Monitoring
License:      GPL-2.0
Autoreqprov:  on
Version:      1.0
Release:      1
Source:       %{name}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}
Buildarch:    noarch
BuildRequires: fdupes
Requires:     sca-patterns-base
%description
Supportconfig Analysis (SCA) appliance patterns to identify known
issues relating to all versions of SLES 15

Authors:
--------
    Jason Record <jason.record@suse.com>

%prep
%setup -q

%build

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/sle15all
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/sle15sp0
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/sle15sp1
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/sle15sp2
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/sle15sp3
install -d $RPM_BUILD_ROOT/usr/share/doc/packages/%{sca_common}
install -m 444 patterns/COPYING.GPLv2 $RPM_BUILD_ROOT/usr/share/doc/packages/%{sca_common}
install -m %{mode} patterns/%{category}/sle15all/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle15all
install -m %{mode} patterns/%{category}/sle15sp0/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle15sp0
install -m %{mode} patterns/%{category}/sle15sp1/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle15sp1
install -m %{mode} patterns/%{category}/sle15sp2/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle15sp2
install -m %{mode} patterns/%{category}/sle15sp3/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle15sp3
%fdupes %{buildroot}

%files
%defattr(-,%{patuser},%{patgrp})
%dir %{patdirbase}
%dir %{patdir}
%dir %{patdir}/%{category}
%dir %{patdir}/%{category}/sle15all
%dir %{patdir}/%{category}/sle15sp0
%dir %{patdir}/%{category}/sle15sp1
%dir %{patdir}/%{category}/sle15sp2
%dir %{patdir}/%{category}/sle15sp3
%dir /usr/share/doc/packages/%{sca_common}
%doc %attr(-,root,root) /usr/share/doc/packages/%{sca_common}/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle15all/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle15sp0/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle15sp1/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle15sp2/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle15sp3/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

