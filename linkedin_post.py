from linkedin import linkedin
import json

API_KEY = '779llc1jtnh1rv'
API_SECRET = 'ORxeaAQKo1PTs4yU'
RETURN_URL = 'https://smartbox.in'
authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print authentication.authorization_url  # open this url on your browser
application = linkedin.LinkedInApplication(authentication)
authentication.authorization_code= 'AQQrPsMaHUBP4iWS2lR3BhvaBlKJz9NcunEuDbuOKWliXrhzPxC9tliw5AkMnW9a453Vp_DjKu6QMFXE3h2hLiZ6AydsbQh7s6zzC9s3EdcE6USrDzUW9q9lJkbdFacN32GwvtSRa9K4dzTVFDB5v-4Nu6tO37xtHMHfe0taPIXOqf3-1S4RqmtT6bj_Ng'
print authentication.get_access_token()
a=application.get_profile()
print json.dumps(a,indent=4)
application.submit_share(' "Life is 10 percent what happens to me and 90 percent of how I react to it." -Charles Swindoll', 'Motivational Evening', None, None, None)
