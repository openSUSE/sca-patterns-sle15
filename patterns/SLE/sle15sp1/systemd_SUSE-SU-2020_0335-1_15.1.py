#!/usr/bin/python3
#
# Title:       Important Security Announcement for systemd SUSE-SU-2020:0335-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP1
# Source:      Security Announcement Parser v1.5.2
# Modified:    2020 Nov 16
#
##############################################################################
# Copyright (C) 2020 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record (jason.record@suse.com)
#
##############################################################################

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "systemd"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-February/006455.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'systemd'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:0335-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'libsystemd0': '234-24.39.1',
			'libsystemd0-32bit': '234-24.39.1',
			'libsystemd0-32bit-debuginfo': '234-24.39.1',
			'libsystemd0-debuginfo': '234-24.39.1',
			'libsystemd0-mini': '234-24.39.1',
			'libsystemd0-mini-debuginfo': '234-24.39.1',
			'libudev-devel': '234-24.39.1',
			'libudev-devel-32bit': '234-24.39.1',
			'libudev-mini-devel': '234-24.39.1',
			'libudev-mini1': '234-24.39.1',
			'libudev-mini1-debuginfo': '234-24.39.1',
			'libudev1': '234-24.39.1',
			'libudev1-32bit': '234-24.39.1',
			'libudev1-32bit-debuginfo': '234-24.39.1',
			'libudev1-debuginfo': '234-24.39.1',
			'nss-myhostname': '234-24.39.1',
			'nss-myhostname-32bit': '234-24.39.1',
			'nss-myhostname-32bit-debuginfo': '234-24.39.1',
			'nss-myhostname-debuginfo': '234-24.39.1',
			'nss-mymachines': '234-24.39.1',
			'nss-mymachines-32bit': '234-24.39.1',
			'nss-mymachines-32bit-debuginfo': '234-24.39.1',
			'nss-mymachines-debuginfo': '234-24.39.1',
			'nss-systemd': '234-24.39.1',
			'nss-systemd-debuginfo': '234-24.39.1',
			'systemd': '234-24.39.1',
			'systemd-32bit': '234-24.39.1',
			'systemd-32bit-debuginfo': '234-24.39.1',
			'systemd-bash-completion': '234-24.39.1',
			'systemd-container': '234-24.39.1',
			'systemd-container-debuginfo': '234-24.39.1',
			'systemd-coredump': '234-24.39.1',
			'systemd-coredump-debuginfo': '234-24.39.1',
			'systemd-debuginfo': '234-24.39.1',
			'systemd-debugsource': '234-24.39.1',
			'systemd-devel': '234-24.39.1',
			'systemd-logger': '234-24.39.1',
			'systemd-mini': '234-24.39.1',
			'systemd-mini-bash-completion': '234-24.39.1',
			'systemd-mini-container-mini': '234-24.39.1',
			'systemd-mini-container-mini-debuginfo': '234-24.39.1',
			'systemd-mini-coredump-mini': '234-24.39.1',
			'systemd-mini-coredump-mini-debuginfo': '234-24.39.1',
			'systemd-mini-debuginfo': '234-24.39.1',
			'systemd-mini-debugsource': '234-24.39.1',
			'systemd-mini-devel': '234-24.39.1',
			'systemd-mini-sysvinit': '234-24.39.1',
			'systemd-sysvinit': '234-24.39.1',
			'udev': '234-24.39.1',
			'udev-debuginfo': '234-24.39.1',
			'udev-mini': '234-24.39.1',
			'udev-mini-debuginfo': '234-24.39.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

