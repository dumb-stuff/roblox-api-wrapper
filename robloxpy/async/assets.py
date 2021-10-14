import aiohttp
import json
from . import errors
class Dummy():
    pass
async def __makerequest(session, url, params):
    return await session.get(url, params=params)
async def __sessionmaker():
    session = await aiohttp.ClientSession()
    return session
async def GetAssetInfo(id:int=None,placeid=None,page:int=None):
    params = {}
    if id is not None:
        params['id'] = id
    if placeid is not None:
        params['placeId'] = placeid
    if page is not None:
        params['page'] = page
    url = "https://api.roblox.com/assets/{}/versions".format(id)
    asset = __makerequest(await __sessionmaker(), url, params)
    if asset.status != 200:
        raise errors.PlatformException("PlatformError")
    asset = json.loads(asset.text)
    nojson = Dummy()
    nojson.Id = asset["Id"]
    nojson.AssetId = asset["AssetId"]
    nojson.VersionNumber = asset["VersionNumber"]
    nojson.RawContentId = asset["RawContentId"]
    nojson.ParentAssetVersionId = asset["ParentAssetVersionId"]
    nojson.CreatorType = asset["CreatorType"]
    nojson.CreatorTargetId = asset["CreatorTargetId"]
    nojson.CreatingUniverseId = asset["CreatingUniverseId"]
    nojson.Created = asset["Created"]
    nojson.Updated = asset["Updated"]
    return nojson

async def GetAssetsInfoV2(id:int=None,placeid=None,page:int=None,cursor:str=None,limit:int=None):
    params = {}
    if id is not None:
        params['id'] = id
    if placeid is not None:
        params['placeId'] = placeid
    if page is not None:
        params['page'] = page
    if cursor is not None:
        params['cursor'] = cursor
    if limit is not None:
        params['limit'] = limit
    url = "https://api.roblox.com/v2/assets/{}/versions".format(id)
    asset = __makerequest(await __sessionmaker(), url, params)
    if asset.status == 400:
        raise errors.InvalidRequest("Invalid Request!")
    if asset.status == 404:
        raise errors.NotFound("Not Found!")
    if asset.status == 409:
        raise errors.PlatformException("PlatformException")
    if asset.status == 500:
        raise errors.InternalServerError("Internal Server Error!")
    if asset.status == 502:
        raise errors.BadGateway("Bad Gateway!")
    asset = json.loads(asset.text)
    nojson = Dummy()
    nojson.previousPageCursor = asset["previousPageCursor"]
    nojson.nextPageCursor = asset["nextPageCursor"]
    nojson.data = []
    for i in asset["data"]:
        nojson.data.append(Dummy())
        nojson.data[-1].Id = i["Id"]
        nojson.data[-1].AssetId = i["AssetId"]
        nojson.data[-1].VersionNumber = i["VersionNumber"]
        nojson.data[-1].RawContentId = i["RawContentId"]
        nojson.data[-1].ParentAssetVersionId = i["ParentAssetVersionId"]
        nojson.data[-1].CreatorType = i["CreatorType"]
        nojson.data[-1].CreatorTargetId = i["CreatorTargetId"]
        nojson.data[-1].CreatingUniverseId = i["CreatingUniverseId"]
        nojson.data[-1].Created = i["Created"]
        nojson.data[-1].Updated = i["Updated"]
    return nojson

async def GetListOfFriends(userId:int=None,page:int=None):
    params = {}
    if page is not None:
        params['page'] = page
    url = "https://api.roblox.com/users/{}/friends".format(userId)
    friends = __makerequest(await __sessionmaker(), url, params)
    if friends.status != 200:
        raise errors.PlatformException("PlatformError")
    nojson = Dummy()
    nojson.friends = []
    if asset.status == 404:
        raise errors.NotFound("Not Found!")
    asset = json.loads(friends.text)
    for friend in friends:
        nojson.friends.append(Dummy())
        nojson.friends[-1].Id = friend["Id"]
        nojson.friends[-1].Username = friend["Username"]
        nojson.friends[-1].AvatarUri = friend["AvatarUri"]
        nojson.friends[-1].AvatarFinal= friend["AvatarFinal"]
        nojson.friends[-1].IsOnline = friend["IsOnline"]
    return nojson
