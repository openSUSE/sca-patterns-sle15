#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for zeromq SUSE-SU-2020:3264-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP0 LTSS
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
META_COMPONENT = "zeromq"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-November/007741.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'zeromq'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2020:3264-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'libunwind': '1.2.1-4.2.3',
			'libunwind-32bit': '1.2.1-4.2.3',
			'libunwind-32bit-debuginfo': '1.2.1-4.2.3',
			'libunwind-debuginfo': '1.2.1-4.2.3',
			'libunwind-debugsource': '1.2.1-4.2.3',
			'libunwind-devel': '1.2.1-4.2.3',
			'libzmq5': '4.2.3-3.15.4',
			'libzmq5-32bit': '4.2.3-3.15.4',
			'libzmq5-32bit-debuginfo': '4.2.3-3.15.4',
			'libzmq5-debuginfo': '4.2.3-3.15.4',
			'zeromq-debugsource': '4.2.3-3.15.4',
			'zeromq-devel': '4.2.3-3.15.4',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

