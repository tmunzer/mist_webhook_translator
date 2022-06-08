from cryptography.fernet import Fernet
from mist.topics import topic_names
import json
import secrets
from mwtt import Console

console = Console("model_orgSettings")


class OrgSettings():

    def __init__(self, key, db) -> None:
        self.enable_wh_secret = True
        self.topics = topic_names
        self.fernet = Fernet(key)
        self.db = db


    def _encode(self, clear_data: object) -> str:
        str_data = json.dumps(clear_data)
        return self.fernet.encrypt(str_data.encode())

    def _decode(self, encrypted_data: str) -> object:
        if "encrypted_data" in encrypted_data:
            decrypted_data = self.fernet.decrypt(encrypted_data["encrypted_data"]).decode()
        else:
            decrypted_data = self.fernet.decrypt(encrypted_data).decode()
        return json.loads(decrypted_data)


    def _validate(self, host: str, org_id: str, data: object) -> object:
        secured_data = {
            "topics_status": {},
            "topics": {},
            "slack_settings": {"enabled": False, "url": {}},
            "teams_settings": {"enabled": False, "url": {}},
            "mist_settings": {"mist_host": "", "mist_secret": "", "approved_admins": []}
        }

        if type(data.get("topics_status") is dict):
            for entry in data["topics_status"]:
                if entry in topic_names and type(data["topics_status"][entry]) is bool:
                    secured_data["topics_status"][entry] = data["topics_status"][entry]

        if type(data.get("topics")) is list:
            for entry in data["topics"]:
                if type(entry.get("topic")) is str \
                        and type(entry.get("topic")) is str \
                        and type(entry.get("name")) is str \
                        and type(entry.get("channel")) is str \
                        and entry["topic"] in topic_names:
                    if not entry["topic"] in secured_data["topics"]:
                        secured_data["topics"][entry["topic"]] = {}
                    secured_data["topics"][entry["topic"]
                                           ][entry["name"]] = entry["channel"]

        if type(data.get("slack_settings")) is dict:
            if type(data["slack_settings"].get("enabled")) is bool:
                secured_data["slack_settings"]["enabled"] = data["slack_settings"]["enabled"]
            if type(data["slack_settings"].get("url")) is dict:
                for channel in data["slack_settings"]["url"]:
                    if type(data["slack_settings"]["url"][channel]) is str:
                        secured_data["slack_settings"]["url"][channel] = data["slack_settings"]["url"][channel]

        if type(data.get("teams_settings")) is dict:
            if type(data["teams_settings"].get("enabled")) is bool:
                secured_data["teams_settings"]["enabled"] = data["teams_settings"]["enabled"]
            if type(data["teams_settings"].get("url")) is dict:
                for channel in data["teams_settings"]["url"]:
                    if type(data["teams_settings"]["url"][channel]) is str:
                        secured_data["teams_settings"]["url"][channel] = data["teams_settings"]["url"][channel]

        if (type(data.get("mist_settings"))) is dict:
            if type(data["mist_settings"].get("approved_admins")) is list:
                for admin in data["mist_settings"]["approved_admins"]:
                    if type(admin) is str:
                        secured_data["mist_settings"]["approved_admins"].append(
                            admin)

        secured_data["mist_settings"]["mist_host"] = host
        secured_data["org_id"] = org_id
        console.debug(f"received data cleaned for org {org_id}")
        return secured_data


    def get(self, org_id: str) -> object:
        try:
            data_from_db = self.db.find_one({"org_id": org_id})
            if data_from_db:
                return self._decode(data_from_db)
        except:
            console.error(f"Unable to retrive data for the org {org_id}")
        return None

    def save(self, host: str, org_id: str, data: object):
        secured_data = self._validate(host, org_id, data)
        decoded_data_from_db = self.get(org_id)
        if not decoded_data_from_db:
            try:
                encrypted_data = self._encode(secured_data)
                res = self.db.insert_one(
                    {"org_id": org_id, "encrypted_data": encrypted_data})
                console.info(f"New org {org_id} created")
                return "", 200
            except:
                console.error(f"Unable to create new org {org_id}")
                return "Error when saving data", 500
        else:
            try:
                secured_data["mist_settings"]["mist_secret"] = decoded_data_from_db["mist_settings"]["mist_secret"]
                encrypted_data = self._encode(secured_data)
                res = self.db.update(
                    {"org_id": decoded_data_from_db["org_id"]}, {"$set": {"encrypted_data": encrypted_data}})
                if res["ok"] == 1:
                    console.info(f"data updated for org {org_id}")
                    return "", 200
                else:
                    console.error(f"unable to update data for org {org_id}")
                    return "", 500
            except:
                console.error(f"Error when saving data for org {org_id}")
                return "Error when saving data", 500

    def get_webhook_secret(self, org_id: str):
        decoded_data_from_db = self.get(org_id)

        if not decoded_data_from_db:
            console.error(
                f"Unable to find the settings in the DB for org {org_id}")
            return "Unable to find the settings in the DB", 500, None
        elif decoded_data_from_db["mist_settings"].get("mist_secret"):
            console.debug(
                f"Settings data retrieved from DB for org {org_id}. Secret already set.")
            secret = decoded_data_from_db["mist_settings"]["mist_secret"]
        else:
            console.debug(
                f"Settings data retrieved from DB for org {org_id}. Secret not set yet.")
            try:
                if self.enable_wh_secret:
                    secret = secrets.token_urlsafe()
                else:
                    secret = ""
                decoded_data_from_db["mist_settings"]["mist_secret"] = secret
                encoded_data = self._encode(decoded_data_from_db)
                res = self.db.update(
                    {"org_id": org_id},
                    {"$set": {"encrypted_data": encoded_data}}
                )
                if res["ok"] != 1:
                    console.error(
                        f"Unable to save the webhook secret in the DB for org {org_id}")
                    return "", 500, None
                else:
                    console.debug(
                        f"webhook secret saved in the DB for org {org_id}")
            except:
                console.error(
                    f"Error when saving the webhook secret in the DB for org {org_id}")
                return "Error when saving data", 500, None
        return "", 200, secret

    def delete(self, org_id: str):
        try:
            self.db.delete_one({"org_id": org_id})
            console.info(f"Settings deleted for org {org_id}")
            return "", 200
        except:
            console.error(
                f"Error when deleting the configuration for org {org_id}")
            return "Error when deleting the configuration", 500
