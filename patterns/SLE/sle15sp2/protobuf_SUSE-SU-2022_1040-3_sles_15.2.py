#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for protobuf SUSE-SU-2022:1040-3
# Description: Security fixes for SUSE Linux Enterprise 15 SP2
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-October/012505.html
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
meta_component = "protobuf"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-October/012505.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = False
	name = 'protobuf'
	main = ''
	severity = 'Moderate'
	tag = 'SUSE-SU-2022:1040-3'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 2 ):
			packages = {
				'libprotobuf-lite20': '3.9.2-4.12.1',
				'libprotobuf-lite20-debuginfo': '3.9.2-4.12.1',
				'libprotobuf20': '3.9.2-4.12.1',
				'libprotobuf20-debuginfo': '3.9.2-4.12.1',
				'libprotoc20': '3.9.2-4.12.1',
				'libprotoc20-debuginfo': '3.9.2-4.12.1',
				'protobuf-debugsource': '3.9.2-4.12.1',
				'protobuf-devel': '3.9.2-4.12.1',
				'protobuf-devel-debuginfo': '3.9.2-4.12.1',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

