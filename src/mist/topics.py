topic_names = ["audits", "alarms", "device-updowns", "device-events", "mxedge-events"]

topics = [
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_CLAIMED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_UNCLAIMED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_ASSIGNED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_UNASSIGNED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_CONFIG_CHANGED_BY_RRM", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_CONFIG_CHANGED_BY_USER", "channel": "info"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_CONFIG_FAILED", "channel": "critical"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_CONFIGURED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_RECONFIGURED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_RRM_ACTION", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_BEACON_STUCK", "channel": "critical"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_RESTART_BY_USER", "channel": "info"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_RESTARTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_CONNECTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_DISCONNECTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_DISCONNECTED_LONG", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_UPGRADED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_UPGRADE_BY_SCHEDULE", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_UPGRADE_BY_USER", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_UPGRADE_FAILED", "channel": "critical"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_RADAR_DETECTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_CERT_REGENERATED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "access point", "name": "AP_GET_SUPPORT_FILES", "channel": "debug"},

    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_CLAIMED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_UNCLAIMED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_ASSIGNED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_UNASSIGNED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_ZTP_FINISHED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_CONFIG_CHANGED_BY_USER", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_RECONFIGURED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_CONFIGURED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_CONFIG_LOCK_FAILED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_CONFIG_FAILED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_PORT_UP", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_PORT_DOWN", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_CONNECTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_DISCONNECTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_DISCONNECTED_LONG", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_RESTARTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_RESTARTED_BY_USER", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_OSPF_NEIGHBOR_UP", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_OSPF_NEIGHBOR_DOWN", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_BGP_NEIGHBOR_STATE_CHANGED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_VPN_PATH_DOWN", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_VPN_PATH_UP", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_VPN_PEER_UP", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_VPN_PEER_DOWN", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_CERT_REGENERATED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_ALARM", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_UPGRADE_BY_USER", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_UPGRADED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_UPGRADE_PENDING", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_UPGRADE_FAILED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_CONDUCTOR_CONNECTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_ARP_RESOLVED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_ARP_UNRESOLVED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_DHCP_RESOLVED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_DHCP_UNRESOLVED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_HA_CONTROL_LINK_UP", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_HA_CONTROL_LINK_DOWN", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_HA_HEALTH_WEIGHT_LOW", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_HA_HEALTH_WEIGHT_RECOVERY", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_CONDUCTOR_DISCONNECTED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_SYSTEM_SERVICE_RESTART", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_REJECTED", "channel": "critical"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_RG_STATE_CHANGED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "wan edge", "name": "GW_PORT_RG_STATE_CHANGED", "channel": "info"}, 

    {"topic": "device-events", "sub_topic": "switch", "name": "SW_CLAIMED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_UNCLAIMED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_ASSIGNED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_UNASSIGNED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_ZTP_FINISHED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_CONFIG_CHANGED_BY_USER", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_RECONFIGURED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_CONFIGURED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_CONFIG_LOCK_FAILED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_CONFIG_FAILED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_PORT_UP", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_PORT_DOWN", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_CONNECTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_DISCONNECTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_RESTARTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_RESTART_BY_USER", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_OSPF_NEIGHBOR_UP", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_OSPF_NEIGHBOR_DOWN", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_BGP_NEIGHBOR_STATE_CHANGED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_ALARM", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_ALARM_CHASSIS_PARTITION", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_ALARM_CHASSIS_POE", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_ALARM_CHASSIS_PSU", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_UPGRADE_BY_USER", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_UPGRADED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_UPGRADE_PENDING", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_UPGRADE_FAILED", "channel": "critical"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_SYSTEM_SERVICE_RESTART", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_REJECTED", "channel": "critical"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_DYNAMIC_PORT_ASSIGNED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_PORT_BPDU_BLOCKED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_PORT_STORM_CONTROL", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_HANDSHAKE_ERROR", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_STP_TOPO_CHANGED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_VC_BACKUP_ELECTED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_VC_MASTER_CHANGED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_VC_MEMBER_ADDED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_VC_MEMBER_DELETED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_MASTER_ON_RECOVERY", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_MEMBER_ON_RECOVERY", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_RECOVERY_SNAPSHOT_REQUESTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_RECOVERY_SNAPSHOT_SUCCEEDED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_RECOVERY_SNAPSHOT_FAILED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_RECOVERY_SNAPSHOT_NOTNEEDED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_RECOVERY_SNAPSHOT_UNSUPPORTED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_DOT1X_USER_AUTHENTICATED", "channel": "debug"},
    {"topic": "device-events", "sub_topic": "switch", "name": "SW_RADIUS_SERVER_UNREACHABLE", "channel": "warning"},
{'topic': 'device-events', 'sub_topic': '', 'name': 'SW_ALARM_POE_CONTROLLER_UPGRADE_AVAILABLE', 'channel': ''},
{'topic': 'device-events', 'sub_topic': '', 'name': 'GW_RESTART_BY_USER', 'channel': ''},
{'topic': 'device-events', 'sub_topic': '', 'name': 'GW_ALARM_POE_CONTROLLER_UPGRADE_AVAILABLE', 'channel': ''},
{'topic': 'device-events', 'sub_topic': '', 'name': 'GW_PORT_RG_ST_CHANGED', 'channel': ''},
{'topic': 'device-events', 'sub_topic': '', 'name': 'GW_UPGRADE_BY_MIST', 'channel': ''},
{'topic': 'device-events', 'sub_topic': '', 'name': 'AP_RADIUS_ACCOUNTING_SERVER_CHANGE', 'channel': ''},
{'topic': 'device-events', 'sub_topic': '', 'name': 'AP_RADIUS_AUTHENTICATION_SERVER_CHANGE', 'channel': ''},
{'topic': 'device-events', 'sub_topic': '', 'name': 'AP_RADSEC_FAILURE', 'channel': ''},
{'topic': 'device-events', 'sub_topic': '', 'name': 'AP_RADSEC_SERVER_CHANGE', 'channel': ''},
{'topic': 'device-events', 'sub_topic': '', 'name': 'AP_RADSEC_RECOVERY', 'channel': ''},

    {"topic": "device-events", "sub_topic": "mist edge", "name": "ME_CLAIMED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "mist edge", "name": "ME_UNCLAIMED", "channel": "warning"},
    {"topic": "device-events", "sub_topic": "mist edge", "name": "ME_ASSIGNED", "channel": "info"},
    {"topic": "device-events", "sub_topic": "mist edge", "name": "ME_UNASSIGNED", "channel": "info"},


    {"topic": "device-updowns", "sub_topic": "access point", "name": "AP_CONNECTED", "channel": "info"},
    {"topic": "device-updowns", "sub_topic": "access point", "name": "AP_DISCONNECTED", "channel": "info"},
    {"topic": "device-updowns", "sub_topic": "access point", "name": "AP_RESTARTED", "channel": "info"},
    {"topic": "device-updowns", "sub_topic": "wan edge", "name": "GW_CONNECTED", "channel": "info"},
    {"topic": "device-updowns", "sub_topic": "wan edge", "name": "GW_DISCONNECTED", "channel": "info"},
    {"topic": "device-updowns", "sub_topic": "wan edge", "name": "GW_RESTARTED", "channel": "info"},
    {"topic": "device-updowns", "sub_topic": "switch", "name": "SW_CONNECTED", "channel": "info"},
    {"topic": "device-updowns", "sub_topic": "switch", "name": "SW_DISCONNECTED", "channel": "info"},
    {"topic": "device-updowns", "sub_topic": "switch", "name": "SW_RESTARTED", "channel": "info"},


    {"topic": "alarms", "sub_topic": "infrastructure", "name": "device_down", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "device_restarted", "channel": "info"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "switch_down", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "switch_restarted", "channel": "info"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "gateway_down", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "gateway_restarted", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "device_reconnected", "channel": "info"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "switch_reconnected", "channel": "info"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "gateway_reconnected", "channel": "info"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "vpn_peer_down", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "vc_master_changed", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "vc_backup_failed", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "vc_member_added", "channel": "info"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "vc_member_deleted", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "sw_alarm_chassis_poe", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "sw_alarm_chassis_pem", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "sw_alarm_chassis_psu", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "sw_alarm_chassis_partition", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "sw_dhcp_pool_exhausted", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "gw_dhcp_pool_exhausted", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "sw_bgp_neighbor_state_changed", "channel": "info"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "sw_bad_optics", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "infrastructure", "name": "sw_bpdu_error", "channel": "warning"},
{'topic': 'alarms', 'sub_topic': 'infrastructure', 'name': 'loop_detected_by_ap', 'channel': 'warning'},
{'topic': 'alarms', 'sub_topic': 'infrastructure', 'name': 'infra_dhcp_failure', 'channel': 'critical'},
{'topic': 'alarms', 'sub_topic': 'infrastructure', 'name': 'infra_dhcp_success', 'channel': 'info'},
{'topic': 'alarms', 'sub_topic': 'infrastructure', 'name': 'infra_dns_failure', 'channel': 'critical'},
{'topic': 'alarms', 'sub_topic': 'infrastructure', 'name': 'infra_dns_success', 'channel': 'info'},
{'topic': 'alarms', 'sub_topic': 'infrastructure', 'name': 'infra_arp_failure', 'channel': 'critical'},
{'topic': 'alarms', 'sub_topic': 'infrastructure', 'name': 'infra_arp_success', 'channel': 'info'},

    {"topic": "alarms", "sub_topic": "security", "name": "secpolicy_violation", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "bssid_spoofing", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "security", "name": "honeypot_ssid", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "security", "name": "adhoc_network", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "rogue_ap", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "security", "name": "rogue_client", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "security", "name": "watched_station", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "eap_handshake_flood", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "air_magnet_scan", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "excessive_eapol_start", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "eapol_logoff_attack", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "eap_dictionary_attack", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "disassociation_flood", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "beacon_flood", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "essid_jack", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "krack_attack", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "vendor_ie_missing", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "tkip_icv_attack", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "repeated_auth_failures", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "eap_failure_injection", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "eap_spoofed_success", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "out_of_sequence", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "zero_ssid_association", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "monkey_jack", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "excessive_client", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "security", "name": "ssid_injection", "channel": "warning"},

    {"topic": "alarms", "sub_topic": "marvis", "name": "missing_vlan", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "bad_cable", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "port_flap", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "gw_bad_cable", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "authentication_failure", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "dhcp_failure", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "arp_failure", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "dns_failure", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "negotiation_mismatch", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "gw_negotiation_mismatch", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "ap_offline", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "non_compliant", "channel": "warning"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "ap_bad_cable", "channel": "critical"},
    {"topic": "alarms", "sub_topic": "marvis", "name": "health_check_failed", "channel": "warning"},
{'topic': 'alarms', 'sub_topic': 'marvis', 'name': 'bad_wan_uplink', 'channel': 'critical'},
{'topic': 'alarms', 'sub_topic': 'marvis', 'name': 'switch_stp_loop', 'channel': 'critical'},
{'topic': 'alarms', 'sub_topic': 'marvis', 'name': 'insufficient_coverage', 'channel': 'critical'},
{'topic': 'alarms', 'sub_topic': 'marvis', 'name': 'insufficient_capacity', 'channel': 'critical'},


    {"topic": "audits", "sub_topic": "", "name": "approved_admins", "channel": "debug"},
    {"topic": "audits", "sub_topic": "", "name": "other_admins", "channel": "critical"},


    {"topic": "mxedge-events", "sub_topic": "config", "name": "ME_CONFIG_CHANGED_BY_USER", "channel": "info"},
    {"topic": "mxedge-events", "sub_topic": "service", "name": "ME_SERVICE_STOPPED", "channel": "debug"},
    {"topic": "mxedge-events", "sub_topic": "service", "name": "ME_SERVICE_STARTED", "channel": "debug"},
    {"topic": "mxedge-events", "sub_topic": "service", "name": "ME_SERVICE_RESTARTED", "channel": "debug"},
    {"topic": "mxedge-events", "sub_topic": "service", "name": "ME_SERVICE_FAILED", "channel": "critical"},
    {"topic": "mxedge-events", "sub_topic": "tunterm", "name": "TT_TUNNELS_LOST", "channel": "warning"},
    {"topic": "mxedge-events", "sub_topic": "package", "name": "ME_PACKAGE_INSTALLED", "channel": "info"},
    {"topic": "mxedge-events", "sub_topic": "package", "name": "ME_PACKAGE_UPDATE_BY_USER", "channel": "info"},
    {"topic": "mxedge-events", "sub_topic": "", "name": "ME_RESTARTED", "channel": "info"},
    {"topic": "mxedge-events", "sub_topic": "", "name": "ME_RESOURCE_USAGE", "channel": "warning"},
{'topic': 'mxedge-events', 'sub_topic': 'config', 'name': 'ME_CONFIGURED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'connectivity', 'name': 'ME_CONNECTED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'connectivity', 'name': 'ME_DISCONNECTED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'service', 'name': 'ME_RESTART_BY_USER', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'package', 'name': 'ME_PACKAGE_INSTALL_FAILED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'package', 'name': 'ME_PACKAGE_UNINSTALLED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'package', 'name': 'ME_PACKAGE_UNINSTALL_FAILED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'package', 'name': 'ME_PACKAGE_UPDATED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'package', 'name': 'ME_PACKAGE_UPDATE_FAILED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'service', 'name': 'ME_SERVICE_CRASHED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_PORTS_BOUNCE_BY_USER', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_PORTS_BOUNCED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_PORTS_BOUNCE_FAILED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_AP_DISCONNECT_BY_USER', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_AP_DISCONNECTED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_AP_DISCONNECT_FAILED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'hardware', 'name': 'ME_FAN_PLUGGED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'hardware', 'name': 'ME_FAN_UNPLUGGED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'hardware', 'name': 'ME_PSU_PLUGGED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'hardware', 'name': 'ME_PSU_UNPLUGGED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'hardware', 'name': 'ME_POWERINPUT_CONNECTED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'hardware', 'name': 'ME_POWERINPUT_DISCONNECTED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_PORT_BLOCKED', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_PORT_RECOVERY', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_PORT_LINK_DOWN', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_PORT_LINK_RECOVERY', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_PORT_DROPPED_FROM_LACP', 'channel': ''},
{'topic': 'mxedge-events', 'sub_topic': 'tunterm', 'name': 'TT_PORT_JOINED_LACP', 'channel': ''}
]