#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for zypper SUSE-SU-2021:0770-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP0 LTSS
# Source:      Security Announcement Parser v1.6.1
# Modified:    2021 Mar 31
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
META_COMPONENT = "zypper"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2021-March/008472.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'zypper'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2021:0770-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'libsolv-debuginfo': '0.7.17-3.40.1',
			'libsolv-debugsource': '0.7.17-3.40.1',
			'libsolv-devel': '0.7.17-3.40.1',
			'libsolv-devel-debuginfo': '0.7.17-3.40.1',
			'libsolv-tools': '0.7.17-3.40.1',
			'libsolv-tools-debuginfo': '0.7.17-3.40.1',
			'libzypp': '17.25.8-3.66.1',
			'libzypp-debuginfo': '17.25.8-3.66.1',
			'libzypp-debugsource': '17.25.8-3.66.1',
			'libzypp-devel': '17.25.8-3.66.1',
			'perl-solv': '0.7.17-3.40.1',
			'perl-solv-debuginfo': '0.7.17-3.40.1',
			'python-solv': '0.7.17-3.40.1',
			'python-solv-debuginfo': '0.7.17-3.40.1',
			'python3-solv': '0.7.17-3.40.1',
			'python3-solv-debuginfo': '0.7.17-3.40.1',
			'ruby-solv': '0.7.17-3.40.1',
			'ruby-solv-debuginfo': '0.7.17-3.40.1',
			'yast2-installation': '4.0.77-3.22.5',
			'zypper': '1.14.43-3.49.1',
			'zypper-debuginfo': '1.14.43-3.49.1',
			'zypper-debugsource': '1.14.43-3.49.1',
			'zypper-log': '1.14.43-3.49.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

