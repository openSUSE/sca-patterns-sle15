#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for wireshark SUSE-SU-2020:0693-1
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
META_COMPONENT = "wireshark"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-March/006613.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'wireshark'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2020:0693-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'libmaxminddb-debugsource': '1.4.2-1.3.1',
			'libmaxminddb-devel': '1.4.2-1.3.1',
			'libmaxminddb0': '1.4.2-1.3.1',
			'libmaxminddb0-32bit': '1.4.2-1.3.1',
			'libmaxminddb0-32bit-debuginfo': '1.4.2-1.3.1',
			'libmaxminddb0-debuginfo': '1.4.2-1.3.1',
			'libspandsp2': '0.0.6-3.2.1',
			'libspandsp2-32bit': '0.0.6-3.2.1',
			'libspandsp2-32bit-debuginfo': '0.0.6-3.2.1',
			'libspandsp2-debuginfo': '0.0.6-3.2.1',
			'libwireshark13': '3.2.2-3.35.2',
			'libwireshark13-debuginfo': '3.2.2-3.35.2',
			'libwiretap10': '3.2.2-3.35.2',
			'libwiretap10-debuginfo': '3.2.2-3.35.2',
			'libwsutil11': '3.2.2-3.35.2',
			'libwsutil11-debuginfo': '3.2.2-3.35.2',
			'mmdblookup': '1.4.2-1.3.1',
			'spandsp-debugsource': '0.0.6-3.2.1',
			'spandsp-devel': '0.0.6-3.2.1',
			'spandsp-doc': '0.0.6-3.2.1',
			'wireshark': '3.2.2-3.35.2',
			'wireshark-debuginfo': '3.2.2-3.35.2',
			'wireshark-debugsource': '3.2.2-3.35.2',
			'wireshark-devel': '3.2.2-3.35.2',
			'wireshark-ui-qt': '3.2.2-3.35.2',
			'wireshark-ui-qt-debuginfo': '3.2.2-3.35.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

