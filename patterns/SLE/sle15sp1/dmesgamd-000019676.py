#!/usr/bin/python

# Title:       dmesg CCP and PSP messages
# Description: dmesg shows CCP and PSP initialization failure related messages
# Modified:    2021 Feb 18
# Distro:      SLES15 SP1
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

##############################################################################
# Module Definition
##############################################################################

import os
import re
import Core

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Kernel"
META_COMPONENT = "dmesg"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019676"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)
##############################################################################
# Local Function Definitions
##############################################################################

def amdCPU():
	fileOpen = "hardware.txt"
	section = "/proc/cpuinfo"
	AMD = re.compile("vendor_id.*:.*AMD.*", re.IGNORECASE)
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if AMD.search(content[line]):
				return True
	return False

def errorsFound():
	fileOpen = "boot.txt"
	section = "/bin/dmesg"
	content = {}
	ERRORS = re.compile("CCP initialization failed|PSP Initialization failed", re.IGNORECASE)
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if ERRORS.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( amdCPU() ):
	if( errorsFound() ):
		Core.updateStatus(Core.REC, "Detected CCP or PSP initialization failures on AMD processors, update to avoid")
	else:
		Core.updateStatus(Core.IGNORE, "No errors found with AMD processors")
else:
	Core.updateStatus(Core.ERROR, "Only applies to AMD Rome processors")

Core.printPatternResults()

