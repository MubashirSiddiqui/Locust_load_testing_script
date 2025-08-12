from locust import HttpUser, task, between

class GolootloUser(HttpUser):
    wait_time = between(0, 0)  # No delay between requests
    #host = "https://"

    headers = {
    #    "Content-Type": "application/json",
    #    "User-Agent": "LocustTest/1.0",
    #   "ClientId": "member",
    #    "Coordinates": "24.7896298,67.0739251",
    #    "IPAddress": "10.0.1.76",
    #    "PublicIPAddress": "110.93.217.10",
    #    "PlayStoreAccounts": "",
    #    "BuildFingerprint": "google/coral/coral:13/TP1A.221005.002.B2/9382335:user/release-keys",
    #    "CurrentLocation": "24.7896298,67.0739251",
    #    "CarrierName": "",
    #    "DeviceInfo": "android,33,google,Pixel 4 XL,ceed2e5e53b5e8b3,8.9.454"
    }

    @task
    def get_initial_screen(self):
        self.client.get(
            "/public/v3/initial-screen-v2",
            headers=self.headers
        )
