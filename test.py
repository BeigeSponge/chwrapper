import chwrapper

api_key = "28217ffa-870c-4843-afde-1b5c733334be"
access_token = "da5a2028-bc7a-464b-970d-b6e4350e5fa9"

s = chwrapper.Search(access_token=access_token)
r = s.profile(num="04730752")

print(r.content)
