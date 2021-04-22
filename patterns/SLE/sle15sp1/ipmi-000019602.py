#!/usr/bin/python
#
# Title:       Pattern for TID000019602
# Description: IPMI driver can be unloaded when being accessed by user space
# Source:      Kernel Package Version Pattern Template v0.1.1
# Options:     SLE,Kernel,IPMI,ipmi,000019602,1154768,4.12.14-197.34,0,1
# Distro:      SLES15 SP1
# Modified:    2021 Apr 22
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
META_COMPONENT = "IPMI"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019602|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1154768"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def conditionConfirmed():
	fileOpen = "hardware.txt"
	section = "hwinfo"
	content = []
	CONFIRMED = re.compile("/dev/ipmi", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(line):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

KERNEL_VERSION_FIXED = '4.12.14-197.34'
DRIVER_NAME = 'ipmi_si'

INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION_FIXED)
if( INSTALLED_VERSION >= 0 ):
	Core.updateStatus(Core.IGNORE, "Bug fixes applied in kernel version " + KERNEL_VERSION_FIXED + " or higher")
else:
	DRIVER_INFO = SUSE.getDriverInfo(DRIVER_NAME)
	if( DRIVER_INFO['loaded'] ):
		Core.updateStatus(Core.CRIT, "The " + DRIVER_NAME + " module can be unloaded when its device is opened with user space utilities")
	else:
		if( conditionConfirmed() ):
			Core.updateStatus(Core.WARN, "The " + DRIVER_NAME + " module may have been unloaded by user space utilities")
		else:
			Core.updateStatus(Core.ERROR, "Cannot find IPMI driver or device")

Core.printPatternResults()

