// bindとかはどうすればいいんだ？
// nodejsのsocketの使い方を勉強する必要がある

import makeHashMap from "./makeHashMap";

require('dotenv').config()
const fs = require('fs')

const hashmap = makeHashMap()
const rpcJSONPath = process.env.SERVER_ADDRESS
const rpcJSON = require(rpcJSONPath).parse()

const callable = hashmap.get(rpcJSON.method)
const params = rpcJSON.params
const id = rpcJSON.id

const result = callable(params)
const resultType = typeof(result)

const response = {
    "result" : result, 
    "result_type": resultType, 
    "id": id
}

fs.writeFileSync(process.env.CLIENT_ADDRESS, response)



