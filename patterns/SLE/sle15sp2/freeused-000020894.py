#!/usr/bin/python3
#
# Title:       'free' command reports misleading "used" value
# Description: Pattern for TID000020894
# Template:    SCA Tool Python Pattern Generator v1.0.10
# Modified:    2022 Dec 21
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
meta_category = "Memory"
meta_component = "free"
pattern_id = os.path.basename(__file__)
primary_link = "META_LINK_TID"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020894|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1206412"
Core.init(meta_class, meta_category, meta_component, pattern_id, primary_link, overall, overall_info, other_links)

##############################################################################
# Main
##############################################################################

packages = ['libprocps7', 'procps']
package_version_fixed = '3.3.15-150000.7.25'
fixes_needed = []

for package in packages:
    if( SUSE.packageInstalled(package) ):
	    package_version_installed = SUSE.compareRPM(package, package_version_fixed)
	    if( package_version_installed < 0 ):
	        fixes_needed.append(package)

if( len(fixes_needed) > 0 ):
    Core.updateStatus(Core.WARN, "The free command may display inaccurate 'used' data, please update: " + ' '.join(fixes_needed))
else:
    Core.updateStatus(Core.IGNORE, "All package updates applied.")

Core.printPatternResults()
