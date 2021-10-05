#!/usr/bin/python3
#
# Title:       Pattern for TID000020295
# Description: DASD partitions not recognized on SLES 15 SP3 KVM guest
# Source:      Kernel Package Version Pattern Template v0.1.2
# Options:     SLE,Kernel,DASD,dasdkvm,000020295,1185857,5.3.18-59.5.2,0,1
# Modified:    2021 Jun 28
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
META_COMPONENT = "DASD"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020295|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1185857"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def kvm():
	fileOpen = "systemd.txt"
	section = "hostnamectl status"
	content = []
	CONFIRMED = re.compile("Virtualization.*kvm", re.IGNORECASE)
	if( Core.isFileActive(fileOpen) ):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					return True
	else:
		Core.updateStatus(Core.ERROR, "ERROR: File not found - " + fileOpen)

	return False

def partitionlessVirtio():
	fileOpen = "fs-diskio.txt"
	section = "/proc/partitions"
	content = []
	IDX_LAST = -1
	disks = {}
	virtdisk = ''
	DISKRE = re.compile(" vd[a-z]*$", re.IGNORECASE)
	if( Core.isFileActive(fileOpen) ):
		if Core.getRegExSection(fileOpen, section, content):
			# get the disks without their partition
			for line in content:
				if( len(virtdisk) > 0 ):
					if re.search(virtdisk + "[0-9]", line):
						del disks[virtdisk]
					virtdisk = ''
				elif DISKRE.search(line):
					virtdisk = line.split()[IDX_LAST]
					disks[virtdisk] = True
				else:
					virtdisk = ''
	else:
		Core.updateStatus(Core.ERROR, "ERROR: File not found - " + fileOpen)

	return disks

##############################################################################
# Main Program Execution
##############################################################################

KERNEL_VERSION_FIXED = '5.3.18-59.5.2'
SERVER = SUSE.getHostInfo()

if( 's390' in SERVER['Architecture'].lower() ):
	INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION_FIXED)
	if( INSTALLED_VERSION >= 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied in kernel version " + KERNEL_VERSION_FIXED + " or higher")
	else:
		if( kvm() ):
			partitionless_devices = partitionlessVirtio()
			if( len(partitionless_devices) > 0 ):
				Core.updateStatus(Core.WARN, "Evaluate for possible partitionless DASD devices: " + ' '.join(list(partitionless_devices.keys())))
			else:
				Core.updateStatus(Core.IGNORE, "All virtio disks have partitions")
		else:
			Core.updateStatus(Core.ERROR, "ERROR: KVM virtualization not found")
else:
	Core.updateStatus(Core.ERROR, "ERROR: s390 type system architectures not found")

Core.printPatternResults()

