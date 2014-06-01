#include "includes.h"
 
#ifndef WPA_CTRL_H
#define WPA_CTRL_H
 
#ifdef  __cplusplus
extern "C" {
#endif

/* wpa_supplicant control interface - fixed message prefixes */

#define WPA_CTRL_REQ "CTRL-REQ-"
 
#define WPA_CTRL_RSP "CTRL-RSP-"
 
/* Event messages with fixed prefix */
#define WPA_EVENT_CONNECTED "CTRL-EVENT-CONNECTED "
 
#define WPA_EVENT_DISCONNECTED "CTRL-EVENT-DISCONNECTED "
 
#define WPA_EVENT_ASSOC_REJECT "CTRL-EVENT-ASSOC-REJECT "
 
#define WPA_EVENT_TERMINATING "CTRL-EVENT-TERMINATING "
 
#define WPA_EVENT_PASSWORD_CHANGED "CTRL-EVENT-PASSWORD-CHANGED "
 
#define WPA_EVENT_EAP_NOTIFICATION "CTRL-EVENT-EAP-NOTIFICATION "
 
#define WPA_EVENT_EAP_STARTED "CTRL-EVENT-EAP-STARTED "
 
#define WPA_EVENT_EAP_PROPOSED_METHOD "CTRL-EVENT-EAP-PROPOSED-METHOD "
 
#define WPA_EVENT_EAP_METHOD "CTRL-EVENT-EAP-METHOD "
 
#define WPA_EVENT_EAP_PEER_CERT "CTRL-EVENT-EAP-PEER-CERT "
 
#define WPA_EVENT_EAP_TLS_CERT_ERROR "CTRL-EVENT-EAP-TLS-CERT-ERROR "
 
#define WPA_EVENT_EAP_SUCCESS "CTRL-EVENT-EAP-SUCCESS "
 
#define WPA_EVENT_EAP_FAILURE "CTRL-EVENT-EAP-FAILURE "
 
#define WPA_EVENT_SCAN_RESULTS "CTRL-EVENT-SCAN-RESULTS "
 
#define WPA_EVENT_STATE_CHANGE "CTRL-EVENT-STATE-CHANGE "
 
#define WPA_EVENT_BSS_ADDED "CTRL-EVENT-BSS-ADDED "
 
#define WPA_EVENT_BSS_REMOVED "CTRL-EVENT-BSS-REMOVED "
 
#define WPS_EVENT_OVERLAP "WPS-OVERLAP-DETECTED "
 
#define WPS_EVENT_AP_AVAILABLE_PBC "WPS-AP-AVAILABLE-PBC "
 
#define WPS_EVENT_AP_AVAILABLE_AUTH "WPS-AP-AVAILABLE-AUTH "
 
#define WPS_EVENT_AP_AVAILABLE_PIN "WPS-AP-AVAILABLE-PIN "
 
#define WPS_EVENT_AP_AVAILABLE "WPS-AP-AVAILABLE "
 
#define WPS_EVENT_CRED_RECEIVED "WPS-CRED-RECEIVED "
 
#define WPS_EVENT_M2D "WPS-M2D "
 
#define WPS_EVENT_FAIL "WPS-FAIL "
 
#define WPS_EVENT_SUCCESS "WPS-SUCCESS "
 
#define WPS_EVENT_TIMEOUT "WPS-TIMEOUT "
 
#define WPS_EVENT_ENROLLEE_SEEN "WPS-ENROLLEE-SEEN "
 
#define WPS_EVENT_OPEN_NETWORK "WPS-OPEN-NETWORK "
 
/* WPS ER events */
#define WPS_EVENT_ER_AP_ADD "WPS-ER-AP-ADD "
#define WPS_EVENT_ER_AP_REMOVE "WPS-ER-AP-REMOVE "
#define WPS_EVENT_ER_ENROLLEE_ADD "WPS-ER-ENROLLEE-ADD "
#define WPS_EVENT_ER_ENROLLEE_REMOVE "WPS-ER-ENROLLEE-REMOVE "
#define WPS_EVENT_ER_AP_SETTINGS "WPS-ER-AP-SETTINGS "
#define WPS_EVENT_ER_SET_SEL_REG "WPS-ER-AP-SET-SEL-REG "
 
#define P2P_EVENT_DEVICE_FOUND "P2P-DEVICE-FOUND "
 
#define P2P_EVENT_DEVICE_LOST "P2P-DEVICE-LOST "
 
#define P2P_EVENT_GO_NEG_REQUEST "P2P-GO-NEG-REQUEST "
#define P2P_EVENT_GO_NEG_SUCCESS "P2P-GO-NEG-SUCCESS "
#define P2P_EVENT_GO_NEG_FAILURE "P2P-GO-NEG-FAILURE "
#define P2P_EVENT_GROUP_FORMATION_SUCCESS "P2P-GROUP-FORMATION-SUCCESS "
#define P2P_EVENT_GROUP_FORMATION_FAILURE "P2P-GROUP-FORMATION-FAILURE "
#define P2P_EVENT_GROUP_STARTED "P2P-GROUP-STARTED "
#define P2P_EVENT_GROUP_REMOVED "P2P-GROUP-REMOVED "
#define P2P_EVENT_CROSS_CONNECT_ENABLE "P2P-CROSS-CONNECT-ENABLE "
#define P2P_EVENT_CROSS_CONNECT_DISABLE "P2P-CROSS-CONNECT-DISABLE "
/* parameters: <peer address> <PIN> */
#define P2P_EVENT_PROV_DISC_SHOW_PIN "P2P-PROV-DISC-SHOW-PIN "
/* parameters: <peer address> */
#define P2P_EVENT_PROV_DISC_ENTER_PIN "P2P-PROV-DISC-ENTER-PIN "
/* parameters: <peer address> */
#define P2P_EVENT_PROV_DISC_PBC_REQ "P2P-PROV-DISC-PBC-REQ "
/* parameters: <peer address> */
#define P2P_EVENT_PROV_DISC_PBC_RESP "P2P-PROV-DISC-PBC-RESP "
/* parameters: <peer address> <status> */
#define P2P_EVENT_PROV_DISC_FAILURE "P2P-PROV-DISC-FAILURE"
/* parameters: <freq> <src addr> <dialog token> <update indicator> <TLVs> */
#define P2P_EVENT_SERV_DISC_REQ "P2P-SERV-DISC-REQ "
/* parameters: <src addr> <update indicator> <TLVs> */
#define P2P_EVENT_SERV_DISC_RESP "P2P-SERV-DISC-RESP "
#define P2P_EVENT_INVITATION_RECEIVED "P2P-INVITATION-RECEIVED "
#define P2P_EVENT_INVITATION_RESULT "P2P-INVITATION-RESULT "
#define P2P_EVENT_FIND_STOPPED "P2P-FIND-STOPPED "
 
#define INTERWORKING_AP "INTERWORKING-AP "
#define INTERWORKING_NO_MATCH "INTERWORKING-NO-MATCH "
 
/* hostapd control interface - fixed message prefixes */
#define WPS_EVENT_PIN_NEEDED "WPS-PIN-NEEDED "
#define WPS_EVENT_NEW_AP_SETTINGS "WPS-NEW-AP-SETTINGS "
#define WPS_EVENT_REG_SUCCESS "WPS-REG-SUCCESS "
#define WPS_EVENT_AP_SETUP_LOCKED "WPS-AP-SETUP-LOCKED "
#define WPS_EVENT_AP_SETUP_UNLOCKED "WPS-AP-SETUP-UNLOCKED "
#define WPS_EVENT_AP_PIN_ENABLED "WPS-AP-PIN-ENABLED "
#define WPS_EVENT_AP_PIN_DISABLED "WPS-AP-PIN-DISABLED "
#define AP_STA_CONNECTED "AP-STA-CONNECTED "
#define AP_STA_DISCONNECTED "AP-STA-DISCONNECTED "
 
 
/* BSS command information masks */
 
#define WPA_BSS_MASK_ALL                0xFFFFFFFF
#define WPA_BSS_MASK_ID                 BIT(0)
#define WPA_BSS_MASK_BSSID              BIT(1)
#define WPA_BSS_MASK_FREQ               BIT(2)
#define WPA_BSS_MASK_BEACON_INT         BIT(3)
#define WPA_BSS_MASK_CAPABILITIES       BIT(4)
#define WPA_BSS_MASK_QUAL               BIT(5)
#define WPA_BSS_MASK_NOISE              BIT(6)
#define WPA_BSS_MASK_LEVEL              BIT(7)
#define WPA_BSS_MASK_TSF                BIT(8)
#define WPA_BSS_MASK_AGE                BIT(9)
#define WPA_BSS_MASK_IE                 BIT(10)
#define WPA_BSS_MASK_FLAGS              BIT(11)
#define WPA_BSS_MASK_SSID               BIT(12)
#define WPA_BSS_MASK_WPS_SCAN           BIT(13)
#define WPA_BSS_MASK_P2P_SCAN           BIT(14)
#define WPA_BSS_MASK_INTERNETW          BIT(15)
 
 
/* wpa_supplicant/hostapd control interface access */
 
struct wpa_ctrl * wpa_ctrl_open(const char *ctrl_path);
 
 
void wpa_ctrl_close(struct wpa_ctrl *ctrl);
 
 
int wpa_ctrl_request(struct wpa_ctrl *ctrl, const char *cmd, size_t cmd_len,
                     char *reply, size_t *reply_len,
                     void (*msg_cb)(char *msg, size_t len));
 
 
int wpa_ctrl_attach(struct wpa_ctrl *ctrl);
 
 
int wpa_ctrl_detach(struct wpa_ctrl *ctrl);
 
 
int wpa_ctrl_recv(struct wpa_ctrl *ctrl, char *reply, size_t *reply_len);
 
 
int wpa_ctrl_pending(struct wpa_ctrl *ctrl);
 
 
int wpa_ctrl_get_fd(struct wpa_ctrl *ctrl);
 
#ifdef ANDROID
 
void wpa_ctrl_cleanup(void);
#endif /* ANDROID */
 
#ifdef CONFIG_CTRL_IFACE_UDP
#define WPA_CTRL_IFACE_PORT 9877
#define WPA_GLOBAL_CTRL_IFACE_PORT 9878
#endif /* CONFIG_CTRL_IFACE_UDP */
 
 
#ifdef  __cplusplus
}
#endif
 
#endif /* WPA_CTRL_H */

