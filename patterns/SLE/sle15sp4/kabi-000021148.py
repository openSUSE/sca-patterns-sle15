#!/usr/bin/python3
#
# Title:       kABI breakage causing kernel panic with third-party drivers
# Description: Pattern for TID000021148
# Template:    SCA Tool Python Pattern Generator v2.0.2
# Modified:    2023 Aug 29
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

import re
import os
import Core
import SUSE

meta_class = "SLE"
meta_category = "Kernel"
meta_component = "kABI"
pattern_id = os.path.basename(__file__)
primary_link = "META_LINK_TID"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000021148|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1207894"
Core.init(meta_class, meta_category, meta_component, pattern_id, primary_link, overall, overall_info, other_links)

##############################################################################
# Local Function Definitions
##############################################################################

def third_party_driver():
	file_open = "modules.txt"
	content = {}
	confirmed = re.compile("external|no", re.IGNORECASE)
	Core.listSections(file_open, content)
	for line in content:
		modcmd = content[line]
		if "modinfo" in modcmd:
			driver = modcmd.split()[-1]
			info = SUSE.getDriverInfo(driver)
			if confirmed.search(info['supported']):
				return True
	return False

##############################################################################
# Main
##############################################################################

def main():
	kernel_version_fixed = '5.14.21-150400.24.74'

	kernel_version_installed = SUSE.compareKernel(kernel_version_fixed)
	if( kernel_version_installed >= 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied in kernel version " + kernel_version_fixed + " or higher")
	else:
		if( third_party_driver() ):
			Core.updateStatus(Core.WARN, "The kABI update may adversely affect some third-party drivers")
		else:
			Core.updateStatus(Core.IGNORE, "Ignore: Third-party drivers not found")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

