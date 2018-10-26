import json

str_13095 = '''{
  "runTo": null,
  "databaseIdList": null,
  "prompts": [
    {
      "id": 17307,
      "code": "@asof",
      "prompt": "As Of Date",
      "promptDescription": "",
      "promptType": "Date",
      "defaultValue": "10/26/2018",
      "isPromptUser": true,
      "sortOrder": null
    },
    {
      "id": 23342,
      "code": "@group",
      "prompt": "Group",
      "promptDescription": "Enter FPSUP, CMSUP, OASUP, ACSUP, CCSUP, ACBALA1, ACBALA2, ACBALA3, MISUP, or EQUITY",
      "promptType": "Text",
      "defaultValue": "FPSUP",
      "isPromptUser": true,
      "sortOrder": null
    }
  ],
  "id": 13095,
  "scheduleIsActive": null,
  "entity": "Advisor",
  "title": "FPCM - As of Value by Product by Group",
  "category": "Product",
  "reportDescription": "FPCM - As of Value by Product by Group",
  "isCustom": null,
  "isFavorite": null,
  "scheduleId": null,
  "isLandscape": false,
  "reportClass": null,
  "isInternal": false,
  "guid": "00000000-0000-0000-0000-000000000000",
  "promptClass": null,
  "reportType": "Query",
  "userOwnerId": null
}'''
def generatePayLoad_13095(name, date):
    jobj = json.loads(str_13095)
    prompts = jobj['prompts']
    prompts[0]['defaultValue'] = date
    prompts[1]['defaultValue'] = name
    return json.dumps(jobj)

