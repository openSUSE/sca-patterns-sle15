#!/usr/bin/python3
#
# Title:       Important Security Announcement for poppler SUSE-SU-2023:0677-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP2 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2023-March/013996.html
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
meta_component = "poppler"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2023-March/013996.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = True
	name = 'poppler'
	main = ''
	severity = 'Important'
	tag = 'SUSE-SU-2023:0677-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 2 ):
			packages = {
				'libpoppler-cpp0': '0.79.0-150200.3.8.1',
				'libpoppler-cpp0-debuginfo': '0.79.0-150200.3.8.1',
				'libpoppler-devel': '0.79.0-150200.3.8.1',
				'libpoppler-glib-devel': '0.79.0-150200.3.8.1',
				'libpoppler-glib8': '0.79.0-150200.3.8.1',
				'libpoppler-glib8-debuginfo': '0.79.0-150200.3.8.1',
				'libpoppler89': '0.79.0-150200.3.8.1',
				'libpoppler89-debuginfo': '0.79.0-150200.3.8.1',
				'poppler-debugsource': '0.79.0-150200.3.8.1',
				'poppler-tools': '0.79.0-150200.3.8.1',
				'poppler-tools-debuginfo': '0.79.0-150200.3.8.1',
				'typelib-1_0-Poppler-0_18': '0.79.0-150200.3.8.1',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

