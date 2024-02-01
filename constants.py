
TEST_JSON_1 = {
    "attributes": {
        "appName": "TestApp",
        "sensitive": True
    },
    "message": {
        "user": {
            "id": "TestID",
            "title": "TestTitle",
        },
        "time": 123,
        "acl": ["read", "write"],
        "publicFeed": True,
        "internationalCountries": ["TestCountry"],
        "topTraderFeed": True
    }
}

TEST_JSON_2 = {
    "attributes": {
        "appName": "TestApp2",
        "sensitive": True
    },
    "message": {
        "user": {
            "id": "TestID2",
            "title": "TestTitle2",
        },
        "time": 123,
        "acl": ["read", "write", "edit"],
        "publicFeed": True,
        "internationalCountries": ["TestCountry2"],
        "topTraderFeed": True
    }
}

EXPECTED_SCHEMA_1 = {
   "user": {
      "type": "dict",
      "tag": "",
      "description": "",
      "required": True,
      "properties": {
         "id": {
            "type": "string",
            "tag": "",
            "description": "",
            "required": True
         },
         "title": {
            "type": "string",
            "tag": "",
            "description": "",
            "required": True
         }
      }
   },
   "time": {
      "type": "integer",
      "tag": "",
      "description": "",
      "required": True
   },
   "acl": {
      "type": "enum",
      "tag": "",
      "description": "",
      "required": True
   },
   "publicFeed": {
      "type": "bool",
      "tag": "",
      "description": "",
      "required": True
   },
   "internationalCountries": {
      "type": "enum",
      "tag": "",
      "description": "",
      "required": True
   },
   "topTraderFeed": {
      "type": "bool",
      "tag": "",
      "description": "",
      "required": True
   }
}

EXPECTED_SCHEMA_2 = {
   "user": {
      "type": "dict",
      "tag": "",
      "description": "",
      "required": False,
      "properties": {
         "id": {
            "type": "string",
            "tag": "",
            "description": "",
            "required": False
         },
         "title": {
            "type": "string",
            "tag": "",
            "description": "",
            "required": False
         }
      }
   },
   "time": {
      "type": "integer",
      "tag": "",
      "description": "",
      "required": False
   },
   "acl": {
      "type": "enum",
      "tag": "",
      "description": "",
      "required": False
   },
   "publicFeed": {
      "type": "bool",
      "tag": "",
      "description": "",
      "required": False
   },
   "internationalCountries": {
      "type": "enum",
      "tag": "",
      "description": "",
      "required": False
   },
   "topTraderFeed": {
      "type": "bool",
      "tag": "",
      "description": "",
      "required": False
   }
}