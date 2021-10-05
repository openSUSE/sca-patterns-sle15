#!/usr/bin/python3
#
# Title:       Important Security Announcement for gstreamer-plugins-ugly SUSE-SU-2021:1819-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP2
# Source:      Security Announcement Parser v1.6.1
# Modified:    2021 Jul 02
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
META_COMPONENT = "gstreamer-plugins-ugly"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2021-June/008904.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'gstreamer-plugins-ugly'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2021:1819-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'gstreamer': '1.16.3-3.3.1',
			'gstreamer-debuginfo': '1.16.3-3.3.1',
			'gstreamer-debugsource': '1.16.3-3.3.1',
			'gstreamer-lang': '1.16.3-3.3.1',
			'gstreamer-plugins-bad-debuginfo': '1.16.3-4.4.1',
			'gstreamer-plugins-bad-debugsource': '1.16.3-4.4.1',
			'gstreamer-plugins-base': '1.16.3-4.3.1',
			'gstreamer-plugins-base-debuginfo': '1.16.3-4.3.1',
			'gstreamer-plugins-base-debugsource': '1.16.3-4.3.1',
			'gstreamer-plugins-base-lang': '1.16.3-4.3.1',
			'gstreamer-plugins-good': '1.16.3-3.3.1',
			'gstreamer-plugins-good-debuginfo': '1.16.3-3.3.1',
			'gstreamer-plugins-good-debugsource': '1.16.3-3.3.1',
			'gstreamer-plugins-good-lang': '1.16.3-3.3.1',
			'libgstallocators-1_0-0': '1.16.3-4.3.1',
			'libgstallocators-1_0-0-debuginfo': '1.16.3-4.3.1',
			'libgstapp-1_0-0': '1.16.3-4.3.1',
			'libgstapp-1_0-0-debuginfo': '1.16.3-4.3.1',
			'libgstaudio-1_0-0': '1.16.3-4.3.1',
			'libgstaudio-1_0-0-debuginfo': '1.16.3-4.3.1',
			'libgstfft-1_0-0': '1.16.3-4.3.1',
			'libgstfft-1_0-0-debuginfo': '1.16.3-4.3.1',
			'libgstgl-1_0-0': '1.16.3-4.3.1',
			'libgstgl-1_0-0-debuginfo': '1.16.3-4.3.1',
			'libgstpbutils-1_0-0': '1.16.3-4.3.1',
			'libgstpbutils-1_0-0-debuginfo': '1.16.3-4.3.1',
			'libgstphotography-1_0-0': '1.16.3-4.4.1',
			'libgstphotography-1_0-0-debuginfo': '1.16.3-4.4.1',
			'libgstreamer-1_0-0': '1.16.3-3.3.1',
			'libgstreamer-1_0-0-debuginfo': '1.16.3-3.3.1',
			'libgstriff-1_0-0': '1.16.3-4.3.1',
			'libgstriff-1_0-0-debuginfo': '1.16.3-4.3.1',
			'libgstrtp-1_0-0': '1.16.3-4.3.1',
			'libgstrtp-1_0-0-debuginfo': '1.16.3-4.3.1',
			'libgstrtsp-1_0-0': '1.16.3-4.3.1',
			'libgstrtsp-1_0-0-debuginfo': '1.16.3-4.3.1',
			'libgstsdp-1_0-0': '1.16.3-4.3.1',
			'libgstsdp-1_0-0-debuginfo': '1.16.3-4.3.1',
			'libgsttag-1_0-0': '1.16.3-4.3.1',
			'libgsttag-1_0-0-debuginfo': '1.16.3-4.3.1',
			'libgstvideo-1_0-0': '1.16.3-4.3.1',
			'libgstvideo-1_0-0-debuginfo': '1.16.3-4.3.1',
			'typelib-1_0-Gst-1_0': '1.16.3-3.3.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

