const floor = require('./floor')
const nroot = require('./nroot')
const reverse = require('./reverse')
const sort = require('./sort')
const validAnagram = require('./validAnagram')


const makeHashMap = () => {
    const hashmap = new Map()
    hashmap.set('floor', floor)
    hashmap.set('nroot', nroot)
    hashmap.set('reverse', reverse)
    hashmap.set('sort', sort)
    hashmap.set('validAnagram', validAnagram)
    return hashmap
}

module.exports = makeHashMap