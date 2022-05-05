#!/usr/bin/python3
#
# Title:       Important Security Announcement for util-linux SUSE-SU-2022:1108-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP0 LTSS
# Source:      Security Announcement Parser v1.6.4
# Modified:    2022 May 05
#
##############################################################################
# Copyright (C) 2022 SUSE LLC
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
META_COMPONENT = "util-linux"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-April/010651.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'util-linux'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:1108-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'libblkid-devel': '2.31.1-150000.9.18.2',
			'libblkid-devel-static': '2.31.1-150000.9.18.2',
			'libblkid1': '2.31.1-150000.9.18.2',
			'libblkid1-debuginfo': '2.31.1-150000.9.18.2',
			'libfdisk-devel': '2.31.1-150000.9.18.2',
			'libfdisk1': '2.31.1-150000.9.18.2',
			'libfdisk1-debuginfo': '2.31.1-150000.9.18.2',
			'libmount-devel': '2.31.1-150000.9.18.2',
			'libmount1': '2.31.1-150000.9.18.2',
			'libmount1-debuginfo': '2.31.1-150000.9.18.2',
			'libsmartcols-devel': '2.31.1-150000.9.18.2',
			'libsmartcols1': '2.31.1-150000.9.18.2',
			'libsmartcols1-debuginfo': '2.31.1-150000.9.18.2',
			'libuuid-devel': '2.31.1-150000.9.18.2',
			'libuuid-devel-static': '2.31.1-150000.9.18.2',
			'libuuid1': '2.31.1-150000.9.18.2',
			'libuuid1-debuginfo': '2.31.1-150000.9.18.2',
			'util-linux': '2.31.1-150000.9.18.2',
			'util-linux-debuginfo': '2.31.1-150000.9.18.2',
			'util-linux-debugsource': '2.31.1-150000.9.18.2',
			'util-linux-lang': '2.31.1-150000.9.18.2',
			'util-linux-systemd': '2.31.1-150000.9.18.2',
			'util-linux-systemd-debuginfo': '2.31.1-150000.9.18.2',
			'util-linux-systemd-debugsource': '2.31.1-150000.9.18.2',
			'uuidd': '2.31.1-150000.9.18.2',
			'uuidd-debuginfo': '2.31.1-150000.9.18.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

