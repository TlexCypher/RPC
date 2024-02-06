import floor from "./floor"
import nroot from "./nroot"
import reverse from "./reverse"
import sort from "./sort"
import validAnagram from "./validAnagram"

const makeHashMap = () => {
    const hashmap = new Map()
    hashmap.set('floor', floor)
    hashmap.set('nroot', nroot)
    hashmap.set('reverse', reverse)
    hashmap.set('sort', sort)
    hashmap.set('validAnagram', validAnagram)
    return hashmap
}

export default makeHashMap
