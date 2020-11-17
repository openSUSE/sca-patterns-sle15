#!/usr/bin/python
#
# Title:       Moderate Security Announcement for libnettle SUSE-SU-2020:0948-1
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
META_COMPONENT = "libnettle"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-April/006686.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'libnettle'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2020:0948-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'gmp-debugsource': '6.1.2-4.3.1',
			'gmp-devel': '6.1.2-4.3.1',
			'gmp-devel-32bit': '6.1.2-4.3.1',
			'gnutls': '3.6.7-6.14.1',
			'gnutls-debuginfo': '3.6.7-6.14.1',
			'gnutls-debugsource': '3.6.7-6.14.1',
			'libgmp10': '6.1.2-4.3.1',
			'libgmp10-32bit': '6.1.2-4.3.1',
			'libgmp10-32bit-debuginfo': '6.1.2-4.3.1',
			'libgmp10-debuginfo': '6.1.2-4.3.1',
			'libgmpxx4': '6.1.2-4.3.1',
			'libgmpxx4-32bit': '6.1.2-4.3.1',
			'libgmpxx4-32bit-debuginfo': '6.1.2-4.3.1',
			'libgmpxx4-debuginfo': '6.1.2-4.3.1',
			'libgnutls-devel': '3.6.7-6.14.1',
			'libgnutls30': '3.6.7-6.14.1',
			'libgnutls30-32bit': '3.6.7-6.14.1',
			'libgnutls30-32bit-debuginfo': '3.6.7-6.14.1',
			'libgnutls30-debuginfo': '3.6.7-6.14.1',
			'libgnutls30-hmac': '3.6.7-6.14.1',
			'libgnutls30-hmac-32bit': '3.6.7-6.14.1',
			'libgnutlsxx-devel': '3.6.7-6.14.1',
			'libgnutlsxx28': '3.6.7-6.14.1',
			'libgnutlsxx28-debuginfo': '3.6.7-6.14.1',
			'libhogweed4': '3.4.1-4.12.1',
			'libhogweed4-32bit': '3.4.1-4.12.1',
			'libhogweed4-32bit-debuginfo': '3.4.1-4.12.1',
			'libhogweed4-debuginfo': '3.4.1-4.12.1',
			'libnettle-debugsource': '3.4.1-4.12.1',
			'libnettle-devel': '3.4.1-4.12.1',
			'libnettle6': '3.4.1-4.12.1',
			'libnettle6-32bit': '3.4.1-4.12.1',
			'libnettle6-32bit-debuginfo': '3.4.1-4.12.1',
			'libnettle6-debuginfo': '3.4.1-4.12.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

