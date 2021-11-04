#!/usr/bin/python3
#
# Title:       Pattern for TID000019739
# Description: BIOS update failure when an update is performed using the Linux .bin files
# Source:      Package Version Pattern Template v0.3.5
# Options:     SLE,Kernel,Update,000019739,1175952,kernel,kernel-default,5.3.18-24.24,0,1
# Distro:      SLES15 SP2
# Modified:    2021 Mar 25
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
META_COMPONENT = "Update"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019739|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1175952"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def conditionConfirmed():
	fileOpen = "basic-environment.txt"
	section = "Virtualization"
	content = {}
	CONFIRMED = re.compile("PowerEdge.*R240|PowerEdge.*R340|PowerEdge.*T140|PowerEdge.*T340", re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'kernel-default'
RPM_VERSION_FIXED = '5.3.18-24.24'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION_FIXED)
	if( INSTALLED_VERSION >= 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME + "")
	else:
		if( conditionConfirmed() ):
			Core.updateStatus(Core.WARN, "BIOS update with .bin files may fail, install updated kernel first")
		else:
			Core.updateStatus(Core.ERROR, "Issue does not apply to this hardware")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")

Core.printPatternResults()

