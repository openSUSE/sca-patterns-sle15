#!/usr/bin/python3
#
# Title:       Pattern for TID000020653
# Description: NFS mount attempt with vers=n returns invalid argument or incorrect mount option
# Source:      Basic Python Pattern Template v1.0.0
# Options:     SLE,NFS,Client,nfsvers,000020653,1178947,2,1,0
# Modified:    2022 May 20
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

import re
import os
import Core
import SUSE

META_CLASS = "SLE"
META_CATEGORY = "NFS"
META_COMPONENT = "Client"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020653|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1178947"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def nfsversConfig():
	fileOpen = "etc.txt"
	section = "/etc/nfsmount.conf"
	content = []
	CONFIRMED = re.compile("^nfsvers.*=", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					return True
	return False

def errorFound():
	fileOpen = "boot.txt"
	section = "dmesg -T"
	content = []
	CONFIRMED = re.compile("NFS.*mount option vers=3 does not support minorversion=1", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

PACKAGE = "nfs-client"

if( SUSE.packageInstalled(PACKAGE) ):
	if( nfsversConfig() ):
		if( errorFound() ):
			Core.updateStatus(Core.CRIT, "NFS mounts have failed due to nfsvers configuration")
		else:
			Core.updateStatus(Core.WARN, "NFS mount risk from nfsvers configuration")
	else:
		Core.updateStatus(Core.ERROR, "nfsvers not configured in nfsmount.conf")
else:
	Core.updateStatus(Core.ERROR, "ERROR: RPM package " + PACKAGE + " not installed")

Core.printPatternResults()

