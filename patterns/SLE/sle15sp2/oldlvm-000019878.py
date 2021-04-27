#!/usr/bin/python
#
# Title:       Pattern for TID000019878
# Description: Physical Volume is using an old PV header
# Source:      Basic Python Pattern Template v0.3.4
# Options:     SLE,LVM,Metadata,oldlvm,000019878,1179170,1,1,0
# Distros:     SLES15 SP2 and SP3
# Modified:    2021 Apr 27
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
META_CATEGORY = "LVM"
META_COMPONENT = "Metadata"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019878|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1179170"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def oldMetadata():
	global OLD_DEVS
	fileOpen = "lvm.txt"
	section = "/sbin/pvs"
	content = []
	DEVICE_NAME = 2
	CONFIRMED = re.compile("WARNING.*PV.*in VG.*is using an old PV header", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					OLD_DEVS[line.split()[DEVICE_NAME]] = True

	if( len(OLD_DEVS) > 0 ):
		return True
	else:
		return False

##############################################################################
# Main Program Execution
##############################################################################

OLD_DEVS = {}

if( oldMetadata() ):
	Core.updateStatus(Core.WARN, "Detected LVM PV devices with old metadata: " + ' '.join(OLD_DEVS.keys()))
else:
	Core.updateStatus(Core.IGNORE, "No outdated LVM PV metadata found")

Core.printPatternResults()

