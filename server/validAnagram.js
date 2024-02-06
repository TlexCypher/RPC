const validAnagram = (s1, s2) => {
    return [...s1].sort() === [...s2].sort()
}

export default validAnagram