from locust import HttpUser, task, between

class GolootloUser(HttpUser):
    wait_time = between(0, 0)  # No delay between requests
    #host = "https://www.google.com"

    # Define multiple routes with their own headers
    routes = [
        {
            "path": "/public/v3/",
            "headers": {
                # "Content-Type": "application/json",
                # "User-Agent": "LocustTest/1.0",
                # "ClientId": "member",
                # "Coordinates": "24.7896298,67.0739251",
                # "IPAddress": "10.0.1.76",
                # "PublicIPAddress": "",
                # "PlayStoreAccounts": "",
                # "BuildFingerprint": "google/coral/coral:13/TP1A.221005.002.B2/9382335:user/release-keys",
                # "CurrentLocation": "24.7896298,67.0739251",
                # "CarrierName": "",
                # "DeviceInfo": "android,33,google,Pixel 4 XL,ceed2e5e53b5e8b3,8.9.454"
            }
        },
        {
            "path": "/public/v3/",
            "headers": {
                # "Content-Type": "application/json",
                # "User-Agent": "LocustTest/1.0",
                # "ClientId": "member",
                # "Coordinates": "24.7896298,67.0739251",
                # "IPAddress": "10.0.1.76",
                # "PublicIPAddress": "",
                # "PlayStoreAccounts": "",
                # "BuildFingerprint": "google/coral/coral:13/TP1A.221005.002.B2/9382335:user/release-keys",
                # "CurrentLocation": "24.7896298,67.0739251",
                # "CarrierName": "",
                # "DeviceInfo": "android,33,google,Pixel 4 XL,ceed2e5e53b5e8b3,8.9.454"
            }
        },
        {
            "path": "/public/v3/",
            "headers": {
                # "Content-Type": "application/json",
                # "User-Agent": "LocustTest/1.0",
                # "ClientId": "member",
                # "Coordinates": "24.7896298,67.0739251",
                # "IPAddress": "10.0.1.76",
                # "PublicIPAddress": "",
                # "PlayStoreAccounts": "",
                # "BuildFingerprint": "google/coral/coral:13/TP1A.221005.002.B2/9382335:user/release-keys",
                # "CurrentLocation": "24.7896298,67.0739251",
                # "CarrierName": "",
                # "DeviceInfo": "android,33,google,Pixel 4 XL,ceed2e5e53b5e8b3,8.9.454"
            }
        },
        {
            "path": "/public/v2/",
            "headers": {
                # "Content-Type": "application/json",
                # "User-Agent": "LocustTest/1.0",
                # "ClientId": "member",
                # "Coordinates": "24.7896298,67.0739251",
                # "IPAddress": "10.0.1.76",
                # "PublicIPAddress": "",
                # "PlayStoreAccounts": "",
                # "BuildFingerprint": "google/coral/coral:13/TP1A.221005.002.B2/9382335:user/release-keys",
                # "CurrentLocation": "24.7896298,67.0739251",
                # "CarrierName": "",
                # "DeviceInfo": "android,33,google,Pixel 4 XL,ceed2e5e53b5e8b3,8.9.454"
            }
        },
        {
            "path": "/public/v3/",
            "headers": {
                # "Content-Type": "application/json",
                # "User-Agent": "LocustTest/1.0",
                # "ClientId": "member",
                # "Coordinates": "24.7896298,67.0739251",
                # "IPAddress": "10.0.1.76",
                # "PublicIPAddress": "",
                # "PlayStoreAccounts": "",
                # "BuildFingerprint": "google/coral/coral:13/TP1A.221005.002.B2/9382335:user/release-keys",
                # "CurrentLocation": "24.7896298,67.0739251",
                # "CarrierName": "",
                # "DeviceInfo": "android,33,google,Pixel 4 XL,ceed2e5e53b5e8b3,8.9.454"
            }
        },
        {
            "path": "/public/v3/",
            "headers": {
                # "Content-Type": "application/json",
                # "User-Agent": "LocustTest/1.0",
                # "ClientId": "member",
                # "Coordinates": "24.7896298,67.0739251",
                # "IPAddress": "10.0.1.76",
                # "PublicIPAddress": "",
                # "PlayStoreAccounts": "",
                # "BuildFingerprint": "google/coral/coral:13/TP1A.221005.002.B2/9382335:user/release-keys",
                # "CurrentLocation": "24.7896298,67.0739251",
                # "CarrierName": "",
                # "DeviceInfo": "android,33,google,Pixel 4 XL,ceed2e5e53b5e8b3,8.9.454"
            }
        }
    ]

    @task
    def hit_multiple_routes(self):
        for route in self.routes:
            with self.client.get(route["path"], headers=route["headers"], catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Failed {route['path']} with {response.status_code}")
