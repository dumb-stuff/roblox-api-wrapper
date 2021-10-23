"""
This module will be used to make requests anything that was all about account.
Needed to get authorized
Get token by go to roblox website and login.
And click at padlock. and click at cookies
After that go to roblox.com/Cookies and find .ROBLOSECURITY and copy it.
"""
import requests
import json
from . import errors

def __makerequest(session, method:str , url:str, params:dict=None, headers:dict=None, cookies:dict=None, data=None):
	"""
	This function was all about making requests. Return requests Response
	"""
	if method == "GET":
		return  session.get(url, params=params, headers=headers, cookies=cookies, data=data)
	elif method == "POST":
		return  session.post(url, params=params, headers=headers, cookies=cookies, data=data)
	elif method == "PUT":
		return  session.put(url, params=params, headers=headers, cookies=cookies, data=data)
	elif method == "DELETE":
		return  session.delete(url, params=params, headers=headers, cookies=cookies, data=data)
	else:
		raise errors.InvalidRequestMethodError(method)
def __sessionmaker():
	"""
	This is session maker. Return requests session
	"""
	session =  requests.ClientSession()
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
	
	def get(self):
		"""
		This function is used to get the date of birth of the user.

		"""
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response =  __makerequest(session, self.__url, cookies=cookie)
		if response.status == 400:
			raise errors.UserNotFound("User not found")
		if response.status == 401:
			raise errors.InvalidCredentials("Invalid credentials")
		self.day =  response.json()["birthDay"]
		self.month =  response.json()["birthMonth"]
		self.year =  response.json()["birthYear"]
		session.close()
	
	def changedate(self, day, month, year, password):
		"""
		This function used to change the date of birth of the user.
		"""
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		data = {
			"birthDay": day,
			"birthMonth": month,
			"birthYear": year,
			"password":password
		}
		response =  __makerequest(session, self.__url, cookies=cookie, data=data)
		if response.status == 400:
			if json.loads( response.text())["error"][0]["code"] == 1:
				raise errors.UserNotFound("User not found")
			if json.loads( response.text())["error"][0]["code"] == 4:
				raise errors.InvalidBirthday("Invalid birthday")
			if json.loads( response.text())["error"][0]["code"] == 8:
				raise errors.InvalidPassword("Invalid password")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 403:
			if json.loads( response.text())["error"][0]["code"] == 0:
				raise errors.TokenValidationFailed("Token validation failed")
			if json.loads( response.text())["error"][0]["code"] == 2:
				raise errors.PinIsLocked("Pin is locked")
			if json.loads( response.text())["error"][0]["code"] == 5:
				raise errors.InvalidBirthdateChange("Invalid birthday change")
		if response.status == 500:
			if json.loads( response.text())["error"][0]["code"] == 0:
				raise errors.UnknownError("Unknown error")
			if json.loads( response.text())["error"][0]["code"] == 5:
				raise errors.InvalidBirthdateChange("Invalid birthday change")
		session.close()

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
	def getdescription(self):
		"""
		This function used to get the description of the user.
		"""
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response =  __makerequest(session, "GET" ,self.__url, cookies=cookie)
		if response.status == 400:
			raise errors.UserNotFound("User not found")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		self.description =  response.json()["description"]
		session.close()
	def setdescription(self, description):
		"""
		This function used to set the description of the user.
		"""
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		data = {
			"description": description
		}
		response =  __makerequest(session, "POST" , self.__url, cookies=cookie, data=data)
		if response.status == 400:
			raise errors.UserNotFound("User not found")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 403:
			if json.loads( response.text())["error"][0]["code"] == 0:
				raise errors.TokenValidationFailed("Token validation failed")
			if json.loads( response.text())["error"][0]["code"] == 2:
				raise errors.PinIsLocked("Pin is locked")
		if response.status == 500:
			raise errors.UnknownError("Unknown error")
		if response.status == 503:
			raise errors.FeatureDisabled("Feature disabled")
		self.description =  response.json()["description"]
		session.close()

class Gender():
	"""
	This is gender class
	Where you can look at your gender and change your gender
	"""
	def __init__(self,token):
		self.__token = token
		self.gender = None
		self.__url = "https://accountinformation.roblox.com/v1/gender"
	def GetGender(self):
		"""
		This function used to get gender
		"""
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response =  __makerequest(session, "GET" ,self.__url, cookies=cookie)
		if response.status == 400:
			raise errors.UserNotFound("User not found")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		self.gender = "Male" if  response.json()["gender"] == "2" else "Female"
		session.close()
	def SetGender(self,gender:str):
		if gender != "Male" or gender != "Female":
			raise errors.UnknownGender("Unknown Gender")
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response =  __makerequest(session, "POST" ,self.__url, cookies=cookie)
		if response.status == 400:
			if json.loads( response.text())["error"][0]["code"] == 1:
				raise errors.UserNotFound("User not found")
			if json.loads( response.text())["error"][0]["code"] == 6:
				raise errors.UnknownGender("Unknown Gender")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 403:
			if json.loads( response.text())["error"][0]["code"] == 0:
				raise errors.TokenValidationFailed("Token validation failed")
			if json.loads( response.text())["error"][0]["code"] == 2:
				raise errors.PinIsLocked("Pin is locked")
		if response.status == 500:
			raise errors.UnknownError("Unknown error")
		self.gender = gender
		session.close()

class Xbox():
	def __init__(self,token):
		self.__token = token
		self.consecutive_login_days = 0

	def GetConsecutiveLoginDays(self):
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response =  __makerequest(session, "GET" ,self.__url, cookies=cookie)
		
		if response.status == 401:
			if json.loads( response.text())["error"][0]["code"] == 0:
				raise errors.AuthorizationDenied("Authorization has been denied for this request.")
			if json.loads( response.text())["error"][0]["code"] == 7:
				raise errors.NotConnectedToXboxLive("The account is not connected to an Xbox Live account.")
		for key in list( response.json().keys()):
			self.consecutive_login_days =  response.json()[key]
		session.close()

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
	
	def GetMetaData(self):
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response =  __makerequest(session, "GET" ,self.__url, cookies=cookie)
		self.isAllowedNotificationsEndpointDisabled =  response.json()["isAllowedNotificationsEndpointDisabled"]
		self.isAccountSettingsPolicyEnabled =  response.json()["isAccountSettingsPolicyEnabled"]
		self.isPhoneNumberEnabled =  response.json()["isPhoneNumberEnabled"]
		self.MaxUserDescriptionLength =  response.json()["MaxUserDescriptionLength"]
		self.isUserDescriptionEnabled =  response.json()["isUserDescriptionEnabled"]
		self.isUserBlockEndpointsUpdated =  response.json()["isUserBlockEndpointsUpdated"]
		self.isIDVerificationEnabled =  response.json()["isIDVerificationEnabled"]
		self.isPasswordRequiredForAgingDown =  response.json()["isPasswordRequiredForAgingDown"]
		session.close()
class Phone():
	def __init__(self,token):
		self.__url = "https://accountinformation.roblox.com/v1/phone"
		self.__token = token
	def DeletePhoneNumber(self,countrycode,prefix,phone,password):
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		data = {
			"countryCode": countrycode,
			"prefix": prefix,
			"phone": phone,
			"password": password
		}
		response =  __makerequest(session, "POST" ,self.__url +"/delete", cookies=cookie,data=data)
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 403:
			if json.loads( response.text())["error"][0]["code"] == 0:
				raise errors.TokenValidationFailed("Token validation failed")
			if json.loads( response.text())["error"][0]["code"] == 4:
				raise errors.PinIsLocked("Pin is locked")
			if json.loads( response.text())["error"][0]["code"] == 5:
				raise errors.PhoneNumberNotFound("Phone number not found")
		if response.status == 429:
			raise errors.Flooded("Flooded")
		if response.status == 500:
			raise errors.UnknownError("Unknown error")
		if response.status == 503:
			raise errors.FeatureDisabled("Feature Disabled")
		self.DeletePhoneResponse =  response.json()
		session.close()
	def ResendOTP(self,countrycode,prefix,phone,password):
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		data = {
			"countryCode": countrycode,
			"prefix": prefix,
			"phone": phone,
			"password": password
		}
		response =  __makerequest(session, "POST" ,self.__url+"/resend", cookies=cookie,data=data)
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
		self.ResendOTPResponse =  response.json()
		session.close()
	def VerifyOTP(self,code):
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		data = {
			"code":code
		}
		response =  __makerequest(session, "POST" ,self.__url+"/verify", cookies=cookie,data=data)
		if response.status == 400:
			if json.loads( response.text())["error"][0]["code"] == 2:
				raise errors.InvalidPhoneNumber("Invalid phone number")
			if json.loads( response.text())["error"][0]["code"] == 3:
				raise errors.PhoneNumberAlreadyAssocidated("Phone number already associated with another account")
			if json.loads( response.text())["error"][0]["code"] == 7:
				raise errors.InvalidCode("Invalid code")
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
		self.VerifyOTPResponse =  response.json()
		session.close()
	def GetPhoneNumber(self):
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response =  __makerequest(session, "GET" ,self.__url, cookies=cookie)
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 500:
			raise errors.UnknownError("Unknown error")
		self.countryCode =  response.json()["countryCode"]
		self.prefix =  response.json()["prefix"]
		self.phone =  response.json()["phone"]
		self.isVerified =  response.json()["isVerified"]
		self.verificationCodeLength =  response.json()["verificationCodeLength"]
		session.close()
	def UpdatePhoneNumber(self,countrycode,prefix,phone,password):
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		data = {
			"countryCode": countrycode,
			"prefix": prefix,
			"phone": phone,
			"password": password
		}
		response =  __makerequest(session, "POST" ,self.__url+"/update", cookies=cookie,data=data)
		if response.status == 400:
			if json.loads( response.text())["error"][0]["code"] == 2:
				raise errors.InvalidPhoneNumber("Invalid phone number")
			if json.loads( response.text())["error"][0]["code"] == 3:
				raise errors.PhoneNumberAlreadyAssocidated("Phone number already associated with another account")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 403:
			if json.loads( response.text())["error"][0]["code"] == 0:
				raise errors.TokenValidationFailed("Token validation failed")
			if json.loads( response.text())["error"][0]["code"] == 4:
				raise errors.PinIsLocked("Pin is locked")
			if json.loads( response.text())["error"][0]["code"] == 5:
				raise errors.IncorrectPassword("Incorrect password")
			
		if response.status == 429:
			raise errors.Flooded("Flooded")
		if response.status == 500:
			raise errors.UnknownError("Unknown error")
		if response.status == 503:
			raise errors.FeatureDisabled("Feature Disabled")
		self.UpdatePhoneResponse =  response.json()
        session.close()
class Promotion():
	def __init__(self,token):
		self.__token = token
		self.__url = "https://accountinformation.roblox.com/v1/promotion-channels"
	def GetUserPromotionChannel(self):
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		response =  __makerequest(session, "GET" ,self.__url, cookies=cookie)
		if response.status == 400:
			raise errors.UserNotFound("User not found")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		self.promotionChannelsVisibilityPrivacy =  response.json()["promotionChannelsVisibilityPrivacy"]
		self.facebook =  response.json()["facebook"]
		self.twitter =  response.json()["twitter"]
		self.youtube =  response.json()["youtube"]
		self.twitch =  response.json()["twitch"]
		session.close()
	def UpdateUserPromotionChannel(self,facebook,twitter,youtube,twitch,promotionChannelsVisibilityPrivacy):
		session =  __sessionmaker()
		cookie = {
			'.ROBLOSECURITY': self.__token
		}
		data = {
			"facebook": facebook,
			"twitter": twitter,
			"youtube": youtube,
			"twitch": twitch,
			"promotionChannelsVisibilityPrivacy": promotionChannelsVisibilityPrivacy
		}
		response =  __makerequest(session, "POST" ,self.__url+"/update", cookies=cookie,data=data)
		if response.status == 400:
			if json.loads( response.text())["error"][0]["code"] == 2:
				raise errors.RequestEmpty("Request is empty")
			if json.loads( response.text())["error"][0]["code"] == 11:
				raise errors.FacebookURLInvalid("Facebook URL is invalid")
			if json.loads( response.text())["error"][0]["code"] == 12:
				raise errors.TwitterHandleInvalid("Twitter URL is invalid")
			if json.loads( response.text())["error"][0]["code"] == 13:
				raise errors.YoutubeURLInvalid("Youtube URL is invalid")
			if json.loads( response.text())["error"][0]["code"] == 14:
				raise errors.TwitchURLInvalid("Twitch URL is invalid")
		if response.status == 401:
			raise errors.AuthorizationDenied("Authorization has been denied for this request.")
		if response.status == 403:
			if json.loads( response.text())["error"][0]["code"] == 0:
				raise errors.TokenValidationFailed("Token validation failed")
			if json.loads( response.text())["error"][0]["code"] == 3:
				raise errors.PinIsLocked("Pin is locked")
			if json.loads( response.text())["error"][0]["code"] == 4:
				raise errors.AgeTooLow("Only users who are over twelve years of age may edit social network channels.")
		self.result =  response.json()		