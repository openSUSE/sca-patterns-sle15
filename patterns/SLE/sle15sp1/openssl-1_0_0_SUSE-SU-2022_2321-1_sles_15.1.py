#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for openssl-1_0_0 SUSE-SU-2022:2321-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP1
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-July/011468.html
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
META_COMPONENT = "openssl-1_0_0"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-July/011468.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'openssl-1_0_0'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2022:2321-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'libopenssl-1_0_0-devel': '1.0.2p-150000.3.56.1',
			'libopenssl1_0_0': '1.0.2p-150000.3.56.1',
			'libopenssl1_0_0-debuginfo': '1.0.2p-150000.3.56.1',
			'openssl-1_0_0': '1.0.2p-150000.3.56.1',
			'openssl-1_0_0-debuginfo': '1.0.2p-150000.3.56.1',
			'openssl-1_0_0-debugsource': '1.0.2p-150000.3.56.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()
