#!/usr/bin/python
#
# Title:       Pattern for TID000019688
# Description: dmesg shows NFIT related messages after updating the kernel
# Source:      Basic Python Pattern Template v0.3.4
# Options:     SLE,Kernel,nfit,nfit,000019688,1159356,1,0,0
# Distro:      SLES15 SP1
# Modified:    2021 May 12
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
META_COMPONENT = "nfit"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019688|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1159356"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def symbolErrors():
	fileOpen = "boot.txt"
	section = "/dmesg"
	content = []
	CONFIRMED = re.compile("nfit:.*Unknown symbol nvdimm_blk_region_create|nfit:.*Unknown symbol nvdimm_region_notify|nfit:.*Unknown symbol to_nvdimm_bus", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

DRIVER_NAME = 'nfit'
DRIVER_INFO = SUSE.getDriverInfo(DRIVER_NAME)
if( DRIVER_INFO['loaded'] ):
	if( symbolErrors() ):
		Core.updateStatus(Core.WARN, "Detected nfit symbol errors nvdimm_blk_region, nvdimm_region_notify or to_nvdimm_buss, review work around or upgrade")
	else:
		Core.updateStatus(Core.IGNORE, "No nfit symbol errors found")
else:
	Core.updateStatus(Core.ERROR, "ERROR: Driver not loaded - " + DRIVER_NAME)


Core.printPatternResults()

