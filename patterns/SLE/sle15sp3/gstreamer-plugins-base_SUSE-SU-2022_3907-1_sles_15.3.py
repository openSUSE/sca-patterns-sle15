#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for gstreamer-plugins-base SUSE-SU-2022:3907-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP3
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-November/012843.html
# Source:      Security Announcement Generator (sagen.py) v2.0.6
# Modified:    2023 Jun 13
#
##############################################################################
# Copyright (C) 2023 SUSE LLC
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

meta_class = "Security"
meta_category = "SLE"
meta_component = "gstreamer-plugins-base"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-November/012843.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = False
	name = 'gstreamer-plugins-base'
	main = ''
	severity = 'Moderate'
	tag = 'SUSE-SU-2022:3907-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 3 ):
			packages = {
				'gstreamer-plugins-base': '1.16.3-150200.4.6.2',
				'gstreamer-plugins-base-debuginfo': '1.16.3-150200.4.6.2',
				'gstreamer-plugins-base-debugsource': '1.16.3-150200.4.6.2',
				'gstreamer-plugins-base-devel': '1.16.3-150200.4.6.2',
				'libgstallocators-1_0-0': '1.16.3-150200.4.6.2',
				'libgstallocators-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'libgstapp-1_0-0': '1.16.3-150200.4.6.2',
				'libgstapp-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'libgstaudio-1_0-0': '1.16.3-150200.4.6.2',
				'libgstaudio-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'libgstfft-1_0-0': '1.16.3-150200.4.6.2',
				'libgstfft-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'libgstgl-1_0-0': '1.16.3-150200.4.6.2',
				'libgstgl-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'libgstpbutils-1_0-0': '1.16.3-150200.4.6.2',
				'libgstpbutils-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'libgstriff-1_0-0': '1.16.3-150200.4.6.2',
				'libgstriff-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'libgstrtp-1_0-0': '1.16.3-150200.4.6.2',
				'libgstrtp-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'libgstrtsp-1_0-0': '1.16.3-150200.4.6.2',
				'libgstrtsp-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'libgstsdp-1_0-0': '1.16.3-150200.4.6.2',
				'libgstsdp-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'libgsttag-1_0-0': '1.16.3-150200.4.6.2',
				'libgsttag-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'libgstvideo-1_0-0': '1.16.3-150200.4.6.2',
				'libgstvideo-1_0-0-debuginfo': '1.16.3-150200.4.6.2',
				'typelib-1_0-GstAllocators-1_0': '1.16.3-150200.4.6.2',
				'typelib-1_0-GstApp-1_0': '1.16.3-150200.4.6.2',
				'typelib-1_0-GstAudio-1_0': '1.16.3-150200.4.6.2',
				'typelib-1_0-GstGL-1_0': '1.16.3-150200.4.6.2',
				'typelib-1_0-GstPbutils-1_0': '1.16.3-150200.4.6.2',
				'typelib-1_0-GstRtp-1_0': '1.16.3-150200.4.6.2',
				'typelib-1_0-GstRtsp-1_0': '1.16.3-150200.4.6.2',
				'typelib-1_0-GstSdp-1_0': '1.16.3-150200.4.6.2',
				'typelib-1_0-GstTag-1_0': '1.16.3-150200.4.6.2',
				'typelib-1_0-GstVideo-1_0': '1.16.3-150200.4.6.2',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

