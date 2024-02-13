const net = require('net')
const fs = require('fs')
const path = require('path')
require('dotenv').config({ path: path.resolve(__dirname, '../.env') })

const server_file = process.env.SERVER_ADDRESS
const callableHashMap = require('./makeHashMap')()

const server = net.createServer((socket) => {
    socket.on('data', (bytes) => {
        console.log('Client is here.')
        client_inputs = bytes.toString()
        console.log(client_inputs)
        client_json = JSON.parse(client_inputs)
        console.log(client_json)

        method = client_json.method
        params = client_json.params

        callable = callableHashMap.get(method)
        console.log(callable)
        console.log(params)
        result = callable(...params)
        
        socket.write(JSON.stringify({ result: result }));

    })
})

if(fs.existsSync(server_file)) {
    fs.unlinkSync(server_file)
}

server.listen(server_file, () => {
    console.log(`Server is binded with ${server_file}`)
})



