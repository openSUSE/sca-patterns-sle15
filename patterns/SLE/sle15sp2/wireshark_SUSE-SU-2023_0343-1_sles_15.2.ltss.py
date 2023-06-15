#!/usr/bin/python3
#
# Title:       Important Security Announcement for wireshark SUSE-SU-2023:0343-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP2 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2023-February/013723.html
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
meta_component = "wireshark"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2023-February/013723.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = True
	name = 'wireshark'
	main = ''
	severity = 'Important'
	tag = 'SUSE-SU-2023:0343-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 2 ):
			packages = {
				'libwireshark15': '3.6.11-150000.3.83.1',
				'libwireshark15-debuginfo': '3.6.11-150000.3.83.1',
				'libwiretap12': '3.6.11-150000.3.83.1',
				'libwiretap12-debuginfo': '3.6.11-150000.3.83.1',
				'libwsutil13': '3.6.11-150000.3.83.1',
				'libwsutil13-debuginfo': '3.6.11-150000.3.83.1',
				'wireshark': '3.6.11-150000.3.83.1',
				'wireshark-debuginfo': '3.6.11-150000.3.83.1',
				'wireshark-debugsource': '3.6.11-150000.3.83.1',
				'wireshark-devel': '3.6.11-150000.3.83.1',
				'wireshark-ui-qt': '3.6.11-150000.3.83.1',
				'wireshark-ui-qt-debuginfo': '3.6.11-150000.3.83.1',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

