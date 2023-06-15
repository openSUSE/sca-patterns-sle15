#!/usr/bin/python3
#
# Title:       Important Security Announcement for ffmpeg SUSE-SU-2023:0005-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP1 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2023-January/013405.html
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
meta_component = "ffmpeg"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2023-January/013405.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = True
	name = 'ffmpeg'
	main = ''
	severity = 'Important'
	tag = 'SUSE-SU-2023:0005-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 1 ):
			packages = {
				'ffmpeg-debuginfo': '3.4.2-150000.4.44.1',
				'ffmpeg-debugsource': '3.4.2-150000.4.44.1',
				'libavcodec-devel': '3.4.2-150000.4.44.1',
				'libavcodec57': '3.4.2-150000.4.44.1',
				'libavcodec57-debuginfo': '3.4.2-150000.4.44.1',
				'libavdevice-devel': '3.4.2-150000.4.44.1',
				'libavdevice57': '3.4.2-150000.4.44.1',
				'libavdevice57-debuginfo': '3.4.2-150000.4.44.1',
				'libavfilter-devel': '3.4.2-150000.4.44.1',
				'libavfilter6': '3.4.2-150000.4.44.1',
				'libavfilter6-debuginfo': '3.4.2-150000.4.44.1',
				'libavformat-devel': '3.4.2-150000.4.44.1',
				'libavformat57': '3.4.2-150000.4.44.1',
				'libavformat57-debuginfo': '3.4.2-150000.4.44.1',
				'libavresample-devel': '3.4.2-150000.4.44.1',
				'libavresample3': '3.4.2-150000.4.44.1',
				'libavresample3-debuginfo': '3.4.2-150000.4.44.1',
				'libavutil-devel': '3.4.2-150000.4.44.1',
				'libavutil55': '3.4.2-150000.4.44.1',
				'libavutil55-debuginfo': '3.4.2-150000.4.44.1',
				'libpostproc-devel': '3.4.2-150000.4.44.1',
				'libpostproc54': '3.4.2-150000.4.44.1',
				'libpostproc54-debuginfo': '3.4.2-150000.4.44.1',
				'libswresample-devel': '3.4.2-150000.4.44.1',
				'libswresample2': '3.4.2-150000.4.44.1',
				'libswresample2-debuginfo': '3.4.2-150000.4.44.1',
				'libswscale-devel': '3.4.2-150000.4.44.1',
				'libswscale4': '3.4.2-150000.4.44.1',
				'libswscale4-debuginfo': '3.4.2-150000.4.44.1',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

