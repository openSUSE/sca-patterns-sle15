#!/usr/bin/python
#
# Title:       Pattern for TID000019537
# Description: A kernel message shows EDAC amd64 Error F0 not found, device 0x1460 broken BIOS
# Source:      Kernel Package Version Pattern Template v0.1.1
# Options:     SLE,Kernel,EDAC,edac,000019537,1131489,4.12.14-197.18,0,1
# Distro:      SLES15 SP1
# Modified:    2021 Apr 23
#
##############################################################################
# Copyright (C) 2021, SUSE LLC
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

META_CLASS = "SLE"
META_CATEGORY = "Kernel"
META_COMPONENT = "EDAC"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019537|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1131489"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def PowerEdge():
	fileOpen = "basic-environment.txt"
	section = "Virtualization"
	content = []
	CONFIRMED = re.compile("Hardware.*PowerEdge", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(line):
				return True
	return False

def errorFound():
	fileOpen = "boot.txt"
	section = "/dmesg"
	content = []
	CONFIRMED = re.compile("EDAC amd64.*Error.*F0 not found.*device.*broken BIOS", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(line):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

KERNEL_VERSION_FIXED = '4.12.14-197.18'

INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION_FIXED)
if( INSTALLED_VERSION >= 0 ):
	Core.updateStatus(Core.IGNORE, "Bug fixes applied in kernel version " + KERNEL_VERSION_FIXED + " or higher")
else:
	if( PowerEdge() ):
		if( errorFound() ):
			Core.updateStatus(Core.CRIT, "Missing AMD ROME CPU enablement, update system for fixes")
		else:
			Core.updateStatus(Core.WARN, "Possible AMD ROME CPU enablement issue, update system to avoid")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: Only Dell EMC PowerEdge systems affected")

Core.printPatternResults()

