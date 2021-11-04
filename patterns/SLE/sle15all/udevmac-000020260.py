#!/usr/bin/python3
#
# Title:       Pattern for TID000020260
# Description: systemd-udevd Could not generate persistent MAC address for br0 No such file or directory
# Source:      Basic Python Pattern Template v0.3.4
# Options:     SLE,Network,MAC,udevmac,000020260,1185357,1,0,0
# Modified:    2021 Jun 02
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

META_CLASS = "SLE"
META_CATEGORY = "Network"
META_COMPONENT = "MAC"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020260|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1185357"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

MACMSGS = {}

##############################################################################
# Local Function Definitions
##############################################################################

def getMacMessages():
	fileOpen = "boot.txt"
	section = "bin/journalctl --no-pager --boot"
	content = []
	FOUND = {}
	CONFIRMED = re.compile("systemd-udevd.*Could not generate persistent MAC address for.*No such file or directory", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					FOUND[line.split(':')[-2].split()[-1]] = True
	return FOUND

def bbIface(CHK_IFACE):
	fileOpen = "network.txt"
	section = "ethtool -i " + CHK_IFACE
	content = []
	FOUND = {}
	CONFIRMED = re.compile("driver:.*bridge|driver:.*bonding", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

MACMSGS = getMacMessages()
AFFECTED = []
for IFACE in list(MACMSGS.keys()):
	if( bbIface(IFACE) ):
		AFFECTED.append(IFACE)

if( AFFECTED ):
	Core.updateStatus(Core.REC, "Detected warning message(s) for: " + ' '.join(AFFECTED))
else:
	Core.updateStatus(Core.IGNORE, "Interface not bridged or bonded")

Core.printPatternResults()

