#!/usr/bin/python3
#
# Title:       Important Security Announcement for qemu SUSE-SU-2022:3594-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP2
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-October/012542.html
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
meta_component = "qemu"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-October/012542.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = False
	name = 'qemu'
	main = ''
	severity = 'Important'
	tag = 'SUSE-SU-2022:3594-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 2 ):
			packages = {
				'qemu': '4.2.1-150200.69.1',
				'qemu-audio-alsa': '4.2.1-150200.69.1',
				'qemu-audio-alsa-debuginfo': '4.2.1-150200.69.1',
				'qemu-audio-pa': '4.2.1-150200.69.1',
				'qemu-audio-pa-debuginfo': '4.2.1-150200.69.1',
				'qemu-block-curl': '4.2.1-150200.69.1',
				'qemu-block-curl-debuginfo': '4.2.1-150200.69.1',
				'qemu-block-iscsi': '4.2.1-150200.69.1',
				'qemu-block-iscsi-debuginfo': '4.2.1-150200.69.1',
				'qemu-block-rbd': '4.2.1-150200.69.1',
				'qemu-block-rbd-debuginfo': '4.2.1-150200.69.1',
				'qemu-block-ssh': '4.2.1-150200.69.1',
				'qemu-block-ssh-debuginfo': '4.2.1-150200.69.1',
				'qemu-debuginfo': '4.2.1-150200.69.1',
				'qemu-debugsource': '4.2.1-150200.69.1',
				'qemu-guest-agent': '4.2.1-150200.69.1',
				'qemu-guest-agent-debuginfo': '4.2.1-150200.69.1',
				'qemu-kvm': '4.2.1-150200.69.1',
				'qemu-lang': '4.2.1-150200.69.1',
				'qemu-tools': '4.2.1-150200.69.1',
				'qemu-tools-debuginfo': '4.2.1-150200.69.1',
				'qemu-ui-curses': '4.2.1-150200.69.1',
				'qemu-ui-curses-debuginfo': '4.2.1-150200.69.1',
				'qemu-ui-gtk': '4.2.1-150200.69.1',
				'qemu-ui-gtk-debuginfo': '4.2.1-150200.69.1',
				'qemu-ui-spice-app': '4.2.1-150200.69.1',
				'qemu-ui-spice-app-debuginfo': '4.2.1-150200.69.1',
				'qemu-x86': '4.2.1-150200.69.1',
				'qemu-x86-debuginfo': '4.2.1-150200.69.1',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

