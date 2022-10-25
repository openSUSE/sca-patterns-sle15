#!/usr/bin/python3
#
# Title:       SSSD Authentication with AD fails with a MEMORY:/etc/krb5.keytab error
# Description: Pattern for TID000020793
# Template:    SCA Tool Python Pattern Generator v1.0.3
# Modified:    2022 Oct 06
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

meta_class = "SLE"
meta_category = "SSSD"
meta_component = "Authentication"
pattern_id = os.path.basename(__file__)
primary_link = "META_LINK_TID"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020793"
Core.init(meta_class, meta_category, meta_component, pattern_id, primary_link, overall, overall_info, other_links)

##############################################################################
# Local Function Definitions
##############################################################################

def packages_installed(package_list):
	file_open = "rpm.txt"
	section = "rpm.*-35{NAME}"
	content = []
	found = 0
	required = len(package_list)
	confirmed = re.compile("", re.IGNORECASE)
	if Core.isFileActive(file_open):
		if Core.getRegExSection(file_open, section, content):
			for line in content:
				chk_package = line.split()[0]
				if chk_package in package_list:
					found += 1
#	print(found, required)
	if found < required:
		return False
	else:
		return True

def nsswitch_configured():
	file_open = "etc.txt"
	section = "/etc/nsswitch.conf"
	content = []
	found = 0
	required = 2
	confirmed = re.compile("passwd:.*compat.*sss|group:.*compat.*sss", re.IGNORECASE)
	if Core.isFileActive(file_open):
		if Core.getRegExSection(file_open, section, content):
			for line in content:
				if confirmed.search(line):
					# if passwd or group is configured twice, without the other; nsswitch_configured will return true, even though it's not actually configured. 
					found += 1
#	print(found, required)
	if found < required:
		return False
	else:
		return True

def kerberos_configured():
	file_open = "etc.txt"
	section = "/etc/krb5.conf"
	content = []
	found = {}
	required = 3
	config_section = ''
	confirmed = re.compile("default_realm.*=.*[a-zA-Z0-9]|default_ccache_name.*=.*[a-zA-Z0-9]|admin_server.*=.*[a-zA-Z0-9]", re.IGNORECASE)
	if Core.isFileActive(file_open):
		if Core.getRegExSection(file_open, section, content):
			for line in content:
				if line.startswith("["):
					config_section = line.strip('[').strip(']')
				else:
					if confirmed.search(line):
						option = line.split()[0].strip()
						if option == 'default_realm' and config_section == 'libdefaults':
							found[option] = True
						elif option == 'default_ccache_name' and config_section == 'libdefaults':
							found[option] = True
						elif option == 'admin_server' and config_section == 'realms':
							found[option] = True
	configured = len(found.keys())
#	print(found, configured, required)
	if configured < required:
		return False
	else:
		return True

def sssd_configured():
	file_open = "etc.txt"
	section = "/etc/sssd/sssd.conf"
	content = []
	found = {}
	required = 8
	regexstr = "services.*=.*[a-zA-z0-9]|domains.*=.*[a-zA-z0-9]|id_provider.*=.*ad|auth_provider.*=.*ad|ldap_schema.*=.*ad|ad_domain.*=.*[a-zA-z0-9]|ldap_id_mapping.*=.*true|ldap_referrals.*=.*false"
	confirmed = re.compile(regexstr, re.IGNORECASE)
	if Core.isFileActive(file_open):
		if Core.getRegExSection(file_open, section, content):
			for line in content:
				if line.startswith("["):
					config_section = line.strip('[').strip(']')
				else:
					if confirmed.search(line):
						option = line.split()[0].strip()
						if option == 'services' and config_section == 'sssd':
							found[option] = True
						elif option == 'domains' and config_section == 'sssd':
							found[option] = True
						elif option == 'auth_provider' and config_section.startswith('domain/'):
							found[option] = True
						elif option == 'id_provider' and config_section.startswith('domain/'):
							found[option] = True
						elif option == 'ldap_schema' and config_section.startswith('domain/'):
							found[option] = True
						elif option == 'ad_domain' and config_section.startswith('domain/'):
							found[option] = True
						elif option == 'ldap_id_mapping' and config_section.startswith('domain/'):
							found[option] = True
						elif option == 'ldap_referrals' and config_section.startswith('domain/'):	
							found[option] = True
	configured = len(found.keys())
#	print(found, configured, required)
	if configured < required:
		return False
	else:
		return True

def errors_found():
	file_open = "sssd.txt"
	section = "/ldap_child.log"
	content = []
	confirmed = re.compile("Failed to init credentials:.*Client", re.IGNORECASE)
	if Core.isFileActive(file_open):
		if Core.getRegExSection(file_open, section, content):
			for line in content:
				if confirmed.search(line):
					return True
	return False

##############################################################################
# Main
##############################################################################

package_list = ['krb5-client', 'adcli', 'sssd', 'sssd-ldap', 'sssd-ad', 'sssd-tools']
sssd_service_name = 'sssd.service'
time_service_name = 'chronyd.service' # SLES15+
#time_service_name = 'ntpd.service' # SLES12+

if( packages_installed(package_list) ):
	sssd_service = SUSE.getServiceDInfo(sssd_service_name)
	time_service = SUSE.getServiceDInfo(time_service_name)
	if( sssd_service ):
		if( sssd_service['UnitFileState'] != 'enabled' ):
			Core.updateStatus(Core.ERROR, "Service is disabled: " + str(sssd_service_name))
		elif( sssd_service['ActiveState'] != 'active' ):
			Core.updateStatus(Core.ERROR, "Service is not active: " + str(sssd_service_name))
	else:
		Core.updateStatus(Core.ERROR, "Service details not found: " + str(sssd_service_name))
	if( time_service ):
		if( time_service['UnitFileState'] != 'enabled' ):
			Core.updateStatus(Core.ERROR, "Service is disabled: " + str(time_service_name))
		elif( time_service['ActiveState'] != 'active' ):
			Core.updateStatus(Core.ERROR, "Service is not active: " + str(time_service_name))
	else:
		Core.updateStatus(Core.ERROR, "Service details not found: " + str(time_service_name))

	if( nsswitch_configured() ):
		if( kerberos_configured() ):
			if( sssd_configured() ):
				if( errors_found() ):
						Core.updateStatus(Core.CRIT, "Detected possible SSSD authentication with AD issue")
				else:
						Core.updateStatus(Core.IGNORE, "SSSD authentication with AD seems fine")
			else:
				Core.updateStatus(Core.ERROR, "SSSD is not configured for AD")
		else:
			Core.updateStatus(Core.ERROR, "Kerberos client is not configured for AD")
	else:
		Core.updateStatus(Core.ERROR, "The name service switch is not configured for SSSD")
else:
	Core.updateStatus(Core.ERROR, "ERROR: Missing required packages for SSSD authentication with AD")

Core.printPatternResults()
