#!/usr/bin/python3
#
# Title:       TID000019637, cpupower
# Description: Pattern for TID000019637
# Source:      Package Version Pattern Template v0.2.0
# Options:     SLE,CPU,Tools,000019637,1152967,cpupower,cpupower,4.19-6.5,0,1
# Modified:    2021 Feb 18
#
##############################################################################
# Copyright (C) 2021 SUSE LLC
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
import re
import Core
import SUSE

META_CLASS = "SLE"
META_CATEGORY = "CPU"
META_COMPONENT = "Tools"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019637|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1152967"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def conditionConfirmed():
	fileOpen = "hardware.txt"
	section = "/proc/cpuinfo"
	AMD = re.compile("vendor_id.*:.*amd.*", re.IGNORECASE)
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if AMD.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'cpupower'
RPM_VERSION_FIXED = '4.19-6.5'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION_FIXED)
	if( INSTALLED_VERSION >= 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME + "")
	else:
		if( conditionConfirmed() ):
			Core.updateStatus(Core.WARN, "Unable to read boost states using cpupower on AMD Rome CPUs, update to resolve")
		else:
			Core.updateStatus(Core.WARN, "cpupower may be unable to read boost states, update to resolve")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")

Core.printPatternResults()

