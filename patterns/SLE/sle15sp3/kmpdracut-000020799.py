#!/usr/bin/python3
#
# Title:       System fails to boot or losses functionality after kernel update when third party kernel modules are used
# Description: Pattern for TID000020799
# Template:    SCA Tool Python Pattern Generator v1.0.7
# Modified:    2022 Oct 17
#
##############################################################################
# Copyright (C) 2022 SUSE LLC
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
meta_category = "KMP"
meta_component = "dracut"
pattern_id = os.path.basename(__file__)
primary_link = "META_LINK_TID"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020799|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1185277"
Core.init(meta_class, meta_category, meta_component, pattern_id, primary_link, overall, overall_info, other_links)

##############################################################################
# Local Function Definitions
##############################################################################

def kmp_package_found():
	file_open = "rpm.txt"
	section = "rpm -qa --queryformat.*NAME}"
	content = []
	confirmed = re.compile("kmp-", re.IGNORECASE)
	exception_list = re.compile("^dpdk-kmp-default |^oracleasm-kmp-default |^crash-kmp-default |^lttng-modules-kmp-default |^reiserfs-kmp-default |^cluster-md-kmp-default |^dlm-kmp-default |^drbd-kmp-default |^gfs2-kmp-default |^ocfs2-kmp-default ", re.IGNORECASE)
	if Core.isFileActive(file_open):
		if Core.getRegExSection(file_open, section, content):
			for line in content:
				if confirmed.search(line):
					if exception_list.search(line):
						continue
					else:
						return True
	return False

##############################################################################
# Main
##############################################################################

package = 'dracut'
package_version_fixed = '049.1+suse.238.gd8dbb075-150200.3.60'

if( SUSE.packageInstalled(package) ):
	package_version_installed = SUSE.compareRPM(package, package_version_fixed)
	if( package_version_installed >= 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + package + "")
	else:
		if( kmp_package_found() ):
			Core.updateStatus(Core.WARN, "If KMP drivers are required for booting, update dracut first")
		else:
			Core.updateStatus(Core.ERROR, "ERROR: No KMP packages found")
else:
	Core.updateStatus(Core.ERROR, "ERROR: RPM package " + package + " not installed")

Core.printPatternResults()
