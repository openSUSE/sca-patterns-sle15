#!/usr/bin/python3
#
# Title:       Important Security Announcement for postgresql12 SUSE-SU-2022:1894-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP2 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-May/011207.html
# Source:      Security Announcement Generator (sagen.py) v2.0.0-beta4
# Modified:    2022 Oct 05
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
META_COMPONENT = "postgresql12"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-May/011207.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'postgresql12'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:1894-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'postgresql12': '12.11-150200.8.32.1',
			'postgresql12-contrib': '12.11-150200.8.32.1',
			'postgresql12-contrib-debuginfo': '12.11-150200.8.32.1',
			'postgresql12-debuginfo': '12.11-150200.8.32.1',
			'postgresql12-debugsource': '12.11-150200.8.32.1',
			'postgresql12-devel': '12.11-150200.8.32.1',
			'postgresql12-devel-debuginfo': '12.11-150200.8.32.1',
			'postgresql12-plperl': '12.11-150200.8.32.1',
			'postgresql12-plperl-debuginfo': '12.11-150200.8.32.1',
			'postgresql12-plpython': '12.11-150200.8.32.1',
			'postgresql12-plpython-debuginfo': '12.11-150200.8.32.1',
			'postgresql12-pltcl': '12.11-150200.8.32.1',
			'postgresql12-pltcl-debuginfo': '12.11-150200.8.32.1',
			'postgresql12-server': '12.11-150200.8.32.1',
			'postgresql12-server-debuginfo': '12.11-150200.8.32.1',
			'postgresql12-server-devel': '12.11-150200.8.32.1',
			'postgresql12-server-devel-debuginfo': '12.11-150200.8.32.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

