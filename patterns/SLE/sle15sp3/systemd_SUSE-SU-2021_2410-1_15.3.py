#!/usr/bin/python3
#
# Title:       Important Security Announcement for systemd SUSE-SU-2021:2410-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP3
# Source:      Security Announcement Parser v1.6.1
# Modified:    2021 Aug 05
#
##############################################################################
# Copyright (C) 2021 SUSE LLC
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
#   Jason Record <jason.record@suse.com>
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
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2021-July/009162.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'systemd'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2021:2410-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'libsystemd0': '246.13-7.8.1',
			'libsystemd0-32bit': '246.13-7.8.1',
			'libsystemd0-32bit-debuginfo': '246.13-7.8.1',
			'libsystemd0-debuginfo': '246.13-7.8.1',
			'libudev-devel': '246.13-7.8.1',
			'libudev1': '246.13-7.8.1',
			'libudev1-32bit': '246.13-7.8.1',
			'libudev1-32bit-debuginfo': '246.13-7.8.1',
			'libudev1-debuginfo': '246.13-7.8.1',
			'systemd': '246.13-7.8.1',
			'systemd-32bit': '246.13-7.8.1',
			'systemd-32bit-debuginfo': '246.13-7.8.1',
			'systemd-container': '246.13-7.8.1',
			'systemd-container-debuginfo': '246.13-7.8.1',
			'systemd-coredump': '246.13-7.8.1',
			'systemd-coredump-debuginfo': '246.13-7.8.1',
			'systemd-debuginfo': '246.13-7.8.1',
			'systemd-debugsource': '246.13-7.8.1',
			'systemd-devel': '246.13-7.8.1',
			'systemd-doc': '246.13-7.8.1',
			'systemd-journal-remote': '246.13-7.8.1',
			'systemd-journal-remote-debuginfo': '246.13-7.8.1',
			'systemd-lang': '246.13-7.8.1',
			'systemd-sysvinit': '246.13-7.8.1',
			'udev': '246.13-7.8.1',
			'udev-debuginfo': '246.13-7.8.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

