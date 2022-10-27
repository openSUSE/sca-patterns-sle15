#!/usr/bin/python3
#
# Title:       vim Error detected while processing
# Description: Pattern for TID000020735
# Template:    SCA Tool Python Pattern Generator v1.0.7
# Modified:    2022 Oct 27
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

import os
import Core
import SUSE

meta_class = "SLE"
meta_category = "Editor"
meta_component = "Vim"
pattern_id = os.path.basename(__file__)
primary_link = "META_LINK_TID"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020735|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1200184"
Core.init(meta_class, meta_category, meta_component, pattern_id, primary_link, overall, overall_info, other_links)

##############################################################################
# Main
##############################################################################

package = 'vim'
package_version_fixed = '8.2'
package_needed = 'vim-data'

if( SUSE.packageInstalled(package) ):
	package_version_installed = SUSE.compareRPM(package, package_version_fixed)
	if( package_version_installed == 0 ):
		if( SUSE.packageInstalled(package_needed) ):
			Core.updateStatus(Core.IGNORE, "Required package installed: " + package_needed)
		else:
			Core.updateStatus(Core.WARN, "Detected vim issue from missing package, install the " + package_needed + " package")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: Incorrect package version for " + package)
else:
	Core.updateStatus(Core.ERROR, "ERROR: RPM package " + package + " not installed")

Core.printPatternResults()
