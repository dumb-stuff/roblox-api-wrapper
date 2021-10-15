"""
This module will be used to make requests anything that was all about account.
Needed to get authorized
Get token by go to roblox website and login.
And click at padlock. and click at cookies
After that go to roblox.com/Cookies and find .ROBLOSECURITY and copy it.
"""
import aiohttp
import json
from . import errors

async def __makerequest(session, method:str , url:str, params:dict=None, headers:dict=None, cookies:dict=None, data=None):
	"""
	This function was all about making requests. Return aiohttp Response
	"""
	if method == "GET":
		return await session.get(url, params=params, headers=headers, cookies=cookies, data=data)
	elif method == "POST":
		return await session.post(url, params=params, headers=headers, cookies=cookies, data=data)
	elif method == "PUT":
		return await session.put(url, params=params, headers=headers, cookies=cookies, data=data)
	elif method == "DELETE":
		return await session.delete(url, params=params, headers=headers, cookies=cookies, data=data)
	else:
		raise errors.InvalidRequestMethodError(method)
async def __sessionmaker():
	"""
	This is session maker. Return aiohttp session
	"""
	session = await aiohttp.ClientSession()
	return session
class Birthday():
	"""
	This is birthdate class.
	Manage the date of birth of the user.
	Or
	Look up the date of birth of the user.
	"""
	def __init__(self,token):
		self.__token =  token
		self.__url = "https://api.roblox.com/v1/birthdate"
		self.day = None
		self.month = None
		self.year = None
	
	async def get(self):
		"""
		This function is used to get the date of birth of the user.

		"""
		session = await __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response = await __makerequest(session, self.__url, cookies=cookie)
		if response.status == 400:
			raise errors.UserNotFound("User not found")
		if response.status == 401:
			raise errors.InvalidCredentials("Invalid credentials")
		self.day = await response.json()["birthDay"]
		self.month = await response.json()["birthMonth"]
		self.year = await response.json()["birthYear"]
		await session.close()
	
	async def changedate(self, day, month, year, password):
		"""
		This function used to change the date of birth of the user.
		"""
		session = await __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		data = {
			"birthDay": day,
			"birthMonth": month,
			"birthYear": year,
			"password":password
		}
		response = await __makerequest(session, self.__url, cookies=cookie, data=data)
		if response.status == 400:
			if json.loads(await response.text())["error"][0]["code"] == 1:
				raise errors.UserNotFound("User not found")
			if json.loads(await response.text())["error"][0]["code"] == 4:
				raise errors.InvalidBirthday("Invalid birthday")
			if json.loads(await response.text())["error"][0]["code"] == 8:
				raise errors.InvalidPassword("Invalid password")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 403:
			if json.loads(await response.text())["error"][0]["code"] == 0:
				raise errors.TokenValidationFailed("Token validation failed")
			if json.loads(await response.text())["error"][0]["code"] == 2:
				raise errors.PinIsLocked("Pin is locked")
			if json.loads(await response.text())["error"][0]["code"] == 5:
				raise errors.InvalidBirthdateChange("Invalid birthday change")
		if response.status == 500:
			if json.loads(await response.text())["error"][0]["code"] == 0:
				raise errors.UnknownError("Unknown error")
			if json.loads(await response.text())["error"][0]["code"] == 5:
				raise errors.InvalidBirthdateChange("Invalid birthday change")
		await session.close()

class Description():
	"""
	This is description class.
	Where you can change the description of the user.
	Or look it up.
	"""
	def __init__(self, token):
		self.description = None
		self.__token = token
		self.__url = "https://accountinformation.roblox.com/v1/description"
	async def getdescription(self):
		"""
		This function used to get the description of the user.
		"""
		session = await __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response = await __makerequest(session, "GET" ,self.__url, cookies=cookie)
		if response.status == 400:
			raise errors.UserNotFound("User not found")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		self.description = await response.json()["description"]
		await session.close()
	async def setdescription(self, description):
		"""
		This function used to set the description of the user.
		"""
		session = await __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		data = {
			"description": description
		}
		response = await __makerequest(session, "POST" , self.__url, cookies=cookie, data=data)
		if response.status == 400:
			raise errors.UserNotFound("User not found")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 403:
			if json.loads(await response.text())["error"][0]["code"] == 0:
				raise errors.TokenValidationFailed("Token validation failed")
			if json.loads(await response.text())["error"][0]["code"] == 2:
				raise errors.PinIsLocked("Pin is locked")
		if response.status == 500:
			raise errors.UnknownError("Unknown error")
		if response.status == 503:
			raise errors.FeatureDisabled("Feature disabled")
		self.description = await response.json()["description"]
		await session.close()

class Gender():
	"""
	This is gender class
	Where you can look at your gender and change your gender
	"""
	def __init__(self,token):
		self.__token = token
		self.gender = None
		self.__url = "https://accountinformation.roblox.com/v1/gender"
	async def GetGender(self):
		"""
		This function used to get gender
		"""
		session = await __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response = await __makerequest(session, "GET" ,self.__url, cookies=cookie)
		if response.status == 400:
			raise errors.UserNotFound("User not found")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		self.gender = "Male" if await response.json()["gender"] == "2" else "Female"
		await session.close()
	async def SetGender(self,gender:str):
		if gender != "Male" or gender != "Female":
			raise errors.UnknownGender("Unknown Gender")
		session = await __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response = await __makerequest(session, "POST" ,self.__url, cookies=cookie)
		if response.status == 400:
			if json.loads(await response.text())["error"][0]["code"] == 1:
				raise errors.UserNotFound("User not found")
			if json.loads(await response.text())["error"][0]["code"] == 6:
				raise errors.UnknownGender("Unknown Gender")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 403:
			if json.loads(await response.text())["error"][0]["code"] == 0:
				raise errors.TokenValidationFailed("Token validation failed")
			if json.loads(await response.text())["error"][0]["code"] == 2:
				raise errors.PinIsLocked("Pin is locked")
		if response.status == 500:
			raise errors.UnknownError("Unknown error")
		self.gender = gender
		await session.close()

class Xbox():
	def __init__(self,token):
		self.__token = token
		self.consecutive_login_days = 0

	async def GetConsecutiveLoginDays(self):
		session = await __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response = await __makerequest(session, "GET" ,self.__url, cookies=cookie)
		
		if response.status == 401:
			if json.loads(await response.text())["error"][0]["code"] == 0:
				raise errors.AuthorizationDenied("Authorization has been denied for this request.")
			if json.loads(await response.text())["error"][0]["code"] == 7:
				raise errors.NotConnectedToXboxLive("The account is not connected to an Xbox Live account.")
		for key in list(await response.json().keys()):
			self.consecutive_login_days = await response.json()[key]
		await session.close()

class MetaData():
	def __init____(self,token):
		self.__token = token
		self.__url = "https://accountinformation.roblox.com/v1/metadata"
		self.isAllowedNotificationsEndpointDisabled = None
		self.isAccountSettingsPolicyEnabled = None
		self.isPhoneNumberEnabled = None
		self.MaxUserDescriptionLength = None
		self.isUserDescriptionEnabled = None
		self.isUserBlockEndpointsUpdated = None
		self.isIDVerificationEnabled = None
		self.isPasswordRequiredForAgingDown = None
	
	async def GetMetaData(self):
		session = await __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response = await __makerequest(session, "GET" ,self.__url, cookies=cookie)
		self.isAllowedNotificationsEndpointDisabled = await response.json()["isAllowedNotificationsEndpointDisabled"]
		self.isAccountSettingsPolicyEnabled = await response.json()["isAccountSettingsPolicyEnabled"]
		self.isPhoneNumberEnabled = await response.json()["isPhoneNumberEnabled"]
		self.MaxUserDescriptionLength = await response.json()["MaxUserDescriptionLength"]
		self.isUserDescriptionEnabled = await response.json()["isUserDescriptionEnabled"]
		self.isUserBlockEndpointsUpdated = await response.json()["isUserBlockEndpointsUpdated"]
		self.isIDVerificationEnabled = await response.json()["isIDVerificationEnabled"]
		self.isPasswordRequiredForAgingDown = await response.json()["isPasswordRequiredForAgingDown"]
		await session.close()
class Phone():
	def __init__(self,token):
		self.__url = "https://accountinformation.roblox.com/v1/phone"
		self.__token = token
	async def DeletePhoneNumber(self,countrycode,prefix,phone,password):
		session = await __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		data = {
			"countryCode": countrycode,
			"prefix": prefix,
			"phone": phone,
			"password": password
		}
		response = await __makerequest(session, "POST" ,self.__url +"/delete", cookies=cookie,data=data)
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 403:
			if json.loads(await response.text())["error"][0]["code"] == 0:
				raise errors.TokenValidationFailed("Token validation failed")
			if json.loads(await response.text())["error"][0]["code"] == 4:
				raise errors.PinIsLocked("Pin is locked")
			if json.loads(await response.text())["error"][0]["code"] == 5:
				raise errors.PhoneNumberNotFound("Phone number not found")
		if response.status == 429:
			raise errors.Flooded("Flooded")
		if response.status == 500:
			raise errors.UnknownError("Unknown error")
		if response.status == 503:
			raise errors.FeatureDisabled("Feature Disabled")
		self.DeletePhoneResponse = await response.json()
		await session.close()
	async def ResendOTP(self,countrycode,prefix,phone,password):
		session = await __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		data = {
			"countryCode": countrycode,
			"prefix": prefix,
			"phone": phone,
			"password": password
		}
		response = await __makerequest(session, "POST" ,self.__url+"/resend", cookies=cookie,data=data)
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 403:
			raise errors.TokenValidationFailed("Token validation failed")
		if response.status == 429:
			raise errors.Flooded("Flooded")
		if response.status == 500:
			raise errors.UnknownError("Unknown error")
		if response.status == 503:
			raise errors.FeatureDisabled("Feature Disabled")
		self.ResendOTPResponse = await response.json()
		await session.close()
	