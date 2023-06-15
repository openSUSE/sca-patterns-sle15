#!/usr/bin/python3
#
# Title:       Important Security Announcement for openvswitch SUSE-SU-2023:2275-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP3 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2023-May/014938.html
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
meta_component = "openvswitch"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2023-May/014938.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = True
	name = 'openvswitch'
	main = ''
	severity = 'Important'
	tag = 'SUSE-SU-2023:2275-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 3 ):
			packages = {
				'libopenvswitch-2_14-0': '2.14.2-150300.19.8.1',
				'libopenvswitch-2_14-0-debuginfo': '2.14.2-150300.19.8.1',
				'libovn-20_06-0': '20.06.2-150300.19.8.1',
				'libovn-20_06-0-debuginfo': '20.06.2-150300.19.8.1',
				'openvswitch': '2.14.2-150300.19.8.1',
				'openvswitch-debuginfo': '2.14.2-150300.19.8.1',
				'openvswitch-debugsource': '2.14.2-150300.19.8.1',
				'openvswitch-devel': '2.14.2-150300.19.8.1',
				'openvswitch-ipsec': '2.14.2-150300.19.8.1',
				'openvswitch-pki': '2.14.2-150300.19.8.1',
				'openvswitch-test': '2.14.2-150300.19.8.1',
				'openvswitch-test-debuginfo': '2.14.2-150300.19.8.1',
				'openvswitch-vtep': '2.14.2-150300.19.8.1',
				'openvswitch-vtep-debuginfo': '2.14.2-150300.19.8.1',
				'ovn': '20.06.2-150300.19.8.1',
				'ovn-central': '20.06.2-150300.19.8.1',
				'ovn-central-debuginfo': '20.06.2-150300.19.8.1',
				'ovn-debuginfo': '20.06.2-150300.19.8.1',
				'ovn-devel': '20.06.2-150300.19.8.1',
				'ovn-docker': '20.06.2-150300.19.8.1',
				'ovn-host': '20.06.2-150300.19.8.1',
				'ovn-host-debuginfo': '20.06.2-150300.19.8.1',
				'ovn-vtep': '20.06.2-150300.19.8.1',
				'ovn-vtep-debuginfo': '20.06.2-150300.19.8.1',
				'python3-ovs': '2.14.2-150300.19.8.1',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

