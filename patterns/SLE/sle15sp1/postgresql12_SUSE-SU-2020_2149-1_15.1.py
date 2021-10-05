#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for postgresql12 SUSE-SU-2020:2149-1
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
META_COMPONENT = "postgresql12"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-August/007234.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'postgresql12'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2020:2149-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'libecpg6': '12.3-3.8.1',
			'libecpg6-debuginfo': '12.3-3.8.1',
			'libpq5': '12.3-3.8.1',
			'libpq5-32bit': '12.3-3.8.1',
			'libpq5-32bit-debuginfo': '12.3-3.8.1',
			'libpq5-debuginfo': '12.3-3.8.1',
			'postgresql': '12.0.1-8.14.1',
			'postgresql-contrib': '12.0.1-8.14.1',
			'postgresql-devel': '12.0.1-8.14.1',
			'postgresql-docs': '12.0.1-8.14.1',
			'postgresql-plperl': '12.0.1-8.14.1',
			'postgresql-plpython': '12.0.1-8.14.1',
			'postgresql-pltcl': '12.0.1-8.14.1',
			'postgresql-server': '12.0.1-8.14.1',
			'postgresql-server-devel': '12.0.1-8.14.1',
			'postgresql-test': '12.0.1-8.14.1',
			'postgresql12': '12.3-3.8.1',
			'postgresql12-contrib': '12.3-3.8.1',
			'postgresql12-contrib-debuginfo': '12.3-3.8.1',
			'postgresql12-debuginfo': '12.3-3.8.1',
			'postgresql12-debugsource': '12.3-3.8.1',
			'postgresql12-devel': '12.3-3.8.1',
			'postgresql12-devel-debuginfo': '12.3-3.8.1',
			'postgresql12-docs': '12.3-3.8.1',
			'postgresql12-plperl': '12.3-3.8.1',
			'postgresql12-plperl-debuginfo': '12.3-3.8.1',
			'postgresql12-plpython': '12.3-3.8.1',
			'postgresql12-plpython-debuginfo': '12.3-3.8.1',
			'postgresql12-pltcl': '12.3-3.8.1',
			'postgresql12-pltcl-debuginfo': '12.3-3.8.1',
			'postgresql12-server': '12.3-3.8.1',
			'postgresql12-server-debuginfo': '12.3-3.8.1',
			'postgresql12-server-devel': '12.3-3.8.1',
			'postgresql12-server-devel-debuginfo': '12.3-3.8.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

