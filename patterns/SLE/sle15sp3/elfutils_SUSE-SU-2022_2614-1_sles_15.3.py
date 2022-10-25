#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for elfutils SUSE-SU-2022:2614-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP3
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-August/011724.html
# Source:      Security Announcement Generator (sagen.py) v2.0.0-beta4
# Modified:    2022 Oct 25
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
META_COMPONENT = "elfutils"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-August/011724.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'elfutils'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2022:2614-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'dwarves': '1.22-150300.7.3.1',
			'dwarves-debuginfo': '1.22-150300.7.3.1',
			'dwarves-debugsource': '1.22-150300.7.3.1',
			'elfutils': '0.177-150300.11.3.1',
			'elfutils-debuginfo': '0.177-150300.11.3.1',
			'elfutils-debugsource': '0.177-150300.11.3.1',
			'libasm-devel': '0.177-150300.11.3.1',
			'libasm1': '0.177-150300.11.3.1',
			'libasm1-debuginfo': '0.177-150300.11.3.1',
			'libdw-devel': '0.177-150300.11.3.1',
			'libdw1': '0.177-150300.11.3.1',
			'libdw1-debuginfo': '0.177-150300.11.3.1',
			'libdwarves-devel': '1.22-150300.7.3.1',
			'libdwarves1': '1.22-150300.7.3.1',
			'libdwarves1-debuginfo': '1.22-150300.7.3.1',
			'libebl-devel': '0.177-150300.11.3.1',
			'libebl-plugins': '0.177-150300.11.3.1',
			'libebl-plugins-debuginfo': '0.177-150300.11.3.1',
			'libelf-devel': '0.177-150300.11.3.1',
			'libelf1': '0.177-150300.11.3.1',
			'libelf1-debuginfo': '0.177-150300.11.3.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

