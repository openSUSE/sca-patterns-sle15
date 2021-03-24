#!/usr/bin/python
#
# Title:       Pattern for TID000019639
# Description: Intel X710 based NIC is not detected
# Source:      Package Version Pattern Template v0.3.5
# Options:     SLE,Kernel,Drivers,000019639,1151067,x710,kernel-default,4.12.14-197.29,0,1
# Modified:    2021 Mar 24
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

import re
import os
import Core
import SUSE

META_CLASS = "SLE"
META_CATEGORY = "Kernel"
META_COMPONENT = "Drivers"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019639|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1151067"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def x710Controller():
	fileOpen = "hardware.txt"
	section = "lspci"
	content = {}
	CONFIRMED = re.compile("Intel Corporation Ethernet Controller x710", re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(content[line]):
				return True
	return False

def conditionConfirmed():
	fileOpen = "boot.txt"
	section = "/dmesg"
	content = {}
	CONFIRMED = re.compile("i40e.*probe of.*failed with error -11", re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'kernel-default'
RPM_VERSION_FIXED = '4.12.14-197.29'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION_FIXED)
	if( INSTALLED_VERSION >= 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME + "")
	else:
		if( x710Controller() ):
			if( conditionConfirmed() ):
				Core.updateStatus(Core.CRIT, "The x710 network controller cannot be recognized, update system for fixes")
			else:
				Core.updateStatus(Core.WARN, "The x710 network controller may not be recognized, update system for fixes")
		else:
			Core.updateStatus(Core.ERROR, "ERROR: Missing Intel x710 controller")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")

Core.printPatternResults()

